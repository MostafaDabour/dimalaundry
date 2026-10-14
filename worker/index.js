// Dima Laundry edge worker.
// Static pages are served from /public. This script only handles /api/*.
//
// Secrets (Cloudflare > dimalaundry > Settings > Variables and Secrets):
//   GHL_WEBHOOK_URL        GoHighLevel inbound webhook URL (workflow trigger "Inbound Webhook")
//   GHL_QUOTE_WEBHOOK_URL  optional: separate webhook for commercial quote requests
//   GOOGLE_PLACES_API_KEY  Google Places API (New) key, restricted to the Places API
// Optional:
//   LEAD_FORWARD_URL       a second webhook (Make, Zapier, Formspree) if you want leads copied elsewhere

const PLACES = {
  q4: "ChIJXcqBG0VrXz4RUiFV4V1j264",
  q3: "ChIJPahJ_LlrXz4RBd1Lm0bkoH8",
  f3: "ChIJgTqXI65rXz4RRWovjL8ZuF0",
  "al-sufouh": "ChIJv2Sj0JhrXz4R5G-ShOGE3_4",
  "dubai-marina": "ChIJTbiBTBtrXz4RnDVogr_MZvE",
  "dubai-marina-crown": "ChIJET00KK5rXz4RaSAjaKpdnrU",
  jumeirah: "ChIJ8ay36ZFDXz4RZ2L7zsU7xcA",
  "downtown-dubai": "ChIJPfrWwDxpXz4RwoUXIm-MOBw",
  "sheikh-zayed-road": "ChIJF-NCOztDXz4RXTCOvi5IHOo",
  karama: "ChIJ9Rq_bEdDXz4RqjU51zOA-q4",
};
const ALL = ["al-sufouh", "karama", "jumeirah", "dubai-marina", "sheikh-zayed-road", "downtown-dubai", "q4"];

const json = (data, status = 200, extra = {}) =>
  new Response(JSON.stringify(data), { status, headers: { "content-type": "application/json; charset=utf-8", ...extra } });

async function placeReviews(id, key, lang) {
  const url = `https://places.googleapis.com/v1/places/${id}?languageCode=${lang}`;
  const r = await fetch(url, {
    headers: { "X-Goog-Api-Key": key, "X-Goog-FieldMask": "displayName,rating,userRatingCount,googleMapsUri,reviews" },
    cf: { cacheTtl: 21600, cacheEverything: true },
  });
  if (!r.ok) return null;
  const p = await r.json();
  return {
    name: p.displayName && p.displayName.text,
    rating: p.rating, count: p.userRatingCount, url: p.googleMapsUri,
    reviews: (p.reviews || [])
      .filter((v) => v.rating >= 4 && v.text && v.text.text && v.text.text.length > 40)
      .map((v) => ({
        rating: v.rating, text: v.text.text, author: v.authorAttribution ? v.authorAttribution.displayName : "Google user",
        authorUrl: v.authorAttribution ? v.authorAttribution.uri : null, when: v.relativePublishTimeDescription,
        time: v.publishTime, place: p.displayName && p.displayName.text, placeUrl: p.googleMapsUri,
      })),
  };
}

async function reviews(request, env, ctx) {
  const u = new URL(request.url);
  const place = u.searchParams.get("place") || "all";
  const lang = u.searchParams.get("lang") === "ar" ? "ar" : "en";
  if (!env.GOOGLE_PLACES_API_KEY) return json({ enabled: false, reviews: [] }, 200, { "cache-control": "public, max-age=300" });

  const cache = caches.default;
  const cacheKey = new Request(`https://cache.dimalaundry/reviews/${place}/${lang}`);
  const hit = await cache.match(cacheKey);
  if (hit) return hit;

  const ids = place === "all" ? ALL : [place];
  const results = (await Promise.all(ids.filter((k) => PLACES[k]).map((k) => placeReviews(PLACES[k], env.GOOGLE_PLACES_API_KEY, lang).catch(() => null)))).filter(Boolean);
  const list = results.flatMap((r) => r.reviews).sort((a, b) => (b.time || "").localeCompare(a.time || "")).slice(0, 9);
  const summary = results.map((r) => ({ name: r.name, rating: r.rating, count: r.count, url: r.url }));
  const res = json({ enabled: true, summary, reviews: list }, 200, { "cache-control": "public, max-age=21600" });
  ctx.waitUntil(cache.put(cacheKey, res.clone()));
  return res;
}

async function lead(request, env) {
  if (request.method !== "POST") return json({ ok: false, error: "POST only" }, 405);
  let data;
  try { data = await request.json(); } catch (e) { return json({ ok: false, error: "bad request" }, 400); }
  if (data.website) return json({ ok: true }); // honeypot filled, silently drop bots
  const required = ["form", "Phone"];
  for (const k of required) if (!data[k]) return json({ ok: false, error: `missing ${k}` }, 400);

  const name = String(data["Name"] || data["Contact name"] || "").trim();
  const [firstName, ...rest] = name.split(/\s+/);
  const payload = {
    source: "dimalaundry.com",
    form: data.form,
    page: data.page || "",
    language: data.lang || "en",
    first_name: firstName || "",
    last_name: rest.join(" "),
    full_name: name,
    phone: String(data.Phone || "").trim(),
    email: String(data.Email || "").trim(),
    company: String(data.Company || "").trim(),
    tags: data.form === "business-quote" ? ["website lead", "commercial quote"] : ["website lead", "pickup booking"],
    fields: data,
    submitted_at: new Date().toISOString(),
  };

  // commercial quotes can go to their own GHL workflow; otherwise everything uses the main webhook
  const ghl = data.form === "business-quote" && env.GHL_QUOTE_WEBHOOK_URL ? env.GHL_QUOTE_WEBHOOK_URL : env.GHL_WEBHOOK_URL;
  const targets = [ghl, env.LEAD_FORWARD_URL].filter(Boolean);
  if (!targets.length) return json({ ok: false, error: "not configured" }, 503);
  const sends = await Promise.all(targets.map((t) =>
    fetch(t, { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(payload) })
      .then((r) => r.ok).catch(() => false)));
  return sends.some(Boolean) ? json({ ok: true }) : json({ ok: false, error: "delivery failed" }, 502);
}

export default {
  async fetch(request, env, ctx) {
    const u = new URL(request.url);
    if (u.pathname === "/api/lead") return lead(request, env);
    if (u.pathname === "/api/reviews") return reviews(request, env, ctx);
    return env.ASSETS.fetch(request);
  },
};
