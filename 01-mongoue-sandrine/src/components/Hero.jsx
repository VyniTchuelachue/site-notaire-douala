import Rich from "./Rich.jsx";
import Seal from "./Seal.jsx";

export default function Hero({ c }) {
  const h = c.hero;
  return (
    <section aria-labelledby="titre" className="border-b border-rule pt-12 pb-18 split:pt-20 split:pb-24">
      <div className="container-site grid items-start gap-9 split:grid-cols-[minmax(0,1.5fr)_minmax(280px,0.85fr)] split:gap-12 nav:gap-[72px]">
        <div>
          <h1 id="titre" className="text-[clamp(2.1rem,1.2rem+2.6vw,3.1rem)] font-bold leading-[1.12] tracking-[-0.015em]">
            <span className="font-extrabold tracking-[0.03em]">{h.formula}</span> {h.title}
          </h1>
          <p className="mt-3 mb-9 text-[clamp(1.2rem,1.05rem+0.5vw,1.4rem)] italic leading-snug text-ink-soft">
            <Rich text={h.cont} />
          </p>
          <p className="mb-1 font-heading text-[0.9375rem] font-bold tracking-[0.08em]">{h.comparu}</p>
          <ul className="mb-8 max-w-[36em] text-[1.125rem] leading-[1.45] sm:text-[1.1875rem]">
            {h.parties.map((p) => (
              <li
                key={p}
                className="relative border-b border-rule py-[11px] pl-[22px] before:absolute before:top-[1.15em] before:left-[2px] before:h-[7px] before:w-[7px] before:bg-brand before:content-['']"
              >
                <Rich text={p} linkClassName="text-ink no-underline hover:text-brand hover:underline" />
              </li>
            ))}
          </ul>
          <p className="mb-7 max-w-[34em] text-ink-soft">{h.lead}</p>
          <div className="flex flex-wrap gap-3">
            <a className="btn btn-primary max-sm:flex-[1_1_100%]" href={h.primary.href}>
              {h.primary.label}
            </a>
            <a className="btn btn-secondary max-sm:flex-[1_1_100%]" href={h.whatsapp.href} target="_blank" rel="noopener">
              {h.whatsapp.label}
            </a>
          </div>
        </div>

        <aside
          aria-label={h.card.aria}
          className="rounded-md border border-rule bg-white px-5 py-6 shadow-[0_1px_2px_rgba(22,32,46,0.04),0_16px_40px_-20px_rgba(22,32,46,0.18)] max-split:max-w-[520px] sm:p-8"
        >
          <Seal ringId="seal-ring-card" className="mb-5 h-[92px] w-[92px] text-brand" />
          <p className="mb-1 font-heading text-[1.125rem] font-bold leading-snug">{h.card.title}</p>
          <p className="mb-5 text-[0.9375rem] text-ink-soft">{h.card.sub}</p>
          <dl className="mb-5">
            {h.card.facts.map((f) => (
              <div key={f.dt} className="border-t border-rule py-3">
                <dt className="text-[0.8125rem] text-ink-soft">{f.dt}</dt>
                <dd className="mt-0.5 text-[0.9375rem] font-bold leading-snug">
                  <Rich text={f.dd} />
                </dd>
              </div>
            ))}
          </dl>
          <a href={h.card.link.href} className="font-heading text-[0.9375rem] font-semibold">
            {h.card.link.label}
          </a>
        </aside>
      </div>
    </section>
  );
}
