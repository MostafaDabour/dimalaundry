# Blog agent: how to write, review and publish a Dima Laundry post

Repo: MostafaDabour/dimalaundry (public). Site: https://www.dimalaundry.com, hosted on Cloudflare Workers, deploys automatically about 1 minute after a push to `main`.
The owner reviews every post before it goes live. Never publish without the owner saying so in chat.

## 1. Set up
- Attach the repo with push access (add_repo owner MostafaDabour, repo dimalaundry, access push), clone it, `cd` into it.
- Read `src/content.py`, `src/prices.json`, `src/blog_posts.py` (style and format), `src/blog_drafts.py` and `docs/blog-plan.md`.

## 2. Check the queue
- If `DRAFTS` in `src/blog_drafts.py` already holds 2 or more posts, do not write another. Send the owner the preview links of the waiting drafts and ask for a review. Stop.

## 3. Write the draft
- Take the first `[ ]` topic in `docs/blog-plan.md`.
- Write it as one dict in `DRAFTS` with the same fields as `POSTS`: slug, short, title, desc, h1, answer, sections, faqs, links, plus `"date": "<today YYYY-MM-DD>"`.
- Rules:
  - `answer`: 40 to 70 words that directly answer the title question, so AI assistants can quote it. Name Dima Laundry once.
  - 4 to 6 sections, 800 to 1300 words in total, short paragraphs and lists, written for Dubai residents.
  - Every price, branch, phone number, hour or service claim must come from `src/content.py` or `src/prices.json`. Never invent prices, statistics, awards, customer quotes or turnaround promises. If a fact is not in the repo, leave it out or phrase it as "ask the team".
  - 3 to 5 FAQs. 2 to 4 `links` to existing pages (use the pages listed for the topic, check they exist in `public/`).
  - Never use em dashes or en dashes. Plain, specific, no hype.
- Mark the topic `[d]` in `docs/blog-plan.md`.

## 4. Build, check, push
- `python3 src/build.py` must succeed (it rejects em dashes). Confirm `public/preview/<slug>/index.html` exists and that the slug does not appear in `public/sitemap.xml`.
- Commit "Blog draft: <title>" and push to `main`.
- Wait about 2 minutes, then fetch `https://www.dimalaundry.com/preview/<slug>` to confirm it is live.

## 5. Ask for review
Send the owner (with SendUserMessage) the title, the preview link, the target search phrase and a 2 line summary, and say: reply "ok" to publish, or tell me what to change. Then stop and wait.

## 6. When the owner replies
- Changes: edit the draft, rebuild, push, send the new preview link.
- "ok": move the dict from `DRAFTS` to the TOP of `POSTS` in `src/blog_posts.py`, set `date` to today, mark the topic `[x] <date>` and move it under "Published" in the plan. Build, commit "Publish blog: <title>", push. After about 2 minutes confirm `https://www.dimalaundry.com/blog/<slug>` loads. Then submit `https://www.dimalaundry.com/blog/<slug>` and `https://www.dimalaundry.com/blog` with the OpenSEO IndexNow tool (project "Dima Laundry"). Tell the owner it is live, with the link, and remind them to request indexing for it in Google Search Console.
