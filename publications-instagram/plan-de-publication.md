# Plan de publication Instagram : trophytracker (après la refonte)

Du **jeudi 15 octobre 2026 (ce soir) au lundi 11 janvier 2027** : 40 posts datés, 14 séquences de stories datées, des stories
du quotidien tous les jours, et 4 posts sans date (P43 prêt, P40 à P42 à sortir quand l'occasion se présente).
Chaque post a son dossier dans `posts/` : **les images prêtes à poster** (PNG 2160 × 2700) et `post.txt` (texte de chaque slide,
légende à copier, hashtags). Chaque story a son dossier dans `stories/` : les images (PNG 2160 × 3840) et `story.txt`
(stickers à ajouter dans Instagram, horaires). Les règles sont dans le `CLAUDE.md` du repo.

Horaires : **12h15** ou **19h**. Rythme : 3 posts par semaine (lundi, mercredi, vendredi), au moins une story par jour.

## 0 · Remise à zéro du compte (ce soir, jeudi 15 octobre, avant le premier post)

- [ ] **Archiver** (pas supprimer) tous les anciens posts publiés depuis le 28/09 : sur chaque post, « ⋯ » › **Archiver**.
  Ils disparaissent du profil mais restent récupérables dans ton archive. Tous parlent de l'ancien produit.
- [ ] Retirer les anciennes **stories à la une** (L'histoire, Comment ça marche, Tarifs, FAQ) : elles citent l'ancien
  événement et l'ancien prix.
- [ ] Désépingler les anciens posts épinglés (ils sont archivés de toute façon).
- [ ] Mettre la nouvelle **bio**, le nom et les liens : voir [bio-et-a-la-une.md](bio-et-a-la-une.md).
- [ ] Photo de profil : garder l'avatar actuel (`branding/logo/avatar-instagram.svg`), c'est le logo du site.
- [ ] **Messages privés** : ne plus prospecter via les hashtags d'un événement précis. Mettre à jour les réglages de
  l'extension DM : réglages › Prompts › « Remettre le texte d'origine » (le nouveau contexte est dans `defaults.js`).
- [ ] Mettre en place les 7 **stories à la une** (S01 à S07, images prêtes) d'ici samedi 17/10.

> On ne raconte jamais pourquoi le compte change. Le compte se présente simplement comme il est aujourd'hui :
> « Ton road trip, en direct. »

## 1 · La nouvelle grille de départ (15 → 17 octobre)

6 posts en 3 jours (ce soir, vendredi, samedi), pour que le profil soit complet dès le week-end. Instagram affiche les plus récents en haut :
les 3 posts à épingler sont publiés en dernier.

Après le post P06 du samedi 17/10 à 19h : **épingler P06 (c'est quoi), P05 (comment ça marche), P04 (c'est combien)**.

## 2 · Calendrier des posts et des stories datées

Chaque dossier contient les images prêtes à poster (`PNN_1-sur-N.png`…, à importer dans l'ordre) et `post.txt` (légende à copier).

### Semaine du 12/10 au 18/10

| | Date | Heure | Post | Cible | Stories du jour |
|---|---|---|---|---|---|
| [ ] | jeu. 15/10 | 20h | [P01 · Pas de réseau ? C'est normal.](posts/P01_2026-10-15_pas-de-reseau-cest-normal/post.txt) | raid / rallye, road trip en montagne | repartage du post (S27) |
| [ ] | jeu. 15/10 | 21h30 | [P02 · Le soir, tu racontes. L'IA écrit.](posts/P02_2026-10-15_le-soir-tu-racontes-lia-ecrit/post.txt) | road trip en voiture (et toutes les cibles) | repartage du post (S27) |
| [ ] | ven. 16/10 | 12h15 | [P03 · Ta page. Ton lien. Personne d'autre.](posts/P03_2026-10-16_ta-page-ton-lien-personne-dautre/post.txt) | tout le monde (road trip, proches) | repartage du post (S27) |
| [ ] | ven. 16/10 | 19h | [P04 · 15 €. Une fois. Pas d'abonnement.](posts/P04_2026-10-16_15-euros-une-fois-sans-abonnement/post.txt) | toutes les cibles | repartage du post (S27) |
| [ ] | sam. 17/10 | 12h15 | [P05 · Prêt en 5 minutes. Zéro prise de tête.](posts/P05_2026-10-17_pret-en-5-minutes/post.txt) | road trip en voiture, moto, raid (toutes cibles) | [S08 · Relance du compte : « Ton road trip, en direct. »](stories/S08_2026-10-17_relance-du-compte/story.txt) |
| [ ] | sam. 17/10 | 19h | [P06 · Ton road trip, en direct. (c'est quoi trophytracker ?)](posts/P06_2026-10-17_ton-road-trip-en-direct/post.txt) | toutes les cibles | [S08 · Relance du compte : « Ton road trip, en direct. »](stories/S08_2026-10-17_relance-du-compte/story.txt) |

### Semaine du 19/10 au 25/10

| | Date | Heure | Post | Cible | Stories du jour |
|---|---|---|---|---|---|
| [ ] | mer. 21/10 | 19h | [P07 · Ce que voient tes proches pendant que tu roules](posts/P07_2026-10-21_ce-que-voient-tes-proches/post.txt) | les proches (et les voyageurs qui veulent les rassurer) | [S09 · Visite guidée de la page d'exemple](stories/S09_2026-10-21_visite-guidee-de-la-page-dexemple/story.txt) |
| [ ] | ven. 23/10 | 12h15 | [P08 · Route des Grandes Alpes : 675 km en direct (la page d'exemple)](posts/P08_2026-10-23_route-des-grandes-alpes-en-direct/post.txt) | road trip en voiture, moto | [S10 · Vacances de la Toussaint : tu pars ?](stories/S10_2026-10-23_vacances-de-la-toussaint/story.txt) |

### Semaine du 26/10 au 01/11

| | Date | Heure | Post | Cible | Stories du jour |
|---|---|---|---|---|---|
| [ ] | lun. 26/10 | 19h | [P09 · Raid, rallye : tout l'équipage en direct](posts/P09_2026-10-26_raid-rallye-tout-lequipage-en-direct/post.txt) | raid / rallye | repartage du post (S27) |
| [ ] | mer. 28/10 | 12h15 | [P10 · Humour : « Je t'écris ce soir. »](posts/P10_2026-10-28_humour-je-tecris-ce-soir/post.txt) | road trip (voyageurs + proches) | repartage du post (S27) |
| [ ] | ven. 30/10 | 19h | [P11 · Moto : toi, les virages. Eux, la trace.](posts/P11_2026-10-30_moto-toi-les-virages-eux-la-trace/post.txt) | à moto | [S11 · Moto : ton col préféré](stories/S11_2026-10-30_moto-ton-col-prefere/story.txt) |

### Semaine du 02/11 au 08/11

| | Date | Heure | Post | Cible | Stories du jour |
|---|---|---|---|---|---|
| [ ] | lun. 02/11 | 19h | [P12 · Ce que tu as pour 15 €](posts/P12_2026-11-02_lancement-ce-que-tu-as-pour-15-euros/post.txt) | toutes les cibles | [S12 · Lancement : 15 € par road trip (quiz)](stories/S12_2026-11-02_lancement-15-euros-quiz/story.txt) |
| [ ] | mer. 04/11 | 12h15 | [P13 · Entre amis : toute la bande sur la même page](posts/P13_2026-11-04_entre-amis-toute-la-bande/post.txt) | entre amis | [S13 · Entre amis : qui raconte le mieux ?](stories/S13_2026-11-04_entre-amis-qui-raconte-le-mieux/story.txt) |
| [ ] | ven. 06/11 | 19h | [P14 · Carnet IA : ce que tu dis, ce que l'IA écrit](posts/P14_2026-11-06_carnet-ia-ce-que-tu-dis-ce-que-lia-ecrit/post.txt) | road trip (toutes cibles) | [S14 · Démo : le carnet raconté à l'IA, en vrai](stories/S14_2026-11-06_demo-carnet-ia/story.txt) |
| [ ] | sam. 07/11 | 12h15 | [P44 · On ne voit jamais ta carte bancaire](posts/P44_2026-11-07_paiement-securise-par-stripe/post.txt) | toutes les cibles | repartage du post (S27) |

### Semaine du 09/11 au 15/11

| | Date | Heure | Post | Cible | Stories du jour |
|---|---|---|---|---|---|
| [ ] | lun. 09/11 | 19h | [P15 · 5 phrases pour convaincre un sponsor](posts/P15_2026-11-09_5-phrases-pour-convaincre-un-sponsor/post.txt) | raid / rallye (et sponsors) | [S15 · Raid : ta galère n°1 avec les sponsors](stories/S15_2026-11-09_raid-ta-galere-sponsors/story.txt) |
| [ ] | mer. 11/11 | 12h15 | [P16 · Revis tout ton voyage en 3D](posts/P16_2026-11-11_revis-ton-voyage-en-3d/post.txt) | road trip, moto, raid (toutes cibles) | [S16 · Replay 3D en story](stories/S16_2026-11-11_replay-3d-teaser/story.txt) |
| [ ] | ven. 13/11 | 19h | [P17 · Humour : les 3 états de ta mère pendant ton road trip](posts/P17_2026-11-13_humour-les-3-etats-de-ta-mere/post.txt) | proches (via les voyageurs) | [S17 · Proches : tu stresses quand ils partent ?](stories/S17_2026-11-13_proches-tu-stresses/story.txt) |

### Semaine du 16/11 au 22/11

| | Date | Heure | Post | Cible | Stories du jour |
|---|---|---|---|---|---|
| [ ] | lun. 16/11 | 19h | [P18 · Ton sponsor t'a fait confiance. Montre-lui ce que ça a donné.](posts/P18_2026-11-16_rapport-pdf-pour-tes-sponsors/post.txt) | raid / rallye, sponsors | repartage du post (S27) |
| [ ] | mer. 18/11 | 12h15 | [P19 · Il fait quel temps là-bas ?](posts/P19_2026-11-18_il-fait-quel-temps-la-bas/post.txt) | proches | repartage du post (S27) |
| [ ] | ven. 20/11 | 19h | [P20 · Pourquoi pas d'abonnement ?](posts/P20_2026-11-20_lancement-pourquoi-pas-dabonnement/post.txt) | toutes les cibles | repartage du post (S27) |

### Semaine du 23/11 au 29/11

| | Date | Heure | Post | Cible | Stories du jour |
|---|---|---|---|---|---|
| [ ] | lun. 23/11 | 19h | [P21 · Les messages qu'on lit le soir (mur d'encouragements)](posts/P21_2026-11-23_le-mur-dencouragements/post.txt) | proches, raid / rallye | [S18 · Le mur d'encouragements](stories/S18_2026-11-23_mur-dencouragements/story.txt) |
| [ ] | mer. 25/11 | 12h15 | [P22 · Prêt au départ : le guide en 8 étapes](posts/P22_2026-11-25_pret-au-depart-la-check-list/post.txt) | raid / rallye, road trip | repartage du post (S27) |
| [ ] | ven. 27/11 | 19h | [P23 · Le bingo du road trip](posts/P23_2026-11-27_le-bingo-du-road-trip/post.txt) | road trip, entre amis | repartage du post (S27) |

### Semaine du 30/11 au 06/12

| | Date | Heure | Post | Cible | Stories du jour |
|---|---|---|---|---|---|
| [ ] | lun. 30/11 | 19h | [P24 · Colle ton QR code : ils scannent, ils suivent](posts/P24_2026-11-30_tes-qr-codes-prets-a-imprimer/post.txt) | raid / rallye, moto | repartage du post (S27) |
| [ ] | mer. 02/12 | 12h15 | [P25 · À quatre dans la voiture : 3,75 € chacun](posts/P25_2026-12-02_lancement-a-quatre-3-euros-75-chacun/post.txt) | entre amis | repartage du post (S27) |
| [ ] | ven. 04/12 | 19h | [P26 · FAQ : tu te demandes…](posts/P26_2026-12-04_faq/post.txt) | toutes les cibles | repartage du post (S27) |

### Semaine du 07/12 au 13/12

| | Date | Heure | Post | Cible | Stories du jour |
|---|---|---|---|---|---|
| [ ] | lun. 07/12 | 19h | [P27 · Ta cagnotte et tes sponsors, juste à côté de la carte](posts/P27_2026-12-07_soutenir-le-voyage-cagnotte-et-sponsors/post.txt) | raid / rallye | repartage du post (S27) |
| [ ] | mer. 09/12 | 12h15 | [P28 · Ce que tu partages. Et ce que personne ne voit.](posts/P28_2026-12-09_ce-que-personne-ne-voit/post.txt) | road trip, van, tour du monde | repartage du post (S27) |
| [ ] | ven. 11/12 | 19h | [P29 · Concours : gagne ton road trip en direct](posts/P29_2026-12-11_concours-gagne-ton-road-trip/post.txt) | toutes les cibles | [S19 · Concours (stories d'accompagnement)](stories/S19_2026-12-11_concours/story.txt) |

### Semaine du 14/12 au 20/12

| | Date | Heure | Post | Cible | Stories du jour |
|---|---|---|---|---|---|
| [ ] | lun. 14/12 | 19h | [P30 · Van, camping-car : ta maison roule, ta famille suit](posts/P30_2026-12-14_van-ta-maison-roule/post.txt) | van / camping-car (cible secondaire) | repartage du post (S27) |
| [ ] | mer. 16/12 | 12h15 | [P31 · Chaque soir, le résumé de ta journée chez tes proches](posts/P31_2026-12-16_le-resume-du-soir/post.txt) | proches | repartage du post (S27) |
| [ ] | ven. 18/12 | 19h | [P32 · Moto : casque posé, tu racontes](posts/P32_2026-12-18_moto-casque-pose-tu-racontes/post.txt) | à moto | repartage du post (S27) |

### Semaine du 21/12 au 27/12

| | Date | Heure | Post | Cible | Stories du jour |
|---|---|---|---|---|---|
| [ ] | lun. 21/12 | 19h | [P33 · Au repas de Noël, montre ton replay](posts/P33_2026-12-21_noel-montre-ton-replay/post.txt) | entre amis, proches, road trip | [S20 · Noël : ton plus beau road trip de l'année](stories/S20_2026-12-21_noel/story.txt) |
| [ ] | mer. 23/12 | 12h15 | [P34 · Tu pars loin, longtemps ? Ils suivent tout, d'ici.](posts/P34_2026-12-23_tour-du-monde/post.txt) | tour du monde (cible secondaire) | repartage du post (S27) |

### Semaine du 28/12 au 03/01

| | Date | Heure | Post | Cible | Stories du jour |
|---|---|---|---|---|---|
| [ ] | lun. 28/12 | 19h | [P35 · Ton road trip 2027, c'est lequel ?](posts/P35_2026-12-28_tes-road-trips-2027/post.txt) | toutes les cibles prioritaires | [S21 · Tes road trips 2027](stories/S21_2026-12-28_tes-road-trips-2027/story.txt) |

### Semaine du 04/01 au 10/01

| | Date | Heure | Post | Cible | Stories du jour |
|---|---|---|---|---|---|
| [ ] | lun. 04/01 | 19h | [P36 · Sans réseau dans le désert : ce qui se passe vraiment](posts/P36_2027-01-04_sans-reseau-dans-le-desert-ce-qui-se-passe/post.txt) | raid / rallye | repartage du post (S27) |
| [ ] | mer. 06/01 | 12h15 | [P37 · Gratuit pour ceux qui te suivent](posts/P37_2027-01-06_lancement-gratuit-pour-ceux-qui-te-suivent/post.txt) | proches | repartage du post (S27) |
| [ ] | ven. 08/01 | 19h | [P38 · Humour : les rôles dans la voiture](posts/P38_2027-01-08_humour-les-roles-dans-la-voiture/post.txt) | entre amis | repartage du post (S27) |

### Semaine du 11/01 au 17/01

| | Date | Heure | Post | Cible | Stories du jour |
|---|---|---|---|---|---|
| [ ] | lun. 11/01 | 19h | [P39 · Ton itinéraire est prêt ? Importe ton GPX. (Sinon, roule.)](posts/P39_2027-01-11_ton-itineraire-gpx-ou-pas/post.txt) | à moto, road trip en voiture | repartage du post (S27) |

## 3 · Stories du quotidien (tous les jours, en plus des séquences datées)

| Jour | Story | Modèle |
|---|---|---|
| Le jour de chaque post | Repartage du post | [S27](stories/S27_modele_quotidien-repartage-dun-post/story.txt) |
| Mardi | La fonction de la semaine | [S25](stories/S25_modele_quotidien-fonction-de-la-semaine/story.txt) |
| Jeudi | Boîte à questions | [S22](stories/S22_modele_quotidien-boite-a-questions/story.txt) |
| Vendredi 17h | « Ce week-end, tu roules ? » | [S26](stories/S26_modele_quotidien-ce-week-end-tu-roules/story.txt) |
| Dès qu'un voyageur tague le compte | Repartage | [S23](stories/S23_modele_quotidien-repartage-voyageur/story.txt) ⚠ à compléter |
| De temps en temps | Coulisses (sans visage) | [S24](stories/S24_modele_quotidien-coulisses/story.txt) ⚠ à compléter |

Les 7 stories à la une (S01 à S07) sont permanentes : voir [bio-et-a-la-une.md](bio-et-a-la-une.md).

## 4 · Posts de réserve (sans date)

| Post | Quand le sortir |
|---|---|
| [P40 · Le road trip de la semaine](posts/P40_modele_modele-road-trip-de-la-semaine/post.txt) | Dès qu'un vrai voyageur accepte (accord écrit), en collaboration. Ensuite 1 par semaine à la place d'un post du mercredi. |
| [P41 · Un vrai retour](posts/P41_modele_modele-avis-reel/post.txt) | Seulement avec une vraie citation d'un utilisateur de la nouvelle appli. |
| [P42 · Nouveau : c'est en ligne](posts/P42_modele_modele-nouveau-cest-en-ligne/post.txt) | Le jour où une nouvelle fonctionnalité est réellement en ligne. |
| [P43 · Qui est derrière trophytracker ?](posts/P43_modele_modele-qui-est-derriere/post.txt) | Prêt : quand tu veux, un samedi par exemple (relis le texte, il parle en ton nom). |

## 5 · Captures et visuels

Les visuels utilisent de **vraies captures de la page d'exemple** (prises le 15/10 sur trophytracker.fr/road-trip/exemple :
couverture, carte, relief 3D, tableau de bord, météo, profil d'altitude, carnet, photos, sponsors, mur d'encouragements),
toujours avec la pastille « road trip d'exemple ».

Ce qui demande ton compte (création guidée, QR code Traccar, e-mails « C'est parti » et « résumé du soir », rapport PDF,
autocollants QR, guide « Prêt au départ », arrêt de nuit flouté) est traité en visuel typographique, sans fausse capture.
Tu peux remplacer ces slides par de vraies captures quand tu veux : dis-le-moi et je regénère.

Trois visuels attendent du vrai contenu de ta part (marqués `[À COMPLÉTER]`) :
- **P14, slide 3** : la vraie page de carnet obtenue en dictant le texte de la slide 2 (6/11) ;
- **P16, slide 2** : la vidéo du replay 3D, exportée depuis la page d'exemple (bouton « Exporter en vidéo ») ou ton road trip (11/11) ;
- **S16** : la même vidéo au format story.

## 6 · ⚠ Le prix sur le site

Le code du site affiche encore « Tarif de lancement jusqu'au 30 novembre 2026, puis 19 € » sur la page de paiement et dans
les conditions de vente, et facture **19 € à partir du 1er décembre** (`apps/web/src/lib/legal.ts` + fonction
`private.crew_price_at` en base). Tous les posts disent « 15 € par road trip » : pour qu'ils restent vrais après le 30/11,
il faut passer le prix normal à 15 € dans le site (ou me dire de revoir les posts).

## 7 · Routine (20 minutes par jour)

- **5 min**, stories : la story du jour (voir le tableau ci-dessus).
- **7 min**, commentaires : 5 vrais commentaires sous des posts de road trip, de moto, de raid ou de van
  (encouragement, pas de lien, pas de pub).
- **5 min**, réponses : répondre à tous les commentaires et messages de la veille.
- **3 min**, repartages : chaque story qui tague le compte.

Pas de follow/unfollow en masse, pas d'abonnés achetés, jamais de faux avis. Messages privés : seulement à des
personnes qui ont réagi au compte ou qui parlent d'un road trip à venir, jamais en ciblant les participants d'un
événement précis via ses hashtags.

**Chaque dimanche**, noter 4 chiffres : road trips créés, clics sur le lien en bio, enregistrements et partages,
réponses aux stories (sondages, questions). Et regarder quel post a le mieux marché pour le décliner la semaine suivante.
