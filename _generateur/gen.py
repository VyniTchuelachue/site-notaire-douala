import json, os, re, shutil, copy, html
from urllib.parse import quote
from jinja2 import Environment, FileSystemLoader
import sites as S
from content import T, HERO, PAGES, PAGE_INTRO, HOME, SERVICE_DETAILS, DETAIL_LABEL, FAQ_EXTRA, CREDITS

OUT = "/mnt/user-data/outputs/notaires"
HERE = os.path.dirname(os.path.abspath(__file__))

PAL = {
 "navy-gold":   dict(bg="#fbfaf7", surface="#ffffff", tint="#f3efe6", ink="#14213a", muted="#5b6475", line="#e5e0d6", line_strong="#c9c3b6", brand="#1d3157", brand_2="#14213a", on_brand="#ffffff", accent="#c5a35a", dark="#0f1a30", on_dark="#f5f1e8", on_dark_muted="#b9bfcc"),
 "forest-brass":dict(bg="#fbfbf8", surface="#ffffff", tint="#eef1ea", ink="#17261f", muted="#56635c", line="#e1e5de", line_strong="#c3cbc1", brand="#24483a", brand_2="#17302a", on_brand="#ffffff", accent="#c49a55", dark="#13241d", on_dark="#f2efe6", on_dark_muted="#b4c0b8"),
 "aubergine":   dict(bg="#fcfafb", surface="#ffffff", tint="#f3eef3", ink="#241a2b", muted="#625869", line="#e6dfe6", line_strong="#cbc0cb", brand="#4a2b55", brand_2="#331d3c", on_brand="#ffffff", accent="#c9a66b", dark="#21152a", on_dark="#f6f0f4", on_dark_muted="#c0b3c4"),
 "burgundy":    dict(bg="#fffdf9", surface="#ffffff", tint="#f6eee7", ink="#241514", muted="#6a5a57", line="#eadfd8", line_strong="#d3c3ba", brand="#7c1f2c", brand_2="#5c1520", on_brand="#ffffff", accent="#c9893a", dark="#2a1416", on_dark="#f7efe9", on_dark_muted="#cdb8b2"),
 "terracotta":  dict(bg="#fffcf9", surface="#ffffff", tint="#f7ece4", ink="#2a1c16", muted="#6b5b53", line="#ecdfd6", line_strong="#d6c4b8", brand="#a74a24", brand_2="#843a1b", on_brand="#ffffff", accent="#2f5d50", dark="#23332e", on_dark="#f3eee8", on_dark_muted="#b8c4bf"),
 "harbor-sand": dict(bg="#fcfbf8", surface="#ffffff", tint="#efeae0", ink="#142430", muted="#56636d", line="#e3ded3", line_strong="#c9c2b4", brand="#1f4e6b", brand_2="#163a50", on_brand="#ffffff", accent="#c2995b", dark="#102230", on_dark="#f1ede4", on_dark_muted="#aebbc4"),
 "ink-lime":    dict(bg="#fafaf7", surface="#ffffff", tint="#eef3e4", ink="#0e1a22", muted="#55616a", line="#e2e6df", line_strong="#c5ccc3", brand="#0e1a22", brand_2="#000000", on_brand="#ffffff", accent="#c6f24e", dark="#0b1820", on_dark="#f2f5ee", on_dark_muted="#9fb0b8"),
 "night-coral": dict(bg="#fbfaf9", surface="#ffffff", tint="#fbeceb", ink="#121a2e", muted="#596075", line="#e7e3e2", line_strong="#cdc6c4", brand="#c8463c", brand_2="#a63930", on_brand="#ffffff", accent="#ff7a6b", dark="#0f1629", on_dark="#f5f3f6", on_dark_muted="#a9afc2"),
 "teal":        dict(bg="#fbfdfc", surface="#ffffff", tint="#e8f4f2", ink="#12302e", muted="#55706c", line="#dcebe8", line_strong="#bcd5d0", brand="#11756f", brand_2="#0b5a55", on_brand="#ffffff", accent="#f2c94c", dark="#0d2a28", on_dark="#eef7f5", on_dark_muted="#a9c6c1"),
 "sun":         dict(bg="#fffdf8", surface="#ffffff", tint="#fff4d6", ink="#2b2410", muted="#6b6250", line="#f0e6cd", line_strong="#dccfae", brand="#9a6212", brand_2="#7a4d0e", on_brand="#ffffff", accent="#3c8d7a", dark="#2b2410", on_dark="#fbf6e9", on_dark_muted="#cfc5a9"),
 "mauve":       dict(bg="#fdfbfc", surface="#ffffff", tint="#f5edf3", ink="#2c1c2a", muted="#6c5a68", line="#ece0e9", line_strong="#d4c2cf", brand="#8a3f74", brand_2="#6b2f5a", on_brand="#ffffff", accent="#e2a87d", dark="#2a1a28", on_dark="#f8f1f5", on_dark_muted="#cbb6c5"),
 "emerald":     dict(bg="#ffffff", surface="#f7faf8", tint="#e7f5ee", ink="#10291f", muted="#53685f", line="#dfe9e4", line_strong="#bfd2c8", brand="#0f7a55", brand_2="#0a5c40", on_brand="#ffffff", accent="#f2b01e", dark="#0c2a1f", on_dark="#eef7f2", on_dark_muted="#a5c2b4"),
 "cobalt":      dict(bg="#ffffff", surface="#f7f9fd", tint="#e9effc", ink="#101c36", muted="#566079", line="#e1e6f1", line_strong="#c2cbe0", brand="#2449b8", brand_2="#1a378f", on_brand="#ffffff", accent="#f2994a", dark="#0e1a38", on_dark="#eef2fb", on_dark_muted="#a7b3d1"),
 "ochre":       dict(bg="#fffefb", surface="#fbf8f1", tint="#f8f0de", ink="#2a210f", muted="#6a604c", line="#ece4d1", line_strong="#d6caaf", brand="#8f600e", brand_2="#6f4a0a", on_brand="#ffffff", accent="#2d6a8a", dark="#241c0c", on_dark="#faf5e9", on_dark_muted="#cbbf9f"),
 "slate":       dict(bg="#ffffff", surface="#f6f7fa", tint="#edf0f5", ink="#17202e", muted="#5a6475", line="#e2e6ed", line_strong="#c6cdd8", brand="#3c4f7a", brand_2="#26355a", on_brand="#ffffff", accent="#e0b45c", accent_ink="#8a6420", dark="#141d2e", on_dark="#eef1f6", on_dark_muted="#a8b2c4"),
 "harbor":      dict(bg="#ffffff", surface="#f5f8fa", tint="#e9f1f6", ink="#0f2230", muted="#536572", line="#dfe7ec", line_strong="#c0ced7", brand="#1d6896", brand_2="#164f73", on_brand="#ffffff", accent="#f0a04b", accent_ink="#a25e15", dark="#0d1f2c", on_dark="#edf3f7", on_dark_muted="#a3b6c3"),
 "violet":      dict(bg="#fbfaff", surface="#ffffff", tint="#efeafb", ink="#1a1230", muted="#5d5672", line="#e6e1f2", line_strong="#cbc3e0", brand="#4b2e83", brand_2="#3a2367", on_brand="#ffffff", accent="#c3b1ff", dark="#170f2b", on_dark="#f4f1fb", on_dark_muted="#b3a9cc"),
 "pine":        dict(bg="#ffffff", surface="#f5f8f6", tint="#e9f2ee", ink="#12261f", muted="#536860", line="#dee8e3", line_strong="#bfd0c8", brand="#2e6b55", brand_2="#1f4b3c", on_brand="#ffffff", accent="#d9b35b", accent_ink="#7f6119", dark="#102019", on_dark="#eef5f1", on_dark_muted="#a6bdb3"),
}

