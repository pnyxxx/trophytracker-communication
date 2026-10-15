# Générateur des publications

Les textes des publications sont écrits **ici**, dans des fichiers Python (une entrée par post ou par story) :
`posts1.py` (P01 à P14), `posts2.py` (P15 à P44), `stories.py` (S01 à S27), `hashtags.py` (4 hashtags maximum par post).
À partir de là, trois scripts fabriquent tout le reste :

```sh
cd outils/generateur
npm install                                  # une fois (playwright-core)
python3 main.py ../../publications-instagram     # écrit les post.txt et story.txt
python3 render.py ../../publications-instagram   # prépare les visuels (ajouter P05,S01 en 2e argument pour n'en refaire que certains)
node shoot.mjs                                   # les photographie en PNG HD (2160 × 2700, stories 2160 × 3840)
python3 calendrier.py                            # tableau du calendrier, à recoller dans plan-de-publication.md
node captures.mjs                                # refait les captures de la page d'exemple dans captures/
```

- Modifier un texte : le changer dans le `.py`, puis relancer `main.py` (et `render.py` + `shoot.mjs` si le texte est sur l'image).
  Une modification faite à la main dans un `post.txt` serait écrasée à la prochaine génération.
- Si une date change, le nom du dossier change : supprimer l'ancien dossier généré.
- Chromium : celui de Playwright en cache (`~/.cache/ms-playwright/chromium-1243`).
- Mise en page : `render.py` lit le texte de chaque slide (« Titre : … », « Pastille : … », « DM Mono : … », lignes « … »)
  et choisit le gabarit (couverture, texte, écran, dernière slide) ; styles dans `render.css`, charte dans `branding/charte-visuelle.md`.
