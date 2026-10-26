# Données des 18 études. Source principale : fiche de prospection (vérifiée le 19/10/2026),
# complétée par la recherche du 26/10/2026 (voir "research" de chaque étude).
# Rien ici n'est inventé : ce qui n'est pas connu reste absent ou est signalé "à confirmer".

def tel(n):
    d = "".join(c for c in n if c.isdigit())
    if not d.startswith("237"):
        d = "237" + d
    return "+" + d

def phones(s):
    out = []
    for p in s.replace("+237", "").split("/"):
        p = p.strip()
        if p:
            out.append({"label": "+237 " + p, "href": "tel:" + tel(p), "mobile": p.startswith("6")})
    return out

def charge_en(c):
    # "Douala Ndokoti 4e charge" -> "Office no. 4, Douala-Ndokoti"
    import re
    m = re.match(r"(Douala(?: \w+)?) (\d+)(?:re|e) charge", c.replace("Bonabéri", "Bonaberi"))
    if not m:
        return c
    place = m.group(1).replace(" ", "-").replace("Bonaberi", "Bonabéri")
    return f"Office no. {m.group(2)}, {place}"

def charge_short(c):
    import re
    m = re.match(r"(.*?) (\d+)(re|e) charge", c)
    return (m.group(1), m.group(2), m.group(3)) if m else (c, "", "")

