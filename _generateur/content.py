# Textes communs à toutes les études (FR / EN).
# Les contenus de base reprennent ceux du site de Me Mongoue (même auteur), généralisés.
# Rien de propre à une étude ici : les faits particuliers viennent de sites.py.

T = {
"fr": {
  "lang": "fr", "other_lang": "English", "other_label": "Version anglaise",
  "skip": "Aller au contenu",
  "demo": "Maquette de démonstration — proposition de site, non publiée par l'étude.",
  "nav": [("#domaines", "Domaines"), ("#pieces", "Pièces à fournir"), ("#etude", "L'étude"), ("#questions", "Questions"), ("#contact", "Contact")],
  "cta_rdv": "Prendre rendez-vous", "cta_call": "Appeler l'étude", "cta_whatsapp": "Écrire sur WhatsApp",
  "cta_route": "Itinéraire", "cta_prepare": "Préparer mon dossier", "menu": "Menu", "close": "Fermer",
  "eyebrow_office": "Étude notariale",

  "notary_title": "Le notaire",
  "notary_def": "Le notaire est un officier public, nommé par l'État, qui reçoit les actes auxquels les parties doivent ou veulent donner le caractère d'authenticité. Il en garantit la date, en conserve l'original — la minute — et en délivre des copies.",
  "notary_points": [
    ("Un acte qui fait foi", "Son contenu et sa date ne peuvent être contestés que par une procédure spéciale."),
    ("Un acte exécutoire", "Revêtu de la formule exécutoire, il s'applique sans passer par un tribunal."),
    ("Un acte conservé", "L'original reste à l'étude : vous pouvez en obtenir copie des années plus tard."),
  ],

  "services_title": "Ce que l'étude fait pour vous",
  "services_intro": "Le notaire prépare, reçoit et conserve les actes qui engagent votre patrimoine, votre famille et votre entreprise.",
  "services": [
    ("terrain", "Terrains et immeubles", "Achat, vente, échange, bail de longue durée, prêt avec hypothèque. Avant toute signature, l'étude vérifie le titre foncier et demande un certificat de propriété à la conservation foncière."),
    ("succession", "Successions", "Inventaire des biens, partage entre héritiers, transfert des titres fonciers et des parts de société au nom des héritiers."),
    ("famille", "Famille", "Contrat de mariage, y compris pour les couples binationaux. Donations aux enfants ou entre époux. Testaments."),
    ("societe", "Entreprises", "Constitution de sociétés selon le droit OHADA (SARL, SAS, SA), augmentation de capital, cession de parts ou d'actions, procès-verbaux d'assemblée."),
    ("procuration", "Procurations", "Pour qu'une personne de confiance signe à votre place au Cameroun : achat d'un terrain, succession, opération bancaire."),
    ("copie", "Authentifications et copies", "Dépôt de pièces au rang des minutes, copies authentiques d'actes reçus par l'étude."),
  ],

  "steps_title": "Comment se déroule votre dossier",
  "steps": [
    ("Premier contact", "Par téléphone, WhatsApp ou à l'étude : vous présentez l'opération envisagée."),
    ("Liste des pièces et estimation", "L'étude vous indique les pièces à fournir et une estimation des frais : droits d'enregistrement, frais de conservation foncière, émoluments du notaire."),
    ("Vérifications", "L'étude examine les pièces et procède aux vérifications : titre foncier, état civil, pouvoirs des signataires."),
    ("Signature", "Lecture de l'acte et signature à l'étude, ou par procuration si vous ne pouvez pas vous déplacer."),
    ("Formalités", "Enregistrement, puis inscription à la conservation foncière ou immatriculation au registre du commerce, selon le cas. Vous recevez une copie authentique de l'acte."),
  ],

  "docs_title": "Préparez votre dossier",
  "docs_intro": "Choisissez votre opération, cochez les pièces que vous avez déjà, puis envoyez la liste à l'étude.",
  "docs_note": "Listes indicatives. L'étude vous confirme les pièces exactes après examen de votre dossier.",
  "docs_send_wa": "Envoyer la liste sur WhatsApp", "docs_send_mail": "Envoyer par e-mail",
  "docs_status": "pièce(s) prête(s) sur",
  "docs": [
    ("terrain", "Terrain", "Achat ou vente d'un terrain titré", [
      "Pièce d'identité (CNI ou passeport) de l'acheteur et du vendeur",
      "Copie du titre foncier",
      "Certificat de propriété récent, délivré par la conservation foncière",
      "Plan de situation ou plan cadastral du terrain",
      "Acte de mariage des parties mariées, avec leur régime matrimonial",
      "Si une société achète ou vend : statuts, RCCM et pouvoir du signataire"]),
    ("succession", "Succession", "Règlement d'une succession", [
      "Acte de décès", "Jugement d'hérédité",
      "Actes de naissance et pièces d'identité des héritiers",
      "Acte de mariage du défunt, le cas échéant",
      "Titres fonciers, relevés de comptes et justificatifs des autres biens",
      "Testament, s'il en existe un"]),
    ("societe", "Société", "Création d'une société", [
      "Pièce d'identité de chaque associé",
      "Nom envisagé et activité de la société",
      "Montant du capital et répartition entre les associés",
      "Extrait de casier judiciaire du dirigeant, ou déclaration sur l'honneur",
      "Adresse du siège : contrat de bail ou attestation de domiciliation, et plan de localisation"]),
    ("mariage", "Mariage", "Contrat de mariage", [
      "Pièces d'identité des deux futurs époux",
      "Actes de naissance des deux futurs époux",
      "Date et lieu prévus pour la célébration",
      "Liste des biens apportés par chacun : terrains, comptes, parts de société",
      "Pour un futur époux étranger : justificatif de nationalité et, le cas échéant, certificat de coutume"]),
    ("procuration", "Procuration", "Procuration depuis l'étranger", [
      "Copie de votre passeport ou de votre CNI",
      "Identité complète de la personne qui vous représentera au Cameroun",
      "Description de l'opération : bien concerné, références du titre foncier, montant",
      "Adresse où recevoir le projet de procuration"]),
  ],

  "abroad_title": "Vous vivez hors du Cameroun",
  "abroad_intro": "Acheter un terrain au pays, régler la succession d'un parent, créer une société à Douala : la plupart des dossiers avancent sans que vous ayez à faire le voyage.",
  "abroad_points": [
    ("Vous écrivez à l'étude", "Par WhatsApp ou par e-mail : l'opération, le bien concerné et votre pays de résidence."),
    ("Vous envoyez les pièces", "D'abord en copie numérisée pour examen ; les originaux suivent par courrier ou par votre représentant."),
    ("Vous signez à distance", "Par procuration : vous signez le projet devant un notaire de votre pays de résidence ou le faites légaliser au consulat du Cameroun."),
  ],
  "pay_note": "Avant tout paiement, confirmez les coordonnées bancaires en appelant l'étude sur sa ligne fixe.",

  "office_title": "L'étude",
  "office_photo": "Emplacement réservé : photo de l'étude ou portrait du notaire",
  "office_member": "Membre de la Chambre nationale des notaires du Cameroun.",
  "office_auth": "Un acte notarié est un acte authentique : sa date et son contenu ne peuvent être contestés que par une procédure spéciale. Le notaire en garde l'original, appelé minute, et vous en remet des copies.",
  "facts": {"charge": "Charge", "address": "Adresse", "phone": "Téléphone", "email": "E-mail", "since": "Notaire depuis", "area": "Quartier"},

  "faq_title": "Questions fréquentes",
  "faq": [
    ("Comment éviter d'acheter un terrain litigieux ?", "Privilégiez un terrain titré et ne versez aucune somme avant que le notaire ait vérifié le titre. L'étude demande un certificat de propriété à la conservation foncière : il indique le propriétaire actuel et les charges éventuelles, comme une hypothèque ou une opposition."),
    ("Combien coûte un acte notarié ?", "Les frais comprennent les droits et taxes reversés à l'État (enregistrement, conservation foncière) et les émoluments du notaire, fixés par la réglementation. Ils dépendent de la nature et de la valeur de l'opération : demandez une estimation avant de commencer."),
    ("Puis-je acheter un terrain sans me déplacer ?", "Oui. Vous donnez procuration à une personne de confiance, qui signe l'acte de vente à l'étude en votre nom. L'étude fait ensuite établir le titre foncier à votre nom."),
    ("Pourquoi faire un contrat de mariage ?", "Il fixe le régime qui s'appliquera à vos biens pendant le mariage et en cas de séparation ou de décès. Il se signe chez le notaire avant la célébration."),
    ("Comment vérifier qu'un notaire est bien en exercice ?", "La Chambre nationale des notaires du Cameroun publie la liste des notaires en exercice et de leurs études. En cas de doute, renseignez-vous auprès d'elle."),
  ],

  "contact_title": "Prendre rendez-vous",
  "contact_intro": "Appelez l'étude, écrivez sur WhatsApp ou remplissez le formulaire : votre message s'ouvre prêt à être envoyé.",
  "c_address": "Adresse", "c_phone": "Téléphone", "c_whatsapp": "WhatsApp", "c_email": "E-mail", "c_hours": "Horaires",
  "map_title": "Plan d'accès à l'étude", "map_link": "Ouvrir l'itinéraire dans Google Maps",
  "f_name": "Votre nom", "f_country": "Ville ou pays de résidence", "f_optional": "(facultatif)",
  "f_subject": "Objet", "f_subjects": ["Achat ou vente d'un terrain", "Succession", "Création de société", "Contrat de mariage", "Donation ou testament", "Procuration", "Autre"],
  "f_message": "Votre message", "f_placeholder": "Décrivez votre projet en quelques lignes.",
  "f_send_wa": "Envoyer sur WhatsApp", "f_send_mail": "Envoyer par e-mail",
  "f_note": "Votre message s'ouvre dans WhatsApp ou dans votre messagerie. Ce site n'enregistre aucune donnée.",
  "footer_disclaimer": "Les informations de ce site sont générales. Elles ne remplacent pas un rendez-vous avec le notaire.",
  "msg": {"hello": "Bonjour Maître,", "file": "Je prépare un dossier : ", "ready": "Pièces prêtes :", "missing": "Pièces manquantes :", "none": "(aucune)", "confirm": "Pouvez-vous me confirmer la liste exacte des pièces ?", "name": "Nom : ", "country": "Résidence : ", "topic": "Objet : ", "rdv": "Demande de rendez-vous : ", "dossier": "Dossier : "},

  # Blocs propres à l'angle de chaque étude
  "angle": {
    "reviews": {"title": "La confiance de ses clients", "lead": "L'étude compte parmi les notaires les mieux notés de Douala sur Google, y compris par des clients installés à l'étranger.", "score_label": "sur Google", "reviews_label": "avis", "link": "Lire les avis sur Google", "placeholder": "Emplacement réservé : extraits d'avis choisis avec l'étude, publiés avec l'accord de leurs auteurs."},
    "institution": {"title": "Au service de la profession", "lead": "Maître Régine DOOH COLLINS a présidé la Chambre nationale des notaires du Cameroun, l'institution qui représente et encadre la profession.", "quote": "Le notaire garantit la sécurité juridique des actes qu'il reçoit : il vérifie la légalité de l'opération pour protéger chacune des parties."},
    "expertise": {"title": "Plus de trente ans d'exercice", "lead": "Notaire depuis 1991, l'étude accompagne sociétés et particuliers dans les opérations qui demandent le plus de rigueur : vie des sociétés et transactions immobilières.", "cols": [("Sociétés", "Constitution, modification des statuts, augmentation ou réduction de capital, cessions de parts et d'actions, fusions et dissolutions selon le droit OHADA."), ("Immobilier", "Ventes et acquisitions, baux de longue durée, prêts hypothécaires, vérification des titres fonciers avant signature.")]},
    "transparency": {"title": "Délais et suivi de votre dossier", "lead": "Un dossier notarial passe par l'étude, puis par plusieurs administrations. Voici ce qui dépend de chacune, pour savoir à tout moment où en est le vôtre.", "rows": [("Pièces complètes", "Vous", "Le délai commence quand le dossier est complet."), ("Vérifications et projet d'acte", "L'étude", "Délai indiqué à l'ouverture du dossier."), ("Signature", "Vous et l'étude", "À la date convenue ensemble."), ("Enregistrement", "Administration fiscale", "Après paiement des droits."), ("Conservation foncière ou RCCM", "Administrations", "L'étude suit la formalité et vous tient informé.")], "track_title": "Suivre mon dossier", "track_intro": "Indiquez votre nom et la référence de votre dossier : l'étude vous répond avec un point d'étape.", "track_ref": "Référence du dossier", "track_send": "Demander un point d'étape", "placeholder": "À compléter avec l'étude : délais habituels pour chaque type d'acte."},
    "documents": {"title": "Préparer votre visite", "lead": "Pour que votre premier rendez-vous soit utile, venez avec les bonnes pièces.", "points": [("Choisissez votre opération", "La liste ci-dessous indique les pièces habituelles."), ("Envoyez la liste à l'étude", "Sur WhatsApp ou par e-mail, avant de vous déplacer."), ("Venez au rendez-vous", "Avec les originaux et une pièce d'identité.")]},
    "team": {"title": "L'équipe", "lead": "Une étude organisée autour d'un notaire titulaire et de ses collaborateurs.", "members": [("Notaire titulaire", "Nom à confirmer"), ("Notaire associé(e)", "À compléter"), ("Principal clerc", "À compléter"), ("Accueil et formalités", "À compléter")], "placeholder": "Emplacements réservés : noms, fonctions et photos fournis par l'étude."},
    "local": {"title": "Votre notaire à Ndokoti", "lead": "L'étude est installée avenue Roger Milla, au-dessus d'Afriland First Bank : un notaire à proximité pour les habitants de Ndokoti, Japoma et des quartiers voisins."},
    "saturday": {"title": "Ouvert le samedi matin", "lead": "Vous travaillez en semaine ? L'étude vous reçoit aussi le samedi matin.", "badge": "Samedi matin", "placeholder": "Horaires exacts à confirmer avec l'étude."},
    "social": {"title": "Des clients satisfaits", "lead": "Une note parfaite sur Google. Écrivez à l'étude en un clic.", "score_label": "sur Google", "reviews_label": "avis", "link": "Voir les avis sur Google"},
    "bilingual": {"title": "Un site en français et en anglais", "lead": "Toutes les informations de l'étude sont publiées dans les deux langues officielles, pour que chaque client prépare son dossier dans la langue qu'il lit le mieux."},
    "bonaberi": {"title": "Votre notaire à Bonabéri", "lead": "Sur la rive gauche du Wouri : pour les habitants de Bonabéri et de ses environs, un notaire tout proche, sans traverser le pont."},
    "email": {"title": "Au cœur de Bonanjo", "lead": "L'étude est installée rue de la Chambre de commerce, au cœur du quartier administratif et des affaires de Douala."},
    "diaspora": {"title": "Pour les Camerounais de l'étranger", "lead": "Acheter un terrain au pays, régler une succession, signer un contrat de mariage franco-camerounais : l'étude reçoit à Akwa et suit aussi les dossiers à distance, par procuration.", "score_label": "sur Google", "reviews_label": "avis", "link": "Voir les avis sur Google"},
    "visibility": None,
  },
  "since_label": "Notaire depuis",
},

"en": {
  "lang": "en", "other_lang": "Français", "other_label": "Version française",
  "skip": "Skip to content",
  "demo": "Demonstration mock-up — website proposal, not published by the office.",
  "nav": [("#domaines", "Services"), ("#pieces", "Documents"), ("#etude", "The office"), ("#questions", "FAQ"), ("#contact", "Contact")],
  "cta_rdv": "Book an appointment", "cta_call": "Call the office", "cta_whatsapp": "Message on WhatsApp",
  "cta_route": "Directions", "cta_prepare": "Prepare my file", "menu": "Menu", "close": "Close",
  "eyebrow_office": "Notary office",

  "notary_title": "The notary",
  "notary_def": "A notary is a public officer appointed by the State to receive the deeds that the parties must, or wish to, make authentic. The notary guarantees their date, keeps the original — the minute — and issues copies.",
  "notary_points": [
    ("A deed that is proof", "Its content and date can only be challenged through a special procedure."),
    ("An enforceable deed", "With the enforcement formula, it can be enforced without going to court."),
    ("A deed kept safe", "The original stays at the office: you can obtain a copy years later."),
  ],

  "services_title": "What the office does for you",
  "services_intro": "The notary prepares, receives and keeps the deeds that bind your property, your family and your business.",
  "services": [
    ("terrain", "Land and buildings", "Purchase, sale, exchange, long leases, mortgage loans. Before anything is signed, the office checks the land title and requests a certificate of ownership from the land registry."),
    ("succession", "Estates", "Inventory of assets, division between heirs, transfer of land titles and company shares to the heirs."),
    ("famille", "Family", "Marriage contracts, including for binational couples. Gifts to children or between spouses. Wills."),
    ("societe", "Business", "Company formation under OHADA law (SARL, SAS, SA), capital increases, transfers of shares, minutes of general meetings."),
    ("procuration", "Powers of attorney", "So that a trusted person can sign on your behalf in Cameroon: land purchase, estate, banking."),
    ("copie", "Authentication and copies", "Filing of documents with the office's records, certified copies of deeds received by the office."),
  ],

  "steps_title": "How your file proceeds",
  "steps": [
    ("First contact", "By phone, WhatsApp or at the office: you describe the transaction you have in mind."),
    ("Document list and estimate", "The office tells you which documents to provide and gives an estimate of the costs: registration duties, land registry fees, notary fees."),
    ("Checks", "The office reviews the documents and runs the checks: land title, civil status, signatories' powers."),
    ("Signing", "The deed is read and signed at the office, or by power of attorney if you cannot travel."),
    ("Formalities", "Registration, then entry at the land registry or the trade register, as the case may be. You receive a certified copy of the deed."),
  ],

  "docs_title": "Prepare your file",
  "docs_intro": "Choose your transaction, tick the documents you already have, then send the list to the office.",
  "docs_note": "Indicative lists. The office confirms the exact documents once it has reviewed your file.",
  "docs_send_wa": "Send the list on WhatsApp", "docs_send_mail": "Send by email",
  "docs_status": "document(s) ready out of",
  "docs": [
    ("terrain", "Land", "Buying or selling titled land", [
      "ID (national ID card or passport) of buyer and seller",
      "Copy of the land title",
      "Recent certificate of ownership from the land registry",
      "Location plan or cadastral plan of the land",
      "Marriage certificate of married parties, with their matrimonial regime",
      "If a company buys or sells: articles, trade register (RCCM) and signatory's power"]),
    ("succession", "Estate", "Settling an estate", [
      "Death certificate", "Court judgment of heirship",
      "Birth certificates and IDs of the heirs",
      "Marriage certificate of the deceased, if applicable",
      "Land titles, bank statements and proof of other assets",
      "Will, if there is one"]),
    ("societe", "Company", "Forming a company", [
      "ID of each partner",
      "Proposed name and business activity",
      "Share capital and its split between partners",
      "Criminal record extract of the manager, or sworn statement",
      "Registered office: lease or domiciliation certificate, and location plan"]),
    ("mariage", "Marriage", "Marriage contract", [
      "IDs of both future spouses",
      "Birth certificates of both future spouses",
      "Planned date and place of the wedding",
      "List of assets brought by each: land, accounts, company shares",
      "For a foreign future spouse: proof of nationality and, if needed, certificate of custom"]),
    ("procuration", "Power of attorney", "Power of attorney from abroad", [
      "Copy of your passport or ID card",
      "Full identity of the person who will represent you in Cameroon",
      "Description of the transaction: property, land title references, amount",
      "Address where you will receive the draft power of attorney"]),
  ],

  "abroad_title": "You live outside Cameroon",
  "abroad_intro": "Buying land back home, settling a parent's estate, setting up a company in Douala: most files move forward without you having to travel.",
  "abroad_points": [
    ("Write to the office", "By WhatsApp or email: the transaction, the property and your country of residence."),
    ("Send your documents", "First as scans for review; the originals follow by post or through your representative."),
    ("Sign remotely", "By power of attorney: you sign the draft before a notary where you live, or have it legalised at the Cameroonian consulate."),
  ],
  "pay_note": "Before any payment, confirm the bank details by calling the office's landline.",

  "office_title": "The office",
  "office_photo": "Reserved space: photo of the office or portrait of the notary",
  "office_member": "Member of the National Chamber of Notaries of Cameroon.",
  "office_auth": "A notarial deed is an authentic deed: its date and content can only be challenged through a special procedure. The notary keeps the original, called the minute, and gives you copies.",
  "facts": {"charge": "Office", "address": "Address", "phone": "Phone", "email": "Email", "since": "Notary since", "area": "Area"},

  "faq_title": "Frequently asked questions",
  "faq": [
    ("How can I avoid buying disputed land?", "Prefer titled land and pay nothing until the notary has checked the title. The office requests a certificate of ownership from the land registry: it shows the current owner and any charges, such as a mortgage or an objection."),
    ("How much does a notarial deed cost?", "Costs include duties and taxes paid to the State (registration, land registry) and the notary's fees, which are set by regulation. They depend on the type and value of the transaction: ask for an estimate before you start."),
    ("Can I buy land without travelling?", "Yes. You give a power of attorney to a trusted person, who signs the deed of sale at the office in your name. The office then has the land title issued in your name."),
    ("Why sign a marriage contract?", "It sets the regime that will apply to your assets during the marriage and in case of separation or death. It is signed before the notary, before the wedding."),
    ("How can I check that a notary is practising?", "The National Chamber of Notaries of Cameroon publishes the list of practising notaries and their offices. If in doubt, ask the Chamber."),
  ],

  "contact_title": "Book an appointment",
  "contact_intro": "Call the office, message on WhatsApp or fill in the form: your message opens ready to send.",
  "c_address": "Address", "c_phone": "Phone", "c_whatsapp": "WhatsApp", "c_email": "Email", "c_hours": "Opening hours",
  "map_title": "Map to the office", "map_link": "Open directions in Google Maps",
  "f_name": "Your name", "f_country": "City or country of residence", "f_optional": "(optional)",
  "f_subject": "Subject", "f_subjects": ["Buying or selling land", "Estate", "Company formation", "Marriage contract", "Gift or will", "Power of attorney", "Other"],
  "f_message": "Your message", "f_placeholder": "Describe your project in a few lines.",
  "f_send_wa": "Send on WhatsApp", "f_send_mail": "Send by email",
  "f_note": "Your message opens in WhatsApp or your email app. This site stores no data.",
  "footer_disclaimer": "The information on this site is general. It does not replace an appointment with the notary.",
  "msg": {"hello": "Hello Maître,", "file": "I am preparing a file: ", "ready": "Documents ready:", "missing": "Documents missing:", "none": "(none)", "confirm": "Could you confirm the exact list of documents?", "name": "Name: ", "country": "Residence: ", "topic": "Subject: ", "rdv": "Appointment request: ", "dossier": "File: "},

  "angle": {
    "reviews": {"title": "Trusted by clients", "lead": "The office is among the best-rated notaries in Douala on Google, including by clients living abroad.", "score_label": "on Google", "reviews_label": "reviews", "link": "Read the reviews on Google", "placeholder": "Reserved space: review excerpts chosen with the office, published with their authors' consent."},
    "institution": {"title": "Serving the profession", "lead": "Maître Régine DOOH COLLINS has served as President of the National Chamber of Notaries of Cameroon, the body that represents and oversees the profession.", "quote": "The notary guarantees the legal security of the deeds received: the notary checks that the transaction is lawful, to protect every party."},
    "expertise": {"title": "More than thirty years of practice", "lead": "A notary since 1991, the office advises companies and individuals on the transactions that demand the most rigour: corporate matters and real estate.", "cols": [("Companies", "Formation, amendments to articles, capital increases or reductions, transfers of shares, mergers and dissolutions under OHADA law."), ("Real estate", "Sales and acquisitions, long leases, mortgage loans, land title checks before signing.")]},
    "transparency": {"title": "Timing and tracking of your file", "lead": "A notarial file goes through the office, then through several administrations. Here is what depends on each, so you always know where yours stands.", "rows": [("Complete documents", "You", "The clock starts once the file is complete."), ("Checks and draft deed", "The office", "Timing given when the file is opened."), ("Signing", "You and the office", "On the date agreed together."), ("Registration", "Tax administration", "After the duties are paid."), ("Land registry or trade register", "Administrations", "The office follows up and keeps you informed.")], "track_title": "Track my file", "track_intro": "Give your name and your file reference: the office replies with a progress update.", "track_ref": "File reference", "track_send": "Ask for an update", "placeholder": "To be completed with the office: usual timing for each type of deed."},
    "documents": {"title": "Prepare your visit", "lead": "To make your first appointment worthwhile, bring the right documents.", "points": [("Choose your transaction", "The list below shows the usual documents."), ("Send the list to the office", "On WhatsApp or by email, before you travel."), ("Come to the appointment", "With the originals and an ID.")]},
    "team": {"title": "The team", "lead": "An office organised around a notary and their staff.", "members": [("Notary", "Name to be confirmed"), ("Associate notary", "To be completed"), ("Chief clerk", "To be completed"), ("Front desk and formalities", "To be completed")], "placeholder": "Reserved spaces: names, roles and photos provided by the office."},
    "local": {"title": "Your notary in Ndokoti", "lead": "The office is on Avenue Roger Milla, above Afriland First Bank: a notary close by for residents of Ndokoti, Japoma and the surrounding neighbourhoods."},
    "saturday": {"title": "Open on Saturday mornings", "lead": "Working during the week? The office also sees clients on Saturday mornings.", "badge": "Saturday morning", "placeholder": "Exact hours to be confirmed with the office."},
    "social": {"title": "Satisfied clients", "lead": "A perfect score on Google. Write to the office in one click.", "score_label": "on Google", "reviews_label": "reviews", "link": "See the reviews on Google"},
    "bilingual": {"title": "A site in English and French", "lead": "All the office's information is published in both official languages, so every client can prepare their file in the language they read best."},
    "bonaberi": {"title": "Your notary in Bonabéri", "lead": "On the left bank of the Wouri: for residents of Bonabéri and the surrounding area, a notary close by, without crossing the bridge."},
    "email": {"title": "In the heart of Bonanjo", "lead": "The office is on rue de la Chambre de commerce, in the heart of Douala's administrative and business district."},
    "diaspora": {"title": "For Cameroonians abroad", "lead": "Buying land back home, settling an estate, signing a Franco-Cameroonian marriage contract: the office sees you in Akwa and also handles files remotely, by power of attorney.", "score_label": "on Google", "reviews_label": "reviews", "link": "See the reviews on Google"},
    "visibility": None,
  },
  "since_label": "Notary since",
},
}

