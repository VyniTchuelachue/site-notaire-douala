import Rich from "./Rich.jsx";

export default function Footer({ c }) {
  const f = c.footer;
  return (
    <footer className="bg-ink text-[0.875rem] leading-relaxed text-footer">
      <div className="container-site grid items-start gap-5 py-12 split:grid-cols-[minmax(0,1.2fr)_minmax(0,1fr)_auto] split:gap-10">
        <div>
          <p className="mb-1.5 font-heading text-[1.0625rem] font-bold text-white">{f.name}</p>
          <p>
            <Rich text={f.role} />
          </p>
        </div>
        <div>
          <p className="mb-1.5">
            <Rich text={f.address} />
          </p>
          <p>{f.disclaimer}</p>
        </div>
        <p>
          <a href={f.lang.href} hrefLang={f.lang.hreflang} lang={f.lang.hreflang} className="text-white hover:text-white">
            {f.lang.label}
          </a>
        </p>
      </div>
    </footer>
  );
}
