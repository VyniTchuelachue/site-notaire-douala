// Affiche une chaîne avec un balisage léger :
// {e} → exposant, **texte** → gras, [texte](lien) → lien, \n → retour à la ligne.
const TOKEN = /(\*\*[^*]+\*\*|\[[^\]]+\]\([^)]+\)|\{[^}]+\}|\n)/g;

export default function Rich({ text, linkClassName }) {
  return text.split(TOKEN).map((part, i) => {
    if (!part) return null;
    if (part === "\n") return <br key={i} />;
    if (part.startsWith("**")) return <strong key={i}>{part.slice(2, -2)}</strong>;
    if (part.startsWith("{")) return <sup key={i}>{part.slice(1, -1)}</sup>;
    const link = part.match(/^\[([^\]]+)\]\(([^)]+)\)$/);
    if (link) {
      return (
        <a key={i} href={link[2]} className={linkClassName}>
          {link[1]}
        </a>
      );
    }
    return part;
  });
}