# Accroches de héros par étude (FR, EN). Factuelles, sans promesse invérifiable.
HERO = {
  "02-njongue-etame-florence": ("Vos actes, reçus au cœur de Bonanjo.", "Your deeds, received in the heart of Bonanjo."),
  "03-grace-nkake-bollanga": ("Une notaire reconnue par ses clients, ici et à l'étranger.", "A notary trusted by her clients, at home and abroad."),
  "04-dooh-collins-ekollo-regine": ("La sécurité juridique de vos actes.", "The legal security of your deeds."),
  "05-alam-eboutou-marquise": ("Le droit des sociétés et de l'immobilier, depuis 1991.", "Corporate and property law, since 1991."),
  "06-kamako-biabo-evelyne": ("Votre dossier, étape par étape.", "Your file, step by step."),
  "07-nkono-lunduobe-marie-jeanne": ("Venez au rendez-vous avec le bon dossier.", "Come to your appointment with the right file."),
  "08-nkoue-mawafo-fonkoua-marie-louise": ("Trente-cinq ans au service de vos actes.", "Thirty-five years at the service of your deeds."),
  "09-mbollo-mbassi-dikongue-anne-marie": ("Famille, patrimoine, entreprise : vos actes en de bonnes mains.", "Family, property, business: your deeds in good hands."),
  "10-nova-notaire-associes": ("Une étude, une équipe, vos projets.", "One office, one team, your projects."),
  "11-moukory-eyango-jean-jacques": ("Un notaire près de chez vous, à Ndokoti.", "A notary near you, in Ndokoti."),
  "12-enguele-dipanda-gisele": ("Un notaire qui vous reçoit aussi le samedi.", "A notary who also sees you on Saturdays."),
  "13-ngalla-joseph": ("Votre notaire entre Deido et Bassa.", "Your notary between Deido and Bassa."),
  "14-baiye-daniel-bechem": ("Votre notaire à Bonamoussadi.", "Your notary in Bonamoussadi."),
  "15-tongoue-hamedak-jacques": ("Votre notaire à Bonabéri, au carrefour Fokou.", "Your notary in Bonabéri, at Carrefour Fokou."),
  "16-wansi-kameni-narcisse": ("Le notaire de la rive gauche du Wouri.", "The notary on the left bank of the Wouri."),
  "17-ngo-yon-benga-fride-epoune": ("Votre notaire à Bonambappè, Bonabéri.", "Your notary in Bonambappè, Bonabéri."),
  "01-mongoue-sandrine-demo": ("Votre notaire à Akwa, et à distance pour la diaspora.", "Your notary in Akwa, and remotely for Cameroonians abroad."),
  "18-nzue-rose-biteck-lima": ("Vos projets de vie, authentifiés à Bali.", "Your life projects, authenticated in Bali."),
}

