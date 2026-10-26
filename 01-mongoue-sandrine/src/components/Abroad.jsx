import Section from "./Section.jsx";

export default function Abroad({ c }) {
  const a = c.abroad;
  return (
    <Section id={a.id} title={a.title} intro={a.intro} note={a.note} band>
      <ol>
        {a.steps.map((step, i) => (
          <li key={step.title} className="grid grid-cols-[40px_minmax(0,1fr)] gap-5 pb-7 last:pb-0">
            <span
              aria-hidden="true"
              className="grid h-10 w-10 place-items-center rounded-full border-[1.5px] border-brand bg-white font-heading text-[0.9375rem] font-bold text-brand"
            >
              {i + 1}
            </span>
            <div>
              <h3 className="mt-1.5 mb-1.5 text-[1.0625rem] font-bold leading-snug">{step.title}</h3>
              <p className="text-ink-soft">{step.text}</p>
            </div>
          </li>
        ))}
      </ol>
    </Section>
  );
}
