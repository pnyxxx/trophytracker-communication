# Générateur des publications

Les textes et la mise en page des publications sont écrits **ici**, dans deux fichiers Python :
`posts.py` (P01 à P32) et `stories.py` (S01 à S22). Chaque slide déclare son gabarit (`S("photo", …)`, `S("screen", …)`…,
voir `render.py`). Les photos et captures disponibles sont listées dans `assets.py`.

```sh
cd outils/generateur
npm install                                       # une fois (playwright-core)
node captures-j4l.mjs france                      # captures de la vraie page j4l-club (F_…)
node captures-j4l.mjs desert                      # la même page mise en scène dans les dunes (D_…)
node captures-j4l.mjs sansreseau                  # idem, hors réseau depuis 2 h (N_…)
python3 main.py ../../publications-instagram      # écrit les post.txt et story.txt
python3 render.py ../../publications-instagram    # prépare les visuels (ajouter P05,S01 en 2e argument pour n'en refaire que certains)
node shoot.mjs                                    # les photographie en PNG HD (2160 × 2700, stories 2160 × 3840)
python3 calendrier.py                             # tableau du calendrier, à recoller dans plan-de-publication.md
```

- Modifier un texte : le changer dans le `.py`, puis relancer `main.py`, `render.py` et `shoot.mjs`.
  Une modification faite à la main dans un `post.txt` serait écrasée à la prochaine génération.
- Si une date change, le nom du dossier change : supprimer l'ancien dossier généré.
- Photos : `photos-j4l/`, téléchargées depuis la page j4l-club, utilisées telles quelles (sans flou).
- Captures « désert » : `captures-j4l.mjs` intercepte les réponses de l'API de la page (trace, position, statistiques,
  étapes, carnet) et les remplace par une journée de piste le long des dunes. La météo est la vraie, à cette position ;
  le nom de lieu est masqué ; le numéro d'équipage et le texte du carnet de la vraie page sont retirés.
  Les horaires dépendent de l'heure de la capture (« en direct · à l'instant »).
- Chromium : celui de Playwright en cache (`~/.cache/ms-playwright/chromium-1243`).
- Mise en page : `render.css` ; charte dans `branding/charte-visuelle.md`.