# ---------- Multi-pages ----------
PAGES = {
 "fr": [("home", "index.html", "Accueil"), ("services", "domaines.html", "Domaines"), ("docs", "pieces-a-fournir.html", "Pièces à fournir"),
        ("office", "etude.html", "L'étude"), ("faq", "questions.html", "Questions"), ("contact", "contact.html", "Contact")],
 "en": [("home", "index.html", "Home"), ("services", "services.html", "Services"), ("docs", "documents.html", "Documents"),
        ("office", "office.html", "The office"), ("faq", "faq.html", "FAQ"), ("contact", "contact.html", "Contact")],
}

PAGE_INTRO = {
 "fr": {
  "services": ("Domaines d'intervention", "Terrains, successions, famille, entreprises : les actes que l'étude prépare, reçoit et conserve pour vous."),
  "docs": ("Pièces à fournir", "Préparez votre dossier avant le rendez-vous : cochez les pièces que vous avez et envoyez la liste à l'étude."),
  "office": ("L'étude", "Une étude notariale à Douala, au service des particuliers, des familles et des entreprises."),
  "faq": ("Questions fréquentes", "Les réponses aux questions que l'on pose le plus souvent au notaire."),
  "contact": ("Contact et rendez-vous", "Adresse, téléphones, plan d'accès et formulaire de rendez-vous."),
 },
 "en": {
  "services": ("Areas of practice", "Land, estates, family, business: the deeds the office prepares, receives and keeps for you."),
  "docs": ("Documents to provide", "Prepare your file before the appointment: tick the documents you have and send the list to the office."),
  "office": ("The office", "A notary office in Douala, serving individuals, families and businesses."),
  "faq": ("Frequently asked questions", "Answers to the questions most often asked of a notary."),
  "contact": ("Contact and appointments", "Address, phone numbers, map and appointment form."),
 },
}