FONTS = {
 "navy-gold":   ("Cormorant Garamond", "500;600", "Lato", "400;700", 500, "0"),
 "forest-brass":("Playfair Display", "500;600", "Source Sans 3", "400;600;700", 500, "0"),
 "aubergine":   ("Libre Baskerville", "400;700", "Karla", "400;600;700", 400, "0"),
 "burgundy":    ("Fraunces", "400;500;600", "Inter", "400;500;600", 500, "-.02em"),
 "terracotta":  ("DM Serif Display", "400", "DM Sans", "400;500;700", 400, "-.01em"),
 "harbor-sand": ("Newsreader", "400;500;600", "Public Sans", "400;500;600", 500, "-.015em"),
 "ink-lime":    ("Archivo", "700;800", "Archivo", "400;500;600", 800, "-.035em"),
 "night-coral": ("Bebas Neue", "400", "Montserrat", "400;500;600", 400, ".01em"),
 "teal":        ("Manrope", "700;800", "Open Sans", "400;600", 800, "-.02em"),
 "sun":         ("Outfit", "600;700", "Nunito Sans", "400;600;700", 700, "-.02em"),
 "mauve":       ("Lora", "500;600", "Mulish", "400;600;700", 600, "-.01em"),
 "emerald":     ("DM Sans", "700", "Heebo", "400;500;600", 700, "-.02em"),
 "cobalt":      ("Plus Jakarta Sans", "700;800", "Plus Jakarta Sans", "400;500;600", 800, "-.025em"),
 "ochre":       ("Sora", "600;700", "Inter", "400;500;600", 600, "-.02em"),
 "slate":       ("Unna", "700", "Hind", "400;500;600", 700, "0"),
 "harbor":      ("IBM Plex Serif", "500;600", "IBM Plex Sans", "400;500;600", 600, "-.01em"),
 "violet":      ("Space Grotesk", "600;700", "Inter", "400;500;600", 700, "-.03em"),
 "pine":        ("Spectral", "500;600", "Work Sans", "400;500;600", 600, "-.01em"),
}

