# Notaires de Douala — 18 sites de démonstration

Un dossier par étude. Pour voir un site : ouvrir le dossier, double-cliquer sur `index.html`.
Chaque site est bilingue (FR/EN) et compte six pages par langue : accueil, domaines (détail des actes), pièces à fournir (cases à cocher envoyées sur WhatsApp ou par e-mail), l'étude, questions fréquentes, contact (carte et formulaire). Photos d'illustration Unsplash (licence Unsplash), sans visage reconnaissable ; il faut être connecté à internet pour les voir.
Ce sont des maquettes de prospection : bandeau « Maquette de démonstration » en haut, pages non indexées (`noindex`, `robots.txt`). Ne pas les mettre en ligne sous le nom d'une étude avant accord.

| Dossier | Priorité | Étude | Quartier | Thème |
|---|---|---|---|---|
| `01-mongoue-sandrine` | A | Maître Sandrine MONGOUE | Akwa | Site React/Vite existant (repo Notaire-Me-MONGOUE-Sandrine) |
| `01-mongoue-sandrine-demo` | A | Maître Sandrine MONGOUE | Akwa | Nouvelle version (générateur) · moderne · violet |
| `02-njongue-etame-florence` | A | Maître Florence NJONGUE ETAME | Bonanjo | institutionnel · slate |
| `03-grace-nkake-bollanga` | A | Maître Grâce NKAKE BOLLANGA | Ndogbat / Japoma | notaria · emerald |
| `04-dooh-collins-ekollo-regine` | A | Maître Régine DOOH COLLINS | Bonanjo | prestige · navy-gold |
| `05-alam-eboutou-marquise` | B | Maître Marquise ALAM EBOUTOU | Bonanjo | editorial · burgundy |
| `06-kamako-biabo-evelyne` | B | Maître Evelyne KAMAKO BIABO | Akwa | accueil · teal |
| `07-nkono-lunduobe-marie-jeanne` | B | Maître Marie Jeanne NKONO LUNDUOBE | Akwa | notaria · cobalt |
| `08-nkoue-mawafo-fonkoua-marie-louise` | B | Maître Marie Louise MAWAFO FONKOUA | Akwa | prestige · forest-brass |
| `09-mbollo-mbassi-dikongue-anne-marie` | B | Maître Anne Marie MBOLLO MBASSI | Bali | editorial · terracotta |
| `10-nova-notaire-associes` | B | Nova Notaire & Associés | Akwa / Bonabekombo | moderne · ink-lime |
| `11-moukory-eyango-jean-jacques` | C | Maître Jean Jacques MOUKORY EYANGO | Ndokoti | institutionnel · harbor |
| `12-enguele-dipanda-gisele` | C | Maître Gisèle ENGUELE DIPANDA | Ndokoti | accueil · sun |
| `13-ngalla-joseph` | C | Maître Joseph NGALLA | Deido / Bassa | notaria · ochre |
| `14-baiye-daniel-bechem` | C | Maître Daniel Bechem BAIYE | Bonamoussadi | moderne · night-coral |
| `15-tongoue-hamedak-jacques` | C | Maître Jacques TONGOUE HAMEDAK | Bonabéri | institutionnel · pine |
| `16-wansi-kameni-narcisse` | C | Maître Narcisse WANSI KAMENI | Bonabéri | editorial · harbor-sand |
| `17-ngo-yon-benga-fride-epoune` | C | Maître Fride NGO YON BENGA épouse EPOUNE | Bonambappè | accueil · mauve |
| `18-nzue-rose-biteck-lima` | C | Maître Rose NZUE BITECK LIMA | Bali | prestige · aubergine |

## Ce qui vient d'où
- Coordonnées : fiche de prospection (Drive), vérifiée le 19/10/2026. Les téléphones et e-mails des pages sont contrôlés automatiquement contre la fiche.
- Recherche complémentaire du 26/10/2026 : notée dans le `CLAUDE.md` de chaque dossier.
- Rien d'inventé : pas de biographie, horaires, avis ou photos. Les manques sont des « emplacements réservés ».

## Modifier
- Petite retouche d'un site : éditer ses deux pages HTML (ou demander à Claude en ouvrant le dossier).
- Retouche commune aux 17 sites : `_generateur/` (Python + Jinja2), voir son README.

## Points à vérifier en priorité
- Me DOOH COLLINS : la fiche dit « ex-présidente » de la Chambre ; Cameroon Tribune la présentait encore comme présidente en juillet 2025. Le site écrit « a présidé ».
- Me ALAM EBOUTOU : l'almanach 2019 la place dans le bloc Yaoundé ; vérifier la charge et l'adresse à Douala.
- Nova Notaire & Associés : nom du notaire titulaire inconnu.
- Pour toutes les études : le mobile affiché comme WhatsApp est-il bien sur WhatsApp ?

## Sites en ligne (Vercel, équipe Tchuelachue)

Chaque projet Vercel est relié à ce dépôt GitHub (dossier racine = le dossier de l'étude) : un push sur `main` met les sites à jour automatiquement.

| Dossier | Lien |
|---|---|
| `01-mongoue-sandrine` | projet Vercel existant `notaire-me-mongoue` |
| `01-mongoue-sandrine-demo` | https://notaire-01-mongoue.vercel.app |
| `02-njongue-etame-florence` | https://notaire-02-njongue-etame.vercel.app |
| `03-grace-nkake-bollanga` | https://notaire-03-nkake-bollanga.vercel.app |
| `04-dooh-collins-ekollo-regine` | https://notaire-04-dooh-collins.vercel.app |
| `05-alam-eboutou-marquise` | https://notaire-05-alam-eboutou.vercel.app |
| `06-kamako-biabo-evelyne` | https://notaire-06-kamako-biabo.vercel.app |
| `07-nkono-lunduobe-marie-jeanne` | https://notaire-07-nkono-lunduobe.vercel.app |
| `08-nkoue-mawafo-fonkoua-marie-louise` | https://notaire-08-mawafo-fonkoua.vercel.app |
| `09-mbollo-mbassi-dikongue-anne-marie` | https://notaire-09-mbollo-mbassi.vercel.app |
| `10-nova-notaire-associes` | https://notaire-10-nova-associes.vercel.app |
| `11-moukory-eyango-jean-jacques` | https://notaire-11-moukory-eyango.vercel.app |
| `12-enguele-dipanda-gisele` | https://notaire-12-enguele-dipanda.vercel.app |
| `13-ngalla-joseph` | https://notaire-13-ngalla.vercel.app |
| `14-baiye-daniel-bechem` | https://notaire-14-baiye.vercel.app |
| `15-tongoue-hamedak-jacques` | https://notaire-15-tongoue-hamedak.vercel.app |
| `16-wansi-kameni-narcisse` | https://notaire-16-wansi-kameni.vercel.app |
| `17-ngo-yon-benga-fride-epoune` | https://notaire-17-ngo-yon-benga.vercel.app |
| `18-nzue-rose-biteck-lima` | https://notaire-18-nzue-biteck-lima.vercel.app |
