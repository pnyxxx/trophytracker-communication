from common import d, H, HANDLE, EXEMPLE, CTA_FINAL

POSTS = []
P = POSTS.append

# ───────────────────────── GRILLE DE DÉPART (17 → 19 octobre) ─────────────────────────

P(dict(
    id=1, date=d("2026-10-15"), heure="20h", slug="pas-de-reseau-cest-normal",
    titre="Pas de réseau ? C'est normal.",
    cible="raid / rallye, road trip en montagne", sujet="le direct même sans réseau",
    format="post simple", objectif="partager (en message privé)",
    remarque="Grille de départ. Remplace l'ancien post 5 (objection « on partagera notre position »).",
    slides=[
        ("VISUEL UNIQUE",
         "En haut, pastille : « pas de réseau, c'est normal »\nTitre : « Pas de réseau ? » / « C'est normal. » (2ᵉ ligne en rouge)\n"
         "Sous le titre : « Ton téléphone garde tout en mémoire et envoie ta trace dès que ça capte. »\nEn bas : petit logo + trophytracker.fr",
         "Gabarit COUVERTURE. Photo d'une piste qui file dans le désert au coucher du soleil (ou d'une route de col "
         "qui disparaît dans les nuages), assombrie par un dégradé encre. Une trace ambre en pointillés part du bas "
         "de l'image et redevient une ligne continue plus haut, avec la balise rouge au bout : on comprend que les "
         "points « en attente » finissent par arriver. Aucun véhicule reconnaissable au premier plan."),
    ],
    legende="""Dans les dunes, au fond d'une vallée, en haut d'un col : à un moment, ça ne capte plus. Et ce n'est pas grave.

Pendant que tu roules sans réseau, ton téléphone garde chaque position en mémoire. Dès que ça capte à nouveau, tout part d'un coup et ta trace se complète sur ta page.

Et pour que personne ne s'inquiète pour rien, ceux qui te suivent voient un bandeau clair sur ta page : « Pas de réseau, c'est normal ».

Envoie ça à celui qui dit « on verra bien s'il y a du réseau là-bas ».
Ton road trip, en direct : lien en bio.""",
    hashtags="#raid #rallye #desert #roadtrip #montagne #trophytracker",
))

P(dict(
    id=2, date=d("2026-10-15"), heure="21h30", slug="le-soir-tu-racontes-lia-ecrit",
    titre="Le soir, tu racontes. L'IA écrit.",
    cible="road trip en voiture (et toutes les cibles)", sujet="carnet de bord raconté à l'IA (fonction phare)",
    format="carrousel 6 visuels", objectif="enregistrer + lien en bio",
    remarque="Grille de départ. Nouvelle fonctionnalité phare, à mettre en avant souvent.",
    slides=[
        ("1/6 · COUVERTURE", "Pastille : « carnet de bord »\nTitre : « Le soir, tu racontes. » / « L'IA écrit. » (en rouge)\n« glisse → »",
         "Photo de nuit : un téléphone posé sur une table de camping ou un capot, écran allumé avec un gros bouton "
         "micro rouge, guirlande ou lampe frontale floue derrière. Aucun visage."),
        ("2/6 · TEXTE", "« 1. Tu appuies sur le micro. »\n« Et tu racontes ta journée comme à un pote. Avec les « euh », les détours et les fous rires. »",
         "Gabarit TEXTE. Grand bouton micro rouge stylisé au centre (rond rouge, icône micro papier), ondes sonores ambre autour."),
        ("3/6 · ÉCRAN", "« 2. L'IA en fait une page de carnet. »\n« Elle garde tes anecdotes, retire les hésitations et ajoute les kilomètres et l'altitude du jour. »",
         "Gabarit ÉCRAN. Capture réelle d'une page de carnet générée dans l'espace voyageur (capture C7 du plan)."),
        ("4/6 · TEXTE", "« Sans rien inventer. »\n« Ce que tu n'as pas raconté n'apparaît pas. C'est ton voyage, avec tes mots. »",
         "Gabarit TEXTE, fond encre, le titre en très grand. Pas d'image."),
        ("5/6 · ÉCRAN", "« 3. Tu relis. Tu publies. »\n« Tes proches la lisent sur ta page. »\nSous la capture, en DM Mono : « exemple : “L'Iseran à 4 °C” »",
         "Gabarit ÉCRAN. Capture du carnet de la page d'exemple avec l'anecdote « L'Iseran à 4 °C », "
         "pastille « road trip d'exemple » visible."),
        ("6/6 · DERNIÈRE SLIDE", "« Ton carnet de voyage s'écrit le soir, en 2 minutes. »", CTA_FINAL),
    ],
    legende="""Tout le monde se promet de tenir un carnet de voyage. Personne ne le tient après le deuxième jour.

Avec trophytracker, le soir, tu appuies sur le micro et tu racontes ta journée à voix haute (ou tu l'écris, si tu préfères). L'IA en fait une vraie page de carnet : elle garde tes anecdotes, enlève les « euh » et les hésitations, ajoute les kilomètres et l'altitude du jour. Sans rien inventer.

Tu relis, tu publies. Tes proches la lisent sur ta page, et toi tu gardes tout ton voyage raconté avec tes mots.

Envie de voir à quoi ça ressemble ? Va lire le carnet de Léa et Sam sur la page d'exemple (lien en bio).

Enregistre ce post pour ton prochain road trip.""",
    hashtags="#carnetdevoyage #carnetderoute #roadtrip #roadtripfrance #voyage #trophytracker",
))