def fonts_url(pal):
    h, hw, b, bw, *_ = FONTS[pal]
    fam = lambda n, w: "family=" + n.replace(" ", "+") + ":wght@" + w
    parts = [fam(h, hw)] if h == b else [fam(h, hw), fam(b, bw)]
    if h == b:
        ws = sorted(set(hw.split(";") + bw.split(";")), key=int)
        parts = [fam(h, ";".join(ws))]
    return "https://fonts.googleapis.com/css2?" + "&".join(parts) + "&display=swap"

def css_vars(pal):
    p = PAL[pal]; h, _, b, _, w, tr = FONTS[pal]
    v = {k.replace("_", "-"): val for k, val in p.items()}
    v.setdefault("accent-ink", p["accent"])
    serif = any(x in h for x in ["Garamond", "Playfair", "Baskerville", "Fraunces", "Serif", "Newsreader", "Lora", "Unna", "Spectral"])
    v["font-head"] = f'"{h}", {"Georgia, serif" if serif else "system-ui, sans-serif"}'
    v["font-body"] = f'"{b}", system-ui, -apple-system, "Segoe UI", sans-serif'
    v["head-weight"] = str(w); v["head-tracking"] = tr
    if pal == "night-coral":
        v["head-case"] = "uppercase"
    return ":root{" + ";".join(f"--{k}:{val}" for k, val in v.items()) + "}\n"

I = lambda d: f'<svg class="i" viewBox="0 0 24 24" aria-hidden="true">{d}</svg>'
ICONS = {
 "phone": I('<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>'),
 "chat": I('<path d="M21 12a8.5 8.5 0 0 1-12.6 7.4L3 21l1.6-5.2A8.5 8.5 0 1 1 21 12z"/><path d="M8.5 10.5h7M8.5 13.5h4.5"/>'),
 "calendar": I('<rect x="3.5" y="5" width="17" height="15.5" rx="2"/><path d="M3.5 10h17M8 3v4M16 3v4"/>'),
 "pin": I('<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>'),
 "mail": I('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.5 6.5 8.5 7 8.5-7"/>'),
 "clock": I('<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>'),
 "arrow": I('<path d="M5 12h14M13 6l6 6-6 6"/>'),
 "file": I('<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h4"/>'),
 "check": I('<circle cx="12" cy="12" r="8.5"/><path d="m8.5 12.5 2.5 2.5 4.5-5"/>'),
 "shield": I('<path d="M12 3 4.5 6v5.5c0 4.6 3.2 8.3 7.5 9.5 4.3-1.2 7.5-4.9 7.5-9.5V6z"/><path d="m9 12 2 2 4-4"/>'),
 "user": I('<circle cx="12" cy="8.5" r="3.5"/><path d="M5 20c.8-3.6 3.6-5.5 7-5.5s6.2 1.9 7 5.5"/>'),
 "svc-terrain": I('<path d="M3 11.5 12 4l9 7.5"/><path d="M5.5 10v10h13V10"/><path d="M10 20v-5h4v5"/>'),
 "svc-succession": I('<circle cx="12" cy="5.5" r="2.5"/><circle cx="6" cy="18.5" r="2.5"/><circle cx="18" cy="18.5" r="2.5"/><path d="M12 8v4M12 12H6v4M12 12h6v4"/>'),
 "svc-famille": I('<circle cx="9" cy="13" r="5"/><circle cx="15" cy="13" r="5"/><path d="M10.5 4.5 12 6l1.5-1.5"/>'),
 "svc-societe": I('<rect x="3" y="7.5" width="18" height="12.5" rx="2"/><path d="M9 7.5V5.5a1.5 1.5 0 0 1 1.5-1.5h3A1.5 1.5 0 0 1 15 5.5v2M3 13h18M11 13v2h2v-2"/>'),
 "svc-procuration": I('<path d="M4 20h4L19 9a2.8 2.8 0 0 0-4-4L4 16z"/><path d="m13.5 6.5 4 4M14 20h6"/>'),
 "svc-copie": I('<rect x="8" y="8" width="12" height="13" rx="2"/><path d="M16 8V5a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h2"/><circle cx="14" cy="14.5" r="2.5"/>'),
}

