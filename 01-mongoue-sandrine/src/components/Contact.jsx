import { useRef } from "react";
import Rich from "./Rich.jsx";
import { openEmail, openWhatsApp } from "../content/office.js";

const label = "mb-1.5 block font-heading text-[0.875rem] font-semibold text-ink";

export default function Contact({ c }) {
  const k = c.contact;
  const f = k.form;
  const m = c.messages;
  const channel = useRef("whatsapp");

  const onSubmit = (e) => {
    e.preventDefault();
    const form = e.currentTarget;
    if (!form.reportValidity()) return;
    const data = new FormData(form);
    const lines = [m.greeting, "", m.name + data.get("nom").trim()];
    const pays = (data.get("pays") || "").trim();
    if (pays) lines.push(m.country + pays);
    lines.push(m.topic + data.get("objet"));
    lines.push(m.mode + data.get("mode"));
    lines.push("", data.get("message").trim());
    const body = lines.join("\n");
    if (channel.current === "email") openEmail(m.subjectRdv + data.get("objet"), body);
    else openWhatsApp(body);
  };

  return (
    <section id={k.id} aria-labelledby={`${k.id}-titre`} className="bg-band py-18 split:py-24">
      <div className="container-site">
        <div className="mb-10">
          <h2 id={`${k.id}-titre`} className="mb-3 text-[1.75rem] font-bold leading-[1.2] tracking-[-0.01em] split:text-[2rem]">
            {k.title}
          </h2>
          <p className="max-w-[40em] text-ink-soft">{k.intro}</p>
        </div>

        <div className="grid items-start gap-9 split:grid-cols-[minmax(0,1fr)_minmax(0,1.15fr)] split:gap-14">
          <div>
            <dl className="mb-6">
              {k.coords.map((row) => (
                <div key={row.dt} className="border-t border-rule-strong py-3.5 last:border-b">
                  <dt className="text-[0.8125rem] text-ink-soft">{row.dt}</dt>
                  <dd className="mt-0.5 font-bold leading-normal">
                    <Rich text={row.dd} linkClassName="text-ink no-underline hover:text-brand hover:underline" />
                  </dd>
                </div>
              ))}
            </dl>
            <iframe
              title={k.map.title}
              src={k.map.src}
              loading="lazy"
              referrerPolicy="no-referrer-when-downgrade"
              className="h-[260px] w-full rounded border border-rule-strong bg-white"
            />
            <a href={k.map.link.href} target="_blank" rel="noopener" className="mt-2.5 inline-block font-heading text-[0.9375rem] font-semibold">
              {k.map.link.label}
            </a>
          </div>

          <form noValidate onSubmit={onSubmit} className="rounded-md border border-rule bg-white px-5 py-6 sm:p-8">
            <div className="mb-[18px]">
              <label htmlFor="f-nom" className={label}>{f.name}</label>
              <input id="f-nom" name="nom" type="text" autoComplete="name" required className="field-input" />
            </div>
            <div className="mb-[18px]">
              <label htmlFor="f-pays" className={label}>
                {f.country} <span className="font-sans font-normal text-ink-soft">{f.optional}</span>
              </label>
              <input id="f-pays" name="pays" type="text" autoComplete="country-name" placeholder={f.countryPlaceholder} className="field-input" />
            </div>
            <div className="mb-[18px]">
              <label htmlFor="f-objet" className={label}>{f.subject}</label>
              <select id="f-objet" name="objet" className="field-input">
                {f.subjects.map((s) => (
                  <option key={s}>{s}</option>
                ))}
              </select>
            </div>
            <fieldset className="mb-[18px]">
              <legend className={label}>{f.mode}</legend>
              <div className="flex flex-wrap gap-x-6 gap-y-2">
                {f.modes.map((mode, i) => (
                  <label key={mode.value} className="flex cursor-pointer items-center gap-2 text-[0.9375rem]">
                    <input type="radio" name="mode" value={mode.value} defaultChecked={i === 0} className="h-[18px] w-[18px] accent-brand" />
                    {mode.label}
                  </label>
                ))}
              </div>
            </fieldset>
            <div className="mb-[18px]">
              <label htmlFor="f-message" className={label}>{f.message}</label>
              <textarea id="f-message" name="message" required placeholder={f.messagePlaceholder} className="field-input min-h-32 resize-y" />
            </div>
            <div className="mt-1.5 flex flex-wrap gap-3">
              <button type="submit" onClick={() => (channel.current = "whatsapp")} className="btn btn-primary max-sm:flex-[1_1_100%]">
                {f.sendWhatsapp}
              </button>
              <button type="submit" onClick={() => (channel.current = "email")} className="btn btn-secondary max-sm:flex-[1_1_100%]">
                {f.sendEmail}
              </button>
            </div>
            <p className="mt-3.5 text-[0.875rem] leading-normal text-ink-soft">{f.note}</p>
          </form>
        </div>
      </div>
    </section>
  );
}
