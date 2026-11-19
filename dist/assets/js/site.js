/* Gaertner Innsbruck – Interaktionen (ohne Abhängigkeiten) */
(function () {
  "use strict";
  var doc = document.documentElement;
  doc.classList.remove("no-js");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* Navigation: Glas-Hintergrund beim Scrollen, mobiles Menü */
  var nav = document.querySelector(".nav");
  var mnav = document.querySelector(".mnav");
  var burger = document.querySelector(".nav__burger");
  function onScroll() {
    if (nav) nav.classList.toggle("is-scrolled", window.scrollY > 24);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
  if (burger && mnav) {
    burger.addEventListener("click", function () {
      var open = !nav.classList.contains("is-open");
      nav.classList.toggle("is-open", open);
      mnav.classList.toggle("is-open", open);
      burger.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.style.overflow = open ? "hidden" : "";
    });
    mnav.addEventListener("click", function (e) {
      if (e.target.closest("a")) {
        nav.classList.remove("is-open");
        mnav.classList.remove("is-open");
        document.body.style.overflow = "";
      }
    });
  }

  /* Einblenden beim Scrollen */
  var rv = document.querySelectorAll(".rv");
  if ("IntersectionObserver" in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    rv.forEach(function (el) { io.observe(el); });
  } else {
    rv.forEach(function (el) { el.classList.add("in"); });
  }

  /* Spotlight-Effekt auf Karten */
  document.querySelectorAll(".spot").forEach(function (el) {
    el.addEventListener("pointermove", function (e) {
      var r = el.getBoundingClientRect();
      el.style.setProperty("--x", (e.clientX - r.left) + "px");
      el.style.setProperty("--y", (e.clientY - r.top) + "px");
    });
  });

  /* Statement: Wort für Wort beim Scrollen */
  document.querySelectorAll("[data-words]").forEach(function (el) {
    var words = el.textContent.trim().split(/\s+/);
    el.textContent = "";
    words.forEach(function (w, i) {
      var s = document.createElement("span");
      s.className = "w";
      s.textContent = w;
      el.appendChild(s);
      if (i < words.length - 1) el.appendChild(document.createTextNode(" "));
    });
    var spans = el.querySelectorAll(".w");
    if (reduce) { spans.forEach(function (s) { s.classList.add("on"); }); return; }
    function update() {
      var r = el.getBoundingClientRect();
      var vh = window.innerHeight;
      var p = (vh * 0.85 - r.top) / (r.height + vh * 0.35);
      p = Math.max(0, Math.min(1, p));
      var n = Math.round(p * spans.length);
      spans.forEach(function (s, i) { s.classList.toggle("on", i < n); });
    }
    window.addEventListener("scroll", update, { passive: true });
    window.addEventListener("resize", update);
    update();
  });

  /* Zähler in Kennzahlen */
  document.querySelectorAll("[data-count]").forEach(function (el) {
    var target = parseInt(el.getAttribute("data-count"), 10);
    if (reduce || !("IntersectionObserver" in window)) { el.textContent = target; return; }
    el.textContent = "0";
    var o = new IntersectionObserver(function (en) {
      if (!en[0].isIntersecting) return;
      o.disconnect();
      var t0 = performance.now(), dur = 1600;
      (function tick(t) {
        var k = Math.min(1, (t - t0) / dur);
        var e = 1 - Math.pow(1 - k, 4);
        el.textContent = Math.round(target * e);
        if (k < 1) requestAnimationFrame(tick);
      })(t0);
    });
    o.observe(el);
  });

  /* Tabs (Zubehör) */
  document.querySelectorAll("[role=tablist]").forEach(function (list) {
    var tabs = list.querySelectorAll("[role=tab]");
    tabs.forEach(function (tab) {
      tab.addEventListener("click", function () {
        tabs.forEach(function (t) {
          var sel = t === tab;
          t.setAttribute("aria-selected", sel ? "true" : "false");
          document.getElementById(t.getAttribute("aria-controls")).hidden = !sel;
        });
      });
    });
  });

  /* Lightbox für Galerien */
  var lb, lbImg, lbCount, group = [], idx = 0, lastFocus;
  function buildLb() {
    lb = document.createElement("div");
    lb.className = "lb";
    lb.setAttribute("role", "dialog");
    lb.setAttribute("aria-modal", "true");
    lb.setAttribute("aria-label", "Bildansicht");
    var ic = function (d) { return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="' + d + '"/></svg>'; };
    lb.innerHTML = '<img alt="">' +
      '<button class="lb__btn lb__close" aria-label="Schließen">' + ic("M6 6l12 12M18 6L6 18") + '</button>' +
      '<button class="lb__btn lb__prev" aria-label="Vorheriges Bild">' + ic("M15 18l-6-6 6-6") + '</button>' +
      '<button class="lb__btn lb__next" aria-label="Nächstes Bild">' + ic("M9 18l6-6-6-6") + '</button>' +
      '<div class="lb__count"></div>';
    document.body.appendChild(lb);
    lbImg = lb.querySelector("img");
    lbCount = lb.querySelector(".lb__count");
    lb.querySelector(".lb__close").onclick = close;
    lb.querySelector(".lb__prev").onclick = function () { show(idx - 1); };
    lb.querySelector(".lb__next").onclick = function () { show(idx + 1); };
    lb.addEventListener("click", function (e) { if (e.target === lb) close(); });
    document.addEventListener("keydown", function (e) {
      if (!lb.classList.contains("is-open")) return;
      if (e.key === "Escape") close();
      if (e.key === "ArrowLeft") show(idx - 1);
      if (e.key === "ArrowRight") show(idx + 1);
    });
  }
  function show(i) {
    idx = (i + group.length) % group.length;
    var b = group[idx];
    var im = b.querySelector("img");
    lbImg.src = b.getAttribute("data-full") || im.currentSrc || im.src;
    lbImg.alt = im.alt;
    lbCount.textContent = (idx + 1) + " / " + group.length;
    var multi = group.length > 1;
    lb.querySelector(".lb__prev").hidden = !multi;
    lb.querySelector(".lb__next").hidden = !multi;
  }
  function close() {
    lb.classList.remove("is-open");
    document.body.style.overflow = "";
    if (lastFocus) lastFocus.focus();
  }
  document.addEventListener("click", function (e) {
    var b = e.target.closest("[data-lb]");
    if (!b) return;
    e.preventDefault();
    if (!lb) buildLb();
    lastFocus = b;
    var name = b.getAttribute("data-lb");
    group = Array.prototype.slice.call(document.querySelectorAll('[data-lb="' + name + '"]'));
    show(group.indexOf(b));
    lb.classList.add("is-open");
    document.body.style.overflow = "hidden";
    lb.querySelector(".lb__close").focus();
  });

  /* Galerie aufklappen */
  document.querySelectorAll("[data-expand]").forEach(function (b) {
    b.addEventListener("click", function () {
      var g = document.getElementById(b.getAttribute("data-expand"));
      if (g) g.classList.remove("is-collapsed");
      b.parentNode.remove();
    });
  });

  /* Jahr im Footer */
  var y = document.querySelector("[data-year]");
  if (y) y.textContent = new Date().getFullYear();
})();