def seal(initials, inline=True, colors=None):
    c = colors or {}
    ring = c.get("ring", "var(--brand)"); fg = c.get("fg", "var(--brand)"); acc = c.get("acc", "var(--accent)"); bg = c.get("bg", "var(--bg)")
    font = c.get("font", "var(--font-head)")
    size = 36 if len(initials) <= 2 else 26
    return (f'<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">'
            f'<circle cx="50" cy="50" r="47" fill="{bg}" stroke="{ring}" stroke-width="3"/>'
            f'<circle cx="50" cy="50" r="39" fill="none" stroke="{acc}" stroke-width="1.2" stroke-dasharray="2 3"/>'
            f'<text x="50" y="50" text-anchor="middle" dominant-baseline="central" font-family="{font}" font-size="{size}" font-weight="600" fill="{fg}" letter-spacing="1">{html.escape(initials)}</text>'
            f'</svg>')

def frtypo(x):
    if isinstance(x, str):
        x = re.sub(r" ([:;!?»])", " \\1", x)
        x = re.sub(r"« ", "« ", x)
        x = x.replace("'", "’")
        return x
    if isinstance(x, list): return [frtypo(i) for i in x]
    if isinstance(x, tuple): return tuple(frtypo(i) for i in x)
    if isinstance(x, dict): return {k: (frtypo(v) if k not in ("lang",) else v) for k, v in x.items()}
    return x

def office_intro(s, lang):
    fr = lang == "fr"
    if s.get("firm"):
        return (f"{s['name']} est une étude notariale installée à {s['quartier']}, Douala, avenue de la Liberté."
                if fr else f"{s['name']} is a notary office in {s['quartier']}, Douala, on Avenue de la Liberté.")
    place, num, suf = S.charge_short(s["charge"])
    if fr:
        t = f"{s['name']} est notaire titulaire de la {num}{suf} charge de {place}, à {s['quartier']}."
        if s.get("since_note"): t += f" Notaire depuis {s['since_note']}."
        if s.get("chamber"): t += " Elle a présidé la Chambre nationale des notaires du Cameroun."
        else: t += " " + T["fr"]["office_member"]
        if s.get("minutes"): t += f" L'étude conserve les minutes de {s['minutes']} : vous pouvez y demander la copie d'un acte qu'il a reçu."
    else:
        t = f"{s['name']} holds {S.charge_en(s['charge'])}, in {s['quartier']}."
        if s.get("since_note"): t += f" A notary since {s['since_note']}."
        if s.get("chamber"): t += " She has served as President of the National Chamber of Notaries of Cameroon."
        else: t += " " + T["en"]["office_member"]
        if s.get("minutes"): t += f" The office keeps the records of {s['minutes']}: you can request a copy of a deed he received."
    return t

ABROAD = {"01-mongoue-sandrine-demo", "03-grace-nkake-bollanga", "04-dooh-collins-ekollo-regine", "10-nova-notaire-associes", "14-baiye-daniel-bechem"}

