# Contexte pour Claude — Maître Sandrine MONGOUE

Site vitrine de démonstration pour **Maître Sandrine MONGOUE**, notaire à douala. Il sert à la prospection : on le montre à l'étude pour lui proposer un site.
Ne jamais le mettre en ligne sous le nom de l'étude avant un accord signé.

## Fichiers
- Site statique, sans build : ouvrir `index.html` dans un navigateur suffit (connexion internet nécessaire pour les photos, les polices et la carte).
- Six pages par langue : accueil (`index.html`), domaines, pièces à fournir, l'étude, questions, contact. En anglais : index, services, documents, office, faq, contact.
- Langues : français à la racine (`index.html`), anglais dans `en/`.
- Photos d'illustration : Unsplash (licence Unsplash, usage commercial libre, sans attribution obligatoire), chargées depuis images.unsplash.com. Aucune ne montre de visage reconnaissable. Photos utilisées : baby, books_old, justice, keys, library, office_glass, office_green, pen_black, pen_book, pen_ink, sign_a, sign_b, street (voir `PH` dans le générateur pour les identifiants).
- `assets/style.css` : variables de couleurs et polices en tête de fichier (`:root`), puis styles communs et thème.
- `assets/site.js` : menu mobile, onglets « pièces à fournir », envoi des formulaires vers WhatsApp ou e-mail (aucun serveur).
- Le bandeau jaune « Maquette de démonstration » est la div `.demo-ribbon` en haut de chaque page : la supprimer quand l'étude a signé.
- Les pages sont générées par le générateur commun (dossier `_generateur/` à la racine de `notaires/`). Pour une petite retouche, éditer directement les deux pages HTML ; pour une refonte, modifier le générateur et régénérer.

## Design
- Thème : **moderne** · palette : **violet** · polices : Space Grotesk (titres) / Inter (texte).
- Angle du site : « Vous avez déjà le domaine, il est vide : on le remplit. » Site FR/EN orienté diaspora (RDV à distance, pièces à fournir).

## Faits (source : fiche de prospection, vérifiée le 19/10/2026)
- Notaire / étude : Me MONGOUE Sandrine
- Charge : Douala 9e charge
- Adresse : 581 Bd de la Liberté, imm. CCA, face Pharmacie du Centre, Akwa
- Téléphones : +237 233 43 08 11 / 690 97 80 98
- E-mail (annuaire) : sandrine.mongoue@smnotaire.com
- Présence web : Domaine smnotaire.com acheté MAIS page vide d'hébergeur (« Votre site est opérationnel »)
- Google Maps : 4,6 (8 avis) – clients de la diaspora, mariages franco-camerounais, création d'entreprise

## Recherche complémentaire (26/10/2026)
- Google Maps : 4,6 (8 avis) — clients de la diaspora, mariages franco-camerounais, création d'entreprise.
- Domaine smnotaire.com déjà acheté mais vide (page d'hébergeur) : ce site peut y être publié tel quel.
- Liste de la Chambre (2019), reprise du site React existant : 9e charge de Douala depuis le 23 juin 2017, B.P. 5374, détentrice des minutes de Maître MBOBDA MONGOUE Elie.
- Le site React/Vite existant reste dans le dossier 01-mongoue-sandrine (projet Vercel notaire-me-mongoue).

## Règles
- Ne rien inventer : pas de biographie, diplômes, horaires, avis, témoignages ou photos qui ne viennent pas de l'étude ou d'une source vérifiée. Ce qui manque reste en « emplacement réservé ».
- Ne pas afficher une note Google inférieure à 4,5.
- Les listes de pièces à fournir sont indicatives et doivent être relues par le notaire.

## À confirmer avec l'étude avant mise en ligne
- [ ] Le numéro +237 690 97 80 98 est-il sur WhatsApp, et l'étude veut-elle l'utiliser ?
- [ ] Les e-mails sont-ils relevés à l'adresse sandrine.mongoue@smnotaire.com ?
- [ ] Horaires d'ouverture (non affichés).
- [ ] Vraie photo de l'étude ou portrait, à mettre à la place de la photo d'illustration de la page « L'étude », et texte de présentation.
- [ ] Relecture des pièces à fournir et des questions fréquentes.
- [ ] Le monogramme « SM » est une proposition graphique, pas le sceau officiel.
