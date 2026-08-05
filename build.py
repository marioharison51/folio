#!/usr/bin/env python3
"""Génère un site statique (HTML + QR codes) à partir de data/projects.json.

Usage:
    python build.py

Variables d'environnement optionnelles :
    SITE_BASE_URL       URL publique finale du site (pour que les QR codes
                         pointent au bon endroit), ex:
                         https://votre-utilisateur.github.io/votre-repo
    GITHUB_PROFILE_URL  URL de votre profil GitHub, affichée dans le header
"""
import json
import os
import shutil

import qrcode
from jinja2 import Environment, FileSystemLoader

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")

BASE_URL = os.environ.get(
    "SITE_BASE_URL", "https://votre-utilisateur.github.io/votre-repo"
).rstrip("/")
GITHUB_PROFILE_URL = os.environ.get(
    "GITHUB_PROFILE_URL", "https://github.com/votre-utilisateur"
)


def load_projects():
    path = os.path.join(ROOT, "data", "projects.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def main():
    if os.path.exists(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)
    os.makedirs(os.path.join(DIST, "project"))
    os.makedirs(os.path.join(DIST, "qr"))

    shutil.copytree(os.path.join(ROOT, "static"), os.path.join(DIST, "static"))

    env = Environment(loader=FileSystemLoader(os.path.join(ROOT, "templates")))
    projects = load_projects()

    index_tpl = env.get_template("index.html")
    with open(os.path.join(DIST, "index.html"), "w", encoding="utf-8") as f:
        f.write(
            index_tpl.render(projects=projects, github_profile_url=GITHUB_PROFILE_URL)
        )

    project_tpl = env.get_template("project.html")
    for p in projects:
        page_url = f"{BASE_URL}/project/{p['id']}.html"
        qrcode.make(page_url).save(os.path.join(DIST, "qr", f"{p['id']}.png"))

        with open(
            os.path.join(DIST, "project", f"{p['id']}.html"), "w", encoding="utf-8"
        ) as f:
            f.write(
                project_tpl.render(project=p, github_profile_url=GITHUB_PROFILE_URL)
            )
            # QR code vers la page d'accueil
    qrcode.make(f"{BASE_URL}/").save(os.path.join(DIST, "qr", "home.png"))

    print(f"Site généré dans dist/ ({len(projects)} projet(s), base: {BASE_URL})")


if __name__ == "__main__":
    main()
