# smnotaire.com — Étude de Me Sandrine MONGOUE

Bilingual (FR/EN) website for Me Sandrine MONGOUE, notary holding the 9th office of Douala (Akwa).
Built with **React 19**, **Vite** and **Tailwind CSS 4** on Node.js. The build output is plain static files, so no server code is needed on the host.

```
index.html, en/index.html   the two pages (FR at the root, EN in /en/) with their SEO tags
src/main.jsx                picks the language from <html lang>
src/App.jsx                 page layout
src/components/             TopBar/Header, Hero, Notary (seal + definition), Services, Abroad,
                            Documents (checklists), Office, Faq, Contact (form), Footer
src/content/fr.js, en.js    all the text, in one place per language
src/content/office.js       phone, WhatsApp, e-mail, message helpers
src/index.css               Tailwind theme: colours, fonts (Open Sans + Lato), breakpoints
public/                     favicon, robots.txt, sitemap.xml
archive/site-statique/      previous hand-written HTML/CSS version (not used by the build)
```

## Working on the site

```bash
npm install        # once
npm run dev        # local preview at http://localhost:5173 (and /en/)
npm run build      # production files in dist/
```

To change any text, edit `src/content/fr.js` or `src/content/en.js`. Light markup inside the strings:
`{e}` superscript, `**bold**`, `[link](#anchor)`, `\n` line break. French typography (curly apostrophes, non-breaking spaces before `: ; ? !`) is applied automatically.

## Deploying to smnotaire.com

The domain already points to a host showing a default "Votre site est opérationnel" page.

1. Run `npm run build`.
2. Log in to the hosting panel (cPanel / file manager) or connect by FTP.
3. In the web root (usually `public_html/` or `www/`), remove or rename the host's placeholder `index.html`.
4. Upload the **contents of `dist/`**, keeping the structure (`index.html`, `en/`, `assets/`, `favicon.svg`, `robots.txt`, `sitemap.xml`).
5. Enable HTTPS (free Let's Encrypt certificate in most panels), then check `https://smnotaire.com/` and `https://smnotaire.com/en/`.

The build uses relative paths, so `dist/` also works from a sub-folder (for example GitHub Pages).

The contact form and the checklists don't need a mail server. They open the visitor's WhatsApp or e-mail app with a pre-written message to +237 690 97 80 98 / sandrine.mongoue@smnotaire.com.

## Content sources

Every fact about the office comes from:
- the prospecting sheet (address, phones, e-mail, clients from Google reviews),
- the Chambre nationale des notaires list (2019): 9th office of Douala, date 23 June 2017, B.P. 5374, holder of the records of Maître MBOBDA MONGOUE Elie,
- the Google Maps listing (plus code 2MXV+2GP).

The definition in the "Le notaire" section is the classic statutory definition of the notary in francophone civil-law systems.
The typography (Open Sans titles, Lato text) and the "Le notaire" section layout are inspired by gbanehabiba.ci; no text was copied from it.

The pages contain no invented biography, testimonials, ratings or opening hours.

## To confirm with Me MONGOUE before going live

- [ ] **WhatsApp:** is 690 97 80 98 on WhatsApp, and should clients use it?
- [ ] **English:** can the office answer messages in English? (The EN page implies it can.)
- [ ] **Payment advice:** she agrees with the note "confirm bank details by calling the landline before paying".
- [ ] **Document lists** (Pièces à fournir): she reviews and adjusts each list, especially company formation and marriage contracts.
- [ ] **Remote process:** the "sign before a notary abroad or legalise at the consulate" wording matches how she handles procurations.
- [ ] **Opening hours:** add them to the contact section if she wants them shown.
- [ ] **Photo:** a portrait or a photo of the office would strengthen "L'étude" (none is used now).
- [ ] **Seal design:** the violet "SM" seal is a decorative proposal, not her official seal.
