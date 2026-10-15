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

- **Captures réelles** de la page d'exemple (https://trophytracker.fr/road-trip/exemple) et de l'espace voyageur,
  dans un cadre de téléphone simple (coins arrondis, sans marque de téléphone).
  Laisser visible la mention « Imagerie © Esri, Maxar, Earthstar Geographics » des cartes satellite.
- **Photos d'ambiance** : routes de montagne, cols, pistes, désert, motos en balade, voitures de road trip
  (modèles variés et récents de préférence), vans, groupes d'amis de dos ou au loin. Sources : tes propres photos
  ou banques libres de droits (Unsplash, Pexels), en notant la source.
- **Interdits** : une Renault 4L comme sujet principal ; des autocollants de numéros d'équipage ou le logo d'un
  événement ; une personne qui tient son téléphone en conduisant ou en roulant à moto ; des visages identifiables
  sans accord.

## Formats

| Type | Taille de travail | Export HD (comme avant) |
|---|---|---|
| Post simple ou carrousel (4:5) | 1080 × 1350 | 2160 × 2700 PNG |
| Story (9:16) | 1080 × 1920 | 2160 × 3840 PNG |

Stories : rien d'important dans les 250 px du haut ni les 340 px du bas (à l'échelle 1080).
Pas de bandeau imitant l'interface Instagram (photo de profil, nom du compte, barre de progression).
Les stickers (sondage, quiz, lien…) se posent dans Instagram : sur l'image, on laisse seulement l'emplacement.

## Gabarits utilisés dans les `post.txt`

- **COUVERTURE** : fond satellite ou photo assombrie (dégradé encre de bas en haut), pastille DM Mono en haut,
  grand titre Bricolage sur 2 lignes (2ᵉ ligne en rouge), petit logo en bas, `glisse →` en DM Mono si carrousel.
- **TEXTE** : fond encre + halo rouge, titre Bricolage, 1 à 3 lignes en Atkinson, numéro rouge si liste.
- **ÉCRAN** : fond encre, téléphone centré avec une capture réelle, titre au-dessus, légende courte en DM Mono dessous.
- **AVANT / APRÈS** : écran coupé en deux (gauche : brut, en gris ; droite : résultat, en papier).
- **DERNIÈRE SLIDE (CTA)** : fond encre, logo, phrase d'action, `trophytracker.fr · lien en bio`,
  pastille `15 € par road trip · sans abonnement`.
