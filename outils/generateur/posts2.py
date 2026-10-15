from common import d, H, HANDLE, EXEMPLE, CTA_FINAL

POSTS = []
P = POSTS.append

# ───────────────────────── SEMAINE 4 (9 → 15 novembre) ─────────────────────────

P(dict(
    id=15, date=d("2026-11-09"), heure="19h", slug="5-phrases-pour-convaincre-un-sponsor",
    titre="5 phrases pour convaincre un sponsor",
    cible="raid / rallye (et sponsors)", sujet="vitrine des sponsors, suivi en direct, rapport PDF",
    format="carrousel 7 visuels", objectif="enregistrer + partager",
    remarque="Remplace l'ancien post 12. À repartager en story 2 fois dans la semaine.",
    slides=[
        ("1/7 · COUVERTURE", "Titre : « 5 phrases » / « pour convaincre un sponsor. »\nUn cadre en pointillés : « Ton logo ici »",
         "Gabarit COUVERTURE, fond encre. Le cadre « Ton logo ici » en pointillés ambre, comme un emplacement vide de la vitrine."),
        ("2/7 · TEXTE", "« 1 »\n« Votre logo sera sur notre page de voyage, juste à côté de la carte en direct. »", "Gabarit TEXTE, numéro rouge en très grand, phrase entre guillemets."),
        ("3/7 · TEXTE", "« 2 »\n« Vous suivrez en direct l'aventure que vous financez. »", "Idem."),
        ("4/7 · TEXTE", "« 3 »\n« Voici le lien de notre page : votre place est déjà prête. »", "Idem."),
        ("5/7 · TEXTE", "« 4 »\n« Ce lien, on le partage à nos proches et sur nos réseaux, du départ à l'arrivée. »", "Idem."),
        ("6/7 · TEXTE", "« 5 »\n« À l'arrivée, vous recevez un rapport PDF avec les statistiques de visibilité de la page. »", "Idem, avec une petite vignette du rapport (C15)."),
        ("7/7 · DERNIÈRE SLIDE", "« Enregistre. Copie. Envoie. »", CTA_FINAL),
    ],
    legende="""La chasse aux sponsors, c'est maintenant. Voilà 5 phrases à copier dans tes mails et ton dossier.

Le secret : ne pas promettre de la visibilité, la montrer. Avec le lien de ta page trophytracker, ton sponsor voit sa place dans la vitrine, juste à côté de la carte. Pendant le voyage, il suit tout en direct. Et à l'arrivée, tu lui envoies un rapport PDF avec les statistiques de visibilité.

Astuce : pour un sponsor, pense à rendre ta page publique ou à lui envoyer ton lien.

Enregistre ce carrousel et envoie-le à celui qui gère les sponsors dans ton équipage.""",
    hashtags=H["sponsors"],
))

P(dict(
    id=16, date=d("2026-11-11"), heure="12h15", slug="revis-ton-voyage-en-3d",
    titre="Revis tout ton voyage en 3D",
    cible="road trip, moto, raid (toutes cibles)", sujet="replay 3D exportable en vidéo",
    format="carrousel 5 visuels (dont 1 vidéo)", objectif="partager + lien en bio",
    remarque="Remplace l'ancien post 14 (« dans 10 ans »). La slide 2 est une vidéo : Instagram accepte un mélange photos + vidéos dans un carrousel.",
    slides=[
        ("1/5 · COUVERTURE", "Titre : « Ton voyage entier, » / « rejoué en 3D. »\n« glisse → »",
         "Image fixe du replay : vue satellite oblique d'une vallée alpine, trace rouge qui serpente jusqu'à l'horizon (C11)."),
        ("2/5 · VIDÉO", "Pas de texte ajouté (ou juste « replay 3D · exemple » en DM Mono en bas).",
         "Vidéo carrée de 15 à 30 s : export du replay 3D, en format carré [À COMPLÉTER : export depuis un vrai road trip ou depuis la page d'exemple si l'export y est possible]."),
        ("3/5 · TEXTE", "« En paysage, en story ou en carré. »\n« Prêt à poster le soir du retour. »",
         "Gabarit TEXTE : trois cadres côte à côte (16:9, 9:16, 1:1) avec la même image de replay dedans."),
        ("4/5 · TEXTE", "« Les photos finissent perdues dans ton téléphone. »\n« Ta trace, elle, se revit. »", "Gabarit TEXTE."),
        ("5/5 · DERNIÈRE SLIDE", f"« Partage ton replay et tague {HANDLE} : on repartage. »", CTA_FINAL),
    ],
    legende=f"""Le voyage est fini. Tu le revis quand même.

Sur trophytracker, tout ton road trip se rejoue en survol satellite en 3D : chaque col, chaque vallée, chaque piste, dans l'ordre où tu les as faits. Et tu l'exportes en vidéo, en paysage, en story ou en carré, prête à poster.

Les photos finissent perdues dans un téléphone. Ta trace, elle, se revit.

Tu postes ton replay ? Tague {HANDLE}, on repartage les plus beaux.""",
    hashtags="#roadtrip #souvenirs #voyage #3d #roadtripfrance #trophytracker",
))

P(dict(
    id=17, date=d("2026-11-13"), heure="19h", slug="humour-les-3-etats-de-ta-mere",
    titre="Humour : les 3 états de ta mère pendant ton road trip",
    cible="proches (via les voyageurs)", sujet="les proches suivent sans attendre les messages",
    format="carrousel 4 visuels", objectif="taguer",
    remarque="Remplace l'ancien post 13 (même chute, sans référence à l'ancien événement).",
    slides=[
        ("1/4 · COUVERTURE", "Titre : « Les 3 états de ta mère » / « pendant ton road trip. »\n« glisse → »", "Gabarit TEXTE, fond encre."),
        ("2/4 · TEXTE", "DM Mono : « JOUR 1 »\nTitre : « Fière. »", "Fond papier, texte encre, très grand. Rien d'autre."),
        ("3/4 · TEXTE", "DM Mono : « JOUR 2 · 22:00 »\nTitre : « Aucune nouvelle. » / « Aucune. »", "Fond encre, texte rouge."),
        ("4/4 · TEXTE", "DM Mono : « JOUR 2 · 22:01 »\nTitre : « Ouvre ton lien. Te voit sur la carte. Lit ton carnet du soir. Appelle toute la famille pour raconter. »\nPetit logo",
         "Fond encre, petite capture de la page d'exemple dans un coin (C1)."),
    ],
    legende="""Toutes les mères passent par ces 3 états. Autant sauter directement au troisième.

Envoie-lui ton lien avant de partir : elle verra où tu en es, le temps qu'il fait, tes photos, et le soir ton carnet. Sans compte, sans appli.

Tague celui dont la mère est déjà au jour 2.""",
    hashtags="#roadtrip #humour #famille #maman #vacances #trophytracker",
))

# ───────────────────────── SEMAINE 5 (16 → 22 novembre) ─────────────────────────

