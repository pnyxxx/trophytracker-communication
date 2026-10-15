from common import d, HANDLE, EXEMPLE

STORIES = []
S = STORIES.append
LIEN_SITE = "sticker LIEN → https://trophytracker.fr (texte du sticker : « trophytracker.fr »)"
LIEN_EXEMPLE = f"sticker LIEN → https://{EXEMPLE} (texte du sticker : « voir l'exemple »)"

# ───────────────────────── STORIES À LA UNE (permanentes) ─────────────────────────

S(dict(
    id=1, date=None, permanent=True, heure="à mettre en place le 18/10", slug="a-la-une-cest-quoi",
    titre="À la une « trophytracker » (c'est quoi)", cible="nouveaux visiteurs",
    remarque="1ʳᵉ story à la une. Couverture : symbole du logo sur fond encre.",
    ecrans=[
        ("1/4", "« Ton road trip, » / « en direct. »\nDM Mono : « position · trace · photos · carnet de route »", "aucun",
         "Fond encre + halo rouge, logo en haut, comme l'image de partage du site."),
        ("2/4", "« Tu roules. Ceux que tu invites te suivent. »", "aucun",
         "Enregistrement d'écran de 6 à 8 s de la page d'exemple : la balise avance, la trace se dessine (pastille « road trip d'exemple » visible)."),
        ("3/4", "« Page privée, accessible uniquement par ton lien. Sans compte, sans appli pour eux. »", "aucun",
         "Fond encre, pastille « privé · accès par lien » en grand."),
        ("4/4", "« Va voir un road trip en direct. »\n« Route des Grandes Alpes · exemple »", LIEN_EXEMPLE + ", posé au centre",
         "Capture de la couverture de la page d'exemple (« Route des Grandes Alpes »), assombrie en bas pour le sticker."),
    ],
))

S(dict(
    id=2, date=None, permanent=True, heure="à mettre en place le 18/10", slug="a-la-une-comment-ca-marche",
    titre="À la une « Comment ça marche »", cible="tout le monde",
    remarque="Remplace l'ancienne story à la une « Comment ça marche ». Couverture : « 1·2·3 » en DM Mono rouge.",
    ecrans=[
        ("1/5", "« Prêt en 5 minutes. » / « Zéro prise de tête. »", "aucun", "Fond encre, chrono « 05:00 » rouge."),
        ("2/5", "« 1. Tu crées ton road trip. »\n« Un nom, une photo, tes compagnons, d'où à où, quand. L'itinéraire est facultatif. »", "aucun",
         "Enregistrement d'écran de la création guidée (C9)."),
        ("3/5", "« 2. Tu scannes le QR code avec Traccar Client. »\n« Appli gratuite, Android et iPhone. Ou un boîtier GPS compatible. »", "aucun",
         "Main qui scanne un QR code sur un écran d'ordinateur (C10)."),
        ("4/5", "« 3. Tu invites tes proches. »\n« Par e-mail ou avec ton lien. Ils suivent sans compte et sans appli. »", "aucun", "Fond encre, lien en DM Mono."),
        ("5/5", "« Pas de réseau ? »\n« Tout est gardé en mémoire et envoyé dès que ça capte. »", LIEN_SITE + ", en bas",
         "Photo de piste ou de col, bandeau « Pas de réseau, c'est normal » reproduit."),
    ],
))

S(dict(
    id=3, date=None, permanent=True, heure="à mettre en place le 18/10", slug="a-la-une-carnet-ia",
    titre="À la une « Carnet IA »", cible="tout le monde",
    remarque="Nouvelle story à la une pour la fonction phare. Couverture : bouton micro rouge.",
    ecrans=[
        ("1/4", "« Le soir, tu racontes. » / « L'IA écrit. »", "aucun", "Fond encre, gros bouton micro rouge."),
        ("2/4", "« Tu appuies sur le micro et tu racontes ta journée. Ou tu l'écris. »", "aucun",
         "Enregistrement d'écran : appui sur le micro, onde sonore (C7 en vidéo si possible)."),
        ("3/4", "« L'IA garde tes anecdotes, retire les hésitations, ajoute kilomètres et altitude. Sans rien inventer. »", "aucun",
         "Capture d'une page de carnet générée."),
        ("4/4", "« Tu relis. Tu publies. »\n« Exemple : “L'Iseran à 4 °C” »", LIEN_EXEMPLE,
         "Capture du carnet de la page d'exemple."),
    ],
))

