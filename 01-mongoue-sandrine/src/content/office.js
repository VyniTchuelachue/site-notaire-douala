// Coordonnées de l'étude, partagées par les deux langues.
export const OFFICE = {
  whatsapp: "237690978098",
  email: "sandrine.mongoue@smnotaire.com",
  phone: "+237 233 43 08 11",
  phoneHref: "tel:+237233430811",
  mobile: "+237 690 97 80 98",
  mobileHref: "tel:+237690978098",
};

export function openWhatsApp(text) {
  window.open(`https://wa.me/${OFFICE.whatsapp}?text=${encodeURIComponent(text)}`, "_blank", "noopener");
}

export function openEmail(subject, body) {
  window.location.href =
    `mailto:${OFFICE.email}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
}
