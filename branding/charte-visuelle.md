# Charte visuelle trophytracker (depuis la refonte du 9 octobre 2026)

Relevée sur le site en ligne (trophytracker.fr, page d'accueil, image de partage et page d'exemple) le 15/10/2026.
Elle remplace l'ancienne charte « crème / ambre / pochoir » de l'archive.

## Couleurs

| Nom | Code | Usage |
|---|---|---|
| Encre | `#15161A` | Fond principal (presque noir, légèrement bleuté) |
| Encre profonde | `#111215` / `#1F2026` | Cartes, panneaux, dégradés |
| Papier | `#F5F1EA` | Texte principal sur fond sombre, fonds clairs |
| Rouge trophytracker | `#E1262C` | Mots forts, boutons, « TRACKER » du logo, balise en direct |
| Ambre | `#E8A33D` | Accents secondaires, étapes, trace |
| Vert direct | `#3DBE7A` | Point « en direct » uniquement |
| Gris texte | `#8E8A83` | Textes secondaires, mentions |

Halo rouge diffus (radial, ~20 % d'opacité) en haut à droite des fonds sombres, comme sur l'image de partage du site.

## Polices (toutes gratuites, Google Fonts)

- **Bricolage Grotesque** (800) : grands titres, en minuscules avec majuscule initiale, ex. « Ton road trip, **en direct.** »
  (2ᵉ ligne en rouge).
- **Atkinson Hyperlegible** (400/700) : textes courants.
- **DM Mono** : étiquettes et petites lignes techniques, en minuscules espacées,
  ex. `en direct · à l'instant`, `privé · accès par lien`, `position · trace · photos · carnet de route`.
- **Big Shoulders Display** (900) : réservée au logo « TROPHYTRACKER ».

## Logo

- Fichiers dans `logo/` : symbole sombre / clair, favicon, avatar Instagram. Le symbole s'utilise **tel quel**
  (ne pas le redessiner, ne pas l'animer en voiture qui roule, ne pas le mettre en grand comme sujet du visuel).
- Logotype : symbole + « TROPHY » (papier `#F5F1EA`) + « TRACKER » (rouge `#E1262C`), en capitales Big Shoulders.
- Sur les visuels : petit, en haut à gauche ou en bas à droite. Jamais de slogan sous le logo.

## Éléments graphiques récurrents

- **Pastilles** (comme sur la page d'exemple) : capsules arrondies, texte DM Mono :
  - `● en direct · à l'instant` (point vert),
  - `privé · accès par lien` (fond papier, texte encre),
  - `road trip d'exemple` (contour ambre) : **obligatoire** sur toute capture de la page d'exemple.
- **Étiquettes de carte** : petit point coloré + texte DM Mono en capitales (`COL DU GALIBIER`, `NUIT À VALLOIRE`).
- **Balise en direct** : rond rouge avec halo, comme sur la carte.
- **Trace** : ligne continue ambre ou rouge sur fond satellite.

## Images

- **Photos** : les vraies photos de la page j4l-club (`outils/generateur/photos-j4l/`) : la voiture dans le sable,
  le bivouac au coucher du soleil, le feu de camp, le moteur, la pompe la nuit, le désert… **Telles quelles, sans
  flouter** les autocollants ou les numéros (décision de Julien, 16/10/2026). La 4L peut apparaître.
- **Captures réelles** de la page j4l-club (https://trophytracker.fr/road-trip/j4l-club), en carte arrondie ou dans
  un cadre de téléphone simple (coins arrondis, sans marque), toujours avec la pastille « road trip d'exemple ».
  Les captures « désert » sont la même page mise en scène dans les dunes (`captures-j4l.mjs`).
  Laisser visible la mention « Imagerie © Esri, Maxar, Earthstar Geographics » des cartes satellite.
- **Interdits** : le mot « 4L Trophy » ou « 4L » écrit dans un texte ; une moto ; une personne qui tient son téléphone
  en conduisant ; des visages identifiables en gros plan sans accord ; une fausse capture de l'espace voyageur ou d'un e-mail.

## Formats

| Type | Taille de travail | Export HD (comme avant) |
|---|---|---|
| Post simple ou carrousel (4:5) | 1080 × 1350 | 2160 × 2700 PNG |
| Story (9:16) | 1080 × 1920 | 2160 × 3840 PNG |

Stories : rien d'important dans les 250 px du haut ni les 340 px du bas (à l'échelle 1080).
Pas de bandeau imitant l'interface Instagram (photo de profil, nom du compte, barre de progression).
Les stickers (sondage, quiz, lien…) se posent dans Instagram : sur l'image, on laisse seulement l'emplacement.

## Gabarits (générateur `outils/generateur/render.py`)

- **photo** : photo plein cadre, dégradé encre, titre Bricolage (2ᵉ ligne en rouge), capture flottante possible.
- **bleed** : capture de carte en plein cadre (satellite ou relief 3D), titre par-dessus.
- **screen** : téléphone avec une capture réelle, titre au-dessus.
- **widget** : un bloc de la page (météo, tableau de bord, carnet, sponsors…) en carte arrondie.
- **type** : typographie seule (chiffre géant, liste à puces ou numérotée), fond encre, papier ou rouge.
- **chat**, **timeline**, **bingo** : formats humour et jeu.

Pas de slide finale identique à chaque post : le lien en bio est dans la légende.