P(dict(
    id=18, date=d("2026-11-16"), heure="19h", slug="rapport-pdf-pour-tes-sponsors",
    titre="Ton sponsor t'a fait confiance. Montre-lui ce que ça a donné.",
    cible="raid / rallye, sponsors", sujet="statistiques de visibilité + rapport PDF de fin de voyage",
    format="carrousel 6 visuels", objectif="enregistrer + partager à son équipage",
    remarque="Remplace l'ancien post 4 (sponsors). Contenu du rapport relevé dans le code de l'appli (page « rapport de voyage », à imprimer ou enregistrer en PDF).",
    slides=[
        ("1/6 · COUVERTURE", "Titre : « Ton sponsor t'a fait confiance. » / « Montre-lui ce que ça a donné. »",
         "Photo : un dossier imprimé posé sur un capot poussiéreux ou une table de bivouac, avec la couverture du rapport PDF (C15)."),
        ("2/6 · ÉCRAN", "« Pendant le voyage : sa vitrine. »\n« Son logo sur la même page que la carte en direct. »", "Capture C18."),
        ("3/6 · TEXTE", "« Ce qu'il y a dans le rapport. »\n« le voyage : distance · jours sur la route · altitude max · dénivelé + · étapes · photos »\n« la visibilité : visites de la page · proches abonnés · encouragements · visites des 30 derniers jours »", "Gabarit TEXTE, deux blocs de petites étiquettes (sans chiffres inventés : juste les intitulés)."),
        ("4/6 · ÉCRAN", "« À l'arrivée : un rapport PDF. »\n« Prêt à envoyer. »", "Capture C15 (2 pages du rapport en éventail)."),
        ("5/6 · TEXTE", "« L'an prochain, tu as un argument. »\n« Plus facile de redemander quand tu as montré le résultat. »", "Gabarit TEXTE."),
        ("6/6 · DERNIÈRE SLIDE", "« Un raid, des sponsors, un vrai bilan. »", CTA_FINAL),
    ],
    legende="""Démarcher un sponsor, c'est promettre de la visibilité. Après l'arrivée, il faut la prouver.

Avec trophytracker, tes sponsors ont leur vitrine sur la même page que la carte en direct, pendant tout le voyage. Et à la fin, tu leur envoies un rapport PDF : ta trace sur une vue satellite, les kilomètres, les jours sur la route, l'altitude max, le dénivelé, les étapes, les photos. Et surtout la visibilité : les visites de ta page, le nombre de proches abonnés, les encouragements reçus.

Un vrai bilan, c'est ce qui fait la différence quand tu reviens frapper à la même porte l'année suivante.

Enregistre ce post pour ta prochaine réunion sponsors. Lien en bio.""",
    hashtags=H["sponsors"],
))

P(dict(
    id=19, date=d("2026-11-18"), heure="12h15", slug="il-fait-quel-temps-la-bas",
    titre="Il fait quel temps là-bas ?",
    cible="proches", sujet="météo visuelle à la position du voyageur + tableau de bord",
    format="carrousel 4 visuels", objectif="partager à un proche",
    remarque="",
    slides=[
        ("1/4 · COUVERTURE", "Titre : « Il fait quel temps » / « là où tu es ? »", "Capture C5 (météo visuelle) en grand, cadre téléphone."),
        ("2/4 · TEXTE", "« Ta mère n'a plus besoin de demander. »\n« La météo à ta position, directement sur ta page. »", "Gabarit TEXTE, petite icône soleil/nuage ambre."),
        ("3/4 · ÉCRAN", "« Et l'altitude, la vitesse, la distance du jour. »", "Capture C4 (tableau de bord)."),
        ("4/4 · DERNIÈRE SLIDE", "« Ils savent. Tu roules. »", CTA_FINAL),
    ],
    legende="""« Il fait beau là-bas ? Vous avez froid ? Il neige ? »

Sur ta page trophytracker, ceux qui te suivent voient la météo là où tu es, en direct, à côté de la carte. Et ton tableau de bord : l'altitude, la vitesse, la distance du jour.

Ils savent, sans t'envoyer dix messages. Toi, tu profites.

Envoie ce post à la personne qui te demande toujours la météo.""",
    hashtags=H["proches"],
))

P(dict(
    id=20, date=d("2026-11-20"), heure="19h", slug="lancement-pourquoi-pas-dabonnement",
    titre="Pourquoi pas d'abonnement ?",
    cible="toutes les cibles", sujet="série lancement (3/5) : payer seulement quand on part",
    format="post simple", objectif="lien en bio",
    remarque="",
    slides=[
        ("VISUEL UNIQUE",
         "Titre : « Tu ne pars pas tous les mois. » / « Pourquoi tu paierais tous les mois ? » (rouge)\n"
         "En bas : « 15 € par road trip. Une fois. » + logo",
         "Gabarit TEXTE. Une rangée de 12 petites cases de calendrier en DM Mono (« jan » à « déc »), une seule allumée "
         "en rouge avec une balise : le mois du départ."),
    ],
    legende="""Un road trip, c'est quelques jours, une semaine, un mois si t'as de la chance. Pas toute l'année.

Alors chez trophytracker, tu paies quand tu pars : 15 € par road trip, une seule fois. Rien qui tourne en fond pendant que ta voiture dort au garage.

Trois road trips cette année ? Tu crées trois pages sur le même compte. Aucun l'an prochain ? Tu ne paies rien.

Lien en bio.""",
    hashtags=H["prix"],
))

# ───────────────────────── SEMAINE 6 (23 → 29 novembre) ─────────────────────────

P(dict(
    id=21, date=d("2026-11-23"), heure="19h", slug="le-mur-dencouragements",
    titre="Les messages qu'on lit le soir (mur d'encouragements)",
    cible="proches, raid / rallye", sujet="mur d'encouragements sans compte",
    format="carrousel 5 visuels", objectif="partager à un proche",
    remarque="Les messages de la slide 3 viennent du mur d'encouragements de la page d'exemple (personnages fictifs).",
    slides=[
        ("1/5 · COUVERTURE", "Titre : « Les messages » / « qu'on lit le soir. »",
         "Photo de nuit : lampe frontale, tente ou voiture, téléphone allumé dans une main (pas de visage)."),
        ("2/5 · TEXTE", "« Tes proches t'écrivent sur ta page. »\n« Sans créer de compte. »", "Gabarit TEXTE."),
        ("3/5 · TEXTE", "Pastille : « road trip d'exemple »\n« Couvrez-vous bien en haut de l'Iseran, il paraît qu'il gèle ! — Mamie Jo »\n« Belle trace ! On vous suit tous les soirs avec le résumé. — Papa »\n« Rapportez-moi un magnet du Galibier. — Inès »",
         "Trois cartes de message empilées (fond papier, texte encre), comme un mur d'encouragements."),
        ("4/5 · TEXTE", "« Après une journée de piste, »\n« c'est ce qui recharge les batteries. »", "Gabarit TEXTE."),
        ("5/5 · DERNIÈRE SLIDE", "« Ton lien, et ils peuvent t'écrire. »", CTA_FINAL),
    ],
    legende="""Le soir, après une longue journée de route ou de piste, il y a un moment qu'on adore : lire les messages des gens qui nous suivent.

Sur trophytracker, tes proches t'écrivent directement sur ta page, sur le mur d'encouragements. Pas de compte à créer : ils ouvrent ton lien, ils écrivent, c'est tout.

Envoie ce post à quelqu'un qui part bientôt : il saura quoi faire de ses soirées.""",
    hashtags="#raid #rallye #roadtrip #famille #encouragements #trophytracker",
))