P(dict(
    id=3, date=d("2026-10-16"), heure="12h15", slug="ta-page-ton-lien-personne-dautre",
    titre="Ta page. Ton lien. Personne d'autre.",
    cible="tout le monde (road trip, proches)", sujet="page privée par lien, nuits floutées",
    format="carrousel 5 visuels", objectif="enregistrer + lien en bio",
    remarque="Grille de départ.",
    slides=[
        ("1/5 · COUVERTURE", "Pastille en très grand : « privé · accès par lien »\nTitre : « Ton road trip est privé. » / « Par défaut. »",
         "Gabarit COUVERTURE. Fond : carte satellite floutée de la page d'exemple. La pastille « privé · accès par lien » "
         "(fond papier, texte encre, comme sur le site) en grand au centre, avec une ombre douce."),
        ("2/5 · TEXTE", "« Seuls ceux qui ont ton lien te suivent. »\n« Pas de compte à créer. Pas d'appli à installer. Ils cliquent, ils voient. »",
         "Gabarit TEXTE. Petite illustration : une icône de lien rouge reliée à 3 petits ronds papier (les proches)."),
        ("3/5 · TEXTE", "« Jamais sur Google. »\n« Ta page n'apparaît pas dans les moteurs de recherche. Tu préfères la rendre publique ? C'est une option, tu choisis. »",
         "Gabarit TEXTE. Une barre de recherche vide stylisée (sans logo de moteur de recherche), avec « 0 résultat » en DM Mono."),
        ("4/5 · TEXTE", "« Tes nuits restent à toi. »\n« Les arrêts de nuit sont floutés. Et tu coupes le suivi ou tu effaces ta trace quand tu veux. »",
         "Gabarit ÉCRAN. Capture d'un arrêt de nuit flouté sur la carte (capture C20). Si la capture n'est pas prête : "
         "un cercle flou sur fond satellite avec l'étiquette « NUIT »."),
        ("5/5 · DERNIÈRE SLIDE", "« C'est toi qui choisis qui te suit. »", CTA_FINAL),
    ],
    legende="""Ton road trip, c'est pas une émission de télé.

Sur trophytracker, ta page est privée par défaut : seuls ceux à qui tu envoies le lien peuvent te suivre. Eux n'ont rien à installer et pas de compte à créer. Et ta page n'apparaît jamais sur Google.

Les arrêts de nuit sont floutés sur la carte. Tu peux couper le suivi ou effacer ta trace à tout moment. Et si un jour tu veux que tout le monde voie ton voyage, tu peux la rendre publique : c'est toi qui décides.

Ton road trip, en direct, pour ceux que tu choisis. Lien en bio.""",
    hashtags="#roadtrip #vieprivee #voyage #famille #roadtripfrance #trophytracker",
))

