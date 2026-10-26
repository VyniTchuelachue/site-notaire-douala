// Site text in English. Same light markup as fr.js.
const en = {
  skip: "Skip to content",
  topbar: {
    lang: { label: "Français", href: "../", hreflang: "fr" },
  },
  header: {
    brandAria: "Maître Sandrine MONGOUE, notary in Douala: home",
    name: "Me Sandrine MONGOUE",
    role: "Notary in Douala",
    menu: "Menu",
    close: "Close",
    navAria: "Main navigation",
    nav: [
      { href: "#services", label: "Services" },
      { href: "#from-abroad", label: "From abroad" },
      { href: "#documents", label: "Documents" },
      { href: "#office", label: "The office" },
    ],
    cta: { href: "#contact", label: "Book an appointment" },
  },

  hero: {
    formula: "BEFORE",
    title: "Maître Sandrine MONGOUE, notary in Douala,",
    cont: "holder of the 9th notarial office, the undersigned,",
    comparu: "THERE APPEARED:",
    parties: [
      "[people buying or selling land](#land);",
      "[families settling an estate](#estates) or [preparing a marriage](#family);",
      "[entrepreneurs setting up a company](#companies);",
      "[Cameroonians abroad, in person or by proxy](#from-abroad).",
    ],
    lead: "The office drafts, executes and keeps your notarial deeds. Meet us in Akwa, or work with us remotely if you live outside Cameroon.",
    primary: { href: "#documents", label: "Prepare my file" },
    whatsapp: { href: "https://wa.me/237690978098?text=Dear%20Ma%C3%AEtre%20MONGOUE%2C%20", label: "Message on WhatsApp" },
    card: {
      aria: "The office at a glance",
      title: "Office of Maître Sandrine MONGOUE",
      sub: "Notary in Douala",
      facts: [
        { dt: "Notarial office", dd: "9th office of Douala, since 2017" },
        { dt: "Address", dd: "581 boulevard de la Liberté, immeuble CCA, Akwa" },
        { dt: "Telephone", dd: "[+237 233 43 08 11](tel:+237233430811)" },
        { dt: "Records", dd: "Deeds of Maître MBOBDA MONGOUE Elie" },
      ],
      link: { href: "#contact", label: "See the map" },
    },
  },

  notary: {
    id: "the-notary",
    title: "The notary",
    definition:
      "The notary is a public and ministerial officer, appointed to receive all deeds and contracts to which the parties must or wish to give the authenticity attached to acts of public authority, to certify their date, keep them on deposit, and issue enforceable and certified copies of them.",
  },

  services: {
    id: "services",
    title: "What the office can do for you",
    intro: "In Cameroon, the notary is a public officer: notarial deeds are conclusive evidence and enforceable like a court judgment.",
    items: [
      {
        id: "land",
        title: "Land and property",
        text: "Purchase, sale, exchange, long leases, mortgage loans. Before anything is signed, the office checks the land title and requests a certificate of ownership from the land registry.",
      },
      {
        id: "estates",
        title: "Estates",
        text: "Inventory of assets, division between heirs, transfer of land titles and company shares into the heirs’ names.",
      },
      {
        id: "family",
        title: "Family",
        text: "Marriage contracts, including for binational and Franco-Cameroonian couples. Gifts to children or between spouses. Wills.",
      },
      {
        id: "companies",
        title: "Companies",
        text: "Incorporation under OHADA law (SARL, SAS, SA), capital increases, transfers of shares, minutes of general meetings.",
      },
      {
        id: "proxies",
        title: "Powers of attorney",
        text: "So that someone you trust can sign on your behalf in Cameroon: buying land, settling an estate, a banking transaction.",
      },
      {
        id: "copies",
        title: "Copies of older deeds",
        text: "The office holds the records of Maître MBOBDA MONGOUE Elie. You can request a certified copy of a deed he executed.",
      },
    ],
  },

  abroad: {
    id: "from-abroad",
    title: "If you live outside Cameroon",
    intro: "Buying land back home, settling a parent’s estate, setting up a company in Douala: most files can move forward without you having to travel.",
    note: "**Before making any payment,** confirm the bank details by calling the office on +237 233 43 08 11.",
    steps: [
      { title: "You write to us", text: "By WhatsApp or e-mail: what you want to do, the property concerned and the country where you live." },
      { title: "We reply", text: "With the list of documents required and an estimate of the costs: registration duties, land registry fees and the notary’s fees." },
      { title: "You send the documents", text: "First as scanned copies, so the office can review the file. The originals follow by post or through your representative." },
      { title: "You sign, or someone signs for you", text: "During a visit to Douala, or by power of attorney: the office sends you the draft, which you sign before a notary in your country of residence or have legalised at the Cameroonian consulate." },
      { title: "You receive your deed", text: "A certified copy of the deed, then follow-up of the formalities: registration, entry at the land registry or at the trade and companies register, as the case may be." },
    ],
  },

  documents: {
    id: "documents",
    title: "Prepare your file",
    intro: "Choose your transaction, tick the documents you already have, then send the list to the office.",
    note: "These lists are a guide. The office confirms the exact documents once it has reviewed your file.",
    tabsAria: "Type of transaction",
    sendWhatsapp: "Send the list on WhatsApp",
    sendEmail: "Send by e-mail",
    lists: [
      {
        key: "land",
        tab: "Land",
        title: "Purchase or sale of titled land",
        items: [
          "ID card or passport of the buyer and the seller",
          "Copy of the land title",
          "Recent certificate of ownership from the land registry",
          "Location plan or cadastral plan of the land",
          "Marriage certificate of any married party, with their matrimonial regime",
          "If a company is buying or selling: articles, RCCM extract and the signatory’s authority",
        ],
      },
      {
        key: "estate",
        tab: "Estate",
        title: "Settling an estate",
        items: [
          "Death certificate",
          "Court judgment of heirship (jugement d’hérédité)",
          "Birth certificates and ID of the heirs",
          "Marriage certificate of the deceased, if applicable",
          "Land titles, bank statements and proof of other assets",
          "Will, if there is one",
        ],
      },
      {
        key: "company",
        tab: "Company",
        title: "Setting up a company",
        items: [
          "ID of each shareholder",
          "Proposed company name and business activity",
          "Amount of share capital and how it is split between shareholders",
          "Criminal record extract of the manager, or a sworn statement",
          "Registered office: lease or domiciliation certificate, and a location plan",
        ],
      },
      {
        key: "marriage",
        tab: "Marriage",
        title: "Marriage contract",
        items: [
          "ID of both future spouses",
          "Birth certificates of both future spouses",
          "Planned date and place of the wedding",
          "List of the assets each of you brings: land, accounts, company shares",
          "For a foreign future spouse: proof of nationality and, where required, a certificate of custom",
        ],
      },
      {
        key: "proxy",
        tab: "Power of attorney",
        title: "Power of attorney from abroad",
        items: [
          "Copy of your passport or ID card",
          "Full identity of the person who will represent you in Cameroon",
          "Description of the transaction: property concerned, land title references, amount",
          "Address where you want to receive the draft power of attorney",
        ],
      },
      {
        key: "copy",
        tab: "Copy of a deed",
        title: "Copy of an older deed",
        hint: "Deeds executed by Maître MBOBDA MONGOUE Elie or by Maître Sandrine MONGOUE.",
        items: [
          "Your ID",
          "Your connection to the deed: party, heir, buyer…",
          "Type of deed and names of the parties",
          "Approximate date of signature",
        ],
      },
    ],
  },

  office: {
    id: "office",
    title: "The office",
    intro: "Holder of the 9th notarial office of Douala since 2017. P.O. Box 5374 Douala.",
    paragraphs: [
      "Maître Sandrine MONGOUE holds the 9th notarial office of Douala. She is a member of the National Chamber of Notaries of Cameroon.",
      "The office is in Akwa, at 581 boulevard de la Liberté, immeuble CCA, opposite the Pharmacie du Centre. Its clients come from Douala and from the diaspora: land purchases, marriage contracts for Franco-Cameroonian couples, company formations.",
      "A Cameroonian notary is a civil-law notary, which is a different role from a notary public in the UK or the United States. A notarial deed is an authentic instrument: its date and content can only be challenged through a special procedure, and it can be enforced without going to court. The notary keeps the original, called the minute, and gives you certified copies.",
    ],
    subTitle: "Deeds executed by Maître MBOBDA MONGOUE Elie",
    subText: "The office holds the records of Maître MBOBDA MONGOUE Elie. If you were a party to one of his deeds, or are the heir of a party, you can obtain a certified copy. Tell us the type of deed, the names of the parties and the approximate date.",
  },

  faq: {
    id: "questions",
    title: "Common questions",
    intro: "Can’t find your question? [Write to the office](#contact).",
    items: [
      {
        q: "Can I buy land in Cameroon without travelling?",
        a: "Yes. You give a power of attorney to someone you trust, who signs the deed of sale at the office in your name. The office then has the land title transferred to your name.",
      },
      {
        q: "How do I avoid buying disputed land?",
        a: "Prefer titled land, and pay nothing until the notary has checked the title. The office requests a certificate of ownership from the land registry: it shows the current owner and any charges, such as a mortgage or an objection.",
      },
      {
        q: "How much does a notarial deed cost?",
        a: "Costs include duties and taxes paid to the State (registration, land registry) and the notary’s fees, which are set by regulation. They depend on the type of transaction and its value: ask for an estimate before you start.",
      },
      {
        q: "I am looking for a deed executed by Maître MBOBDA MONGOUE Elie.",
        a: "The office holds his records. Write to us with the type of deed, the names of the parties and the approximate date, and we will tell you how to obtain a copy.",
      },
    ],
  },

  contact: {
    id: "contact",
    title: "Book an appointment",
    intro: "At the office in Akwa, or remotely by phone or video call.",
    coords: [
      { dt: "Address", dd: "581 boulevard de la Liberté, immeuble CCA\nOpposite the Pharmacie du Centre, Akwa, Douala" },
      { dt: "Telephone", dd: "[+237 233 43 08 11](tel:+237233430811)" },
      { dt: "Mobile and WhatsApp", dd: "[+237 690 97 80 98](tel:+237690978098)" },
      { dt: "E-mail", dd: "[sandrine.mongoue@smnotaire.com](mailto:sandrine.mongoue@smnotaire.com)" },
      { dt: "Post", dd: "P.O. Box 5374 Douala, Cameroon" },
    ],
    map: {
      title: "Map to the office, boulevard de la Liberté, Akwa",
      src: "https://maps.google.com/maps?q=Notaire%20Sandrine%20Mongoue%2C%20Douala&z=17&hl=en&output=embed",
      link: { href: "https://www.google.com/maps/search/?api=1&query=Notaire%20Sandrine%20Mongoue%20Douala", label: "Get directions in Google Maps" },
    },
    form: {
      name: "Your name",
      country: "Country of residence",
      optional: "(optional)",
      countryPlaceholder: "Cameroon, United Kingdom, United States…",
      subject: "Subject",
      subjects: [
        "Purchase or sale of land",
        "Estate",
        "Setting up a company",
        "Marriage contract",
        "Gift or will",
        "Power of attorney",
        "Copy of an older deed",
        "Other",
      ],
      mode: "Preferred appointment",
      modes: [
        { value: "At the office in Douala", label: "At the office in Douala" },
        { value: "Remote (phone or video call)", label: "Remote" },
      ],
      message: "Your message",
      messagePlaceholder: "Describe your plans in a few lines.",
      sendWhatsapp: "Send on WhatsApp",
      sendEmail: "Send by e-mail",
      note: "Your message opens in WhatsApp or your e-mail app, ready to send. This site does not store any data.",
    },
  },

  footer: {
    name: "Office of Maître Sandrine MONGOUE",
    role: "Notary in Douala, holder of the 9th notarial office",
    address: "581 boulevard de la Liberté, immeuble CCA, Akwa\nP.O. Box 5374 Douala, Cameroon",
    disclaimer: "The information on this site is general. It does not replace an appointment with the notary.",
    lang: { label: "Version française", href: "../", hreflang: "fr" },
  },

  messages: {
    greeting: "Dear Maître MONGOUE,",
    preparing: "I am preparing a file: ",
    ready: "Documents I have:",
    missing: "Documents still missing:",
    none: "(none)",
    confirm: "Could you confirm the exact list of documents required?",
    subjectFile: "File: ",
    name: "Name: ",
    country: "Country of residence: ",
    topic: "Subject: ",
    mode: "Preferred appointment: ",
    subjectRdv: "Appointment request: ",
  },
  status: (n, total) => ({ count: n, text: ` of ${total} ${total > 1 ? "documents" : "document"} ready` }),
};

export default en;
