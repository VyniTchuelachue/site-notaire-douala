import Section from "./Section.jsx";

export default function Services({ c }) {
  const s = c.services;
  return (
    <Section id={s.id} title={s.title} intro={s.intro}>
      <dl className="grid gap-x-12 sm:grid-cols-2">
        {s.items.map((item) => (
          <div key={item.id} id={item.id} className="border-t border-rule pt-6 pb-7">
            <dt className="mb-2 font-heading text-[1.125rem] font-bold leading-snug">{item.title}</dt>
            <dd className="text-ink-soft">{item.text}</dd>
          </div>
        ))}
      </dl>
    </Section>
  );
}
