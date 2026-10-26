import Seal from "./Seal.jsx";

// Bandeau sombre « Le notaire » : le sceau dans un médaillon blanc, puis la définition.
export default function Notary({ c }) {
  const n = c.notary;
  return (
    <section id={n.id} aria-labelledby={`${n.id}-titre`} className="bg-ink py-18 text-white split:py-24">
      <div className="container-site">
        <div className="mx-auto grid h-[176px] w-[176px] place-items-center rounded-full bg-white shadow-[0_20px_50px_-20px_rgba(0,0,0,0.6)] split:h-[200px] split:w-[200px]">
          <Seal ringId="seal-ring-notary" className="h-[136px] w-[136px] text-brand split:h-[156px] split:w-[156px]" />
        </div>
        <div className="mx-auto mt-12 max-w-[52rem]">
          <h2 id={`${n.id}-titre`} className="text-[1.75rem] font-extrabold uppercase tracking-[0.02em] text-white split:text-[2.25rem]">
            {n.title}
          </h2>
          <p className="mt-5 font-heading text-[1.125rem] font-semibold leading-[1.65] text-white/90 split:text-[1.3125rem]">
            {n.definition}
          </p>
        </div>
      </div>
    </section>
  );
}