S(dict(
    id=4, date=None, permanent=True, heure="à mettre en place le 18/10", slug="a-la-une-proches",
    titre="À la une « Proches »", cible="parents, grands-parents, amis",
    remarque="Story à envoyer directement aux proches. Couverture : un petit cœur papier sur fond rouge.",
    ecrans=[
        ("1/4", "« Quelqu'un que tu aimes part en road trip ? »\n« Voilà comment le suivre. »", "aucun", "Photo d'une table de cuisine, téléphone avec la page ouverte (mains seulement)."),
        ("2/4", "« 1. Il t'envoie son lien (ou une invitation par e-mail). »\n« 2. Tu l'ouvres. Pas de compte, pas d'appli. »", "aucun", "Fond encre, lien en DM Mono."),
        ("3/4", "« Tu vois où il en est, la météo là-bas, ses photos, son carnet du soir. »\n« Et tu peux lui laisser un message sur le mur d'encouragements. »", "aucun",
         "Enregistrement d'écran de la page d'exemple (carte → météo → carnet)."),
        ("4/4", "« Chaque soir, le résumé de sa journée arrive par e-mail. »", LIEN_EXEMPLE, "Capture C13."),
    ],
))

S(dict(
    id=5, date=None, permanent=True, heure="à mettre en place le 18/10", slug="a-la-une-raid-et-sponsors",
    titre="À la une « Raid & sponsors »", cible="raid / rallye, sponsors",
    remarque="Couverture : drapeau à damier stylisé ambre (pas de logo d'événement).",
    ecrans=[
        ("1/5", "« Raid, rallye : » / « tout l'équipage en direct. »", "aucun", "Photo de piste dans le désert, véhicule tout-terrain de loin."),
        ("2/5", "« Toute la bande gère la page. Les proches suivent au même endroit. »", "aucun", "Fond encre, ronds d'initiales."),
        ("3/5", "« Tes sponsors en vitrine et ta cagnotte, sur la même page que la carte. »", "aucun", "Capture C18."),
        ("4/5", "« À l'arrivée : statistiques de visibilité + rapport PDF pour tes sponsors. »", "aucun", "Capture C15."),
        ("5/5", "« Autocollants QR prêts à imprimer, pour le véhicule. »", LIEN_SITE, "Capture C16."),
    ],
))

S(dict(
    id=6, date=None, permanent=True, heure="à mettre en place le 18/10", slug="a-la-une-tarif",
    titre="À la une « Tarif »", cible="tout le monde",
    remarque="Remplace l'ancienne story « tarifs » (qui affichait deux prix). Un seul prix désormais. Couverture : « 15 € » papier sur fond rouge.",
    ecrans=[
        ("1/2", "« 15 € » / « par road trip. »\nDM Mono : « une seule fois · pas d'abonnement · gratuit pour ceux qui te suivent »", "aucun",
         "Même visuel que le post P04, en 9:16."),
        ("2/2", "« Dans ta page : »\n« carte satellite et relief 3D · trace en direct · étapes et photos · météo · carnet raconté à l'IA · replay 3D · page à plusieurs · e-mails aux proches · mur d'encouragements · sponsors et cagnotte · rapport PDF · autocollants QR »",
         LIEN_SITE + ", posé en bas", "Fond encre, liste en DM Mono, puces rouges."),
    ],
))

S(dict(
    id=7, date=None, permanent=True, heure="à mettre en place le 18/10", slug="a-la-une-faq",
    titre="À la une « FAQ »", cible="tout le monde",
    remarque="L'écran 4 (pas un outil de sécurité ni de navigation) est à garder en permanence. Les réponses de la boîte à questions (S22) viennent enrichir cette story. Couverture : « ? » rouge.",
    ecrans=[
        ("1/4", "« Mes proches doivent installer une appli ? »\n« Non : un lien, sans compte. »\n« Il faut un boîtier GPS ? »\n« Non : ton téléphone + Traccar Client (gratuit). Un boîtier compatible marche aussi. »", "aucun", "Fond encre, questions en rouge, réponses en papier."),
        ("2/4", "« Et sans réseau ? »\n« Tout est gardé et envoyé dès que ça capte. »\n« Qui voit ma page ? »\n« Ceux qui ont ton lien. Jamais sur Google. Nuits floutées. »", "aucun", "Idem."),
        ("3/4", "« Je peux arrêter ? »\n« Tu coupes le suivi ou tu effaces ta trace quand tu veux. »\n« On peut gérer la page à plusieurs ? »\n« Oui, toute la bande. »", "aucun", "Idem."),
        ("4/4", "« Ça sert à s'orienter ou en cas de pépin ? »\n« Non. trophytracker n'est ni un outil de navigation, ni un outil de sécurité ou de secours. C'est fait pour partager ton voyage. »\n« Une autre question ? Écris-nous. »", "aucun", "Idem, avec un cadre rouge."),
    ],
))

