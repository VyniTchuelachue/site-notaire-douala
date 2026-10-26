# Contexte pour Claude — Nova Notaire & Associés

Site vitrine de démonstration pour **Nova Notaire & Associés**, étude notariale à douala. Il sert à la prospection : on le montre à l'étude pour lui proposer un site.
Ne jamais le mettre en ligne sous le nom de l'étude avant un accord signé.

## Fichiers
- Site statique, sans build : ouvrir `index.html` dans un navigateur suffit (connexion internet nécessaire pour les photos, les polices et la carte).
- Six pages par langue : accueil (`index.html`), domaines, pièces à fournir, l'étude, questions, contact. En anglais : index, services, documents, office, faq, contact.
- Langues : français à la racine (`index.html`), anglais dans `en/`.
- Photos d'illustration : Unsplash (licence Unsplash, usage commercial libre, sans attribution obligatoire), chargées depuis images.unsplash.com. Aucune ne montre de visage reconnaissable. Photos utilisées : baby, books_old, justice, keys, library, office_glass, office_green, office_modern, pen_black, pen_book, pen_gold, sign_a, sign_c (voir `PH` dans le générateur pour les identifiants).
- `assets/style.css` : variables de couleurs et polices en tête de fichier (`:root`), puis styles communs et thème.
- `assets/site.js` : menu mobile, onglets « pièces à fournir », envoi des formulaires vers WhatsApp ou e-mail (aucun serveur).
- Le bandeau jaune « Maquette de démonstration » est la div `.demo-ribbon` en haut de chaque page : la supprimer quand l'étude a signé.
- Les pages sont générées par le générateur commun (dossier `_generateur/` à la racine de `notaires/`). Pour une petite retouche, éditer directement les deux pages HTML ; pour une refonte, modifier le générateur et régénérer.

## Design
- Thème : **moderne** · palette : **ink-lime** · polices : Archivo (titres) / Archivo (texte).
- Angle du site : Structure récente « & associés » en croissance : site complet avec équipe. Demander le nom du notaire titulaire.

## Faits (source : fiche de prospection, vérifiée le 19/10/2026)
- Notaire / étude : Nova Notaire & Associés
- Charge : À confirmer (absent de la liste 2019)
- Adresse : Avenue de la Liberté (plus code 3P52+9Q8), Akwa / Bonabekombo
- Téléphones : +237 699 72 14 34
- E-mail (annuaire) : —
- Présence web : Aucun site trouvé (fiches annuaires seulement)
- Google Maps : Fiche Google existante

## Recherche complémentaire (26/10/2026)
- Fiche Google existante ; fiches annuaires (doualabouge.com) ; absent de la liste de la Chambre 2019.
- Nom du notaire titulaire inconnu : à demander au premier appel. L'équipe est laissée en emplacements à remplir.

## Règles
- Ne rien inventer : pas de biographie, diplômes, horaires, avis, témoignages ou photos qui ne viennent pas de l'étude ou d'une source vérifiée. Ce qui manque reste en « emplacement réservé ».
- Ne pas afficher une note Google inférieure à 4,5.
- Les listes de pièces à fournir sont indicatives et doivent être relues par le notaire.

## À confirmer avec l'étude avant mise en ligne
- [ ] Le numéro +237 699 72 14 34 est-il sur WhatsApp, et l'étude veut-elle l'utiliser ?
- [ ] Les e-mails sont-ils relevés à l'adresse (aucune adresse connue) ?
- [ ] Horaires d'ouverture (non affichés).
- [ ] Vraie photo de l'étude ou portrait, à mettre à la place de la photo d'illustration de la page « L'étude », et texte de présentation.
- [ ] Relecture des pièces à fournir et des questions fréquentes.
- [ ] Le monogramme « N&A » est une proposition graphique, pas le sceau officiel.