# ---------- Photos (Unsplash, licence Unsplash) ----------
PH = {
 "sign_a": "photo-1450101499163-c8848c66ca85", "sign_b": "photo-1521791055366-0d553872125f", "sign_c": "photo-1648712898089-4435bc87b587",
 "keys_house": "photo-1560518883-ce09059eeffa", "keys": "photo-1575908539614-ff89490f4a78", "family_house": "photo-1758227365187-016878604d94",
 "pen_ink": "photo-1455390582262-044cdead277a", "pen_gold": "photo-1518674660708-0e2c0473e68e", "pen_black": "photo-1473186505569-9c61870c11f9", "pen_book": "photo-1559557809-e9b6eabeabfc",
 "wouri": "photo-1576487194710-67873008c0c6", "sunset": "photo-1474302173007-293973cab927",
 "office_glass": "photo-1643267514395-b36b3f7e8281", "office_green": "photo-1719941032563-75921fe474fc", "office_modern": "photo-1765371512336-99c2b1c6975f",
 "justice": "photo-1589829545856-d10d557cf95f", "books_old": "photo-1765969934461-2f945e5aacb8", "library": "photo-1505664063603-28e48ca204eb",
 "hand_laptop": "photo-1672380135241-c024f7fbfa13",
 "hearts": "photo-1761111566863-708fd5436f17", "baby": "photo-1687277284371-ce4bb9d8f463",
 "street": "photo-1659947234309-804b7fa01cf2", "brick_house": "photo-1787672358119-25cb4c768d14",
}
def U(key, w=1600):
    return f"https://images.unsplash.com/{PH.get(key, key)}?auto=format&fit=crop&w={w}&q=70"

HERO_IMG = {
 "02-njongue-etame-florence": "justice", "03-grace-nkake-bollanga": "pen_gold", "04-dooh-collins-ekollo-regine": "library",
 "05-alam-eboutou-marquise": "sign_a", "06-kamako-biabo-evelyne": "family_house", "07-nkono-lunduobe-marie-jeanne": "sign_b",
 "08-nkoue-mawafo-fonkoua-marie-louise": "office_green", "09-mbollo-mbassi-dikongue-anne-marie": "pen_book", "10-nova-notaire-associes": "office_modern",
 "11-moukory-eyango-jean-jacques": "street", "12-enguele-dipanda-gisele": "sign_c", "13-ngalla-joseph": "hand_laptop",
 "14-baiye-daniel-bechem": "library", "15-tongoue-hamedak-jacques": "wouri", "16-wansi-kameni-narcisse": "pen_ink",
 "17-ngo-yon-benga-fride-epoune": "keys_house", "01-mongoue-sandrine-demo": "sign_b", "18-nzue-rose-biteck-lima": "pen_black",
}
SVC_POOL = {
 "terrain": ["keys_house", "brick_house", "keys"], "succession": ["family_house", "books_old", "pen_book"],
 "famille": ["baby", "hearts", "baby"], "societe": ["hand_laptop", "office_modern", "office_glass"],
 "procuration": ["pen_ink", "sign_c", "pen_black"], "copie": ["library", "pen_gold", "books_old"],
}
OFFICE_POOL = ["office_green", "office_glass", "office_modern", "library"]
BAND_POOL = ["sign_a", "sign_b", "pen_ink", "sign_c", "pen_book"]
BANNER_POOL = ["library", "sign_a", "pen_gold", "office_glass", "books_old", "pen_black", "sign_b", "street", "justice", "office_green"]

def images(s, i):
    rot = lambda pool, k=0: pool[(i + k) % len(pool)]
    svc = {k: rot(v) for k, v in SVC_POOL.items()}
    hero = HERO_IMG[s["slug"]]
    office = rot(OFFICE_POOL)
    if office == hero: office = rot(OFFICE_POOL, 1)
    band = rot(BAND_POOL)
    if band == hero: band = rot(BAND_POOL, 1)
    ban = {k: rot(BANNER_POOL, j) for j, k in enumerate(["services", "docs", "office", "faq", "contact"])}
    if s["slug"] in ("15-tongoue-hamedak-jacques", "16-wansi-kameni-narcisse", "17-ngo-yon-benga-fride-epoune"):
        ban["contact"] = "wouri"
    return {"hero": hero, "office": office, "band": band, "svc": svc, "banner": ban, "wouri": "wouri"}

env = Environment(loader=FileSystemLoader(os.path.join(HERE, "templates")), autoescape=True, trim_blocks=True, lstrip_blocks=True)
env.globals.update(U=U, ICONS=ICONS)
TPL = {"home": "home.html", "services": "services.html", "docs": "docs.html", "office": "office.html", "faq": "faq.html", "contact": "contact.html"}

