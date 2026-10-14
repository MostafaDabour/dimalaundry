(function(){
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  // header shadow on scroll
  var head = document.querySelector(".site-head");
  var onScroll = function(){ if(head){ head.classList.toggle("scrolled", window.scrollY > 10); } };
  window.addEventListener("scroll", onScroll, {passive:true}); onScroll();
  // WhatsApp button: show label briefly after the visitor starts scrolling
  var wa = document.querySelector(".wa-float"), shown = false;
  window.addEventListener("scroll", function(){
    if(!shown && wa && window.scrollY > 400){ shown = true; wa.classList.add("hello"); setTimeout(function(){ wa.classList.remove("hello"); }, 4000); }
  }, {passive:true});
  // mobile app bar: links to the right store, can be closed for the visit
  var bar = document.querySelector(".app-bar");
  if(bar){
    var closed = false; try{ closed = sessionStorage.getItem("dimaAppBar") === "x"; }catch(e){}
    if(!closed){
      var go = bar.querySelector(".app-bar-go");
      if(/android/i.test(navigator.userAgent)){ go.href = go.getAttribute("data-android"); }
      bar.hidden = false;
      bar.querySelector(".app-bar-x").addEventListener("click", function(){ bar.hidden = true; try{ sessionStorage.setItem("dimaAppBar","x"); }catch(e){} });
    }
  }
  // forms: send to /api/lead (GoHighLevel). If that is not set up or fails, fall back to WhatsApp.
  function waFallback(f, fd){
    var lines = [f.getAttribute("data-intro")];
    fd.forEach(function(v, k){ if(k !== "website" && String(v).trim()) lines.push(k + ": " + v); });
    var url = "https://wa.me/" + f.getAttribute("data-wa") + "?text=" + encodeURIComponent(lines.join("\n"));
    window.open(url, "_blank") || (window.location.href = url);
  }
  document.querySelectorAll(".js-lead-form").forEach(function(f){
    f.addEventListener("submit", function(e){
      e.preventDefault();
      if(!f.reportValidity()) return;
      var fd = new FormData(f), data = {form: f.getAttribute("data-form"), lang: f.getAttribute("data-lang"), page: location.pathname};
      fd.forEach(function(v, k){ data[k] = String(v).replace(/[\u0660-\u0669]/g, function(d){ return d.charCodeAt(0) - 0x0660; }).replace(/[\u06F0-\u06F9]/g, function(d){ return d.charCodeAt(0) - 0x06F0; }); });
      var btn = f.querySelector("button[type=submit]"), msg = f.querySelector(".form-msg");
      btn.disabled = true;
      fetch("/api/lead", {method: "POST", headers: {"content-type": "application/json"}, body: JSON.stringify(data)})
        .then(function(r){ return r.json().then(function(j){ return r.ok && j.ok; }); })
        .catch(function(){ return false; })
        .then(function(ok){
          btn.disabled = false;
          if(ok){
            var lid = Date.now().toString(36) + Math.random().toString(36).slice(2, 8);
            var base = (data.lang === "ar" ? "/ar" : "") + (data.form === "business-quote" ? "/thank-you-quote" : "/thank-you");
            window.location.href = base + "?lid=" + lid;
          } else {
            waFallback(f, fd);
          }
        });
    });
  });
  // live Google reviews: replace the saved reviews with the latest 4 and 5 star ones when available
  document.querySelectorAll("[data-live]").forEach(function(box){
    var lang = box.getAttribute("data-lang") || "en";
    fetch("/api/reviews?place=" + encodeURIComponent(box.getAttribute("data-live")) + "&lang=" + lang)
      .then(function(r){ return r.ok ? r.json() : null; })
      .then(function(d){
        if(!d || !d.enabled || !d.reviews || d.reviews.length < 2) return;
        var esc = function(s){ var t = document.createElement("span"); t.textContent = s || ""; return t.innerHTML; };
        var lbl = lang === "ar" ? "على جوجل" : "on Google";
        box.innerHTML = d.reviews.slice(0, 6).map(function(v){
          return '<figure class="rv"><div class="stars" aria-label="' + v.rating + ' out of 5 stars">' + "&#9733;".repeat(v.rating) + '</div>' +
            '<blockquote dir="auto">' + esc(v.text.length > 420 ? v.text.slice(0, 400) + "..." : v.text) + '</blockquote>' +
            '<figcaption>' + esc(v.author) + ', ' + esc(v.when) + ' ' + lbl + ' <a href="' + esc(v.placeUrl) + '" rel="noopener" target="_blank">' + esc(v.place) + '</a></figcaption></figure>';
        }).join("");
        box.classList.add("is-live");
      }).catch(function(){});
  });
  // thank-you pages: count each lead once for Google Ads and GA4
  var conv = document.getElementById("conv");
  if(conv){
    var lid = new URLSearchParams(location.search).get("lid"), seen = false;
    try{ seen = !lid || sessionStorage.getItem("dimaLead_" + lid) === "1"; }catch(e){}
    if(!seen){
      try{ sessionStorage.setItem("dimaLead_" + lid, "1"); }catch(e){}
      var kind = conv.getAttribute("data-kind");
      window.dataLayer = window.dataLayer || [];
      dataLayer.push({event: "generate_lead", lead_type: kind, lead_id: lid});
      if(window.gtag){
        gtag("event", "generate_lead", {lead_type: kind});
        var label = conv.getAttribute("data-label");
        if(window.DIMA_ADS && label) gtag("event", "conversion", {send_to: window.DIMA_ADS + "/" + label, transaction_id: lid});
      }
    }
    if(lid && history.replaceState) history.replaceState(null, "", location.pathname);
  }
  if(reduce) return;
  // soap bubbles
  document.querySelectorAll(".bubbles").forEach(function(box){
    var n = parseInt(box.getAttribute("data-count") || "8", 10);
    for(var i = 0; i < n; i++){
      var b = document.createElement("span");
      var size = 14 + Math.random() * 46;
      b.style.setProperty("--s", size.toFixed(0) + "px");
      b.style.setProperty("--x", (Math.random() * 100).toFixed(1) + "%");
      b.style.setProperty("--d", (9 + Math.random() * 10).toFixed(1) + "s");
      b.style.setProperty("--delay", (-Math.random() * 18).toFixed(1) + "s");
      b.style.setProperty("--drift", ((Math.random() - .5) * 120).toFixed(0) + "px");
      box.appendChild(b);
    }
  });
  // gentle reveal: only starts after a real visitor scrolls, and only for items below the fold,
  // so bots, screenshot tools and anyone who doesn't scroll always see every word
  var started = false;
  function startReveal(){
    if(started || !("IntersectionObserver" in window)) return; started = true;
    var vh = window.innerHeight;
    var items = document.querySelectorAll(".card, .why-card, .pcard, .loc, ol.steps li, details.qa, .tbl, .book-form, .rv, ul.ticks li");
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add("in"); io.unobserve(e.target); } });
    }, {rootMargin:"0px 0px -6% 0px"});
    items.forEach(function(el, i){
      if(el.getBoundingClientRect().top < vh * 1.05) return;
      el.classList.add("reveal");
      el.style.transitionDelay = ((i % 6) * 60) + "ms";
      io.observe(el);
    });
  }
  ["wheel","touchmove","keydown"].forEach(function(ev){ window.addEventListener(ev, startReveal, {once:true, passive:true}); });
  // hero tag leans toward the cursor
  var tag = document.querySelector(".big-tag"), hero = document.querySelector(".hero");
  if(tag && hero){
    hero.addEventListener("mousemove", function(e){
      var r = hero.getBoundingClientRect();
      var dx = (e.clientX - r.left) / r.width - .5;
      tag.style.setProperty("--lean", (dx * 8).toFixed(2) + "deg");
    });
    hero.addEventListener("mouseleave", function(){ tag.style.setProperty("--lean", "0deg"); });
  }
})();