P(dict(
    id=4, date=d("2026-10-16"), heure="19h", slug="15-euros-une-fois-sans-abonnement",
    titre="15 €. Une fois. Pas d'abonnement.",
    cible="toutes les cibles", sujet="série lancement (1/5) : le prix",
    format="post simple", objectif="lien en bio",
    remarque="Grille de départ · À ÉPINGLER (3ᵉ épinglé : « c'est combien »). Remplace l'ancien post 6 (prix).",
    slides=[
        ("VISUEL UNIQUE",
         "En très grand : « 15 € » (papier)\nDessous : « par road trip. » (rouge)\n"
         "Trois lignes en DM Mono : « une seule fois · pas d'abonnement · gratuit pour ceux qui te suivent »\nEn bas : logo",
         "Gabarit TEXTE. Fond encre avec le halo rouge en haut à droite. Derrière le « 15 € », une trace ambre très fine "
         "qui serpente comme une route de col, balise rouge au bout. Rien d'autre : le prix doit se lire en une seconde."),
    ],
    legende="""15 € par road trip. Tu paies une fois, et c'est tout.

Pas d'abonnement qui tourne en fond. Pas de prix au mois. Pas de surprise sur ton relevé dans six mois.

Pour ça, tu as ta page privée avec la carte et ta trace en direct, tes photos, la météo là où tu es, le carnet de bord raconté à l'IA, le replay 3D de tout le voyage, et toute la bande qui gère la page avec toi.

Et ceux qui te suivent ne paient rien : ils ont ton lien, c'est tout.

Ton road trip, en direct : lien en bio.""",
    hashtags=H["prix"],
))

P(dict(
    id=5, date=d("2026-10-17"), heure="12h15", slug="pret-en-5-minutes",
    titre="Prêt en 5 minutes. Zéro prise de tête.",
    cible="road trip en voiture, moto, raid (toutes cibles)", sujet="création guidée, QR code Traccar Client, lien",
    format="carrousel 6 visuels", objectif="enregistrer",
    remarque="Grille de départ · À ÉPINGLER (2ᵉ épinglé : « comment ça marche »). Remplace l'ancien post 2.",
    slides=[
        ("1/6 · COUVERTURE", "Titre : « Prêt en 5 minutes. » / « Zéro prise de tête. »\nChrono en DM Mono : « 05:00 »\n« glisse → »",
         "Gabarit COUVERTURE, fond encre (pas de photo). Un grand chrono « 05:00 » en DM Mono rouge, cerclé comme la balise."),
        ("2/6 · ÉCRAN", "« 1. Tu crées ton road trip. »\n« Un nom, une photo de couverture, tes compagnons de route, d'où à où, quand. L'itinéraire ? Facultatif : la trace s'écrit en roulant. »",
         "Gabarit ÉCRAN. Capture réelle de la création guidée dans l'espace voyageur (capture C9)."),
        ("3/6 · ÉCRAN", "« 2. Tu scannes un QR code. »\n« Avec l'appli gratuite Traccar Client, sur Android ou iPhone. Ton téléphone envoie ta position. (Ou un boîtier GPS compatible.) »",
         "Photo : une main tient un téléphone qui scanne le QR code affiché sur l'écran d'un ordinateur, sur une table "
         "(jamais dans une voiture en marche). Ou capture C10."),
        ("4/6 · TEXTE", "« 3. Tu invites tes proches. »\n« Par e-mail, directement depuis ton espace, ou tu envoies ton lien où tu veux. Eux : sans compte, sans appli. »",
         "Gabarit TEXTE. Un lien « trophytracker.fr/road-trip/ton-voyage » en DM Mono papier, avec 3 enveloppes stylisées qui en partent."),
        ("5/6 · ÉCRAN", "« Et tu pars. »\n« Ta position se met à jour en moins de 10 secondes. Sans réseau, tout est gardé et envoyé dès que ça capte. »",
         "Gabarit ÉCRAN. Capture de la page d'exemple avec la balise en direct et la pastille « en direct · à l'instant » (pastille « road trip d'exemple » visible)."),
        ("6/6 · DERNIÈRE SLIDE", "« 5 minutes ce soir. En direct demain. »", CTA_FINAL),
    ],
    legende="""Pas de boîtier à acheter. Pas d'appli pour tes proches. 5 minutes, et c'est prêt.

1. Tu crées ton road trip : un nom, une photo de couverture, tes compagnons de route, d'où à où, quand. Pas besoin d'itinéraire, ta trace s'écrit en roulant.
2. Tu scannes un QR code avec l'appli gratuite Traccar Client (Android ou iPhone). Ton téléphone envoie ta position. Tu as un boîtier GPS compatible ? Ça marche aussi.
3. Tu invites ceux qui vont te suivre, par e-mail ou en leur envoyant ton lien.

Et tu pars. Ta position se met à jour en moins de 10 secondes, et sans réseau tout est gardé en mémoire puis envoyé dès que ça capte.

Enregistre ce post pour le soir où tu prépares ton départ. Lien en bio.""",
    hashtags=H["rt"],
))