def render(s, lang, page, root, other_lang, other_prefix, IMG):
    fr = lang == "fr"
    tx = lambda x: frtypo(x) if fr else x
    t = tx(copy.deepcopy(T[lang]))
    nav = [(k, f, lab) for k, f, lab in tx(PAGES[lang])]
    P = {k: f for k, f, _ in nav}
    other = {k: f for k, f, _ in PAGES[other_lang]}
    hero = tx(HERO[s["slug"]][0 if fr else 1])
    intro = tx(office_intro(s, lang))
    js = {"whatsapp": s["whatsapp"], "email": s["email"], "msg": t["msg"],
          "trackAsk": tx("Pouvez-vous me faire un point d'étape sur ce dossier ?") if fr else "Could you give me a progress update on this file?"}
    base_meta = (f"{s['name']}, notaire à Douala ({s['quartier']}) : terrains, successions, famille, entreprises." if fr
                 else f"{s['name']}, notary in Douala ({s['quartier']}): land, estates, family, business.")
    if s.get("firm"):
        base_meta = base_meta.replace("notaire à Douala", "étude notariale à Douala").replace("notary in Douala", "notary office in Douala")
    PI = tx(PAGE_INTRO[lang])
    label = dict((k, lab) for k, _, lab in nav)[page]
    title = f"{s['name']} — {s['role_fr'] if fr else s['role_en']}" if page == "home" else f"{label} — {s['name']}"
    meta = base_meta if page == "home" else f"{PI[page][1]} {base_meta}"
    return env.get_template(TPL[page]).render(
        t=t, s=s, page=page, NAV=nav, P=P, PI=PI, H=tx(HOME[lang]), DET=tx(SERVICE_DETAILS[lang]), DL=DETAIL_LABEL[lang],
        faq_all=t["faq"] + tx(FAQ_EXTRA[lang]), hero_txt=hero, office_intro=intro, seal=seal(s["initials"]), IMG=IMG,
        root=root, other_href=other_prefix + other[page], other_hreflang=other_lang, credits=CREDITS[lang],
        fonts_url=fonts_url(s["palette"]), meta_desc=meta, page_title=title,
        js_data=json.dumps(js, ensure_ascii=False).replace("</", "<\\/"))

def favicon(s):
    p = PAL[s["palette"]]
    return seal(s["initials"], colors={"ring": p["brand"], "fg": p["brand"], "acc": p["accent"], "bg": "#ffffff", "font": "Georgia, serif"})