P(dict(
    id=22, date=d("2026-11-25"), heure="12h15", slug="pret-au-depart-la-check-list",
    titre="Prêt au départ : le guide en 8 étapes",
    cible="raid / rallye, road trip", sujet="guide « Prêt au départ » + check-list + bouton « Je pars »",
    format="carrousel 7 visuels", objectif="enregistrer",
    remarque="Remplace l'ancien post 10 (checklist numérique). Les 8 étapes sont celles du guide de l'espace voyageur.",
    slides=[
        ("1/7 · COUVERTURE", "Titre : « Tout est prêt ? » / « Appuie sur Je pars. »", "Capture C17 : le bouton « Je pars » en grand."),
        ("2/7 · TEXTE", "« 1. Ton voyage »\n« Le nom, les dates, la photo de couverture, qui peut voir la page. »\n« 2. Ton équipage »\n« Invite tes compagnons de route : chacun peut publier des photos et écrire dans le journal. »", "Gabarit TEXTE, numéros rouges, cases à cocher."),
        ("3/7 · TEXTE", "« 3. Ton véhicule »\n« Le téléphone qui reste à bord, son support, son alimentation (allume-cigare ou batterie externe). »\n« 4. Ton itinéraire »\n« Départ, étapes ou fichier GPX, arrivée. Facultatif : la trace s'écrit en roulant. »", "Idem."),
        ("4/7 · TEXTE", "« 5. Le suivi GPS »\n« L'appli gratuite, réglée d'un coup avec le QR code. Tu testes le signal. »\n« 6. Le partage »\n« Tu envoies le lien, tu préviens les grands-parents, tu imprimes l'autocollant QR. »", "Idem."),
        ("5/7 · TEXTE", "« 7. Sponsors et cagnotte »\n« Les logos de ceux qui te soutiennent, le lien de ta cagnotte. Facultatif. »\n« 8. La check-list du départ »\n« Batterie externe chargée, signal testé, lien envoyé, plein fait. »", "Idem."),
        ("6/7 · ÉCRAN", "« Le jour J : “Je pars”. »\n« Et tes proches reçoivent l'e-mail “C'est parti”. »", "Capture C17 (check-list cochée) + C14 (e-mail « C'est parti »)."),
        ("7/7 · DERNIÈRE SLIDE", "« Enregistre pour la veille du départ. »", CTA_FINAL),
    ],
    legende="""La veille du départ, tu as mille choses en tête. Ta page, elle, t'accompagne.

Dans ton espace trophytracker, le guide « Prêt au départ » te fait tout vérifier en 8 étapes, et la check-list se termine par un bouton : « Je pars ». Au départ, tes proches reçoivent l'e-mail « C'est parti ».

Ton voyage, ton équipage, ton véhicule, ton itinéraire, le suivi GPS, le partage du lien, tes sponsors et ta cagnotte, et enfin la check-list : batterie externe chargée, signal testé, lien envoyé, plein fait.

Enregistre ce post et ressors-le la veille du départ. Lien en bio.""",
    hashtags="#preparation #raid #rallye #roadtrip #checklist #trophytracker",
))

P(dict(
    id=23, date=d("2026-11-27"), heure="19h", slug="le-bingo-du-road-trip",
    titre="Le bingo du road trip",
    cible="road trip, entre amis", sujet="humour à partager en story",
    format="post simple", objectif="capturer + partager en story + taguer",
    remarque="Remplace l'ancien post 15. Repartager chaque story qui tague le compte.",
    slides=[
        ("VISUEL UNIQUE",
         "Titre : « Le bingo du road trip »\nGrille 3 × 3 :\n"
         "« Quelqu'un a oublié son chargeur » · « La même playlist depuis 400 km » · « Arrêt photo toutes les 10 minutes »\n"
         "« Zéro réseau » · « ✓ Tes proches te suivent en direct » (case du milieu, déjà cochée en rouge) · « Pique-nique sur un parking »\n"
         "« “C'est normal ce bruit ?” » · « Détour imprévu » · « Quelqu'un dort à l'arrière »\n"
         f"En bas, DM Mono : « capture · coche · partage en story · tague {HANDLE} »",
         "Grille sur fond papier, cases encre, case du milieu rouge. Petit logo en bas."),
    ],
    legende=f"""Capture, coche ce que tu as déjà vécu (ou ce que tu vas vivre), partage en story et tague {HANDLE}. On repartage les meilleurs.

La case du milieu, on te l'offre avec ta page.""",
    hashtags="#roadtrip #bingo #humour #roadtripentreamis #vacances #trophytracker",
))

# ───────────────────────── SEMAINE 7 (30 novembre → 6 décembre) ─────────────────────────

P(dict(
    id=24, date=d("2026-11-30"), heure="19h", slug="tes-qr-codes-prets-a-imprimer",
    titre="Colle ton QR code : ils scannent, ils suivent",
    cible="raid / rallye, moto", sujet="visuels QR prêts à imprimer",
    format="carrousel 5 visuels", objectif="enregistrer",
    remarque="",
    slides=[
        ("1/5 · COUVERTURE", "Titre : « Ils scannent. » / « Ils suivent. »",
         "Photo : un autocollant QR carré sur la vitre arrière d'un véhicule tout-terrain poussiéreux (véhicule moderne, sans numéro ni logo), ou sur un top-case de moto."),
        ("2/5 · ÉCRAN", "« L'autocollant carré. »\n« Pour la vitre arrière, le top-case, la caisse à outils. »", "Capture C16 (autocollant carré)."),
        ("3/5 · ÉCRAN", "« L'autocollant rond. »\n« Pour le carnet de bord, la glacière, l'ordi. »", "Capture C16 (autocollant rond)."),
        ("4/5 · ÉCRAN", "« La story satellite, avec ta trace. »\n« Pour partager ta page sur Insta. »", "Capture C16 (story satellite)."),
        ("5/5 · DERNIÈRE SLIDE", "« Prêts à imprimer, dans ton espace. »", CTA_FINAL),
    ],
    legende=f"""Ta page a son QR code, et il est déjà mis en forme.

Dans ton espace trophytracker, tu trouves trois visuels prêts à imprimer ou à partager : un autocollant carré, un autocollant rond, et une story Instagram sur fond satellite avec ta trace.

Bon à savoir : un QR code collé sur ta voiture donne accès à ta page à tous ceux qui le scannent. Colle-le seulement si tu veux être suivi par ceux qui le croisent. Sinon, garde-le pour tes proches et ta story.

Tu postes ta story QR ? Tague {HANDLE}.""",
    hashtags="#raid #rallye #moto #roadtrip #qrcode #trophytracker",
))

