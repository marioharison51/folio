# Portfolio statique

Site de portfolio généré statiquement (aucun serveur à faire tourner) —
adapté pour être déployé gratuitement sur GitHub Pages.

## Personnaliser

1. Éditez `data/projects.json` — un objet par projet (`id`, `title`, `short`,
   `description`, `github`, `demo`, `image` sont tous optionnels sauf `id`,
   `title` et `short`).
2. Testez en local :
   ```bash
   pip install -r requirements.txt
   python build.py
   ```
   Le site généré se trouve dans `dist/` — ouvrez `dist/index.html` dans un
   navigateur pour vérifier.

## Déployer sur GitHub Pages

1. Poussez ce dépôt sur GitHub.
2. Dans **Settings → Pages**, choisissez la source **GitHub Actions**.
3. Le workflow `.github/workflows/deploy.yml` se déclenche à chaque `push`
   sur `main` : il régénère le site et le publie automatiquement.
4. Votre site est en ligne à l'adresse
   `https://<votre-utilisateur>.github.io/<nom-du-repo>`.

Aucun serveur à surveiller, aucune veille à gérer — idéal pour un lien à
montrer en entretien sans risque de panne au mauvais moment.