# ───────────────────────── SÉQUENCES DATÉES ─────────────────────────

S(dict(
    id=8, date=d("2026-10-17"), permanent=False, heure="12h20 → 19h", slug="relance-du-compte",
    titre="Relance du compte : « Ton road trip, en direct. »", cible="abonnés actuels + ton réseau",
    remarque="Le jour où les 3 posts épinglés sont en ligne. Ne pas expliquer le changement : on présente, c'est tout. "
             "Ce jour-là, partage aussi depuis ton compte perso.",
    ecrans=[
        ("12h20", "« Nouveau sur trophytracker : » / « ton road trip, en direct. »\n« ↓ touche pour voir »", "repartage du post P05 (bouton avion › « Ajouter à la story »)",
         "Le post P05 en repartage, sur fond encre avec halo rouge."),
        ("14h", "« Ton prochain road trip, c'est… »", "sticker SONDAGE, 4 options : « En voiture » · « À moto » · « Raid ou rallye » · « Entre amis »",
         "Fond satellite flouté, titre en haut. Le soir : un message privé de remerciement à quelques votants, sans vendre."),
        ("17h", "« Va voir une page en direct. »\n« Léa et Sam sur la Route des Grandes Alpes (exemple) »", LIEN_EXEMPLE,
         "Enregistrement d'écran de la page d'exemple, 8 s."),
        ("19h05", "« Ton road trip, en direct. »\n« 15 € par road trip, sans abonnement. »", "repartage du post P06 + " + LIEN_SITE,
         "Le post P06 en repartage."),
    ],
))

S(dict(
    id=9, date=d("2026-10-21"), permanent=False, heure="18h", slug="visite-guidee-de-la-page-dexemple",
    titre="Visite guidée de la page d'exemple", cible="voyageurs et proches",
    remarque="Le même jour que le post P07. Tout en enregistrements d'écran (téléphone), 6 à 10 s chacun, pastille « road trip d'exemple » visible.",
    ecrans=[
        ("1/5", "« Visite guidée d'une page trophytracker → »", "aucun", "Couverture de la page d'exemple."),
        ("2/5", "« La carte : satellite, plan ou relief 3D. »", "aucun", "Enregistrement : bascule Satellite → Relief 3D."),
        ("3/5", "« La météo, là où ils sont. »", "aucun", "Enregistrement : bloc météo."),
        ("4/5", "« Le profil d'altitude et le tableau de bord. »", "aucun", "Enregistrement : défilement jusqu'au profil d'altitude."),
        ("5/5", "« Le carnet du soir. Ouvre-la toi-même : »", LIEN_EXEMPLE, "Enregistrement : carnet de Léa et Sam."),
    ],
))

S(dict(
    id=10, date=d("2026-10-23"), permanent=False, heure="12h30 → 19h", slug="vacances-de-la-toussaint",
    titre="Vacances de la Toussaint : tu pars ?", cible="road trip en voiture, entre amis",
    remarque="Vacances scolaires (zones A, B, C) du 17 octobre au 2 novembre 2026.",
    ecrans=[
        ("12h30", "« Tu pars pendant les vacances ? »", "sticker SONDAGE : « Oui, ça roule ! » / « Non, je reste »", "Photo de route d'automne (forêt rousse)."),
        ("12h31", "« Tu pars où ? »", "sticker QUESTION « Dis-nous où tu pars »", "Fond encre."),
        ("19h", "« 5 minutes ce soir, en direct demain. »", LIEN_SITE, "Repartage du post P05 avec ce texte au-dessus."),
    ],
))

