import { useRef, useState } from "react";
import Section from "./Section.jsx";
import { openEmail, openWhatsApp } from "../content/office.js";

// Listes de pièces à fournir : un onglet par opération, cases à cocher,
// puis envoi de la liste (prêtes / manquantes) par WhatsApp ou e-mail.
export default function Documents({ c }) {
  const d = c.documents;
  const m = c.messages;
  const [active, setActive] = useState(0);
  const [checked, setChecked] = useState({});
  const tabRefs = useRef([]);

  const list = d.lists[active];
  const isChecked = (i) => Boolean(checked[list.key]?.[i]);
  const toggle = (i) =>
    setChecked((prev) => ({ ...prev, [list.key]: { ...prev[list.key], [i]: !prev[list.key]?.[i] } }));

  const readyCount = list.items.filter((_, i) => isChecked(i)).length;
  const status = c.status(readyCount, list.items.length);

  const select = (i, focus) => {
    setActive(i);
    if (focus) tabRefs.current[i]?.focus();
  };

  const onTabKey = (e, i) => {
    const n = d.lists.length;
    const next = { ArrowRight: (i + 1) % n, ArrowLeft: (i - 1 + n) % n, Home: 0, End: n - 1 }[e.key];
    if (next !== undefined) {
      e.preventDefault();
      select(next, true);
    }
  };

  const buildMessage = () => {
    const ready = list.items.filter((_, i) => isChecked(i)).map((t) => `- ${t}`);
    const missing = list.items.filter((_, i) => !isChecked(i)).map((t) => `- ${t}`);
    return [
      m.greeting,
      "",
      `${m.preparing}${list.title}.`,
      "",
      m.ready,
      ready.length ? ready.join("\n") : m.none,
      "",
      m.missing,
      missing.length ? missing.join("\n") : m.none,
      "",
      m.confirm,
    ].join("\n");
  };

  return (
    <Section id={d.id} title={d.title} intro={d.intro} note={d.note}>
      <div className="rounded-md border border-rule bg-white px-[18px] pt-0 pb-[22px] sm:px-7 sm:pt-1 sm:pb-7">
        <div
          role="tablist"
          aria-label={d.tabsAria}
          className="-mx-[18px] flex gap-x-[22px] overflow-x-auto border-b border-rule px-[18px] [scrollbar-width:none] sm:mx-0 sm:flex-wrap sm:gap-x-[26px] sm:overflow-visible sm:px-0 [&::-webkit-scrollbar]:hidden"
        >
          {d.lists.map((l, i) => (
            <button
              key={l.key}
              ref={(el) => {
                tabRefs.current[i] = el;
              }}
              type="button"
              role="tab"
              id={`tab-${l.key}`}
              aria-controls={`panel-${l.key}`}
              aria-selected={i === active}
              tabIndex={i === active ? 0 : -1}
              onClick={() => select(i, false)}
              onKeyDown={(e) => onTabKey(e, i)}
              className="flex-none cursor-pointer border-b-2 border-transparent bg-transparent pt-[18px] pb-[14px] font-heading text-[0.9375rem] font-semibold text-ink-soft hover:text-ink aria-selected:border-brand aria-selected:text-brand sm:-mb-px"
            >
              {l.tab}
            </button>
          ))}
        </div>

        <div role="tabpanel" id={`panel-${list.key}`} aria-labelledby={`tab-${list.key}`} className="pt-6">
          <h3 className="mb-1 text-[1.0625rem] font-bold">{list.title}</h3>
          {list.hint && <p className="mb-2 text-[0.9375rem] text-ink-soft">{list.hint}</p>}
          <ul>
            {list.items.map((item, i) => (
              <li key={item} className="border-b border-rule">
                <label className="grid cursor-pointer grid-cols-[20px_minmax(0,1fr)] items-start gap-3.5 py-[13px]">
                  <input
                    type="checkbox"
                    checked={isChecked(i)}
                    onChange={() => toggle(i)}
                    className="mt-1 h-[18px] w-[18px] cursor-pointer accent-brand"
                  />
                  <span className={isChecked(i) ? "text-ink-soft" : ""}>{item}</span>
                </label>
              </li>
            ))}
          </ul>
        </div>

        <div className="mt-6 flex flex-wrap items-center justify-between gap-4">
          <p aria-live="polite" className="text-[0.9375rem] font-bold text-ink-soft">
            <strong className="text-brand">{status.count}</strong>
            {status.text}
          </p>
          <div className="flex flex-wrap gap-3 max-sm:w-full">
            <button type="button" className="btn btn-primary max-sm:flex-[1_1_100%]" onClick={() => openWhatsApp(buildMessage())}>
              {d.sendWhatsapp}
            </button>
            <button
              type="button"
              className="btn btn-secondary max-sm:flex-[1_1_100%]"
              onClick={() => openEmail(`${m.subjectFile}${list.title}`, buildMessage())}
            >
              {d.sendEmail}
            </button>
          </div>
        </div>
      </div>
    </Section>
  );
}