P(dict(
    id=6, date=d("2026-10-17"), heure="19h", slug="ton-road-trip-en-direct",
    titre="Ton road trip, en direct. (c'est quoi trophytracker ?)",
    cible="toutes les cibles", sujet="présentation générale",
    format="carrousel 7 visuels", objectif="s'abonner + lien en bio",
    remarque="Grille de départ · À ÉPINGLER (1er épinglé : « c'est quoi »). Remplace les anciens posts 19 et 1. "
             "Après publication, épingler dans cet ordre : P06, P05, P04.",
    slides=[
        ("1/7 · COUVERTURE", "Logo en haut\nTitre : « Ton road trip, » / « en direct. » (rouge)\nDM Mono : « position · trace · photos · carnet de route »\n« en 7 swipes → »",
         "Reprise au format 4:5 de l'image de partage du site (og-image) : fond encre, halo rouge, même typographie."),
        ("2/7 · ÉCRAN", "« Tu roules. Ceux que tu invites te suivent. »",
         "Gabarit ÉCRAN. Capture de la carte satellite de la page d'exemple : trace, étapes, balise rouge (C2)."),
        ("3/7 · ÉCRAN", "« Une page rien qu'à toi. »\n« Carte satellite et relief 3D, ta trace, tes étapes, tes photos (même en 360°), la météo là où tu es. »",
         "Gabarit ÉCRAN. Capture du relief 3D d'un col + vignettes de photos (C3)."),
        ("4/7 · TEXTE", "« Le soir, tu racontes. L'IA écrit. »\n« Ton carnet de bord, raconté au micro, sans rien inventer. »",
         "Gabarit TEXTE avec le bouton micro rouge."),
        ("5/7 · TEXTE", "« À la fin, tu revis tout en 3D. »\n« Ton voyage rejoué en survol satellite, en vidéo à poster. »",
         "Image fixe tirée du replay 3D (C11) : vue oblique d'une vallée, trace rouge."),
        ("6/7 · TEXTE", "« Privée par défaut. »\n« Seuls ceux qui ont ton lien suivent. Sans compte, sans appli. »",
         "Gabarit TEXTE avec la pastille « privé · accès par lien »."),
        ("7/7 · DERNIÈRE SLIDE", "« 15 € par road trip. Sans abonnement. »\n« Va voir l'exemple : trophytracker.fr/road-trip/exemple »", CTA_FINAL),
    ],
    legende=f"""Nouveau ici ? trophytracker en 7 swipes.

Tu pars en road trip, en voiture, à moto, entre amis, en raid ou en rallye ? Tu crées ta page en 5 minutes, ton téléphone envoie ta position, et ceux que tu invites te suivent en direct : ta trace, tes étapes, tes photos, la météo là où tu es.

Le soir, tu racontes ta journée au micro et l'IA en fait une page de carnet. À la fin, tu revis tout le voyage en 3D.

Ta page est privée : seuls ceux qui ont ton lien la voient, sans compte et sans appli.

15 € par road trip, une seule fois. Gratuit pour ceux qui te suivent.
Va voir un road trip d'exemple en direct : {EXEMPLE} (lien en bio).""",
    hashtags=H["rt"],
))

# ───────────────────────── SEMAINE 1 (19 → 25 octobre) ─────────────────────────