P(dict(
    id=25, date=d("2026-12-02"), heure="12h15", slug="lancement-a-quatre-3-euros-75-chacun",
    titre="À quatre dans la voiture : 3,75 € chacun",
    cible="entre amis", sujet="série lancement (4/5) : prix par road trip, partagé",
    format="post simple", objectif="taguer sa bande",
    remarque="",
    slides=[
        ("VISUEL UNIQUE",
         "Titre : « À quatre, » / « 3,75 € chacun. » (rouge)\nSous-titre : « 15 € par road trip, pas par personne. »\nLogo",
         "Gabarit TEXTE. Une voiture vue du dessus, très simplifiée (ligne papier, pas de modèle reconnaissable), "
         "avec 4 sièges ; sur chaque siège, « 3,75 € » en DM Mono ambre."),
    ],
    legende="""15 € par road trip. Pas par personne.

À quatre dans la voiture, ça fait 3,75 € chacun pour une page en direct, le carnet raconté à l'IA, le replay 3D, et les familles de tout le monde qui suivent au même endroit.

Et ceux qui vous suivent ne paient rien.

Tague ta bande, et dis qui avance les 15 €.""",
    hashtags=H["amis"],
))

P(dict(
    id=26, date=d("2026-12-04"), heure="19h", slug="faq",
    titre="FAQ : tu te demandes…",
    cible="toutes les cibles", sujet="lever les freins",
    format="carrousel 9 visuels", objectif="commenter (poser une question)",
    remarque="Remplace l'ancien post 16. La slide 7 (pas un outil de sécurité ni de navigation) est obligatoire.",
    slides=[
        ("1/9 · COUVERTURE", "Titre : « FAQ » / « Tu te demandes… »", "Gabarit TEXTE."),
        ("2/9 · TEXTE", "« Mes proches doivent installer une appli ? »\n« Non. Ils ouvrent ton lien, sans compte, sur téléphone ou ordinateur. »", "Gabarit TEXTE, question en rouge, réponse en papier."),
        ("3/9 · TEXTE", "« Il faut acheter un boîtier GPS ? »\n« Non. Ton téléphone suffit, avec l'appli gratuite Traccar Client (Android et iPhone). Un boîtier compatible marche aussi. »", "Idem."),
        ("4/9 · TEXTE", "« Et sans réseau ? »\n« Tout est gardé en mémoire et envoyé dès que ça capte. »", "Idem."),
        ("5/9 · TEXTE", "« Qui peut voir ma page ? »\n« Seulement ceux qui ont ton lien. Jamais sur Google. Les nuits sont floutées. Public en option. »", "Idem."),
        ("6/9 · TEXTE", "« Combien ça coûte ? »\n« 15 € par road trip, une seule fois. Pas d'abonnement. Gratuit pour ceux qui suivent. »", "Idem."),
        ("7/9 · TEXTE", "« Ça sert à s'orienter, ou en cas de pépin ? »\n« Non. trophytracker n'est ni un outil de navigation, ni un outil de sécurité ou de secours. C'est fait pour partager ton voyage. »", "Idem, cadre rouge autour (comme l'ancienne story FAQ obligatoire)."),
        ("8/9 · TEXTE", "« Je peux arrêter quand je veux ? »\n« Oui : tu coupes le suivi ou tu effaces ta trace à tout moment. »", "Idem."),
        ("9/9 · DERNIÈRE SLIDE", "« Une autre question ? Pose-la en commentaire. »", CTA_FINAL),
    ],
    legende="""Les questions qu'on nous pose le plus, en un carrousel.

Une autre question ? Pose-la en commentaire, on répond à tout. Et retrouve la FAQ dans nos stories à la une.

trophytracker sert à partager ton voyage avec ceux que tu choisis. Ce n'est ni un outil de navigation, ni un outil de sécurité ou de secours.""",
    hashtags="#roadtrip #faq #voyage #raid #moto #trophytracker",
))

# ───────────────────────── SEMAINE 8 (7 → 13 décembre) ─────────────────────────

P(dict(
    id=27, date=d("2026-12-07"), heure="19h", slug="soutenir-le-voyage-cagnotte-et-sponsors",
    titre="Ta cagnotte et tes sponsors, juste à côté de la carte",
    cible="raid / rallye", sujet="soutenir le voyage : cagnotte + vitrine des sponsors",
    format="carrousel 5 visuels", objectif="lien en bio",
    remarque="Remplace l'ancien post 25 (cagnotte).",
    slides=[
        ("1/5 · COUVERTURE", "Titre : « Ta cagnotte et tes sponsors, » / « juste à côté de la carte. »", "Capture C18 en grand, cadre téléphone, fond satellite flouté."),
        ("2/5 · TEXTE", "« Ton lien de cagnotte, sur ta page. »\n« Ceux qui te suivent tombent dessus en regardant où tu es. »", "Gabarit TEXTE, icône de tirelire ambre."),
        ("3/5 · TEXTE", "« Tes sponsors en vitrine. »\n« Pendant tout le voyage, sur la même page que la carte. »", "Gabarit TEXTE avec 3 cadres « logo » en pointillés."),
        ("4/5 · TEXTE", "« Et à la fin, le rapport PDF pour tes sponsors. »", "Vignette C15."),
        ("5/5 · DERNIÈRE SLIDE", "« Ton voyage se soutient là où il se suit. »", CTA_FINAL),
    ],
    legende="""Ton lien de cagnotte traîne dans ta bio, dans une vieille story ou au fond du groupe de la famille ? Résultat : ceux qui veulent t'aider ne le retrouvent jamais.

Sur trophytracker, il est sur ta page, juste à côté de la carte. Ceux qui te suivent le voient en regardant où tu en es. Tes sponsors aussi ont leur vitrine au même endroit. Et à la fin du voyage, tu leur envoies le rapport PDF.

Ton voyage se soutient là où il se suit. Lien en bio.""",
    hashtags="#raid #rallye #cagnotte #sponsoring #financement #trophytracker",
))

