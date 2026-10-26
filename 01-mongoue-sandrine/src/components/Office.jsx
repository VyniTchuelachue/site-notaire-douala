import Rich from "./Rich.jsx";
import Section from "./Section.jsx";

export default function Office({ c }) {
  const o = c.office;
  return (
    <Section id={o.id} title={o.title} intro={o.intro} band>
      {o.paragraphs.map((p) => (
        <p key={p} className="mb-4 max-w-[40em]">
          <Rich text={p} />
        </p>
      ))}
      <h3 className="mt-9 mb-2.5 text-[1.125rem] font-bold">{o.subTitle}</h3>
      <p className="max-w-[40em]">{o.subText}</p>
    </Section>
  );
}