P(dict(
    id=7, date=d("2026-10-21"), heure="19h", slug="ce-que-voient-tes-proches",
    titre="Ce que voient tes proches pendant que tu roules",
    cible="les proches (et les voyageurs qui veulent les rassurer)", sujet="la page vue côté proches",
    format="carrousel 6 visuels", objectif="partager à un proche",
    remarque="Remplace l'ancien post 11 (qui attendait des captures de l'ancienne carte).",
    slides=[
        ("1/6 · COUVERTURE", "Titre : « Toi, tu roules. » / « Eux, ils voient tout ça. »\n« glisse → »",
         "Photo : un téléphone posé sur une table de cuisine à côté d'une tasse, la page d'exemple ouverte "
         "(mains seulement, pas de visage)."),
        ("2/6 · ÉCRAN", "« Où tu en es, en direct. »", "Capture C2 (carte, trace, balise), pastille « road trip d'exemple »."),
        ("3/6 · ÉCRAN", "« Le temps qu'il fait là-bas. »", "Capture C5 (météo visuelle à la position du voyageur)."),
        ("4/6 · ÉCRAN", "« Tes photos, là où tu les as prises. »", "Capture des photos sur la carte, dont une 360° si possible."),
        ("5/6 · ÉCRAN", "« Ta journée, racontée. »", "Capture C7 (carnet du soir)."),
        ("6/6 · DERNIÈRE SLIDE", "« Envoie ce post à ceux qui vont te suivre. »", CTA_FINAL),
    ],
    legende=f"""Toi, tu roules. Ta mère a la page ouverte sur la table de la cuisine, ton grand-père la regarde sur sa tablette.

Ils voient où tu en es, en direct. Le temps qu'il fait là-bas. Tes photos, au bon endroit sur la carte. Et le soir, ta journée racontée dans ton carnet.

Pour eux, aucun compte à créer, aucune appli à installer : ils ouvrent ton lien, c'est tout.

Tu veux leur montrer avant de partir ? Envoie-leur la page d'exemple : {EXEMPLE}

Partage ce post dans le groupe famille. Vraiment.""",
    hashtags=H["proches"],
))

P(dict(
    id=8, date=d("2026-10-23"), heure="12h15", slug="route-des-grandes-alpes-en-direct",
    titre="Route des Grandes Alpes : 675 km en direct (la page d'exemple)",
    cible="road trip en voiture, moto", sujet="tour complet de la page d'exemple : étapes, profil d'altitude, tableau de bord",
    format="carrousel 6 visuels", objectif="visiter l'exemple (lien en bio)",
    remarque="Début des vacances de la Toussaint : bon moment pour un road trip montagne.",
    slides=[
        ("1/6 · COUVERTURE", "Pastille : « road trip d'exemple »\nTitre : « Thonon → Menton. » / « En direct. »\nDM Mono : « 675 km · Iseran · Galibier · Izoard · Bonette »",
         "Capture du relief 3D d'un col de la page d'exemple (C3), assombrie en bas pour le texte."),
        ("2/6 · ÉCRAN", "« Leurs étapes, créées par eux. »\nDM Mono : « col de la Colombière · cormet de Roselend · nuit à Bourg-Saint-Maurice · nuit à Valloire · nuit à Barcelonnette »",
         "Capture C2 : la carte avec les étiquettes d'étapes."),
        ("3/6 · ÉCRAN", "« Chaque montée. Chaque descente. »", "Capture C6 (profil d'altitude)."),
        ("4/6 · ÉCRAN", "« Vitesse, altitude, distance, batterie. »", "Capture C4 (tableau de bord)."),
        ("5/6 · ÉCRAN", "« Et le soir : “L'Iseran à 4 °C.” »", "Capture C7 (carnet)."),
        ("6/6 · DERNIÈRE SLIDE", f"« Elle tourne en direct, en boucle. Va la voir. »\nDM Mono : « {EXEMPLE} »", CTA_FINAL),
    ],
    legende=f"""Léa et Sam font la Route des Grandes Alpes : de Thonon-les-Bains à Menton, 675 km par l'Iseran, le Galibier, l'Izoard et la Bonette.

Ce sont des personnages d'exemple, mais leur page est une vraie page trophytracker, rejouée en direct en boucle. Tu peux l'ouvrir maintenant et voir exactement ce que verront ceux qui te suivent : la balise qui avance, les étapes qu'ils ont créées, le profil d'altitude, la météo, le tableau de bord. Et le carnet du soir, écrit au bivouac.

Tu pars pendant les vacances ? Ta page peut ressembler à ça ce week-end.

👉 {EXEMPLE} (lien en bio)""",
    hashtags=H["alpes"],
))

# ───────────────────────── SEMAINE 2 (26 octobre → 1er novembre) ─────────────────────────