RAW = [
  # slug, prio, name, charge, quartier, address, phones, email, web, maps
  dict(slug="02-njongue-etame-florence", prio="A", first="Florence", last="NJONGUE ETAME",
       charge="Douala 1re charge", quartier="Bonanjo",
       address="39 rue de la Chambre de commerce, 1er étage, immeuble Kitchener",
       addr_en="39 rue de la Chambre de commerce, 1st floor, Kitchener building",
       phones="+237 233 42 95 62 / 677 68 14 04 / 699 97 69 20",
       email="etude@notairefnjongueetame.com", maps=None,
       theme="institutionnel", palette="slate",
       angle="email",
       research=["Fiche maligah.com « ETUDE ME FLORENCE NJONGUE ETAME » confirme l'existence de l'étude (sans détails).",
                 "Almanach 2019 (colonnes mal alignées) : B.P. 12265 Douala, à confirmer ; mention possible « détenteur des minutes de Maître EWANDE Félix », à confirmer.",
                 "Le domaine notairefnjongueetame.com ne répond plus (DNS) : l'adresse e-mail publiée par la Chambre risque de ne plus fonctionner."]),
  dict(slug="03-grace-nkake-bollanga", prio="A", first="Grâce", last="NKAKE BOLLANGA",
       charge="Douala Ndokoti 4e charge", quartier="Ndogbat / Japoma",
       address="Avenue de Japoma, ancienne scierie Ndogbat, face station Africa Petroleum",
       addr_en="Avenue de Japoma, former Ndogbat sawmill, opposite the Africa Petroleum station",
       phones="+237 699 95 67 81 / 233 41 87 47",
       email="etudegbollanga@gmail.com", maps="Notaire Grâce Nkake Bollanga Douala",
       rating="4,8", rating_en="4.8", reviews=45,
       theme="notaria", palette="emerald", angle="reviews",
       research=["Google Maps : 4,8 sur 5 (45 avis) — meilleure note Google des notaires de Douala selon la fiche ; clients de l'étranger.",
                 "Almanach 2019 : Douala Ndokoti 4e charge, prestation de serment le 14 juillet 2017 ; B.P. 3768 (ville non précisée)."],
       since="2017"),
  dict(slug="04-dooh-collins-ekollo-regine", prio="A", first="Régine", last="DOOH COLLINS EKOLLO",
       display_last="DOOH COLLINS", charge="Douala 12e charge", quartier="Bonanjo",
       address="16 rue La Pérouse & 99 rue du Tribunal",
       addr_en="16 rue La Pérouse & 99 rue du Tribunal",
       phones="+237 233 43 16 38 / 233 43 99 08 / 699 21 00 35",
       email="etude.dcollins@gmail.com", maps=None,
       theme="prestige", palette="navy-gold", angle="institution",
       chamber=True,
       research=["Cameroon Tribune (23/10/2023 et 18/07/2025) : « Me Régine Dooh Collins, présidente de la Chambre nationale des notaires du Cameroun ». La fiche dit « ex-présidente » : le site écrit « a présidé », vrai dans les deux cas. À confirmer avec elle.",
                 "maligah.com : « ETUDE REGINE DOOH COLLINS-EKOLLO », B.P. 344, tél. 33 43 16 38 (ancien format du 233 43 16 38).",
                 "Décret n° 2025/316 du 16 juillet 2025 portant organisation de la profession de notaire (contexte de l'interview de juillet 2025)."]),
  dict(slug="05-alam-eboutou-marquise", prio="B", first="Marquise", last="ALAM EBOUTOU",
       charge="Douala 18e charge", quartier="Bonanjo",
       address="215 rue Joss", addr_en="215 rue Joss",
       phones="+237 233 43 16 62 / 694 94 46 56",
       email="mnetude2007@yahoo.fr", maps=None,
       theme="editorial", palette="burgundy", angle="expertise",
       since_note="1991",
       research=["Fiche (source Maathis) : notaire depuis 1991, la plus citée en jurisprudence sur Maathis ; Google 3,5 (2 avis) — note non affichée.",
                 "Almanach 2019 : nom repéré dans le bloc Yaoundé (colonnes mal alignées) — vérifier la charge et l'adresse actuelles avant présentation."]),
  dict(slug="06-kamako-biabo-evelyne", prio="B", first="Evelyne", last="KAMAKO BIABO",
       charge="Douala 3e charge", quartier="Akwa",
       address="381 boulevard de la Liberté, face PTT",
       addr_en="381 boulevard de la Liberté, opposite the PTT post office",
       addr_note="Google Maps indique : 446 rue Boué de Lapeyrère",
       phones="+237 233 43 63 90 / 699 96 02 25",
       email="etudekamako@yahoo.fr", maps=None,
       theme="accueil", palette="teal", angle="transparency",
       research=["Google Maps : 3,9 (12 avis), plusieurs avis négatifs sur les délais — ne pas afficher la note ; le site répond par une page « délais et suivi ». Ne pas citer les avis au téléphone.",
                 "Deux adresses : 381 bd de la Liberté face PTT (Chambre) / 446 rue Boué de Lapeyrère (Google) — à confirmer.",
                 "maligah.com confirme « ETUDE ME EVELYNE KAMAKO BIABO »."]),
  dict(slug="07-nkono-lunduobe-marie-jeanne", prio="B", first="Marie Jeanne", last="NKONO LUNDUOBE",
       charge="Douala 7e charge", quartier="Akwa",
       address="Rue Sylvani, face au Centre de promotion de la femme et de la famille",
       addr_en="Rue Sylvani, opposite the Centre de promotion de la femme et de la famille",
       phones="+237 233 43 79 87 / 699 86 57 95",
       email="menkonomariejeanne@yahoo.fr", maps=None,
       theme="notaria", palette="cobalt", angle="documents",
       research=["Google Maps : 3,3 (6 avis), remarques sur l'accueil et l'orientation — note non affichée ; le site mise sur « pièces à fournir » et la prise de rendez-vous.",
                 "maligah.com : « ME LUNDUOBE MARIE JEANNE EPSE NKONO »."]),
  dict(slug="08-nkoue-mawafo-fonkoua-marie-louise", prio="B", first="Marie Louise", last="NKOUE MAWAFO FONKOUA",
       display_last="MAWAFO FONKOUA", charge="Douala 16e charge", quartier="Akwa",
       address="172 rue Dicka Mpondo", addr_en="172 rue Dicka Mpondo",
       phones="+237 677 70 79 32", email="mawafo1@yahoo.fr", maps=None,
       theme="prestige", palette="forest-brass", angle="visibility",
       since_note="1991",
       research=["Fiche : notaire depuis 1991 ; aucune fiche Google trouvée.",
                 "Almanach 2019 : mention « Conseiller » dans l'en-tête de son bloc (rôle à la Chambre ?) — à confirmer, non affiché."]),
  dict(slug="09-mbollo-mbassi-dikongue-anne-marie", prio="B", first="Anne Marie", last="MBOLLO MBASSI DIKONGUE",
       display_last="MBOLLO MBASSI", charge="Douala 2e charge", quartier="Bali",
       address="Rue Bertaut", addr_en="Rue Bertaut",
       phones="+237 233 43 15 98 / 696 51 90 46",
       email="me_mwilson@yahoo.fr", maps=None,
       theme="editorial", palette="terracotta", angle="visibility",
       research=["Aucune fiche Google ni site trouvés.",
                 "L'e-mail me_mwilson@yahoo.fr ne reprend pas son nom : vérifier qu'il est toujours relevé."]),
  dict(slug="10-nova-notaire-associes", prio="B", first="", last="", firm="Nova Notaire & Associés",
       charge=None, quartier="Akwa / Bonabekombo",
       address="Avenue de la Liberté (plus code 3P52+9Q8)", addr_en="Avenue de la Liberté (plus code 3P52+9Q8)",
       phones="+237 699 72 14 34", email="", maps="Nova Notaire & Associés Douala",
       theme="moderne", palette="ink-lime", angle="team",
       research=["Fiche Google existante ; fiches annuaires (doualabouge.com) ; absent de la liste de la Chambre 2019.",
                 "Nom du notaire titulaire inconnu : à demander au premier appel. L'équipe est laissée en emplacements à remplir."]),
  dict(slug="11-moukory-eyango-jean-jacques", prio="C", first="Jean Jacques", last="MOUKORY EYANGO",
       charge="Douala Ndokoti 3e charge", quartier="Ndokoti",
       address="Avenue Roger Milla, au-dessus d'Afriland First Bank",
       addr_en="Avenue Roger Milla, above Afriland First Bank",
       phones="+237 233 41 86 86 / 699 92 12 24",
       email="etudememoukoryeyango@gmail.com", maps=None,
       theme="institutionnel", palette="harbor", angle="local",
       research=["Aucune fiche Google ni site trouvés. Cible : les habitants de Ndokoti/Japoma qui cherchent « notaire près de chez moi »."]),
  dict(slug="12-enguele-dipanda-gisele", prio="C", first="Gisèle", last="ENGUELE DIPANDA",
       charge="Douala Ndokoti 2e charge", quartier="Ndokoti",
       address="Avenue de Japoma, immeuble Rose, bâtiment A",
       addr_en="Avenue de Japoma, Rose building, block A",
       phones="+237 694 69 91 47 / 233 41 87 15",
       email="etudedigisen@yahoo.com", maps="Notaire Gisèle Enguele Dipanda Douala",
       theme="accueil", palette="sun", angle="saturday",
       saturday=True, since="2017",
       research=["Google Maps : 4,2 (5 avis), ouvert le samedi matin — l'ouverture du samedi est mise en avant (horaires exacts à confirmer).",
                 "Almanach 2019 : Douala Ndokoti 2e charge, prestation de serment le 14 juillet 2017."]),
  dict(slug="13-ngalla-joseph", prio="C", first="Joseph", last="NGALLA",
       charge="Douala Ndokoti 5e charge", quartier="Deido / Bassa",
       address="Route Deido-Bassa, à côté de la pharmacie Djakoumè",
       addr_en="Deido-Bassa road, next to the Djakoumè pharmacy",
       phones="+237 674 95 31 05 / 243 78 87 76",
       email="j.ngalla@yahoo.com", maps="Notaire Joseph Ngalla Douala",
       rating="5,0", rating_en="5.0", reviews=4,
       theme="notaria", palette="ochre", angle="social", since="2017",
       research=["Google Maps : 5,0 (4 avis) ; Facebook personnel — l'approcher aussi par Facebook/WhatsApp.",
                 "Almanach 2019 : Douala Ndokoti 5e charge, prestation de serment le 14 juillet 2017, B.P. 7833 Douala-Ndokoti."]),
  dict(slug="14-baiye-daniel-bechem", prio="C", first="Daniel Bechem", last="BAIYE",
       charge="Douala Ndokoti 6e charge", quartier="Bonamoussadi",
       address="1er étage, immeuble Afriland First Bank", addr_en="1st floor, Afriland First Bank building",
       phones="+237 679 34 74 51 / 699 08 22 34",
       email="bbechem@yahoo.com", maps=None,
       theme="moderne", palette="night-coral", angle="bilingual", en_first=True,
       research=["Profil LinkedIn « Notary Public » ; aucune fiche Google. Site pensé bilingue avec l'anglais à égalité (même argument que pour Abeng)."]),
  dict(slug="15-tongoue-hamedak-jacques", prio="C", first="Jacques", last="TONGOUE HAMEDAK",
       charge="Douala Bonabéri 1re charge", quartier="Bonabéri",
       address="Carrefour Fokou, 2e étage, immeuble NFC Bank",
       addr_en="Carrefour Fokou, 2nd floor, NFC Bank building",
       phones="+237 233 39 03 61 / 698 13 89 89 / 679 82 75 82",
       email="etudetongoue@yahoo.com", maps=None,
       theme="institutionnel", palette="pine", angle="bonaberi",
       research=["Bonabéri : deux confrères (Me Piameu, Me Suna Nso) ont déjà un site — argument concurrentiel."]),
  dict(slug="16-wansi-kameni-narcisse", prio="C", first="Narcisse", last="WANSI KAMENI",
       charge="Douala Bonabéri 5e charge", quartier="Bonabéri",
       address="Face OK Foods et supermarché Santa Lucia",
       addr_en="Opposite OK Foods and the Santa Lucia supermarket",
       phones="+237 233 39 07 77 / 699 96 37 31 / 679 57 53 64",
       email="etudewansikameni@yahoo.com", maps=None,
       theme="editorial", palette="harbor-sand", angle="bonaberi",
       research=["Bonabéri : deux confrères déjà en ligne — argument concurrentiel."]),
  dict(slug="17-ngo-yon-benga-fride-epoune", prio="C", first="Fride", last="NGO YON BENGA",
       display_name="Maître Fride NGO YON BENGA épouse EPOUNE", charge="Douala Bonabéri 4e charge", quartier="Bonambappè",
       address="À côté de la Compagnie de gendarmerie", addr_en="Next to the Gendarmerie company",
       phones="+237 233 39 00 55 / 699 52 95 41 / 671 05 05 98",
       email="etudemengoyonbenga@yahoo.com", maps=None,
       theme="accueil", palette="mauve", angle="bonaberi",
       research=["Almanach 2019 : « NGO YON BENGA Fride Yollande épouse EPOUNE », B.P. 2299 Douala (à confirmer)."]),
  dict(slug="18-nzue-rose-biteck-lima", prio="C", first="Rose", last="NZUE BITECK LIMA",
       display_name="Maître Rose NZUE BITECK LIMA", charge="Douala 10e charge", quartier="Bali",
       address="Face LABTAG", addr_en="Opposite LABTAG",
       phones="+237 243 81 07 12 / 677 46 12 66",
       email="etudenotairelimarose@yahoo.com", maps=None,
       theme="prestige", palette="aubergine", angle="visibility",
       research=["Almanach 2019 (à confirmer) : B.P. 5066 Douala ; « détenteur des minutes de Maîtres Elise LOTTIN et EBONGUE Ernest » — si confirmé, ajouter un service « copies d'actes anciens » comme pour Me Mongoue."]),
  dict(slug="01-mongoue-sandrine-demo", prio="A", first="Sandrine", last="MONGOUE",
       charge="Douala 9e charge", quartier="Akwa",
       address="581 boulevard de la Liberté, immeuble CCA, face à la Pharmacie du Centre",
       addr_en="581 boulevard de la Liberté, CCA building, opposite the Pharmacie du Centre",
       phones="", email="", maps="Notaire Sandrine Mongoue Douala",
       rating="4,6", rating_en="4.6", reviews=8,
       theme="moderne", palette="violet", angle="diaspora",
       since_note="2017", minutes="Maître MBOBDA MONGOUE Elie",
       research=["Google Maps : 4,6 (8 avis) — clients de la diaspora, mariages franco-camerounais, création d'entreprise.",
                 "Domaine smnotaire.com déjà acheté mais vide (page d'hébergeur) : ce site peut y être publié tel quel.",
                 "Liste de la Chambre (2019), reprise du site React existant : 9e charge de Douala depuis le 23 juin 2017, B.P. 5374, détentrice des minutes de Maître MBOBDA MONGOUE Elie.",
                 "Le site React/Vite existant reste dans le dossier 01-mongoue-sandrine (projet Vercel notaire-me-mongoue)."]),
]