S(dict(
    id=11, date=d("2026-10-30"), permanent=False, heure="12h30 → 19h30", slug="moto-ton-col-prefere",
    titre="Moto : ton col préféré", cible="à moto",
    remarque="Le jour du post P11.",
    ecrans=[
        ("12h30", "« Ton col préféré ? »", "sticker SONDAGE, 4 options : « Galibier » · « Izoard » · « Iseran » · « Bonette »", "Photo d'épingle de col vue du dessus."),
        ("17h", "« Les épingles, tu les aimes à quel point ? »", "sticker CURSEUR (emoji 🏍️)", "Fond encre, trace en lacets ambre."),
        ("19h30", "« Ils sont tous sur la page d'exemple. »", LIEN_EXEMPLE, "Enregistrement d'écran : relief 3D d'un col de la page d'exemple."),
    ],
))

S(dict(
    id=12, date=d("2026-11-02"), permanent=False, heure="12h30 → 20h", slug="lancement-15-euros-quiz",
    titre="Lancement : 15 € par road trip (quiz)", cible="toutes les cibles",
    remarque="Le jour du post P12. Série lancement en stories.",
    ecrans=[
        ("12h30", "« Quiz : trophytracker, ça coûte combien ? »", "sticker QUIZ : A « 15 € tous les mois » · B « 15 € par road trip, une seule fois » (bonne réponse : B)",
         "Fond encre, halo rouge."),
        ("17h", "« Bonne réponse : B. »\n« Et pour ceux qui te suivent ? 0 €. »", "aucun", "Visuel P04 (« 15 € ») en 9:16."),
        ("20h", "« Ce qu'il y a dans les 15 € → »", "repartage du post P12 + " + LIEN_SITE, "Le post P12 en repartage."),
    ],
))

S(dict(
    id=13, date=d("2026-11-04"), permanent=False, heure="12h30 → 19h", slug="entre-amis-qui-raconte-le-mieux",
    titre="Entre amis : qui raconte le mieux ?", cible="entre amis",
    remarque="Le jour du post P13.",
    ecrans=[
        ("12h30", "« Dans ta bande, qui raconte le mieux les histoires ? »", "sticker QUESTION « Tague-le ici »", "Photo d'amis de dos autour d'un feu."),
        ("17h", "« Road trip entre potes : »", "sticker SONDAGE : « Tout est prévu » / « On improvise »", "Fond encre."),
        ("19h", "« Une seule page pour toute la bande. »", "repartage du post P13 + " + LIEN_SITE, "Le post P13 en repartage."),
    ],
))

S(dict(
    id=14, date=d("2026-11-06"), permanent=False, heure="18h", slug="demo-carnet-ia",
    titre="Démo : le carnet raconté à l'IA, en vrai", cible="toutes les cibles",
    remarque="⚠ À FILMER pour de vrai (sans visage) dans l'espace voyageur. Le jour du post P14.",
    ecrans=[
        ("1/5", "« Je te montre le carnet IA en 30 secondes → »", "aucun", "Fond encre, bouton micro."),
        ("2/5", "« J'appuie sur le micro… »", "aucun", "Enregistrement d'écran : appui sur le micro."),
        ("3/5", "« Je raconte. »", "aucun", "Enregistrement : la dictée en cours (texte du post P14, slide 2), son activé."),
        ("4/5", "« Et voilà la page. »", "aucun", "Enregistrement : la page de carnet générée apparaît, défilement lent."),
        ("5/5", "« Tu veux tester ? »", LIEN_SITE, "Fond encre, logo."),
    ],
))

S(dict(
    id=15, date=d("2026-11-09"), permanent=False, heure="12h30 → 19h30", slug="raid-ta-galere-sponsors",
    titre="Raid : ta galère n°1 avec les sponsors", cible="raid / rallye",
    remarque="Le jour du post P15. Les réponses nourrissent la story « Raid & sponsors » et de futurs posts.",
    ecrans=[
        ("12h30", "« Ta galère n°1 avec les sponsors ? »", "sticker QUESTION « Raconte »", "Photo de piste, cadre « Ton logo ici » en pointillés."),
        ("17h", "« Astuce : ne promets pas de la visibilité. Montre-la. »\n« Envoie-lui le lien de ta page. »", "aucun", "Fond encre, phrase entre guillemets."),
        ("19h30", "« 5 phrases à copier dans ton dossier sponsor → »", "repartage du post P15", "Le post P15 en repartage."),
    ],
))