P(dict(
    id=9, date=d("2026-10-26"), heure="19h", slug="raid-rallye-tout-lequipage-en-direct",
    titre="Raid, rallye : tout l'équipage en direct",
    cible="raid / rallye", sujet="à plusieurs, sans réseau, sponsors et cagnotte, rapport PDF",
    format="carrousel 6 visuels", objectif="partager à son équipage",
    remarque="Premier post 100 % raid / rallye. Aucune mention d'un événement précis.",
    slides=[
        ("1/6 · COUVERTURE", "Titre : « Raid, rallye : » / « tout l'équipage en direct. »\n« glisse → »",
         "Photo : piste dans le désert, un véhicule tout-terrain vu de dos dans un nuage de poussière, au loin. "
         "Véhicule moderne, sans numéro ni logo d'événement."),
        ("2/6 · TEXTE", "« Toute la bande gère la page. »\n« Photos, étapes, carnet : vous êtes plusieurs, la page aussi. »",
         "Gabarit TEXTE. 2 à 4 ronds avec des initiales (comme « L » et « S » sur la page d'exemple)."),
        ("3/6 · TEXTE", "« Des pistes sans réseau ? Prévu. »\n« Tout est gardé en mémoire et envoyé dès que ça capte. »",
         "Gabarit TEXTE avec le bandeau « Pas de réseau, c'est normal » reproduit."),
        ("4/6 · ÉCRAN", "« Tes sponsors en vitrine. Ta cagnotte à côté de la carte. »",
         "Capture C18 (vitrine des sponsors + bouton de cagnotte)."),
        ("5/6 · ÉCRAN", "« À l'arrivée : un rapport PDF pour tes sponsors. »\n« Avec les statistiques de visibilité de ta page. »",
         "Capture C15 (couverture du rapport PDF)."),
        ("6/6 · DERNIÈRE SLIDE", "« Une page pour tout l'équipage. 15 €. »", CTA_FINAL),
    ],
    legende="""Un raid, un rallye, c'est des mois de prépa, des sponsors à convaincre, une famille qui veut des nouvelles, et des pistes où ça ne capte pas.

Avec trophytracker, tout l'équipage gère la même page. Tes proches suivent votre trace en direct, même après une journée sans réseau : tout est gardé en mémoire et envoyé dès que ça capte.

Tes sponsors ont leur vitrine sur la même page que la carte, ta cagnotte aussi. Et à l'arrivée, tu leur envoies un rapport PDF avec les statistiques de visibilité de ta page.

Envoie ce post à ton équipage. Lien en bio.""",
    hashtags=H["raid"],
))

P(dict(
    id=10, date=d("2026-10-28"), heure="12h15", slug="humour-je-tecris-ce-soir",
    titre="Humour : « Je t'écris ce soir. »",
    cible="road trip (voyageurs + proches)", sujet="les proches ont des nouvelles sans attendre",
    format="post simple", objectif="taguer quelqu'un",
    remarque="Remplace l'ancien post 3 (même idée, sans référence à l'ancien événement).",
    slides=[
        ("VISUEL UNIQUE",
         "En haut, une bulle de message (papier) : « Je t'écris ce soir 😘 » · DM Mono : « envoyé à 9:12 »\n"
         "Au milieu, en rouge DM Mono : « 23:47. Toujours rien. »\nEn bas, titre : « Ta page, elle, » / « donne des nouvelles toute seule. »\nPetit logo",
         "Gabarit TEXTE. Bulle de message générique (aucune interface d'une vraie messagerie reconnaissable)."),
    ],
    legende="""Tu l'as déjà dit. Tu vas le redire. Et tu vas encore oublier.

Entre le col, la pizza et le coucher de soleil, t'auras pas le temps. Pas grave : ta page montre où tu en es pendant que tu profites. Et le soir, si t'as deux minutes, tu racontes ta journée au micro, l'IA s'occupe du reste.

Tague celui qui ne répond jamais pendant les vacances.""",
    hashtags="#roadtrip #vacances #humour #famille #roadtripfrance #trophytracker",
))