P(dict(
    id=28, date=d("2026-12-09"), heure="12h15", slug="ce-que-personne-ne-voit",
    titre="Ce que tu partages. Et ce que personne ne voit.",
    cible="road trip, van, tour du monde", sujet="confidentialité : lien privé, nuits floutées, couper, effacer",
    format="carrousel 6 visuels", objectif="enregistrer",
    remarque="",
    slides=[
        ("1/6 · COUVERTURE", "Titre : « Ce que tu partages. » / « Et ce que personne ne voit. »", "Gabarit COUVERTURE : moitié carte nette, moitié carte floutée."),
        ("2/6 · TEXTE", "« Ta page : seulement par ton lien. »\n« Elle n'apparaît jamais sur Google. Ceux à qui tu ne l'as pas envoyé ne la trouvent pas. »", "Gabarit TEXTE, pastille « privé · accès par lien »."),
        ("3/6 · TEXTE", "« Tes nuits : floutées. »\n« Personne ne sait où tu dors. »", "Capture C20."),
        ("4/6 · TEXTE", "« Le suivi : tu le coupes quand tu veux. »", "Gabarit TEXTE, interrupteur stylisé (rouge → gris)."),
        ("5/6 · TEXTE", "« Ta trace : tu l'effaces quand tu veux. »", "Gabarit TEXTE, trace ambre qui s'efface en pointillés."),
        ("6/6 · DERNIÈRE SLIDE", "« Ton voyage, tes règles. »", CTA_FINAL),
    ],
    legende="""Partager ton voyage, oui. Le partager avec n'importe qui, non.

Sur trophytracker, ta page est privée par défaut : seuls ceux qui ont ton lien la voient, et elle n'apparaît jamais sur Google. Tes arrêts de nuit sont floutés. Tu coupes le suivi quand tu veux, et tu peux effacer ta trace à tout moment.

Ton voyage, tes règles. Lien en bio.""",
    hashtags="#roadtrip #vieprivee #vanlife #voyage #confidentialite #trophytracker",
))

P(dict(
    id=29, date=d("2026-12-11"), heure="19h", slug="concours-gagne-ton-road-trip",
    titre="Concours : gagne ton road trip en direct",
    cible="toutes les cibles", sujet="codes d'accès offerts (TT-XXXX-XXXX)",
    format="post simple", objectif="commenter + taguer + s'abonner",
    remarque="1 code TT-XXXX-XXXX à gagner. Fin le jeudi 17/12 à 23h59, tirage et annonce en story le vendredi 18/12. Envoyer le code au gagnant en message privé, jamais en public.",
    slides=[
        ("VISUEL UNIQUE",
         "Pastille : « concours »\nTitre : « Ton prochain road trip, » / « on te l'offre. »\n"
         "Trois lignes numérotées :\n« 1. Abonne-toi à " + HANDLE + " »\n« 2. Tague la personne avec qui tu pars »\n« 3. Dis-nous en commentaire où vous partez »\n"
         "DM Mono : « 1 road trip à gagner · fin le 17/12 à 23h59 »",
         "Gabarit TEXTE, fond encre, halo rouge. Derrière, une carte satellite très sombre avec plusieurs petites traces ambre. "
         "Un ticket stylisé « TT-XXXX-XXXX » en DM Mono, incliné."),
    ],
    legende=f"""🎁 On t'offre ton prochain road trip en direct : 1 code à gagner, valable pour un road trip complet sur trophytracker.

Pour participer :
1. Abonne-toi à {HANDLE}
2. Tague en commentaire la personne avec qui tu pars
3. Dis-nous où vous partez

Fin le jeudi 17 décembre à 23h59. Tirage au sort le vendredi 18 décembre parmi les participations complètes, résultat annoncé en story. Participation gratuite, sans obligation d'achat.

Ce concours n'est ni organisé ni parrainé par Instagram.""",
    hashtags="#concours #jeuconcours #roadtrip #voyage #giveaway #trophytracker",
))

# ───────────────────────── SEMAINE 9 (14 → 20 décembre) ─────────────────────────

P(dict(
    id=30, date=d("2026-12-14"), heure="19h", slug="van-ta-maison-roule",
    titre="Van, camping-car : ta maison roule, ta famille suit",
    cible="van / camping-car (cible secondaire)", sujet="étapes, détection des nuits, nuits floutées, résumé du soir",
    format="carrousel 4 visuels", objectif="enregistrer",
    remarque="Cible secondaire : pas plus d'un post de ce type par mois.",
    slides=[
        ("1/4 · COUVERTURE", "Titre : « Ta maison roule. » / « Ta famille suit. »", "Photo : van aménagé sur une route côtière au lever du jour, vu de loin."),
        ("2/4 · TEXTE", "« Tes étapes, c'est toi qui les crées. »\n« Les nuits et les arrêts sont détectés tout seuls. Et floutés. »", "Capture C20 ou carte avec étiquettes « NUIT À … »."),
        ("3/4 · TEXTE", "« Un long voyage ? »\n« Chaque soir, tes proches reçoivent le résumé de la journée par e-mail. »", "Capture C13."),
        ("4/4 · DERNIÈRE SLIDE", "« 15 € le voyage. Pas d'abonnement. »", CTA_FINAL),
    ],
    legende="""En van ou en camping-car, tu ne sais pas toujours où tu dormiras ce soir. Ta page, elle, s'en occupe.

Tu crées tes étapes quand tu veux (ou tu importes ton GPX), et trophytracker détecte tout seul tes nuits et tes arrêts. Tes arrêts de nuit sont floutés. Et chaque soir, tes proches reçoivent le résumé de la journée par e-mail.

15 € le voyage, une seule fois. Lien en bio.""",
    hashtags=H["van"],
))

P(dict(
    id=31, date=d("2026-12-16"), heure="12h15", slug="le-resume-du-soir",
    titre="Chaque soir, le résumé de ta journée chez tes proches",
    cible="proches", sujet="e-mail « C'est parti » + résumé du soir + invitation par e-mail",
    format="carrousel 4 visuels", objectif="partager à un proche",
    remarque="Contenu de l'e-mail relevé dans le code de l'appli.",
    slides=[
        ("1/4 · COUVERTURE", "Titre : « Chaque soir, » / « le résumé de ta journée. »", "Capture C13 (e-mail « résumé du soir ») dans un cadre de téléphone, boîte de réception générique."),
        ("2/4 · TEXTE", "« Même pas besoin d'ouvrir la page. »\n« Les kilomètres du jour, l'altitude, les photos, les étapes et ton mot du journal. Par e-mail, chaque soir de route. »", "Gabarit TEXTE, enveloppe ambre."),
        ("3/4 · ÉCRAN", "« Et au départ : “C'est parti”. »", "Capture C14."),
        ("4/4 · DERNIÈRE SLIDE", "« Invite-les par e-mail depuis ton espace. »", CTA_FINAL),
    ],
    legende="""Ton grand-père n'ouvrira peut-être pas ta page tous les jours. Mais ses e-mails, il les lit.

Quand tu invites tes proches par e-mail sur trophytracker, ils reçoivent un e-mail « C'est parti » au départ, puis chaque soir de route le résumé de ta journée : les kilomètres, l'altitude, les photos, les étapes et ton mot du journal. Et quand ils veulent en voir plus, ta page est à un clic, sans compte et sans appli.

Envoie ce post à celui qui lit tout par e-mail.""",
    hashtags=H["proches"],
))

