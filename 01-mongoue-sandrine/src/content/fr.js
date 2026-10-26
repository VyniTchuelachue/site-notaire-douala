// Textes du site en français.
// Balisage léger dans les chaînes : {e} = exposant, **gras**, [lien](#ancre), \n = retour à la ligne.
import { frenchTypography } from "./typo.js";

const fr = {
  skip: "Aller au contenu",
  topbar: {
    lang: { label: "English", href: "en/", hreflang: "en" },
  },
  header: {
    brandAria: "Me Sandrine MONGOUE, notaire à Douala : accueil",
    name: "Me Sandrine MONGOUE",
    role: "Notaire à Douala",
    menu: "Menu",
    close: "Fermer",
    navAria: "Navigation principale",
    nav: [
      { href: "#domaines", label: "Domaines" },
      { href: "#a-distance", label: "Depuis l'étranger" },
      { href: "#pieces", label: "Pièces à fournir" },
      { href: "#etude", label: "L'étude" },
    ],
    cta: { href: "#contact", label: "Prendre rendez-vous" },
  },

  hero: {
    formula: "PAR-DEVANT",
    title: "Maître Sandrine MONGOUE, notaire à Douala,",
    cont: "titulaire de la 9{e} charge, soussignée,",
    comparu: "ONT COMPARU :",
    parties: [
      "[celles et ceux qui achètent ou vendent un terrain](#terrains) ;",
      "[les familles qui règlent une succession](#successions) ou [préparent un mariage](#famille) ;",
      "[les entrepreneurs qui créent leur société](#entreprises) ;",
      "[les Camerounais de l'étranger, présents ou représentés](#a-distance).",
    ],
    lead: "L'étude prépare, reçoit et conserve vos actes authentiques. Rendez-vous à Akwa, ou à distance si vous vivez hors du Cameroun.",
    primary: { href: "#pieces", label: "Préparer mon dossier" },
    whatsapp: { href: "https://wa.me/237690978098?text=Bonjour%20Ma%C3%AEtre%2C%20", label: "Écrire sur WhatsApp" },
    card: {
      aria: "L'étude en bref",
      title: "Étude de Maître Sandrine MONGOUE",
      sub: "Notaire à Douala",
      facts: [
        { dt: "Charge", dd: "9{e} charge de Douala, depuis 2017" },
        { dt: "Adresse", dd: "581 boulevard de la Liberté, immeuble CCA, Akwa" },
        { dt: "Téléphone", dd: "[+237 233 43 08 11](tel:+237233430811)" },
        { dt: "Archives", dd: "Minutes de Maître MBOBDA MONGOUE Elie" },
      ],
      link: { href: "#contact", label: "Voir le plan d'accès" },
    },
  },

  notary: {
    id: "le-notaire",
    title: "Le notaire",
    definition:
      "Le notaire est un officier public et ministériel, établi pour recevoir tous les actes et contrats auxquels les parties doivent ou veulent faire donner le caractère d'authenticité attaché aux actes de l'autorité publique, et pour en assurer la date, en conserver le dépôt, en délivrer des grosses et expéditions.",
  },

  services: {
    id: "domaines",
    title: "Ce que l'étude fait pour vous",
    intro: "Le notaire est un officier public : ses actes font foi et s'exécutent comme un jugement.",
    items: [
      {
        id: "terrains",
        title: "Terrains et immeubles",
        text: "Achat, vente, échange, bail de longue durée, prêt avec hypothèque. Avant toute signature, l'étude vérifie le titre foncier et demande un certificat de propriété à la conservation foncière.",
      },
      {
        id: "successions",
        title: "Successions",
        text: "Inventaire des biens, partage entre héritiers, transfert des titres fonciers et des parts de société au nom des héritiers.",
      },
      {
        id: "famille",
        title: "Famille",
        text: "Contrat de mariage, y compris pour les couples binationaux et franco-camerounais. Donations aux enfants ou entre époux. Testaments.",
      },
      {
        id: "entreprises",
        title: "Entreprises",
        text: "Constitution de sociétés selon le droit OHADA (SARL, SAS, SA), augmentation de capital, cession de parts ou d'actions, procès-verbaux d'assemblée.",
      },
      {
        id: "procurations",
        title: "Procurations",
        text: "Pour qu'une personne de confiance signe à votre place au Cameroun : achat d'un terrain, succession, opération bancaire.",
      },
      {
        id: "copies",
        title: "Copies d'actes anciens",
        text: "L'étude conserve les minutes de Maître MBOBDA MONGOUE Elie. Vous pouvez y demander une copie authentique d'un acte qu'il a reçu.",
      },
    ],
  },

  abroad: {
    id: "a-distance",
    title: "Vous vivez hors du Cameroun",
    intro: "Acheter un terrain au pays, régler la succession d'un parent, créer une société à Douala : la plupart des dossiers avancent sans que vous ayez à faire le voyage.",
    note: "**Avant tout paiement,** confirmez les coordonnées bancaires en appelant l'étude au +237 233 43 08 11.",
    steps: [
      { title: "Vous nous écrivez", text: "Par WhatsApp ou par e-mail : l'opération envisagée, le bien concerné et votre pays de résidence." },
      { title: "Nous vous répondons", text: "Avec la liste des pièces à fournir et une estimation des frais : droits d'enregistrement, frais de conservation foncière, émoluments du notaire." },
      { title: "Vous envoyez les pièces", text: "D'abord en copie numérisée, pour que l'étude examine le dossier. Les originaux suivent par courrier ou par votre représentant." },
      { title: "Vous signez, ou vous vous faites représenter", text: "Lors d'un passage à Douala, ou par procuration : l'étude vous transmet le projet, que vous signez devant un notaire de votre pays de résidence ou faites légaliser au consulat du Cameroun." },
      { title: "Vous recevez votre acte", text: "Une copie authentique de l'acte, puis le suivi des formalités : enregistrement, inscription à la conservation foncière ou immatriculation au registre du commerce selon le cas." },
    ],
  },

  documents: {
    id: "pieces",
    title: "Préparez votre dossier",
    intro: "Choisissez votre opération, cochez les pièces que vous avez déjà, puis envoyez la liste à l'étude.",
    note: "Listes indicatives. L'étude vous confirme les pièces exactes après examen de votre dossier.",
    tabsAria: "Type d'opération",
    sendWhatsapp: "Envoyer la liste sur WhatsApp",
    sendEmail: "Envoyer par e-mail",
    lists: [
      {
        key: "terrain",
        tab: "Terrain",
        title: "Achat ou vente d'un terrain titré",
        items: [
          "Pièce d'identité (CNI ou passeport) de l'acheteur et du vendeur",
          "Copie du titre foncier",
          "Certificat de propriété récent, délivré par la conservation foncière",
          "Plan de situation ou plan cadastral du terrain",
          "Acte de mariage des parties mariées, avec leur régime matrimonial",
          "Si une société achète ou vend : statuts, RCCM et pouvoir du signataire",
        ],
      },
      {
        key: "succession",
        tab: "Succession",
        title: "Règlement d'une succession",
        items: [
          "Acte de décès",
          "Jugement d'hérédité",
          "Actes de naissance et pièces d'identité des héritiers",
          "Acte de mariage du défunt, le cas échéant",
          "Titres fonciers, relevés de comptes et justificatifs des autres biens",
          "Testament, s'il en existe un",
        ],
      },
      {
        key: "societe",
        tab: "Société",
        title: "Création d'une société",
        items: [
          "Pièce d'identité de chaque associé",
          "Nom envisagé et activité de la société",
          "Montant du capital et répartition entre les associés",
          "Extrait de casier judiciaire du dirigeant, ou déclaration sur l'honneur",
          "Adresse du siège : contrat de bail ou attestation de domiciliation, et plan de localisation",
        ],
      },
      {
        key: "mariage",
        tab: "Mariage",
        title: "Contrat de mariage",
        items: [
          "Pièces d'identité des deux futurs époux",
          "Actes de naissance des deux futurs époux",
          "Date et lieu prévus pour la célébration",
          "Liste des biens apportés par chacun : terrains, comptes, parts de société",
          "Pour un futur époux étranger : justificatif de nationalité et, le cas échéant, certificat de coutume",
        ],
      },
      {
        key: "procuration",
        tab: "Procuration",
        title: "Procuration depuis l'étranger",
        items: [
          "Copie de votre passeport ou de votre CNI",
          "Identité complète de la personne qui vous représentera au Cameroun",
          "Description de l'opération : bien concerné, références du titre foncier, montant",
          "Adresse où recevoir le projet de procuration",
        ],
      },
      {
        key: "copie",
        tab: "Copie d'acte",
        title: "Copie d'un acte ancien",
        hint: "Actes reçus par Maître MBOBDA MONGOUE Elie ou par Maître Sandrine MONGOUE.",
        items: [
          "Votre pièce d'identité",
          "Votre lien avec l'acte : partie, héritier, acquéreur…",
          "Nature de l'acte et noms des parties",
          "Date approximative de signature",
        ],
      },
    ],
  },

  office: {
    id: "etude",
    title: "L'étude",
    intro: "Notaire titulaire de la 9{e} charge de Douala depuis 2017. B.P. 5374 Douala.",
    paragraphs: [
      "Maître Sandrine MONGOUE est notaire titulaire de la 9{e} charge de Douala, membre de la Chambre nationale des notaires du Cameroun.",
      "L'étude est installée à Akwa, au 581 boulevard de la Liberté, immeuble CCA, face à la Pharmacie du Centre. Elle reçoit des clients de Douala comme de la diaspora : achats de terrains, contrats de mariage de couples franco-camerounais, créations d'entreprises.",
      "Un acte notarié est un acte authentique : sa date et son contenu ne peuvent être contestés que par une procédure spéciale, et il s'exécute sans passer par un tribunal. Le notaire en garde l'original, appelé minute, et vous en remet des copies.",
    ],
    subTitle: "Actes reçus par Maître MBOBDA MONGOUE Elie",
    subText: "L'étude détient les minutes de Maître MBOBDA MONGOUE Elie. Si vous êtes partie à l'un de ses actes, ou héritier d'une partie, vous pouvez en obtenir une copie authentique. Indiquez-nous la nature de l'acte, les noms des parties et la date approximative.",
  },

  faq: {
    id: "questions",
    title: "Questions fréquentes",
    intro: "Votre question n'y figure pas ? [Écrivez à l'étude](#contact).",
    items: [
      {
        q: "Puis-je acheter un terrain au Cameroun sans me déplacer ?",
        a: "Oui. Vous donnez procuration à une personne de confiance, qui signe l'acte de vente à l'étude en votre nom. L'étude se charge ensuite de faire établir le titre foncier à votre nom.",
      },
      {
        q: "Comment éviter d'acheter un terrain litigieux ?",
        a: "Privilégiez un terrain titré, et ne versez aucune somme avant que le notaire ait vérifié le titre. L'étude demande un certificat de propriété à la conservation foncière : il indique le propriétaire actuel et les charges éventuelles, comme une hypothèque ou une opposition.",
      },
      {
        q: "Combien coûte un acte notarié ?",
        a: "Les frais comprennent les droits et taxes reversés à l'État (enregistrement, conservation foncière) et les émoluments du notaire, fixés par la réglementation. Ils dépendent de la nature de l'opération et de sa valeur : demandez une estimation avant de commencer.",
      },
      {
        q: "Je cherche un acte reçu par Maître MBOBDA MONGOUE Elie.",
        a: "L'étude conserve ses minutes. Écrivez-nous avec la nature de l'acte, les noms des parties et la date approximative : nous vous indiquons la marche à suivre pour en obtenir une copie.",
      },
    ],
  },

  contact: {
    id: "contact",
    title: "Prendre rendez-vous",
    intro: "À l'étude, à Akwa, ou à distance par téléphone ou visioconférence.",
    coords: [
      { dt: "Adresse", dd: "581 boulevard de la Liberté, immeuble CCA\nFace à la Pharmacie du Centre, Akwa, Douala" },
      { dt: "Téléphone", dd: "[+237 233 43 08 11](tel:+237233430811)" },
      { dt: "Mobile et WhatsApp", dd: "[+237 690 97 80 98](tel:+237690978098)" },
      { dt: "E-mail", dd: "[sandrine.mongoue@smnotaire.com](mailto:sandrine.mongoue@smnotaire.com)" },
      { dt: "Courrier", dd: "B.P. 5374 Douala, Cameroun" },
    ],
    map: {
      title: "Plan d'accès à l'étude, boulevard de la Liberté, Akwa",
      src: "https://maps.google.com/maps?q=Notaire%20Sandrine%20Mongoue%2C%20Douala&z=17&output=embed",
      link: { href: "https://www.google.com/maps/search/?api=1&query=Notaire%20Sandrine%20Mongoue%20Douala", label: "Ouvrir l'itinéraire dans Google Maps" },
    },
    form: {
      name: "Votre nom",
      country: "Pays de résidence",
      optional: "(facultatif)",
      countryPlaceholder: "Cameroun, France, Canada…",
      subject: "Objet",
      subjects: [
        "Achat ou vente d'un terrain",
        "Succession",
        "Création de société",
        "Contrat de mariage",
        "Donation ou testament",
        "Procuration",
        "Copie d'un acte ancien",
        "Autre",
      ],
      mode: "Rendez-vous souhaité",
      modes: [
        { value: "À l'étude, à Douala", label: "À l'étude, à Douala" },
        { value: "À distance (téléphone ou visioconférence)", label: "À distance" },
      ],
      message: "Votre message",
      messagePlaceholder: "Décrivez votre projet en quelques lignes.",
      sendWhatsapp: "Envoyer sur WhatsApp",
      sendEmail: "Envoyer par e-mail",
      note: "Votre message s'ouvre dans WhatsApp ou dans votre messagerie, prêt à être envoyé. Ce site n'enregistre aucune donnée.",
    },
  },

  footer: {
    name: "Étude de Maître Sandrine MONGOUE",
    role: "Notaire à Douala, titulaire de la 9{e} charge",
    address: "581 boulevard de la Liberté, immeuble CCA, Akwa\nB.P. 5374 Douala, Cameroun",
    disclaimer: "Les informations de ce site sont générales. Elles ne remplacent pas un rendez-vous avec le notaire.",
    lang: { label: "English version", href: "en/", hreflang: "en" },
  },

  // Messages préparés pour WhatsApp et l'e-mail
  messages: {
    greeting: "Bonjour Maître,",
    preparing: "Je prépare un dossier : ",
    ready: "Pièces prêtes :",
    missing: "Pièces manquantes :",
    none: "(aucune)",
    confirm: "Pouvez-vous me confirmer la liste exacte des pièces ?",
    subjectFile: "Dossier : ",
    name: "Nom : ",
    country: "Pays de résidence : ",
    topic: "Objet : ",
    mode: "Rendez-vous souhaité : ",
    subjectRdv: "Demande de rendez-vous : ",
  },
  status: (n, total) => ({ count: n, text: ` ${n > 1 ? "pièces prêtes" : "pièce prête"} sur ${total}` }),
};

export default frenchTypography(fr);
