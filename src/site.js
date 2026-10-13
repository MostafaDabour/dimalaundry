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
  // forms send the request to WhatsApp with every field filled in
  document.querySelectorAll(".js-wa-form").forEach(function(f){
    f.addEventListener("submit", function(e){
      e.preventDefault();
      if(!f.reportValidity()) return;
      var lines = [f.getAttribute("data-intro")];
      new FormData(f).forEach(function(v, k){ if(String(v).trim()) lines.push(k + ": " + v); });
      var url = "https://wa.me/" + f.getAttribute("data-wa") + "?text=" + encodeURIComponent(lines.join("\n"));
      window.open(url, "_blank") || (window.location.href = url);
    });
  });
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