P(dict(
    id=32, date=d("2026-12-18"), heure="19h", slug="moto-casque-pose-tu-racontes",
    titre="Moto : casque posé, tu racontes",
    cible="à moto", sujet="carnet de bord raconté à l'IA, version motard",
    format="post simple", objectif="enregistrer + partager",
    remarque="Toujours montrer le carnet APRÈS la route (moto à l'arrêt, casque enlevé).",
    slides=[
        ("VISUEL UNIQUE",
         "Titre : « Casque posé. » / « Tu racontes. » (rouge)\nSous-titre : « L'IA écrit ton carnet de route. »\nLogo",
         "Photo : moto à l'arrêt sur un parking de col au coucher du soleil, casque posé sur la selle, téléphone posé sur le réservoir "
         "avec le bouton micro à l'écran. Personne sur la moto."),
    ],
    legende="""Un carnet de voyage à moto, en vrai, personne ne l'écrit. Trop de route, trop de fatigue, des gants partout.

Avec trophytracker, le soir, casque posé, tu appuies sur le micro et tu racontes ta journée : les épingles, le café au sommet, la pluie qui t'a rattrapé. L'IA en fait une page de carnet, ajoute les kilomètres et l'altitude, sans rien inventer. Tu relis, tu publies.

Ceux qui te suivent lisent ta journée. Toi, tu la gardes. Lien en bio.""",
    hashtags=H["moto"],
))

# ───────────────────────── SEMAINE 10 (21 → 27 décembre) ─────────────────────────

P(dict(
    id=33, date=d("2026-12-21"), heure="19h", slug="noel-montre-ton-replay",
    titre="Au repas de Noël, montre ton replay",
    cible="entre amis, proches, road trip", sujet="replay 3D + annoncer le prochain voyage",
    format="carrousel 4 visuels", objectif="partager dans le groupe famille",
    remarque="Remplace l'ancien post 22.",
    slides=[
        ("1/4 · COUVERTURE", "Titre : « Au repas de Noël, » / « sors ton téléphone. »", "Photo : table de fête, lumières floues, un téléphone posé au milieu avec une image du replay 3D à l'écran. Pas de visage."),
        ("2/4 · TEXTE", "« Montre le replay de ton dernier road trip. »\n« Tout le voyage en 3D, en une minute. »", "Image fixe du replay (C11)."),
        ("3/4 · TEXTE", "« Et annonce le prochain. »\n« Ils suivront tout depuis le canapé. »", "Gabarit TEXTE, un lien qui part dans un groupe « Famille » stylisé (sans interface réelle)."),
        ("4/4 · DERNIÈRE SLIDE", "« Le cadeau qu'ils vont ouvrir toute l'année : ton lien. »", CTA_FINAL),
    ],
    legende="""Le seul moment de l'année où toute la famille est autour de la même table.

Sors ton téléphone, lance le replay 3D de ton dernier road trip, et réponds une bonne fois pour toutes à « mais vous êtes passés par où exactement ? ».

Et si tu as déjà un prochain voyage en tête, annonce-le : le jour du départ, ils n'auront qu'à ouvrir ton lien.

Joyeux Noël. 🎄""",
    hashtags="#noel #roadtrip #famille #souvenirs #voyage #trophytracker",
))

P(dict(
    id=34, date=d("2026-12-23"), heure="12h15", slug="tour-du-monde",
    titre="Tu pars loin, longtemps ? Ils suivent tout, d'ici.",
    cible="tour du monde (cible secondaire)", sujet="page privée, sans réseau, résumé du soir, carnet",
    format="post simple", objectif="enregistrer",
    remarque="Cible secondaire. Pas de durée maximale pour un road trip (confirmé par Julien).",
    slides=[
        ("VISUEL UNIQUE",
         "Titre : « Tu pars loin, longtemps ? » / « Ils suivent tout, d'ici. »\nDM Mono : « position · trace · carnet · résumé du soir »\nLogo",
         "Image satellite très large (vue d'une côte ou d'un continent), une longue trace ambre qui traverse l'image, balise rouge au bout."),
    ],
    legende="""Un grand voyage, c'est des mois loin de ceux que tu aimes, et des journées entières sans réseau. Sur trophytracker, pas de durée maximale : trois jours ou six mois, c'est un seul road trip.

Avec trophytracker, ils suivent ta trace en direct sur ta page privée. Sans réseau, tout est gardé en mémoire et envoyé dès que ça capte. Le soir, tu racontes ta journée au micro et l'IA en fait ton carnet. Et chaque soir, ils reçoivent le résumé par e-mail.

Enregistre ce post si un grand départ se prépare. Lien en bio.""",
    hashtags=H["tdm"],
))

P(dict(
    id=35, date=d("2026-12-28"), heure="19h", slug="tes-road-trips-2027",
    titre="Ton road trip 2027, c'est lequel ?",
    cible="toutes les cibles prioritaires", sujet="engagement : un type de voyage par slide",
    format="carrousel 6 visuels", objectif="commenter",
    remarque="Les réponses en commentaire servent à décider des prochains posts.",
    slides=[
        ("1/6 · COUVERTURE", "Titre : « Ton road trip 2027, » / « c'est lequel ? »", "Mosaïque de 4 photos (route, moto, piste, bande d'amis), assombrie."),
        ("2/6 · PHOTO", "« 1. La grande boucle en voiture. »", "Photo : route de côte ou de montagne, voiture de loin."),
        ("3/6 · PHOTO", "« 2. Les cols à moto. »", "Photo : moto dans une épingle."),
        ("4/6 · PHOTO", "« 3. Le raid ou le rallye. »", "Photo : piste dans le désert, véhicule tout-terrain de loin (véhicule moderne, sans numéro ni logo)."),
        ("5/6 · PHOTO", "« 4. Le road trip entre potes. »", "Photo : bande d'amis de dos devant un coucher de soleil."),
        ("6/6 · DERNIÈRE SLIDE", "« Dis-nous en commentaire : 1, 2, 3 ou 4 ? »", CTA_FINAL),
    ],
    legende="""2027 approche. Ton prochain road trip, c'est plutôt :
1. La grande boucle en voiture
2. Les cols à moto
3. Le raid ou le rallye
4. Le road trip entre potes

Réponds en commentaire avec ton chiffre (et ta destination si tu la connais déjà). On lit tout.""",
    hashtags="#roadtrip #2027 #moto #raid #roadtripentreamis #trophytracker",
))

# ───────────────────────── JANVIER ─────────────────────────

