import Header, { TopBar } from "./components/Header.jsx";
import Hero from "./components/Hero.jsx";
import Notary from "./components/Notary.jsx";
import Services from "./components/Services.jsx";
import Abroad from "./components/Abroad.jsx";
import Documents from "./components/Documents.jsx";
import Office from "./components/Office.jsx";
import Faq from "./components/Faq.jsx";
import Contact from "./components/Contact.jsx";
import Footer from "./components/Footer.jsx";

export default function App({ c }) {
  return (
    <>
      <a
        href="#contenu"
        className="absolute -top-16 left-3 z-[100] bg-ink px-4 py-2.5 font-heading text-[0.9375rem] font-semibold text-white focus:top-3 focus:text-white"
      >
        {c.skip}
      </a>
      <TopBar c={c} />
      <Header c={c} />
      <main id="contenu">
        <Hero c={c} />
        <Notary c={c} />
        <Services c={c} />
        <Abroad c={c} />
        <Documents c={c} />
        <Office c={c} />
        <Faq c={c} />
        <Contact c={c} />
      </main>
      <Footer c={c} />
    </>
  );
}
