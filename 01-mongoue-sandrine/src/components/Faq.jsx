import Section from "./Section.jsx";

export default function Faq({ c }) {
  const f = c.faq;
  return (
    <Section id={f.id} title={f.title} intro={f.intro}>
      <div className="border-t border-rule">
        {f.items.map((item) => (
          <details key={item.q} className="group border-b border-rule">
            <summary className="grid cursor-pointer grid-cols-[minmax(0,1fr)_24px] gap-4 py-5 font-heading text-[1.0625rem] font-bold leading-snug hover:text-brand">
              {item.q}
              <span aria-hidden="true" className="text-center font-sans text-2xl leading-none font-normal text-brand">
                <span className="group-open:hidden">+</span>
                <span className="hidden group-open:inline">–</span>
              </span>
            </summary>
            <div className="pr-10 pb-[22px] text-ink-soft">
              <p>{item.a}</p>
            </div>
          </details>
        ))}
      </div>
    </Section>
  );
}