P(dict(
    id=36, date=d("2027-01-04"), heure="19h", slug="sans-reseau-dans-le-desert-ce-qui-se-passe",
    titre="Sans réseau dans le désert : ce qui se passe vraiment",
    cible="raid / rallye", sujet="le fonctionnement sans réseau, raconté comme une journée",
    format="carrousel 6 visuels", objectif="enregistrer + partager à son équipage",
    remarque="Les heures sont un scénario d'illustration (pas un vrai voyage).",
    slides=[
        ("1/6 · COUVERTURE", "Titre : « Une journée sans réseau. » / « Ce qui se passe vraiment. »", "Photo : piste dans les dunes, ciel immense, aucun véhicule reconnaissable."),
        ("2/6 · TEXTE", "DM Mono : « 10:42 »\n« Dernière barre de réseau. »\n« Ton téléphone continue d'enregistrer chaque position. »", "Gabarit TEXTE, icône de barres de réseau qui tombent à zéro."),
        ("3/6 · TEXTE", "DM Mono : « 13:00 »\n« Chez toi, ils voient le bandeau : “Pas de réseau, c'est normal”. »", "Reproduction du bandeau de la page."),
        ("4/6 · TEXTE", "DM Mono : « 16:15 »\n« Ça capte. Tout part d'un coup. »\n« La trace de la journée se complète sur ta page. »", "Trace ambre en pointillés qui devient pleine."),
        ("5/6 · TEXTE", "DM Mono : « 21:00 »\n« Tu racontes ta journée. L'IA écrit. »", "Gabarit TEXTE, bouton micro."),
        ("6/6 · DERNIÈRE SLIDE", "« Même sans réseau, ton voyage se raconte. »", CTA_FINAL),
    ],
    legende="""10 h 42, dernière barre de réseau. Et après ?

Ton téléphone continue d'enregistrer chaque position. Chez toi, ceux qui te suivent voient un bandeau clair : « Pas de réseau, c'est normal ». Dès que ça capte, tout part d'un coup et la trace de la journée se complète sur ta page. Et le soir, tu racontes ta journée au micro.

Enregistre ce post et envoie-le à ton équipage avant la première piste.""",
    hashtags=H["raid"],
))

P(dict(
    id=37, date=d("2027-01-06"), heure="12h15", slug="lancement-gratuit-pour-ceux-qui-te-suivent",
    titre="Gratuit pour ceux qui te suivent",
    cible="proches", sujet="série lancement (5/5) : 0 € côté proches",
    format="post simple", objectif="partager à un proche",
    remarque="",
    slides=[
        ("VISUEL UNIQUE",
         "En très grand : « 0 € » (papier)\nDessous : « pour ceux qui te suivent. » (rouge)\n"
         "DM Mono : « pas de compte · pas d'appli · juste ton lien »\nLogo",
         "Gabarit TEXTE, même mise en page que P04 (« 15 € ») pour que les deux se répondent dans la grille."),
    ],
    legende="""Toi, c'est 15 € par road trip. Eux, c'est 0 €.

Tes parents, tes grands-parents, tes potes, tes sponsors : ils ouvrent ton lien et ils suivent. Pas de compte à créer, pas d'appli à installer, rien à payer.

Envoie ce post à quelqu'un qui pense qu'il faut « encore télécharger un truc ».""",
    hashtags=H["proches"],
))

P(dict(
    id=38, date=d("2027-01-08"), heure="19h", slug="humour-les-roles-dans-la-voiture",
    titre="Humour : les rôles dans la voiture",
    cible="entre amis", sujet="à plusieurs, photos, replay, carnet",
    format="carrousel 7 visuels", objectif="taguer sa bande",
    remarque="",
    slides=[
        ("1/7 · COUVERTURE", "Titre : « Les rôles » / « dans la voiture. »\n« glisse → »", "Gabarit TEXTE, 5 ronds d'initiales façon page d'exemple."),
        ("2/7 · TEXTE", "« Le pilote »\n« Refuse de lâcher le volant depuis 600 km. »", "Gabarit TEXTE, numéro rouge."),
        ("3/7 · TEXTE", "« Le DJ »\n« Même playlist depuis le départ. Personne n'ose rien dire. »", "Idem."),
        ("4/7 · TEXTE", "« Le photographe »\n« 400 photos du même col. Toutes sur la page. »", "Idem."),
        ("5/7 · TEXTE", "« Celui qui dort »\n« A raté le plus beau. Heureusement, il y a le replay 3D. »", "Idem."),
        ("6/7 · TEXTE", "« Le conteur »\n« Le soir, c'est lui qui raconte au micro. L'IA fait le reste. »", "Idem."),
        ("7/7 · DERNIÈRE SLIDE", "« Tague ta bande et dis qui fait quoi. »", CTA_FINAL),
    ],
    legende="""Dans chaque road trip entre potes, il y a toujours les mêmes rôles. Toi, t'es lequel ?

Tague ta bande en commentaire et distribue les rôles. (Et si personne ne veut être le conteur, l'IA aide.)""",
    hashtags=H["amis"],
))

P(dict(
    id=39, date=d("2027-01-11"), heure="19h", slug="ton-itineraire-gpx-ou-pas",
    titre="Ton itinéraire est prêt ? Importe ton GPX. (Sinon, roule.)",
    cible="à moto, road trip en voiture", sujet="import GPX, itinéraire facultatif, détection des nuits et des arrêts",
    format="carrousel 4 visuels", objectif="enregistrer",
    remarque="",
    slides=[
        ("1/4 · COUVERTURE", "Titre : « Ton itinéraire est prêt ? » / « Importe ton GPX. »", "Capture de l'import GPX dans l'espace voyageur [à faire], ou fichier « .gpx » stylisé qui se transforme en trace sur la carte."),
        ("2/4 · TEXTE", "« Pas d'itinéraire ? »\n« Pas grave : ta trace s'écrit en roulant. »", "Trace ambre qui se dessine sur une carte vide."),
        ("3/4 · TEXTE", "« Les nuits et les arrêts ? »\n« Détectés tout seuls. »", "Carte avec étiquettes « NUIT À … » et « ARRÊT »."),
        ("4/4 · DERNIÈRE SLIDE", "« Prépare tout, ou rien. Ta page suit. »", CTA_FINAL),
    ],
    legende="""Il y a ceux qui préparent leur road trip au kilomètre près, avec leur fichier GPX. Et ceux qui partent et voient bien.

Sur trophytracker, les deux marchent. Tu importes ton GPX, ou tu ne mets rien du tout : ta trace s'écrit en roulant. Tes étapes, c'est toi qui les crées, et tes nuits et tes arrêts sont détectés tout seuls.

Tu es plutôt GPX ou plutôt « on verra » ? Dis-le en commentaire.""",
    hashtags="#moto #roadtripmoto #gpx #roadtrip #cols #trophytracker",
))

# ───────────────────────── RÉSERVE : MODÈLES SANS DATE ─────────────────────────

