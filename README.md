# Mon portfolio

Le site que j'utilise pour présenter mes projets — chaque projet a sa propre
page, avec un QR code qui pointe dessus (pratique pour un CV papier ou une
carte de visite).

C'est un site statique, donc pas de serveur à faire tourner ni à surveiller :
tout est généré une fois via `build.py`, puis hébergé gratuitement sur
GitHub Pages.

## Les projets présentés

- **RHMISolens** (`rhmisolen`) — un projet développé pour apprendre à coder
  en autonomie, de la conception au code.
- **Solveur de Rubik's cube** (`rubikbcd`) — un solveur en C et Python,
  pour approfondir la logique algorithmique.

## Comment ça marche

- `data/projects.json` contient le contenu de chaque projet (titre,
  description, lien GitHub...).
- `templates/index.html` et `templates/project.html` sont des modèles HTML :
  ils définissent la mise en forme, pas le contenu.
- `build.py` lit le JSON et remplit les modèles pour générer une vraie page
  par projet — je n'ai jamais besoin de toucher au HTML pour ajouter un
  projet, seulement au JSON.

## Ajouter ou modifier un projet

Tout se passe dans `data/projects.json`. Un objet par projet, par exemple :

\`\`\`json
{
  "id": "rubikbcd",
  "title": "Solveur de Rubik's cube",
  "short": "Un projet pour apprendre et implémenter des algorithmes de résolution.",
  "description": "Implémentation en C et Python, pour approfondir la logique algorithmique.",
  "github": "https://github.com/mariohariso51/rubikbcd",
  "demo": ""
}
\`\`\`

Seuls `id`, `title` et `short` sont obligatoires — le reste est optionnel.
Le `id` sert à construire l'URL de la page (`project/<id>.html`) et le nom
du fichier QR (`qr/<id>.png`) — je reprends le nom du dépôt GitHub pour
rester cohérent.

## Tester en local

\`\`\`bash
pip install -r requirements.txt
python build.py
\`\`\`

Le résultat est généré dans `dist/` — j'ouvre `dist/index.html` dans un
navigateur pour vérifier avant de pousser.

## Déploiement

Le workflow `.github/workflows/deploy.yml` s'occupe de tout à chaque
`push` sur `main` : il régénère le site et le republie sur GitHub Pages.
Un second workflow (`validate.yml`) fait juste un test de build sur les
pull requests, sans rien publier, histoire de repérer une erreur avant
qu'elle n'atterrisse en ligne.

Le site est visible à `https://mariohariso51.github.io/folio`.
