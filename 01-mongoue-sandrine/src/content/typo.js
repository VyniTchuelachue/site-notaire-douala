// Typographie française : apostrophe courbe, espace insécable avant « : »
// et espace fine insécable avant « ; ? ! ». Les liens (href, src) ne sont pas touchés.
const SKIP = new Set(["href", "src", "id", "key"]);

function frenchString(s) {
  return s
    .replace(/'/g, "’")
    .replace(/ ([;?!])/g, " $1")
    .replace(/ :/g, " :");
}

export function frenchTypography(value, key) {
  if (typeof value === "string") return SKIP.has(key) ? value : frenchString(value);
  if (Array.isArray(value)) return value.map((v) => frenchTypography(v));
  if (value && typeof value === "object") {
    return Object.fromEntries(Object.entries(value).map(([k, v]) => [k, frenchTypography(v, k)]));
  }
  return value;
}