S(dict(
    id=16, date=d("2026-11-11"), permanent=False, heure="12h30 → 19h", slug="replay-3d-teaser",
    titre="Replay 3D en story", cible="toutes les cibles",
    remarque="Le jour du post P16. [À COMPLÉTER : export du replay au format story.]",
    ecrans=[
        ("12h30", "« Tout un voyage, rejoué en 3D. Monte le son. »", "aucun", "Vidéo du replay 3D au format story (9:16), 15 s."),
        ("17h", "« Tu le posterais ? »", "sticker SONDAGE : « Direct ! » / « Je le garde pour moi »", "Image fixe du replay."),
        ("19h", f"« Poste le tien et tague {HANDLE} : on repartage. »", "repartage du post P16", "Le post P16 en repartage."),
    ],
))

S(dict(
    id=17, date=d("2026-11-13"), permanent=False, heure="12h30 → 19h30", slug="proches-tu-stresses",
    titre="Proches : tu stresses quand ils partent ?", cible="proches",
    remarque="Le jour du post P17. Ne jamais parler de sécurité : on parle de nouvelles.",
    ecrans=[
        ("12h30", "« Quand ton enfant part en road trip, tu attends ses nouvelles à quel point ? »", "sticker CURSEUR (emoji 😅)", "Fond papier, texte encre."),
        ("17h", "« Avec son lien, tu as des nouvelles sans lui en demander. »", "aucun", "Enregistrement d'écran de la page d'exemple, 6 s."),
        ("19h30", "« Envoie ça à ton enfant avant son départ. »", "repartage du post P17", "Le post P17 en repartage."),
    ],
))

S(dict(
    id=18, date=d("2026-11-23"), permanent=False, heure="12h30 → 19h30", slug="mur-dencouragements",
    titre="Le mur d'encouragements", cible="proches, raid / rallye",
    remarque="Le jour du post P21.",
    ecrans=[
        ("12h30", "« Écris un mot à quelqu'un qui part bientôt. »", "sticker QUESTION « Ton message »", "Fond encre, cartes de message empilées."),
        ("17h", "« Sur une page trophytracker, ses proches peuvent faire pareil, sans créer de compte. »", "aucun", "Capture C12 (mur d'encouragements)."),
        ("19h30", "« Les messages qu'on lit le soir → »", "repartage du post P21", "Le post P21 en repartage."),
    ],
))

S(dict(
    id=19, date=d("2026-12-11"), permanent=False, heure="du 11/12 au 18/12", slug="concours",
    titre="Concours (stories d'accompagnement)", cible="toutes les cibles",
    remarque="Avec le post P29 : 1 code à gagner, fin jeudi 17/12 à 23h59, tirage vendredi 18/12.",
    ecrans=[
        ("jour 1 · 12h30", "« Concours : ton prochain road trip offert ! »", "repartage du post P29", "Le post P29 en repartage."),
        ("jour 1 · 19h", "« Fin du concours dans : »", "sticker COMPTE À REBOURS « Fin du concours » → jeudi 17/12 à 23h59", "Fond encre, ticket « TT-XXXX-XXXX »."),
        ("veille de la fin", "« Dernier jour pour participer ! »", "repartage du post P29", "Idem."),
        ("jour du tirage", "« Bravo à [@gagnant(s)] ! On t'envoie ton code en message. »", "sticker MENTION des gagnants", "Fond encre, confettis rouges et ambre. ⚠ Envoyer les codes TT-XXXX-XXXX en message privé, jamais en story."),
    ],
))

S(dict(
    id=20, date=d("2026-12-21"), permanent=False, heure="12h30 → 19h", slug="noel",
    titre="Noël : ton plus beau road trip de l'année", cible="toutes les cibles",
    remarque="Le jour du post P33.",
    ecrans=[
        ("12h30", "« Ton plus beau road trip de 2026, c'était où ? »", "sticker QUESTION « Raconte »", "Photo de route enneigée, lumières."),
        ("17h", "« Au repas, montre ton replay 3D. »", "aucun", "Image du replay sur un téléphone posé sur une table de fête."),
        ("19h", "« Joyeux Noël 🎄 »", "repartage du post P33", "Le post P33 en repartage."),
    ],
))

