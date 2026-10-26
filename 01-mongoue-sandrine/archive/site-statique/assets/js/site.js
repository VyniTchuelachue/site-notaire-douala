/* Étude de Me Sandrine MONGOUE — comportements du site.
   Aucun serveur : les messages s'ouvrent dans WhatsApp ou la messagerie du visiteur. */
(function () {
  "use strict";

  var OFFICE = {
    whatsapp: "237690978098",
    email: "sandrine.mongoue@smnotaire.com"
  };

  var lang = (document.documentElement.lang || "fr").slice(0, 2);

  var T = {
    fr: {
      menu: "Menu",
      close: "Fermer",
      greeting: "Bonjour Maître,",
      preparing: "Je prépare un dossier : ",
      ready: "Pièces prêtes :",
      missing: "Pièces manquantes :",
      none: "(aucune)",
      confirm: "Pouvez-vous me confirmer la liste exacte des pièces ?",
      subjectFile: "Dossier : ",
      status: function (n, total) {
        return "<strong>" + n + "</strong> " + (n > 1 ? "pièces prêtes" : "pièce prête") + " sur " + total;
      },
      name: "Nom : ",
      country: "Pays de résidence : ",
      topic: "Objet : ",
      mode: "Rendez-vous souhaité : ",
      subjectRdv: "Demande de rendez-vous : "
    },
    en: {
      menu: "Menu",
      close: "Close",
      greeting: "Dear Maître MONGOUE,",
      preparing: "I am preparing a file: ",
      ready: "Documents I have:",
      missing: "Documents still missing:",
      none: "(none)",
      confirm: "Could you confirm the exact list of documents required?",
      subjectFile: "File: ",
      status: function (n, total) {
        return "<strong>" + n + "</strong> of " + total + " " + (total > 1 ? "documents" : "document") + " ready";
      },
      name: "Name: ",
      country: "Country of residence: ",
      topic: "Subject: ",
      mode: "Preferred appointment: ",
      subjectRdv: "Appointment request: "
    }
  }[lang === "en" ? "en" : "fr"];

  function openWhatsApp(text) {
    window.open("https://wa.me/" + OFFICE.whatsapp + "?text=" + encodeURIComponent(text), "_blank", "noopener");
  }

  function openEmail(subject, body) {
    window.location.href = "mailto:" + OFFICE.email +
      "?subject=" + encodeURIComponent(subject) +
      "&body=" + encodeURIComponent(body);
  }

  /* ---------- Menu mobile ---------- */

  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("nav");

  if (toggle && nav) {
    var setOpen = function (open) {
      nav.classList.toggle("is-open", open);
      toggle.setAttribute("aria-expanded", String(open));
      toggle.textContent = open ? T.close : T.menu;
    };
    toggle.addEventListener("click", function () {
      setOpen(toggle.getAttribute("aria-expanded") !== "true");
    });
    nav.addEventListener("click", function (e) {
      if (e.target.closest("a")) setOpen(false);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("is-open")) {
        setOpen(false);
        toggle.focus();
      }
    });
  }

  /* ---------- Pièces à fournir : onglets + liste à cocher ---------- */

  var root = document.querySelector("[data-checklists]");

  if (root) {
    var tablist = root.querySelector("[role=tablist]");
    var tabs = Array.prototype.slice.call(root.querySelectorAll("[role=tab]"));
    var panels = Array.prototype.slice.call(root.querySelectorAll("[role=tabpanel]"));
    var footer = root.querySelector(".check-footer");
    var status = root.querySelector(".check-status");
    var current = panels[0];

    var updateStatus = function () {
      var boxes = current.querySelectorAll("input[type=checkbox]");
      var n = current.querySelectorAll("input[type=checkbox]:checked").length;
      status.innerHTML = T.status(n, boxes.length);
    };

    var select = function (tab, focus) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute("aria-selected", String(on));
        t.tabIndex = on ? 0 : -1;
      });
      panels.forEach(function (p) {
        p.hidden = p.id !== tab.getAttribute("aria-controls");
        if (!p.hidden) current = p;
      });
      if (focus) tab.focus();
      updateStatus();
    };

    // Sans JavaScript, toutes les listes restent affichées les unes sous les autres.
    tablist.hidden = false;
    footer.hidden = false;
    select(tabs[0], false);

    tabs.forEach(function (tab, i) {
      tab.addEventListener("click", function () { select(tab, false); });
      tab.addEventListener("keydown", function (e) {
        var next = null;
        if (e.key === "ArrowRight") next = tabs[(i + 1) % tabs.length];
        if (e.key === "ArrowLeft") next = tabs[(i - 1 + tabs.length) % tabs.length];
        if (e.key === "Home") next = tabs[0];
        if (e.key === "End") next = tabs[tabs.length - 1];
        if (next) {
          e.preventDefault();
          select(next, true);
        }
      });
    });

    root.addEventListener("change", function (e) {
      if (e.target.matches("input[type=checkbox]")) updateStatus();
    });

    var buildList = function () {
      var ready = [];
      var missing = [];
      current.querySelectorAll(".checklist label").forEach(function (label) {
        var text = label.textContent.trim();
        (label.querySelector("input").checked ? ready : missing).push("- " + text);
      });
      var title = current.getAttribute("data-title");
      var body = [
        T.greeting,
        "",
        T.preparing + title + ".",
        "",
        T.ready,
        ready.length ? ready.join("\n") : T.none,
        "",
        T.missing,
        missing.length ? missing.join("\n") : T.none,
        "",
        T.confirm
      ].join("\n");
      return { title: title, body: body };
    };

    root.querySelectorAll("[data-send]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var msg = buildList();
        if (btn.getAttribute("data-send") === "whatsapp") openWhatsApp(msg.body);
        else openEmail(T.subjectFile + msg.title, msg.body);
      });
    });
  }

  /* ---------- Formulaire de rendez-vous ---------- */

  var form = document.getElementById("rdv");

  if (form) {
    var channel = "whatsapp";
    form.querySelectorAll("[data-channel]").forEach(function (btn) {
      btn.addEventListener("click", function () { channel = btn.getAttribute("data-channel"); });
    });

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;

      var data = new FormData(form);
      var lines = [T.greeting, ""];
      lines.push(T.name + data.get("nom").trim());
      var pays = (data.get("pays") || "").trim();
      if (pays) lines.push(T.country + pays);
      lines.push(T.topic + data.get("objet"));
      lines.push(T.mode + data.get("mode"));
      lines.push("", data.get("message").trim());
      var body = lines.join("\n");

      if (channel === "email") openEmail(T.subjectRdv + data.get("objet"), body);
      else openWhatsApp(body);
    });
  }
})();