def claude_md(s):
    sh = s["sheet"]
    langs = "anglais à la racine (`index.html`), français dans `fr/`" if s.get("en_first") else "français à la racine (`index.html`), anglais dans `en/`"
    research = "\n".join(f"- {r}" for r in s.get("research", []))
    return f"""# Contexte pour Claude — {s['name']}

Site vitrine de démonstration pour **{s['name']}**, {s['role_fr'].lower()}. Il sert à la prospection : on le montre à l'étude pour lui proposer un site.
Ne jamais le mettre en ligne sous le nom de l'étude avant un accord signé.

## Fichiers
- Site statique, sans build : ouvrir `index.html` dans un navigateur suffit (connexion internet nécessaire pour les photos, les polices et la carte).
- Six pages par langue : accueil (`index.html`), domaines, pièces à fournir, l'étude, questions, contact. En anglais : index, services, documents, office, faq, contact.
- Langues : {langs}.
- Photos d'illustration : Unsplash (licence Unsplash, usage commercial libre, sans attribution obligatoire), chargées depuis images.unsplash.com. Aucune ne montre de visage reconnaissable. Photos utilisées : {', '.join(sorted(set([s['images']['hero'], s['images']['office'], s['images']['band']] + list(s['images']['svc'].values()) + list(s['images']['banner'].values()))))} (voir `PH` dans le générateur pour les identifiants).
- `assets/style.css` : variables de couleurs et polices en tête de fichier (`:root`), puis styles communs et thème.
- `assets/site.js` : menu mobile, onglets « pièces à fournir », envoi des formulaires vers WhatsApp ou e-mail (aucun serveur).
- Le bandeau jaune « Maquette de démonstration » est la div `.demo-ribbon` en haut de chaque page : la supprimer quand l'étude a signé.
- Les pages sont générées par le générateur commun (dossier `_generateur/` à la racine de `notaires/`). Pour une petite retouche, éditer directement les deux pages HTML ; pour une refonte, modifier le générateur et régénérer.

## Design
- Thème : **{s['theme']}** · palette : **{s['palette']}** · polices : {FONTS[s['palette']][0]} (titres) / {FONTS[s['palette']][2]} (texte).
- Angle du site : {sh['angle']}

## Faits (source : fiche de prospection, vérifiée le 19/10/2026)
- Notaire / étude : {sh['name']}
- Charge : {sh['charge'] or '—'}
- Adresse : {sh['address']}, {sh['quartier']}
- Téléphones : {sh['phones']}
- E-mail (annuaire) : {sh['email'] or '—'}
- Présence web : {sh['web']}
- Google Maps : {sh['maps']}

## Recherche complémentaire (26/10/2026)
{research}

## Règles
- Ne rien inventer : pas de biographie, diplômes, horaires, avis, témoignages ou photos qui ne viennent pas de l'étude ou d'une source vérifiée. Ce qui manque reste en « emplacement réservé ».
- Ne pas afficher une note Google inférieure à 4,5.
- Les listes de pièces à fournir sont indicatives et doivent être relues par le notaire.

## À confirmer avec l'étude avant mise en ligne
- [ ] Le numéro {s['whatsapp_label'] or '(aucun mobile)'} est-il sur WhatsApp, et l'étude veut-elle l'utiliser ?
- [ ] Les e-mails sont-ils relevés à l'adresse {s['email'] or '(aucune adresse connue)'} ?
- [ ] Horaires d'ouverture (non affichés{', sauf « samedi matin »' if s.get('saturday') else ''}).
- [ ] Vraie photo de l'étude ou portrait, à mettre à la place de la photo d'illustration de la page « L'étude », et texte de présentation.
- [ ] Relecture des pièces à fournir et des questions fréquentes.
- [ ] Le monogramme « {s['initials']} » est une proposition graphique, pas le sceau officiel.
"""

def main():
    os.makedirs(OUT, exist_ok=True)
    base = open(os.path.join(HERE, "assets/base.css"), encoding="utf-8").read()
    themes = open(os.path.join(HERE, "assets/themes.css"), encoding="utf-8").read()
    js = open(os.path.join(HERE, "assets/site.js"), encoding="utf-8").read()
    built = []
    for idx, s in enumerate(S.build()):
        s["abroad"] = s["slug"] in ABROAD
        d = os.path.join(OUT, s["slug"])
        for sub in ("en", "fr", "assets"):
            shutil.rmtree(os.path.join(d, sub), ignore_errors=True)
        os.makedirs(os.path.join(d, "assets"), exist_ok=True)
        primary, second = ("en", "fr") if s.get("en_first") else ("fr", "en")
        os.makedirs(os.path.join(d, second), exist_ok=True)
        for f in os.listdir(d):
            if f.endswith(".html"): os.remove(os.path.join(d, f))
        IMG = images(s, idx)
        s["images"] = IMG
        for page in TPL:
            fn1 = dict((k, f) for k, f, _ in PAGES[primary])[page]
            fn2 = dict((k, f) for k, f, _ in PAGES[second])[page]
            open(os.path.join(d, fn1), "w", encoding="utf-8").write(render(s, primary, page, "", second, f"{second}/", IMG))
            open(os.path.join(d, second, fn2), "w", encoding="utf-8").write(render(s, second, page, "../", primary, "../", IMG))
        open(os.path.join(d, "assets/style.css"), "w", encoding="utf-8").write(f"/* {s['name']} — thème {s['theme']}, palette {s['palette']} */\n" + css_vars(s["palette"]) + base + themes)
        open(os.path.join(d, "assets/site.js"), "w", encoding="utf-8").write(js)
        open(os.path.join(d, "assets/favicon.svg"), "w", encoding="utf-8").write(favicon(s))
        open(os.path.join(d, "robots.txt"), "w").write("User-agent: *\nDisallow: /\n")
        open(os.path.join(d, "CLAUDE.md"), "w", encoding="utf-8").write(claude_md(s))
        built.append(s)
    json.dump([{k: s[k] for k in ("slug", "theme", "palette")} for s in built], open(os.path.join(HERE, "built.json"), "w"), indent=1)
    print("built", len(built))

if __name__ == "__main__":
    main()