P(dict(
    id=11, date=d("2026-10-30"), heure="19h", slug="moto-toi-les-virages-eux-la-trace",
    titre="Moto : toi, les virages. Eux, la trace.",
    cible="à moto", sujet="trace en relief 3D, profil d'altitude, rien à toucher en roulant",
    format="carrousel 5 visuels", objectif="enregistrer + partager à un motard",
    remarque="",
    slides=[
        ("1/5 · COUVERTURE", "Titre : « Toi, les virages. » / « Eux, la trace. »",
         "Photo vue du dessus (drone) d'une route en lacets dans un col, une moto minuscule dans une épingle. Trace rouge superposée sur la route."),
        ("2/5 · ÉCRAN", "« Chaque lacet, sur la carte. »", "Capture C3 : relief 3D zoomé sur un col de la page d'exemple."),
        ("3/5 · ÉCRAN", "« Combien t'as grimpé aujourd'hui ? »\n« Le profil d'altitude de ta journée. »", "Capture C6."),
        ("4/5 · TEXTE", "« Une fois lancé, le suivi tourne tout seul. »\n« Téléphone dans la poche ou sur le support : rien à toucher en roulant. »",
         "Gabarit TEXTE. Icône de téléphone dans une poche de blouson, balise rouge qui pulse."),
        ("5/5 · DERNIÈRE SLIDE", "« Le soir, casque posé, tu racontes. L'IA écrit. »", CTA_FINAL),
    ],
    legende="""Toi, tu enchaînes les épingles. Eux, à la maison, ils voient chaque lacet se dessiner sur la carte en relief.

Une fois le suivi lancé avec l'appli gratuite Traccar Client, ton téléphone envoie ta position tout seul : rien à toucher en roulant. Sur ta page, ta trace, tes étapes, le profil d'altitude de la journée, la météo là où tu es.

Et le soir, casque posé, tu racontes ta journée au micro. L'IA en fait une page de carnet, avec les kilomètres et l'altitude.

Envoie ça au motard qui prépare déjà sa saison. Lien en bio.""",
    hashtags=H["moto"],
))

# ───────────────────────── SEMAINE 3 (2 → 8 novembre) ─────────────────────────

P(dict(
    id=12, date=d("2026-11-02"), heure="19h", slug="lancement-ce-que-tu-as-pour-15-euros",
    titre="Ce que tu as pour 15 €",
    cible="toutes les cibles", sujet="série lancement (2/5) : tout ce qu'il y a dans une page",
    format="carrousel 7 visuels", objectif="lien en bio",
    remarque="Tout est inclus dans les 15 € (confirmé par Julien le 15/10).",
    slides=[
        ("1/7 · COUVERTURE", "Titre : « 15 €. » / « Voilà ce qu'il y a dedans. »\n« glisse → »", "Gabarit TEXTE, « 15 € » énorme, comme P04."),
        ("2/7 · ÉCRAN", "« Ta page privée, en direct. »\n« Carte satellite et relief 3D, trace, étapes, photos, météo, tableau de bord. »", "Capture C1."),
        ("3/7 · TEXTE", "« Ton carnet raconté à l'IA. »\n« Tu parles, elle écrit. Sans rien inventer. »", "Gabarit TEXTE, bouton micro."),
        ("4/7 · TEXTE", "« Ton voyage revécu en 3D. »\n« En vidéo paysage, story ou carré. »", "Image fixe du replay (C11)."),
        ("5/7 · TEXTE", "« Toute la bande, et tous les proches. »\n« Page gérée à plusieurs. E-mail « C'est parti », résumé du soir, mur d'encouragements. »",
         "Gabarit TEXTE, ronds d'initiales + enveloppes."),
        ("6/7 · TEXTE", "« Et pour les raids : sponsors, cagnotte, rapport PDF, autocollants QR. »", "Gabarit TEXTE, 4 petites icônes en ligne."),
        ("7/7 · DERNIÈRE SLIDE", "« Une seule fois. Pas d'abonnement. Gratuit pour ceux qui suivent. »", CTA_FINAL),
    ],
    legende="""15 € par road trip. Voilà ce qu'il y a dedans :

📍 Ta page privée en direct : carte satellite et relief 3D, ta trace, tes étapes, tes photos (même en 360°), la météo là où tu es, ton tableau de bord.
🎙️ Ton carnet de bord raconté à l'IA, sans rien inventer.
🎬 Ton voyage rejoué en 3D, à exporter en vidéo.
👥 La page gérée à plusieurs, et pour tes proches : l'e-mail « C'est parti », le résumé du soir et le mur d'encouragements.
🏁 Pour les raids et rallyes : vitrine des sponsors, lien de cagnotte, rapport PDF, autocollants QR à imprimer.

Une seule fois, pas d'abonnement. Et gratuit pour tous ceux qui te suivent.

Lien en bio.""",
    hashtags=H["prix"],
))

