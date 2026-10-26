(function () {
  var D = JSON.parse(document.getElementById("site-data").textContent);
  var M = D.msg;

  function wa(text) {
    if (!D.whatsapp) return;
    window.open("https://wa.me/" + D.whatsapp + "?text=" + encodeURIComponent(text), "_blank", "noopener");
  }
  function mail(subject, body) {
    if (!D.email) return;
    window.location.href = "mailto:" + D.email + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
  }

  // Menu mobile
  var toggle = document.querySelector("[data-nav-toggle]");
  var nav = document.getElementById("nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      document.body.classList.toggle("nav-open", !open);
    });
    nav.addEventListener("click", function (e) {
      if (e.target.closest("a")) {
        toggle.setAttribute("aria-expanded", "false");
        document.body.classList.remove("nav-open");
      }
    });
  }

  // En-tête compact au défilement
  var header = document.querySelector("[data-header]");
  function onScroll() { if (header) header.classList.toggle("is-scrolled", window.scrollY > 24); }
  window.addEventListener("scroll", onScroll, { passive: true }); onScroll();

  // Pièces à fournir
  var box = document.querySelector("[data-docs]");
  if (box) {
    var tabs = box.querySelectorAll("[data-tab]");
    var panels = box.querySelectorAll("[data-panel]");
    function show(key) {
      tabs.forEach(function (t) { t.setAttribute("aria-selected", String(t.dataset.tab === key)); });
      panels.forEach(function (p) { p.hidden = p.dataset.panel !== key; });
    }
    tabs.forEach(function (t) {
      t.addEventListener("click", function () { show(t.dataset.tab); });
      t.addEventListener("keydown", function (e) {
        if (e.key !== "ArrowRight" && e.key !== "ArrowLeft") return;
        var arr = Array.prototype.slice.call(tabs), i = arr.indexOf(t);
        var n = arr[(i + (e.key === "ArrowRight" ? 1 : arr.length - 1)) % arr.length];
        n.focus(); show(n.dataset.tab);
      });
    });
    function fromHash() { var k = location.hash.slice(1); if (box.querySelector('[data-tab="' + k + '"]')) { show(k); box.scrollIntoView({ block: "start" }); } }
    window.addEventListener("hashchange", fromHash); fromHash();
    panels.forEach(function (p) {
      p.addEventListener("change", function () {
        p.querySelector("[data-count]").textContent = p.querySelectorAll("input:checked").length;
      });
    });
    function current() {
      var p = Array.prototype.find.call(panels, function (x) { return !x.hidden; });
      var ready = [], missing = [];
      p.querySelectorAll("input").forEach(function (i) { (i.checked ? ready : missing).push("- " + i.value); });
      var text = [M.hello, "", M.file + p.dataset.title, "", M.ready, ready.length ? ready.join("\n") : M.none, "", M.missing, missing.length ? missing.join("\n") : M.none, "", M.confirm].join("\n");
      return { title: p.dataset.title, text: text };
    }
    box.querySelectorAll("[data-docs-send]").forEach(function (b) {
      b.addEventListener("click", function () {
        var c = current();
        if (b.dataset.docsSend === "wa") wa(c.text); else mail(M.dossier + c.title, c.text);
      });
    });
  }

  // Formulaire de contact
  var form = document.querySelector("[data-contact-form]");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var f = new FormData(form);
      var how = (e.submitter && e.submitter.value) || (D.whatsapp ? "wa" : "mail");
      var lines = [M.hello, "", M.name + f.get("name")];
      if (f.get("country")) lines.push(M.country + f.get("country"));
      lines.push(M.topic + f.get("subject"));
      if (f.get("message")) lines.push("", f.get("message"));
      var text = lines.join("\n");
      if (how === "wa") wa(text); else mail(M.rdv + f.get("subject"), text);
    });
  }

  // Suivi de dossier
  var track = document.querySelector("[data-track-form]");
  if (track) {
    track.addEventListener("submit", function (e) {
      e.preventDefault();
      var f = new FormData(track);
      var text = [M.hello, "", M.name + f.get("name"), M.dossier + f.get("ref"), "", D.trackAsk].join("\n");
      if (D.whatsapp) wa(text); else mail(M.dossier + f.get("ref"), text);
    });
  }
})();
