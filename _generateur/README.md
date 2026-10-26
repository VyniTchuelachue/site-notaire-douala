# Générateur des sites notaires

`python gen.py` régénère les 17 sites (02 à 18), six pages par langue, à partir de :
- `sites.py` : données par étude (thème, palette, angle) ; téléphones, e-mails et charges relus dans `fiche.csv` (export de la fiche Drive) ;
- `content.py` : textes communs FR/EN (pages, domaines détaillés, FAQ, accroches) ;
- `templates/` : `base.html` (en-tête, pied de page), `macros.html` (sections), une page par fichier ;
- `assets/` : CSS commun, thèmes, JavaScript ;
- `gen.py` : palettes, polices, photos Unsplash (`PH`, `HERO_IMG`, pools par domaine).

Avant de lancer sur votre machine, adaptez deux chemins : `OUT` dans `gen.py` et le chemin de `fiche.csv` dans `sites.py`. Dépendance : `pip install jinja2`.
`shot.js` et `checkall.js` servent aux captures et contrôles (Playwright).
Le site 01 (Me Mongoue) n'est pas généré : c'est le projet React/Vite existant.
