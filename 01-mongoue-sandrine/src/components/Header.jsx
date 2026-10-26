import { useEffect, useState } from "react";
import { BrandMark } from "./Seal.jsx";
import { OFFICE } from "../content/office.js";

export function TopBar({ c }) {
  const { lang } = c.topbar;
  return (
    <div className="bg-ink text-topbar text-[0.8125rem] leading-snug">
      <div className="container-site flex min-h-10 items-center gap-7">
        <a href={OFFICE.phoneHref} className="text-white no-underline hover:text-white hover:underline">
          {OFFICE.phone}
        </a>
        <a href={`mailto:${OFFICE.email}`} className="hidden text-white no-underline hover:text-white hover:underline sm:inline">
          {OFFICE.email}
        </a>
        <a href={lang.href} hrefLang={lang.hreflang} lang={lang.hreflang} className="ml-auto font-bold text-white no-underline hover:text-white hover:underline">
          {lang.label}
        </a>
      </div>
    </div>
  );
}

export default function Header({ c }) {
  const h = c.header;
  const [open, setOpen] = useState(false);

  useEffect(() => {
    if (!open) return;
    const onKey = (e) => e.key === "Escape" && setOpen(false);
    document.addEventListener("keydown", onKey);
    return () => document.removeEventListener("keydown", onKey);
  }, [open]);

  return (
    <header className="sticky top-0 z-50 border-b border-rule bg-white">
      <div className="container-site flex min-h-[76px] items-center gap-8">
        <a href="./" aria-label={h.brandAria} className="mr-auto flex items-center gap-3 text-ink no-underline hover:text-ink">
          <BrandMark className="h-9 w-9 flex-none sm:h-[42px] sm:w-[42px]" />
          <span className="flex flex-col leading-tight">
            <span className="whitespace-nowrap font-heading text-base font-bold sm:text-[1.0625rem]">{h.name}</span>
            <span className="text-[0.8125rem] text-ink-soft">{h.role}</span>
          </span>
        </a>

        <button
          type="button"
          aria-expanded={open}
          aria-controls="nav"
          onClick={() => setOpen((o) => !o)}
          className="inline-flex cursor-pointer rounded border border-rule-strong bg-white px-3.5 py-2.5 font-heading text-[0.9375rem] font-semibold text-ink nav:hidden"
        >
          {open ? h.close : h.menu}
        </button>

        <nav
          id="nav"
          aria-label={h.navAria}
          onClick={(e) => e.target.closest("a") && setOpen(false)}
          className={`${open ? "flex" : "hidden"} items-center gap-8 nav:flex
            max-nav:absolute max-nav:inset-x-0 max-nav:top-full max-nav:flex-col max-nav:items-stretch max-nav:gap-4
            max-nav:border-b max-nav:border-rule max-nav:bg-white max-nav:px-[clamp(16px,4vw,40px)] max-nav:pt-2 max-nav:pb-6
            max-nav:shadow-[0_16px_24px_-16px_rgba(22,32,46,0.2)]`}
        >
          <ul className="flex gap-7 max-nav:flex-col max-nav:gap-0">
            {h.nav.map((item) => (
              <li key={item.href}>
                <a
                  href={item.href}
                  className="block whitespace-nowrap py-2 font-heading text-[0.9375rem] font-semibold text-ink no-underline hover:text-brand max-nav:border-b max-nav:border-rule max-nav:py-3.5 max-nav:text-base"
                >
                  {item.label}
                </a>
              </li>
            ))}
          </ul>
          <a href={h.cta.href} className="btn btn-primary px-[18px] py-[11px] max-nav:w-full max-nav:py-3.5">
            {h.cta.label}
          </a>
        </nav>
      </div>
    </header>
  );
}