HOME = {
 "fr": {"more": "En savoir plus", "all_services": "Tous les domaines", "docs_band_title": "Gagnez du temps : préparez votre dossier", "docs_band_text": "Pour chaque opération, la liste des pièces habituelles. Cochez ce que vous avez déjà et envoyez la liste à l'étude avant de vous déplacer.", "docs_band_cta": "Voir les pièces à fournir", "office_cta": "Découvrir l'étude", "faq_cta": "Toutes les questions", "contact_band": "Un projet ? Parlons-en.", "contact_band_text": "Appelez l'étude ou écrivez-lui : vous saurez quelles pièces réunir et à quels frais vous attendre.", "photo_note": "Photo d'illustration"},
 "en": {"more": "Learn more", "all_services": "All services", "docs_band_title": "Save time: prepare your file", "docs_band_text": "For each transaction, the usual list of documents. Tick what you already have and send the list to the office before you travel.", "docs_band_cta": "See the documents to provide", "office_cta": "About the office", "faq_cta": "All questions", "contact_band": "Have a project? Let's talk.", "contact_band_text": "Call or write to the office: you will know which documents to gather and what costs to expect.", "photo_note": "Illustrative photo"},
}

SERVICE_DETAILS = {
 "fr": {
  "terrain": ["Vente et achat de terrains titrés et d'immeubles", "Vérification du titre foncier et certificat de propriété avant signature", "Bail emphytéotique et bail de longue durée", "Prêt immobilier avec constitution d'hypothèque", "Échange, partage et donation de biens immobiliers"],
  "succession": ["Inventaire du patrimoine du défunt", "Acte de partage entre héritiers", "Transfert des titres fonciers au nom des héritiers", "Transmission des parts et actions de société", "Accompagnement des héritiers vivant à l'étranger"],
  "famille": ["Contrat de mariage avant la célébration", "Changement de régime matrimonial", "Donation aux enfants ou entre époux", "Testament authentique et dépôt de testament", "Couples binationaux : choix de la loi applicable"],
  "societe": ["Constitution de SARL, SAS et SA selon le droit OHADA", "Rédaction et modification des statuts", "Augmentation ou réduction du capital", "Cession de parts sociales ou d'actions", "Procès-verbaux d'assemblée, dissolution et liquidation"],
  "procuration": ["Procuration pour acheter ou vendre un bien", "Procuration pour régler une succession", "Procuration bancaire ou administrative", "Procuration signée à l'étranger puis utilisée au Cameroun"],
  "copie": ["Dépôt de pièces au rang des minutes", "Copies authentiques et expéditions d'actes", "Certification de signatures et de copies conformes", "Conservation des actes originaux par l'étude"],
 },
 "en": {
  "terrain": ["Sale and purchase of titled land and buildings", "Land title check and certificate of ownership before signing", "Emphyteutic and long leases", "Mortgage loans", "Exchange, division and gifts of real estate"],
  "succession": ["Inventory of the deceased's estate", "Deed of division between heirs", "Transfer of land titles to the heirs", "Transfer of company shares", "Support for heirs living abroad"],
  "famille": ["Marriage contract before the wedding", "Change of matrimonial regime", "Gifts to children or between spouses", "Authentic will and deposit of a will", "Binational couples: choice of applicable law"],
  "societe": ["Formation of SARL, SAS and SA under OHADA law", "Drafting and amending articles of association", "Capital increase or reduction", "Transfer of shares", "Minutes of general meetings, dissolution and liquidation"],
  "procuration": ["Power of attorney to buy or sell property", "Power of attorney to settle an estate", "Banking or administrative power of attorney", "Power of attorney signed abroad and used in Cameroon"],
  "copie": ["Filing of documents with the office's records", "Certified copies of deeds", "Certification of signatures and true copies", "Safekeeping of original deeds by the office"],
 },
}
DETAIL_LABEL = {"fr": "Actes courants", "en": "Common deeds"}