P(dict(
    id=40, date=None, heure="12h15 ou 19h", slug="modele-road-trip-de-la-semaine",
    titre="MODÈLE · Le road trip de la semaine",
    cible="selon le voyageur", sujet="mettre en avant un vrai voyageur (avec son accord)",
    format="carrousel 3 visuels · en collaboration", objectif="suivre le voyageur + partager",
    remarque="⚠ À COMPLÉTER à chaque fois. Seulement un vrai voyageur, avec son accord écrit, publié en collaboration. "
             "Sa page doit être publique, ou il doit accepter de montrer une capture. Remplace l'ancien post 20.",
    slides=[
        ("1/3 · COUVERTURE", "DM Mono : « road trip de la semaine · n°[X] »\nTitre : « [Nom du road trip] »\nDM Mono : « [d'où] → [où] · [voiture / moto / raid / entre amis] »",
         "[Sa photo de couverture, avec son accord]."),
        ("2/3 · ÉCRAN", "« Sa page »", "[Capture de sa page, avec son accord, nuits floutées visibles]."),
        ("3/3 · TEXTE", "DM Mono : « sa réponse »\n« [Pourquoi ce voyage ? En une phrase, ses mots] »", "Gabarit TEXTE."),
    ],
    legende=f"""Cette semaine, on part avec [@compte] : [d'où → où, en quoi, un détail qu'il t'a donné].

[Une phrase sur son voyage, avec ses mots.]

Tu veux être le prochain road trip de la semaine ? Partage ta page ou ton replay en story et tague {HANDLE}.""",
    hashtags="#roadtripdelasemaine #roadtrip #voyage #trophytracker",
))

P(dict(
    id=41, date=None, heure="12h15 ou 19h", slug="modele-avis-reel",
    titre="MODÈLE · Un vrai retour",
    cible="selon l'auteur", sujet="preuve sociale (vraie)",
    format="post simple", objectif="partager",
    remarque="⚠ À COMPLÉTER. Seulement avec une citation réelle d'un utilisateur de la NOUVELLE appli, validée par écrit. "
             "Jamais de citation inventée, jamais de retour lié à l'ancien produit. Remplace l'ancien post 8.",
    slides=[
        ("VISUEL UNIQUE", "DM Mono : « retour réel »\n« [CITATION RÉELLE] »\n« — [qui : ex. la mère d'un voyageur, un sponsor] »",
         "Gabarit TEXTE, grands guillemets rouges."),
    ],
    legende="""[Contexte en une phrase : qui, quel voyage.]

« [CITATION RÉELLE] »

Envoie ce post à la personne qui va te suivre pendant ton prochain road trip.""",
    hashtags="#roadtrip #avis #voyage #trophytracker",
))

P(dict(
    id=42, date=None, heure="12h15 ou 19h", slug="modele-nouveau-cest-en-ligne",
    titre="MODÈLE · Nouveau : c'est en ligne",
    cible="toutes les cibles", sujet="annonce d'une nouvelle fonctionnalité",
    format="post simple", objectif="tester sur sa page",
    remarque="⚠ À COMPLÉTER. Une fois par fonctionnalité, le jour où elle est réellement en ligne, jamais avant. Remplace l'ancien post 23.",
    slides=[
        ("VISUEL UNIQUE", "Pastille : « nouveau · en ligne »\nTitre : « [Nom de la fonctionnalité] »\n« Déjà dans ta page. »",
         "Gabarit ÉCRAN avec la capture réelle de la fonctionnalité."),
    ],
    legende="""Nouveau sur trophytracker : [fonctionnalité].

[Une phrase : à quoi ça sert, pour le voyageur ou pour ceux qui le suivent.]

C'est déjà dans ta page, rien à faire de ton côté. Lien en bio.""",
    hashtags="#nouveaute #roadtrip #trophytracker",
))

P(dict(
    id=43, date=None, heure="12h15 ou 19h", slug="modele-qui-est-derriere",
    titre="Qui est derrière trophytracker ?",
    cible="toutes les cibles", sujet="montrer qu'une vraie personne est derrière (sans visage si tu préfères)",
    format="carrousel 4 visuels", objectif="s'abonner",
    remarque="Sans date : à sortir quand tu veux (un samedi par exemple). Ne jamais y raconter l'ancien produit ni l'événement d'origine. "
             "Remplace l'ancien post 1 (histoire du créateur, qui racontait l'ancien événement).",
    slides=[
        ("1/4 · COUVERTURE", "Titre : « Qui est derrière » / « trophytracker ? »", "Rendu typographique sur fond encre (tu peux le remplacer par une photo de ton écran de code, sans visage)."),
        ("2/4 · TEXTE", "« Une personne. »\n« Je développe l'appli, je la teste sur la route, et je réponds moi-même à chaque message. »", "Gabarit TEXTE."),
        ("3/4 · TEXTE", "« Pourquoi ? »\n« Parce qu'un road trip mérite mieux qu'un “je t'écris ce soir”. Ceux qu'on aime devraient pouvoir le vivre avec nous. »", "Gabarit TEXTE."),
        ("4/4 · DERNIÈRE SLIDE", "« Une question ? Écris-moi, je réponds à tout. »", CTA_FINAL),
    ],
    legende="""Derrière trophytracker, il n'y a pas une grosse boîte. Il y a moi.

Je développe l'appli, je la teste sur la route, et c'est moi qui te réponds quand tu écris au compte. Je l'ai faite pour une raison simple : un road trip mérite mieux qu'un « je t'écris ce soir ». Ceux qu'on aime devraient pouvoir le vivre avec nous, en direct.

Une question, une idée, un bug ? Écris-moi en message, je réponds à tout.""",
    hashtags="#roadtrip #coulisses #startup #trophytracker",
))

P(dict(
    id=44, date=d("2026-11-07"), heure="12h15", slug="paiement-securise-par-stripe",
    titre="On ne voit jamais ta carte bancaire",
    cible="toutes les cibles", sujet="paiement par carte géré par Stripe, une seule fois",
    format="carrousel 4 visuels", objectif="lien en bio",
    remarque="Remplace l'ancien post 24 (paiement Stripe). Paiement confirmé par Julien : carte bancaire via la page de paiement Stripe.",
    slides=[
        ("1/4 · COUVERTURE", "Titre : « On ne voit jamais » / « ta carte bancaire. »", "Gabarit TEXTE : une carte bancaire stylisée (numéros masqués « •••• »), cadenas papier."),
        ("2/4 · TEXTE", "« Tu paies sur la page de Stripe. »\n« Ton numéro de carte est saisi chez eux, jamais sur nos serveurs. »", "Gabarit TEXTE, sans logo Stripe redessiné (texte simple « Stripe »)."),
        ("3/4 · TEXTE", "« Ta banque garde la main. »\n« Elle peut te demander de valider le paiement dans son appli. »", "Gabarit TEXTE, icône de téléphone avec une coche verte."),
        ("4/4 · DERNIÈRE SLIDE", "« 15 €, une fois. Et c'est tout. »", CTA_FINAL),
    ],
    legende="""On ne voit jamais ta carte bancaire. 🔒

Le paiement de ton road trip passe par Stripe, l'un des grands noms du paiement en ligne. Tu tapes ta carte sur leur page : ton numéro ne passe jamais par nos serveurs. De notre côté, on reçoit une seule info : ton road trip est payé.

15 € par road trip, une seule fois. Pas d'abonnement, rien qui se renouvelle tout seul.

Une question sur le paiement ? Écris-nous, on répond à tout. Lien en bio.""",
    hashtags="",
))