S(dict(
    id=21, date=d("2026-12-28"), permanent=False, heure="12h30 → 19h", slug="tes-road-trips-2027",
    titre="Tes road trips 2027", cible="toutes les cibles",
    remarque="Le jour du post P35.",
    ecrans=[
        ("12h30", "« En 2027, tu pars : »", "sticker SONDAGE, 4 options : « En voiture » · « À moto » · « Raid ou rallye » · « Entre amis »", "Mosaïque de 4 photos."),
        ("17h", "« Ta destination de rêve pour 2027 ? »", "sticker QUESTION", "Fond satellite flouté."),
        ("19h", "« Dis-nous en commentaire → »", "repartage du post P35", "Le post P35 en repartage."),
    ],
))

# ───────────────────────── FORMATS DU QUOTIDIEN (modèles) ─────────────────────────

S(dict(
    id=22, date=None, permanent=False, heure="1 fois par semaine (le jeudi)", slug="quotidien-boite-a-questions",
    titre="Quotidien · Boîte à questions", cible="toutes les cibles",
    remarque="Les réponses vont ensuite dans la story à la une « FAQ » (S07). Répondre à chacune en story, une par écran.",
    ecrans=[
        ("1/1", "« Une question sur trophytracker ? »\n« Pose-la ici, on répond à tout. »", "sticker QUESTION « Ta question »", "Fond encre, halo rouge, logo en haut."),
    ],
))

S(dict(
    id=23, date=None, permanent=False, heure="à chaque fois qu'un voyageur tague le compte", slug="quotidien-repartage-voyageur",
    titre="Quotidien · Repartage d'un voyageur", cible="toutes les cibles",
    remarque="⚠ À COMPLÉTER à chaque fois. Seulement les stories où le compte est tagué (donc publiques). Ne jamais repartager une page privée sans accord.",
    ecrans=[
        ("1/1", "« Bonne route [@compte] ! »", "sticker MENTION du voyageur", "Sa story repartagée au centre, cadre fin rouge, fond encre."),
    ],
))

S(dict(
    id=24, date=None, permanent=False, heure="de temps en temps", slug="quotidien-coulisses",
    titre="Quotidien · Coulisses", cible="toutes les cibles",
    remarque="⚠ À COMPLÉTER : une vraie photo de ton écran (pas de visage obligatoire) et une vraie amélioration en cours. "
             "Jamais annoncer une date ou une fonctionnalité qui n'existe pas encore comme si elle était là.",
    ecrans=[
        ("1/1", "DM Mono : « coulisses · [heure] »\n« Ce soir, je travaille sur [amélioration réelle]. »", "sticker SONDAGE facultatif : « Hâte ! » / « Ça sert à quoi ? »",
         "Photo de ton écran (code ou appli en test)."),
    ],
))

S(dict(
    id=25, date=None, permanent=False, heure="1 fois par semaine (le mardi)", slug="quotidien-fonction-de-la-semaine",
    titre="Quotidien · La fonction de la semaine", cible="toutes les cibles",
    remarque="Faire tourner dans cet ordre : météo visuelle · nuits floutées · profil d'altitude · import GPX · photos 360° · "
             "mur d'encouragements · résumé du soir · couper / effacer sa trace · plusieurs road trips par compte · connexion par code reçu par e-mail.",
    ecrans=[
        ("1/2", "DM Mono : « la fonction de la semaine »\n« [Nom de la fonction] »", "aucun", "Fond encre, titre Bricolage."),
        ("2/2", "« [À quoi elle sert, en une phrase] »", "sticker QUIZ facultatif (« Tu savais ? » Oui / Non) + " + LIEN_SITE, "Capture de la fonction."),
    ],
))

S(dict(
    id=26, date=None, permanent=False, heure="chaque vendredi vers 17h", slug="quotidien-ce-week-end-tu-roules",
    titre="Quotidien · Ce week-end, tu roules ?", cible="road trip, moto",
    remarque="Rendez-vous du vendredi.",
    ecrans=[
        ("1/1", "« Ce week-end, tu roules ? »", "sticker SONDAGE : « Oui, ça roule » / « Canapé »", "Photo de route différente chaque semaine (col, côte, piste, campagne)."),
    ],
))

S(dict(
    id=27, date=None, permanent=False, heure="le jour de chaque post", slug="quotidien-repartage-dun-post",
    titre="Quotidien · Repartage du post du jour", cible="toutes les cibles",
    remarque="Habillage générique pour chaque nouveau post.",
    ecrans=[
        ("1/1", "« Nouveau post ↓ »", "repartage du post (bouton avion › « Ajouter à la story »)", "Fond encre avec halo rouge, petit logo en bas."),
    ],
))
