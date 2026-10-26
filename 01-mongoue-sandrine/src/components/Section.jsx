import Rich from "./Rich.jsx";

// Section en deux colonnes : titre et note à gauche, contenu à droite.
export default function Section({ id, title, intro, note, band = false, children }) {
  return (
    <section id={id} aria-labelledby={`${id}-titre`} className={`py-18 split:py-24 ${band ? "bg-band" : ""}`}>
      <div className="container-site grid items-start gap-9 split:grid-cols-[minmax(0,4fr)_minmax(0,7fr)] split:gap-12 nav:gap-[72px]">
        <div>
          <h2 id={`${id}-titre`} className="mb-4 text-[1.75rem] font-bold leading-[1.2] tracking-[-0.01em] split:text-[2rem]">
            {title}
          </h2>
          {intro && (
            <p className="max-w-[30em] text-ink-soft">
              <Rich text={intro} />
            </p>
          )}
          {note && (
            <p className="note mt-7">
              <Rich text={note} />
            </p>
          )}
        </div>
        <div>{children}</div>
      </div>
    </section>
  );
}