FAQ_EXTRA = {
 "fr": [
  ("Qu'est-ce qu'un titre foncier ?", "C'est le document officiel qui établit la propriété d'un terrain au Cameroun. Il est délivré et tenu par la conservation foncière. Un terrain sans titre foncier présente plus de risques : demandez conseil au notaire avant tout achat."),
  ("Le notaire peut-il conserver mon testament ?", "Oui. Le testament peut être reçu par le notaire sous forme authentique, ou lui être remis en dépôt. Il est ainsi conservé en lieu sûr et retrouvé au moment voulu."),
  ("Combien de temps faut-il pour créer une société ?", "Cela dépend de la rapidité avec laquelle les pièces sont réunies et des formalités d'immatriculation. L'étude vous indique le délai prévisible à l'ouverture du dossier."),
 ],
 "en": [
  ("What is a land title?", "It is the official document that establishes ownership of land in Cameroon. It is issued and kept by the land registry. Land without a title carries more risk: ask the notary for advice before buying."),
  ("Can the notary keep my will?", "Yes. The will can be received by the notary as an authentic deed, or deposited with the notary. It is kept safe and found when needed."),
  ("How long does it take to set up a company?", "It depends on how quickly the documents are gathered and on the registration formalities. The office tells you the expected timing when the file is opened."),
 ],
}

CREDITS = {"fr": "Photos d'illustration : Unsplash (licence Unsplash).", "en": "Illustrative photos: Unsplash (Unsplash licence)."}