def sheet_rows():
    import csv
    rows = list(csv.reader(open("/root/notaires/fiche.csv", encoding="utf-8")))
    return [r for r in rows[4:] if r and r[0] in ("A", "B", "C")]

def build():
    # Les téléphones, e-mails, adresses et charges viennent toujours de la fiche, jamais d'une saisie à la main.
    rows = sheet_rows()
    sites = []
    for r in RAW:
        key = r.get("firm") or r["last"]
        match = [x for x in rows if all(t in x[1].upper() for t in key.upper().split())]
        assert len(match) == 1, (key, len(match))
        x = match[0]
        r = dict(r, prio=x[0], quartier=x[3], address=r["address"], phones=x[5], email=x[6])
        if not r.get("firm"):
            assert r["charge"] == x[2], (r["charge"], x[2])
        s = dict(r)
        s["sheet"] = dict(zip(["prio", "name", "charge", "quartier", "address", "phones", "email", "web", "maps", "angle"], x[:10]))
        s["phones"] = phones(r["phones"])
        mob = [p for p in s["phones"] if p["mobile"]]
        s["whatsapp"] = tel(mob[0]["label"])[1:] if mob else None
        s["whatsapp_label"] = mob[0]["label"] if mob else None
        if r.get("firm"):
            s["name"] = r["firm"]; s["brand"] = r["firm"]; s["initials"] = "N&A"
            s["role_fr"] = "Étude notariale à Douala"; s["role_en"] = "Notary office in Douala"
        else:
            last = r.get("display_last", r["last"])
            s["name"] = r.get("display_name", f"Maître {r['first']} {last}")
            s["short"] = f"Me {r['first']} {last}"
            s["brand"] = f"Me {r['first']} {last}"
            s["initials"] = (r["first"][0] + last[0]).upper()
            s["role_fr"] = "Notaire à Douala"; s["role_en"] = "Notary in Douala"
        if r.get("charge"):
            place, num, suf = charge_short(r["charge"])
            s["charge_fr"] = f"{place} {num}<sup>{suf}</sup> charge"
            s["charge_plain"] = r["charge"]
            s["charge_en"] = charge_en(r["charge"])
            s["charge_num"] = num
        q = r["maps"] or f"{r['address']}, {r['quartier']}, Douala"
        from urllib.parse import quote
        s["map_src"] = f"https://maps.google.com/maps?q={quote(q)}&z=16&output=embed"
        s["map_link"] = f"https://www.google.com/maps/search/?api=1&query={quote(q)}"
        s["full_address"] = f"{r['address']}, {r['quartier']}, Douala"
        s["full_address_en"] = f"{r['addr_en']}, {r['quartier']}, Douala"
        sites.append(s)
    return sites