P(dict(
    id=13, date=d("2026-11-04"), heure="12h15", slug="entre-amis-toute-la-bande",
    titre="Entre amis : toute la bande sur la même page",
    cible="entre amis", sujet="page gérée à plusieurs, proches de tout le monde au même endroit",
    format="carrousel 5 visuels", objectif="taguer sa bande",
    remarque="",
    slides=[
        ("1/5 · COUVERTURE", "Titre : « Un road trip entre potes. » / « Une seule page. »",
         "Photo : 3 ou 4 amis de dos, assis sur le capot ou le toit d'une voiture (ou devant un van), face à un coucher de soleil. Visages non visibles."),
        ("2/5 · TEXTE", "« Tout le monde gère la page. »\n« Pas un seul qui fait tout pendant que les autres dorment. »", "Gabarit TEXTE, 4 ronds d'initiales."),
        ("3/5 · TEXTE", "« Les familles de tout le monde suivent au même endroit. »\n« Fini les trois groupes de discussion différents. »",
         "Gabarit TEXTE : trois bulles de discussion barrées, une seule carte à côté."),
        ("4/5 · TEXTE", "« Le carnet ? »\n« Celui qui raconte le mieux s'y colle. L'IA enlève les “euh”. »", "Gabarit TEXTE, bouton micro."),
        ("5/5 · DERNIÈRE SLIDE", "« 15 € le road trip, pour toute la bande. »", CTA_FINAL),
    ],
    legende="""Un road trip entre potes, c'est quatre familles qui veulent des nouvelles, trois groupes de discussion et personne qui pense à envoyer une photo.

Avec trophytracker, vous avez une seule page pour toute la bande. Tout le monde peut la gérer, et les proches de chacun suivent au même endroit : la trace en direct, les photos, la météo là où vous êtes.

Le soir, celui qui raconte le mieux prend le micro. L'IA en fait une page de carnet (et enlève les « euh »).

15 € le road trip, pour toute la bande. Tague ceux avec qui tu pars.""",
    hashtags=H["amis"],
))

P(dict(
    id=14, date=d("2026-11-06"), heure="19h", slug="carnet-ia-ce-que-tu-dis-ce-que-lia-ecrit",
    titre="Carnet IA : ce que tu dis, ce que l'IA écrit",
    cible="road trip (toutes cibles)", sujet="démo avant / après du carnet raconté à l'IA",
    format="carrousel 5 visuels", objectif="enregistrer",
    remarque="⚠ La slide 3 doit être un VRAI résultat : dicte le texte de la slide 2 dans l'appli et fais la capture "
             "de la page générée. Ne pas écrire soi-même le résultat de l'IA.",
    slides=[
        ("1/5 · COUVERTURE", "Titre : « Ce que tu dis. » / « Ce que l'IA écrit. »\n« glisse → »", "Gabarit AVANT / APRÈS en aperçu, flouté."),
        ("2/5 · AVANT", "En haut, DM Mono : « ce que tu dis (exemple) »\nTexte (en gris, comme une transcription brute) :\n"
         "« Alors aujourd'hui… euh… on est partis tard, genre 9 h, parce que quelqu'un avait perdu les clés. Elles étaient dans le frigo. "
         "Après, le col, euh, magnifique, on s'est arrêtés trois fois pour les photos, et en haut y avait un monsieur qui vendait des… "
         "des tartes aux myrtilles. Le soir, pâtes au camping. Voilà. »",
         "Gabarit AVANT / APRÈS, côté gauche. Bouton micro rouge en bas. C'est le texte à dicter dans l'appli pour obtenir la slide 3."),
        ("3/5 · APRÈS", "En haut, DM Mono : « ce que l'IA écrit »\n[À COMPLÉTER : capture réelle de la page de carnet obtenue]",
         "Gabarit AVANT / APRÈS, côté droit, fond papier."),
        ("4/5 · TEXTE", "« Ce qu'elle ajoute : les kilomètres et l'altitude du jour. »\n« Ce qu'elle n'ajoute pas : tout ce que tu n'as pas dit. »",
         "Gabarit TEXTE, deux colonnes (✓ en vert / ✕ en rouge)."),
        ("5/5 · DERNIÈRE SLIDE", "« Tu relis. Tu publies. »", CTA_FINAL),
    ],
    legende="""À gauche, ce que tu racontes le soir, fatigué, avec les « euh » et les clés retrouvées dans le frigo.
À droite, ce que l'IA en fait : une page de carnet propre, avec tes anecdotes, tes mots, et les kilomètres et l'altitude du jour.

Elle retire les hésitations. Elle n'invente rien : ce que tu n'as pas dit n'apparaît pas. Et c'est toi qui relis avant de publier.

C'est la fonction qu'on préfère dans trophytracker. Enregistre ce post et teste-la sur ton prochain road trip. Lien en bio.""",
    hashtags="#carnetdevoyage #carnetderoute #roadtrip #ia #voyage #trophytracker",
))
