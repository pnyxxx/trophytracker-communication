"""Textes et visuels des posts (refonte du 16/10/2026 : moins de posts, aucun sujet ni visuel répété).
Un post = un sujet. Exemple utilisé partout : la page j4l-club (vraies photos, vraie page ; scènes dans les dunes
mises en scène sur la vraie page, voir captures-j4l.mjs). 4 hashtags maximum. Jamais de moto.
Gabarits des slides : voir render.py (S("photo", …), S("screen", …), etc.)."""
from common import d

POSTS = []
P = POSTS.append


def S(t, **k):
    k["t"] = t
    return k


# ───────────── SEMAINE 1 : le profil (c'est quoi, comment, combien) ─────────────

P(dict(
    id=1, date=d("2026-10-17"), heure="19h", slug="ton-road-trip-en-direct",
    titre="Ton road trip, en direct.", cible="toutes les cibles", sujet="c'est quoi trophytracker (post à épingler)",
    objectif="comprendre en 10 secondes + lien en bio",
    remarque="À épingler (1/3).",
    slides=[
        S("photo", img="dunes", kicker="trophytracker", title=["Ton road trip,", "en direct."],
          sub="Tu roules. Ceux que tu invites te suivent.", swipe="glisse →"),
        S("screen", bg="paper", title=["Une page rien qu'à toi."], red=[],
          sub="Position, trace, photos et stats. Accessible uniquement par ton lien.", cap="D_ecran_carte", tilt=True),
        S("photo", img="chameau", pos="50% 80%", title=["Et même", "le temps qu'il fait là-bas."],
          card=dict(cap="D_meteo")),
        S("type", bg="red", kicker="pour ceux qui te suivent", title=["Sans compte.", "Sans appli.", "Gratuit."], red=[],
          sub="Ils cliquent sur ton lien, ils voient où tu en es."),
    ],
    legende="""Ton road trip, en direct.

Tu roules, ceux que tu invites te suivent. Ta position, ta trace, tes photos et tes stats sur une page privée, accessible uniquement par ton lien.

Eux n'ont rien à installer : pas de compte, pas d'appli. Ils cliquent, ils voient où tu en es, et même le temps qu'il fait là où tu es.

15 € par road trip, payé une fois. Va voir la page d'exemple : lien en bio.""",
    tags="#roadtrip #raid #rallye #voyage",
))

P(dict(
    id=2, date=d("2026-10-18"), heure="19h", slug="pret-en-5-minutes",
    titre="Prêt en 5 minutes.", cible="toutes les cibles", sujet="comment ça marche : créer, scanner, partager (post à épingler)",
    objectif="lever le « ça a l'air compliqué » + enregistrer",
    remarque="À épingler (2/3).",
    slides=[
        S("type", giant="5 min", accent="pour tout préparer.", sub="Zéro prise de tête. Glisse, c'est 3 étapes.", align="center"),
        S("type", bg="red", num="1", title=["Tu crées ta page."], red=[],
          sub="Un nom, une photo, tes compagnons de route, d'où à où, quand. L'itinéraire ? Facultatif."),
        S("type", bg="paper", num="2", title=["Tu scannes", "un QR code."],
          sub="Avec l'appli gratuite Traccar Client, sur Android ou iPhone. Ou avec un boîtier GPS compatible. Ton téléphone envoie ta position."),
        S("screen", num="3", title=["Tu envoies ton lien.", "Et tu pars."], cap="F_ecran_haut",
          sub="Par e-mail depuis ton espace, ou où tu veux."),
    ],
    legende="""Prêt en 5 minutes. Zéro prise de tête.

1. Tu crées ta page : un nom, une photo de couverture, tes compagnons de route, d'où à où, quand. L'itinéraire est facultatif, ta trace s'écrit en roulant.
2. Tu scannes un QR code avec l'appli gratuite Traccar Client (Android et iPhone). Un boîtier GPS compatible marche aussi.
3. Tu envoies ton lien à ceux qui doivent te suivre. Et tu pars.

Enregistre ce post pour le jour où tu prépares ton prochain départ.""",
    tags="#roadtrip #raid #rallye #preparation",
))

P(dict(
    id=3, date=d("2026-10-19"), heure="19h", slug="15-euros-une-fois",
    titre="15 €. Une fois.", cible="toutes les cibles", sujet="le prix (post à épingler)",
    objectif="répondre à « c'est combien ? »",
    remarque="À épingler (3/3). Après ce post : épingler P01, P02 et P03.",
    slides=[
        S("type", bg="paper", giant="15 €", accent="par road trip.",
          bullets=["Payé une seule fois", "Pas d'abonnement", "Gratuit pour ceux qui te suivent"], align="center"),
    ],
    legende="""15 € par road trip. Payé une seule fois.

Pas d'abonnement, rien qui se renouvelle tout seul. Et pour ceux qui te suivent, c'est gratuit : ils ouvrent ton lien, c'est tout.

Ton road trip, en direct : lien en bio.""",
    tags="#roadtrip #voyage #petitbudget #raid",
))

P(dict(
    id=4, date=d("2026-10-21"), heure="12h15", slug="pas-de-reseau-cest-normal",
    titre="Pas de réseau ? C'est normal.", cible="raid / rallye (désert, pistes)", sujet="le suivi même sans réseau",
    objectif="partager à celui qui dit « on verra bien s'il y a du réseau »",
    slides=[
        S("photo", img="chameau", pos="50% 75%", kicker="désert · 0 barre", title=["Ici, zéro réseau.", "Et ce n'est pas grave."]),
        S("widget", bg="ink", title=["Chez toi, la page", "les rassure."],
          sub="« Pas de réseau, c'est normal. » Avec l'heure de ton dernier signal.", cap="N_ecran_haut", crop=(.655, .955)),
        S("screen", title=["Ça capte ?", "Tout part d'un coup."],
          sub="Ton téléphone a tout gardé en mémoire. La trace se complète en quelques secondes.", cap="D_ecran_carte"),
    ],
    legende="""Dans les dunes ou au fond d'une vallée, à un moment, ça ne capte plus. Et ce n'est pas grave.

Sans réseau, ton téléphone garde chaque position en mémoire. Dès que ça capte, tout part d'un coup et ta trace se complète sur ta page.

Pendant ce temps, chez toi, personne ne s'affole : ta page affiche « Pas de réseau, c'est normal », avec l'heure de ton dernier signal.

Envoie ça à celui qui dit « on verra bien s'il y a du réseau là-bas ».""",
    tags="#raid #rallye #desert #roadtrip",
))

P(dict(
    id=5, date=d("2026-10-23"), heure="19h", slug="le-soir-tu-racontes-lia-ecrit",
    titre="Le soir, tu racontes. L'IA écrit.", cible="toutes les cibles", sujet="carnet de bord raconté à l'IA (fonction phare)",
    objectif="enregistrer + lien en bio",
    remarque="[À CONFIRMER] La page de carnet visible sur la capture est un texte d'exemple (feu de camp, sable), écrit d'après tes photos. Dis-moi si tu préfères un vrai texte à toi.",
    slides=[
        S("photo", img="feu", kicker="carnet de bord", title=["Le soir, tu racontes.", "L'IA écrit."], swipe="glisse →"),
        S("type", bg="paper", align="center", items=[
            ("1", "Tu appuies sur le micro.", "Et tu racontes ta journée comme à un pote. Ou tu l'écris."),
            ("2", "L'IA en fait une page de carnet.", "Elle garde tes anecdotes, enlève les « euh », ajoute kilomètres et altitude."),
            ("3", "Tu relis. Tu publies.", "Tes proches la lisent sur ta page."),
        ]),
        S("widget", title=["Sans rien inventer."], red=[], sub="Ce que tu n'as pas raconté n'apparaît pas. C'est ton voyage, avec tes mots.", cap="D_journal"),
    ],
    legende="""Tout le monde se promet de tenir un carnet de voyage. Personne ne le tient après le deuxième jour.

Le soir, tu appuies sur le micro et tu racontes ta journée (ou tu l'écris). L'IA en fait une vraie page de carnet : elle garde tes anecdotes, enlève les hésitations et ajoute les kilomètres et l'altitude. Sans rien inventer.

Tu relis, tu publies. Tes proches la lisent sur ta page, et toi tu gardes ton voyage raconté avec tes mots.

Enregistre ce post pour ton prochain départ.""",
    tags="#carnetdevoyage #roadtrip #raid #voyage",
))

# ───────────── fin octobre ─────────────

P(dict(
    id=6, date=d("2026-10-26"), heure="19h", slug="toi-tu-roules-eux-ils-suivent",
    titre="Toi, tu roules. Eux, ils suivent.", cible="les proches (et les voyageurs qui veulent leur donner des nouvelles)",
    sujet="ce que voient les proches", objectif="partager à sa famille",
    slides=[
        S("photo", img="bivouac", title=["Toi, tu roules.", "Eux, ils suivent."], swipe="glisse →"),
        S("widget", bg="paper", title=["La balise, en direct."], red=[], sub="Mise à jour en moins de 10 secondes.", cap="D_carte", crop=(0, .9)),
        S("widget", title=["Ta journée, en chiffres."], red=[], sub="Distance, vitesse, altitude, temps au volant.", cap="D_tableau"),
    ],
    legende="""Pendant que tu roules, eux ouvrent ton lien.

Ils voient la balise avancer sur la carte satellite, ta trace de la journée, tes étapes, tes photos. Et les chiffres : distance, vitesse, altitude, temps au volant.

Pas de compte, pas d'appli, rien à installer. Juste ton lien.

Envoie ce post à ceux qui vont te suivre.""",
    tags="#roadtrip #famille #voyage #raid",
))

P(dict(
    id=7, date=d("2026-10-28"), heure="12h15", slug="humour-je-tecris-ce-soir",
    titre="Humour : « Je t'écris ce soir. »", cible="road trip (voyageurs + proches)", sujet="humour, les nouvelles qui n'arrivent pas",
    objectif="partager, identification",
    slides=[
        S("chat", msgs=[("me", "Je t'écris ce soir 😘", "envoyé à 8:12"), ("note", "23:47", None), ("them", "Alors ??", "lu"), ("note", "toujours rien.", None)],
          title=["Ta page, elle,", "donne des nouvelles toute seule."]),
    ],
    legende="""« Je t'écris ce soir. » 23h47. Toujours rien. 🙃

Personne ne t'en veut : tu étais au volant, puis au bivouac, puis tu t'es endormi.

Ta page, elle, donne des nouvelles toute seule. Ils ouvrent ton lien et voient où tu en es, sans attendre ton message.

Tague celui qui écrit « ce soir » et n'écrit jamais.""",
    tags="#roadtrip #humour #famille #voyage",
))

P(dict(
    id=8, date=d("2026-10-30"), heure="19h", slug="raid-tes-sponsors-sur-ta-page",
    titre="Tes sponsors sur ta voiture. Et sur ta page.", cible="raid / rallye (et sponsors)",
    sujet="vitrine des sponsors, cagnotte, statistiques, rapport PDF", objectif="enregistrer, partager à son équipage",
    remarque="La 2ᵉ slide montre les vrais logos des sponsors de la page j4l-club.",
    slides=[
        S("photo", img="camp", title=["Tes sponsors sur ta voiture.", "Et sur ta page."], swipe="glisse →"),
        S("widget", title=["Leur logo,", "à côté de la carte."], sub="Ceux qui te suivent les voient à chaque visite.", cap="F_sponsors"),
        S("type", bg="paper", align="center", title=["Et aussi :"], red=[], bullets=[
            "Le lien de ta cagnotte, sur la même page que la carte",
            "Les statistiques de visibilité de ta page",
            "À l'arrivée, un rapport PDF à envoyer à tes sponsors",
        ]),
    ],
    legende="""Tes sponsors t'ont aidé à partir. Sur ta page, ils sont juste à côté de la carte.

Leurs logos s'affichent dans une vitrine que voient tous ceux qui te suivent. Le lien de ta cagnotte est sur la même page. Et à l'arrivée, tu leur envoies un rapport PDF avec les statistiques de visibilité.

Enregistre ce post pour ton dossier sponsors, et envoie-le à ton coéquipier.""",
    tags="#raid #rallye #sponsoring #cagnotte",
))

# ───────────── novembre ─────────────

P(dict(
    id=9, date=d("2026-11-03"), heure="19h", slug="ta-page-ton-lien-personne-dautre",
    titre="Ta page. Ton lien. Personne d'autre.", cible="tout le monde (voyageurs, proches)", sujet="confidentialité",
    objectif="rassurer, enregistrer",
    slides=[
        S("type", bg="ink", pill="privé · accès par lien", title=["Ta page.", "Ton lien.", "Personne d'autre."], align="center"),
        S("type", bg="paper", align="center", title=["C'est toi qui choisis."], red=[], bullets=[
            "Seuls ceux qui ont ton lien te suivent",
            "Jamais sur Google, sauf si tu la rends publique",
            "Tes arrêts de nuit sont floutés",
            "Tu coupes le suivi ou tu effaces ta trace quand tu veux",
        ]),
    ],
    legende="""Ta page est privée par défaut. Seuls ceux à qui tu envoies le lien peuvent te suivre.

Elle n'apparaît jamais sur Google, sauf si tu décides de la rendre publique. Tes arrêts de nuit sont floutés. Et tu peux couper le suivi ou effacer ta trace à tout moment.

Ton voyage, tes règles.""",
    tags="#roadtrip #voyage #vieprivee #famille",
))

P(dict(
    id=10, date=d("2026-11-05"), heure="19h", slug="revis-ton-voyage-en-3d",
    titre="Tout ton voyage, rejoué en 3D.", cible="toutes les cibles", sujet="replay 3D et export vidéo",
    objectif="enregistrer, envie",
    slides=[
        S("bleed", cap="D_relief", pos="45% 75%", size="190%", title=["Tout ton voyage,", "rejoué en 3D."], swipe="glisse →"),
        S("widget", bg="paper", title=["Puis en vidéo."], red=[], sub="Paysage, story ou carré. Prête à poster le soir du retour.", cap="F_replay"),
    ],
    legende="""À la fin, tu revis tout.

Ton voyage entier rejoué en survol satellite, en relief 3D, avec ta trace et tes étapes. Et tu l'exportes en vidéo : paysage, story ou carré.

De quoi faire taire ceux qui disent que tes photos de vacances sont toutes pareilles.""",
    tags="#roadtrip #souvenirs #raid #voyage",
))

P(dict(
    id=11, date=d("2026-11-07"), heure="12h15", slug="toute-la-bande-sur-la-meme-page",
    titre="Toute la bande sur la même page.", cible="entre amis, équipages", sujet="la page gérée à plusieurs",
    objectif="taguer ses potes",
    slides=[
        S("photo", img="moteur", title=["Pendant qu'il répare,", "l'autre poste les photos."]),
        S("type", align="center", title=["Toute la bande", "gère la page."],
          sub=["Photos, étapes, carnet : tout l'équipage peut publier.", "Et toutes les familles suivent au même endroit."]),
    ],
    legende="""Un road trip entre potes, une seule page.

Tout l'équipage la gère ensemble : chacun peut ajouter ses photos, des étapes, écrire dans le carnet. Pendant que l'un répare, l'autre raconte.

Et de l'autre côté, fini les trois groupes de discussion par famille : tout le monde suit au même endroit.

Tague ceux avec qui tu pars.""",
    tags="#roadtripentreamis #roadtrip #raid #entrepotes",
))

P(dict(
    id=12, date=d("2026-11-10"), heure="19h", slug="5-phrases-pour-convaincre-un-sponsor",
    titre="5 phrases pour convaincre un sponsor.", cible="raid / rallye", sujet="conseils pour le dossier sponsor",
    objectif="enregistrer, partager",
    slides=[
        S("type", bg="paper", title=["5 phrases", "pour convaincre un sponsor."], swipe="glisse →", align="center"),
        S("type", align="center", items=[
            ("1", "« Votre logo sera sur notre page de voyage, juste à côté de la carte en direct. »", None),
            ("2", "« Vous suivez en direct l'aventure que vous financez. »", None),
            ("3", "« Voici le lien de notre page : votre place est déjà prête. »", None),
        ]),
        S("type", align="center", items=[
            ("4", "« Ce lien, on le partage à nos proches et sur nos réseaux, du départ à l'arrivée. »", None),
            ("5", "« À l'arrivée, vous recevez un rapport PDF avec les statistiques de visibilité. »", None),
        ]),
        S("type", bg="red", title=["Copie. Colle.", "Envoie."], align="center"),
    ],
    legende="""Trouver des sponsors, c'est la partie la plus dure de la préparation. Voici 5 phrases à glisser dans ton prochain mail.

Ce qui fait la différence : montrer au sponsor ce qu'il va voir, concrètement. Son logo sur ta page, la carte en direct, et à la fin un rapport avec les chiffres.

Enregistre ce post pour ton dossier, et envoie-le à ton coéquipier.""",
    tags="#sponsoring #raid #rallye #partenariat",
))

P(dict(
    id=13, date=d("2026-11-12"), heure="19h", slug="humour-les-3-etats-de-ta-mere",
    titre="Humour : les 3 états de ta mère.", cible="proches (via les voyageurs)", sujet="humour, l'inquiétude des proches",
    objectif="partager à sa mère",
    slides=[
        S("timeline", kicker="les 3 états de ta mère pendant ton voyage", rows=[
            ("jour 1 · 9 h", "Fière."),
            ("jour 2 · 22 h", "Aucune nouvelle. Aucune."),
            ("jour 2 · 22 h 01", "Ouvre ton lien. Te voit au bivouac. Appelle toute la famille."),
        ]),
    ],
    legende="""Jour 1 : fière. Jour 2, 22h : aucune nouvelle. Jour 2, 22h01 : elle ouvre ton lien, te voit au bivouac, et appelle toute la famille pour raconter. 😅

Avec ta page, elle a des nouvelles sans attendre ton message.

Envoie ce post à ta mère. Elle se reconnaîtra.""",
    tags="#roadtrip #humour #famille #maman",
))

P(dict(
    id=14, date=d("2026-11-14"), heure="12h15", slug="tes-photos-360",
    titre="Tes photos 360°, là où tu les as prises.", cible="toutes les cibles", sujet="photos et photos 360° sur la page",
    objectif="envie, enregistrer",
    slides=[
        S("photo", img="station360", title=["Tes photos 360°,", "là où tu les as prises."], swipe="glisse →"),
        S("widget", bg="paper", title=["Ils glissent", "pour explorer."], sub="Tes photos, classiques ou 360°, sur ta page.", cap="F_photos"),
    ],
    legende="""Une photo 360°, c'est tout le décor d'un coup : la station, les autres voitures, le ciel.

Sur ta page, tes photos (classiques ou 360°) apparaissent là où tu les as prises. Ceux qui te suivent glissent du doigt pour regarder autour.""",
    tags="#roadtrip #photo360 #raid #voyage",
))

P(dict(
    id=15, date=d("2026-11-17"), heure="19h", slug="colle-ton-qr-code",
    titre="Colle ton QR code. Ils scannent, ils suivent.", cible="raid / rallye", sujet="visuels QR prêts à imprimer",
    objectif="enregistrer",
    slides=[
        S("photo", img="village", title=["Entre deux stickers,", "ton QR code."], sub="Ils scannent, ils suivent."),
        S("type", bg="paper", align="center", title=["Prêts à imprimer", "dans ton espace."], bullets=[
            "Un autocollant carré, pour la vitre arrière",
            "Un autocollant rond, pour la glacière ou l'ordi",
            "Une story Instagram satellite avec ta trace",
        ]),
    ],
    legende="""Sur ta voiture, il y a les stickers de tes sponsors. Ajoute ton QR code.

Dans ton espace, tu trouves des visuels prêts à imprimer : un autocollant carré, un autocollant rond, et une story Instagram satellite avec ta trace. Ceux qui croisent ta voiture scannent, et ils te suivent.""",
    tags="#raid #rallye #roadtrip #stickers",
))

P(dict(
    id=16, date=d("2026-11-19"), heure="19h", slug="combien-tas-roule-aujourdhui",
    titre="Combien t'as roulé aujourd'hui ?", cible="road trip, raid / rallye", sujet="tableau de bord et profil d'altitude",
    objectif="enregistrer",
    slides=[
        S("widget", bg="red", title=["Combien t'as roulé", "aujourd'hui ?"], sub="Distance, vitesse, altitude, dénivelé, batterie.", cap="D_tableau"),
        S("widget", title=["Et chaque montée,", "chaque descente."], sub="Le profil d'altitude de ta journée.", cap="D_profil"),
    ],
    legende="""Le soir, la question tombe toujours : « On a fait combien aujourd'hui ? »

Sur ta page, le tableau de bord répond : distance, vitesse, altitude, dénivelé, temps au volant, batterie du téléphone. Et le profil d'altitude de la journée, montée après montée.

Pour toi, c'est le souvenir. Pour eux, c'est la preuve que tu avances.""",
    tags="#roadtrip #raid #rallye #stats",
))

P(dict(
    id=17, date=d("2026-11-21"), heure="12h15", slug="on-ne-voit-jamais-ta-carte-bancaire",
    titre="On ne voit jamais ta carte bancaire.", cible="toutes les cibles", sujet="paiement sécurisé par Stripe",
    objectif="lever un frein à l'achat",
    slides=[
        S("type", bg="ink", align="center", title=["On ne voit jamais", "ta carte bancaire."], bullets=[
            "Tu paies sur la page de Stripe : ton numéro n'est jamais sur nos serveurs",
            "Ta banque peut te demander de valider dans son appli",
            "15 €, une fois. Rien qui se renouvelle tout seul",
        ]),
    ],
    legende="""On ne voit jamais ta carte bancaire. 🔒

Le paiement de ton road trip passe par Stripe. Tu tapes ta carte sur leur page : ton numéro ne passe jamais par nos serveurs. De notre côté, on reçoit une seule info : ton road trip est payé.

15 € par road trip, une seule fois. Pas d'abonnement.

Une question sur le paiement ? Écris-nous, on répond à tout.""",
    tags="#roadtrip #paiementsecurise #voyage #raid",
))

P(dict(
    id=18, date=d("2026-11-24"), heure="19h", slug="un-mot-lu-au-bivouac",
    titre="Un mot de chez toi, lu au bivouac.", cible="proches, raid / rallye", sujet="mur d'encouragements",
    objectif="partager aux proches",
    slides=[
        S("widget", title=["Un mot de chez toi,", "lu au bivouac."], sub="Sans créer de compte : un prénom, un message, envoyer.", cap="D_mur", expill=False),
    ],
    legende="""Le soir au bivouac, il y a un moment qu'on attend : lire les messages de ceux qui suivent.

Sur ta page, le mur d'encouragements permet à tes proches de te laisser un mot, sans créer de compte. Un prénom, un message, envoyer. Toi, tu les lis quand ça capte.

Envoie ce post à ceux qui vont t'écrire.""",
    tags="#raid #rallye #famille #roadtrip",
))

P(dict(
    id=19, date=d("2026-11-28"), heure="12h15", slug="pret-au-depart",
    titre="Prêt au départ : le guide en 8 étapes.", cible="raid / rallye, road trip", sujet="guide « Prêt au départ » et bouton « Je pars »",
    objectif="enregistrer",
    slides=[
        S("type", bg="paper", align="center", cols=True, kicker="dans ton espace · prêt au départ", title=["8 étapes,", "et tu pars."], items=[
            ("1", "Ton voyage", None), ("2", "Ton équipage", None), ("3", "Ton véhicule", None), ("4", "Ton itinéraire", None),
            ("5", "Le suivi GPS", None), ("6", "Le partage", None), ("7", "Sponsors et cagnotte", None), ("8", "La check-list du départ", None),
        ]),
        S("type", bg="red", align="center", title=["Tout est prêt ?", "Appuie sur « Je pars »."],
          sub="Tes proches reçoivent l'e-mail « C'est parti »."),
    ],
    legende="""La veille du départ, tout le monde a la même question : on n'a rien oublié ?

Dans ton espace, le guide « Prêt au départ » te prend par la main en 8 étapes : ton voyage, ton équipage, ton véhicule, ton itinéraire, le suivi GPS, le partage, sponsors et cagnotte, et la check-list du départ.

La check-list se termine par un bouton : « Je pars ». Tes proches reçoivent l'e-mail « C'est parti ».

Enregistre ce post pour la veille du départ.""",
    tags="#raid #rallye #roadtrip #preparation",
))

# ───────────── décembre ─────────────

P(dict(
    id=20, date=d("2026-12-01"), heure="19h", slug="le-resume-du-soir",
    titre="Chaque soir, ta journée arrive chez eux.", cible="proches", sujet="résumé du soir par e-mail",
    objectif="partager aux proches",
    slides=[
        S("type", bg="ink", align="center", kicker="chaque soir, par e-mail", title=["Même pas besoin", "d'ouvrir la page."],
          bullets=["Les kilomètres du jour", "L'altitude", "Les photos et les étapes", "Ton mot du carnet"]),
    ],
    legende="""Ta grand-mère n'ouvrira peut-être jamais ta page. Ce n'est pas grave.

Chaque soir, tes proches reçoivent le résumé de ta journée par e-mail : les kilomètres, l'altitude, les photos, les étapes et ton mot du carnet. Ils n'ont rien à faire, ça arrive tout seul.

Et le jour du départ, ils reçoivent l'e-mail « C'est parti ».""",
    tags="#famille #roadtrip #voyage #grandsparents",
))

P(dict(
    id=21, date=d("2026-12-03"), heure="19h", slug="faq",
    titre="FAQ : tu te demandes…", cible="toutes les cibles", sujet="questions fréquentes",
    objectif="enregistrer, commentaires",
    slides=[
        S("type", bg="red", title=["FAQ", "Tu te demandes…"], red=[], swipe="glisse →", align="center"),
        S("type", bg="paper", align="center", items=[
            ("?", "Mes proches doivent installer une appli ?", "Non. Ils ouvrent ton lien, sans compte, sur téléphone ou ordinateur."),
            ("?", "Il faut acheter un boîtier GPS ?", "Non. Ton téléphone suffit, avec l'appli gratuite Traccar Client. Un boîtier compatible marche aussi."),
            ("?", "Et sans réseau ?", "Tout est gardé en mémoire et envoyé dès que ça capte."),
        ]),
        S("type", bg="paper", align="center", items=[
            ("?", "Ça sert à s'orienter, ou en cas de pépin ?", "Non. Ce n'est ni un outil de navigation, ni un outil de sécurité. C'est fait pour partager ton voyage."),
            ("?", "Je peux arrêter quand je veux ?", "Oui : tu coupes le suivi ou tu effaces ta trace à tout moment."),
            ("?", "Combien ça coûte ?", "15 € par road trip, une fois. Gratuit pour ceux qui suivent."),
        ]),
    ],
    legende="""Les questions qu'on nous pose le plus, en un carrousel.

Une autre question ? Pose-la en commentaire, on répond à tout. La FAQ est aussi dans nos stories à la une.

trophytracker sert à partager ton voyage avec ceux que tu choisis. Ce n'est ni un outil de navigation, ni un outil de sécurité ou de secours.""",
    tags="#roadtrip #raid #rallye #voyage",
))

P(dict(
    id=22, date=d("2026-12-05"), heure="12h15", slug="le-bingo-du-rallye",
    titre="Le bingo du rallye.", cible="raid / rallye, entre amis", sujet="jeu, engagement",
    objectif="partager en story, taguer",
    slides=[
        S("bingo", title=["Le bingo du rallye"], red=[], cells=[
            "Ensablés dès le premier jour", "Même playlist depuis 600 km", "Zéro réseau",
            "Le chargeur oublié", "Tes proches te suivent en direct", "Pique-nique sur un parking",
            "Une crevaison", "Détour imprévu", "Quelqu'un dort à l'arrière"],
          mono="capture · coche · partage en story · tague @trophytracker.fr"),
    ],
    legende="""Le bingo du rallye : combien de cases tu coches ? 🎯

Fais une capture, coche tes cases et partage-la en story en taguant @trophytracker.fr. On repartage les meilleures.

(La case du milieu, on te la donne.)""",
    tags="#raid #rallye #roadtrip #humour",
))

P(dict(
    id=23, date=d("2026-12-08"), heure="19h", slug="tes-etapes-cest-toi",
    titre="Tes étapes, c'est toi qui les crées.", cible="road trip, raid / rallye", sujet="étapes, import GPX, détection des nuits",
    objectif="lever le « je n'ai pas d'itinéraire »",
    slides=[
        S("widget", title=["Tes étapes,", "c'est toi qui les crées."], sub="Un bivouac, un coup de cœur, une pause.", cap="D_etapes"),
        S("type", bg="paper", align="center", title=["Pas d'itinéraire ?", "Pas grave."], bullets=[
            "Tu as un fichier GPX ? Importe-le",
            "Sinon, ta trace s'écrit en roulant",
            "Les nuits et les arrêts sont détectés tout seuls",
        ]),
    ],
    legende="""Pas besoin de tout prévoir.

Tu as un itinéraire en GPX ? Importe-le. Tu n'en as pas ? Ta trace s'écrit en roulant. Les nuits et les arrêts sont détectés tout seuls, et tu ajoutes tes étapes quand tu veux : un bivouac, un coup de cœur, une pause.

Ton voyage, à ton rythme.""",
    tags="#roadtrip #raid #gpx #voyage",
))

P(dict(
    id=24, date=d("2026-12-10"), heure="19h", slug="concours-gagne-ton-road-trip",
    titre="Concours : ton prochain road trip, on te l'offre.", cible="toutes les cibles", sujet="concours (code d'accès offert)",
    objectif="abonnés, commentaires",
    remarque="Tirage au sort le vendredi 18/12 parmi les participations complètes, résultat en story. Le gagnant reçoit un code d'accès TT-XXXX-XXXX.",
    slides=[
        S("photo", img="bivouac", pos="50% 60%", pill="concours", title=["Ton prochain road trip,", "on te l'offre."], swipe="glisse →"),
        S("type", bg="paper", align="center", kicker="pour participer", items=[
            ("1", "Abonne-toi à @trophytracker.fr", None), ("2", "Tague la personne avec qui tu pars", None), ("3", "Dis-nous en commentaire où vous partez", None)],
          mono="1 road trip à gagner · fin le 17/12 à 23h59"),
    ],
    legende="""🎁 On t'offre ton prochain road trip en direct : 1 code à gagner, valable pour un road trip complet sur trophytracker.

Pour participer :
1. Abonne-toi à @trophytracker.fr
2. Tague en commentaire la personne avec qui tu pars
3. Dis-nous où vous partez

Fin le jeudi 17 décembre à 23h59. Tirage au sort le vendredi 18 décembre parmi les participations complètes, résultat annoncé en story. Participation gratuite, sans obligation d'achat.

Ce concours n'est ni organisé ni parrainé par Instagram.""",
    tags="#concours #jeuconcours #roadtrip #raid",
))

P(dict(
    id=25, date=d("2026-12-15"), heure="19h", slug="a-quatre-3-euros-75-chacun",
    titre="À quatre, 3,75 € chacun.", cible="entre amis, équipages", sujet="le prix, partagé ; pourquoi pas d'abonnement",
    objectif="partager à son équipage",
    slides=[
        S("type", bg="red", giant="3,75 €", accent="chacun, à quatre.",
          sub="15 € par road trip, payé une fois. Pas d'abonnement : tu ne pars pas tous les mois.", align="center"),
    ],
    legende="""15 € le road trip, ça fait 3,75 € chacun si vous êtes quatre. Moins qu'un café sur l'autoroute.

Et pas d'abonnement : tu ne pars pas tous les mois, alors tu ne paies pas tous les mois. Tu paies quand tu pars, une fois.

Envoie ça à ton équipage pour le partage des frais.""",
    tags="#roadtripentreamis #roadtrip #petitbudget #raid",
))

P(dict(
    id=26, date=d("2026-12-17"), heure="19h", slug="un-voyage-une-page",
    titre="Un voyage. Une page.", cible="road trip, van / camping-car, tour du monde", sujet="plusieurs road trips par compte",
    objectif="montrer que ça sert pour tous les voyages",
    slides=[
        S("screen", bg="paper", title=["Un voyage.", "Une page."], sub="Le raid de février, l'été en van, le week-end entre potes : chacun sa page, son lien, sa trace.", cap="F_ecran_carte"),
    ],
    legende="""Le raid de février, la grande boucle de l'été en van, le week-end entre potes, le tour du monde un jour peut-être.

Avec un seul compte, tu crées autant de road trips que tu veux. Chacun a sa page, son lien, ses étapes et sa trace. 15 € par road trip, payé une fois.""",
    tags="#roadtrip #vanlife #tourdumonde #voyage",
))

P(dict(
    id=27, date=d("2026-12-21"), heure="19h", slug="ton-road-trip-2027",
    titre="Ton road trip 2027, c'est lequel ?", cible="toutes les cibles", sujet="engagement, fin d'année",
    objectif="commentaires",
    slides=[
        S("bleed", cap="D_carte", pos="40% 55%", size="170%", title=["Ton road trip 2027,", "c'est lequel ?"],
          sub="1 · la grande boucle en voiture   2 · le raid ou le rallye   3 · entre potes   4 · en van"),
    ],
    legende="""Ton road trip 2027, c'est lequel ?

1. La grande boucle en voiture
2. Le raid ou le rallye
3. Le road trip entre potes
4. En van ou en camping-car

Réponds en commentaire avec ton chiffre (et ta destination si tu la connais déjà). Bonnes fêtes ! 🎄""",
    tags="#roadtrip #raid #voyage #2027",
))

P(dict(
    id=28, date=d("2027-01-06"), heure="19h", slug="qui-est-derriere-trophytracker",
    titre="Qui est derrière trophytracker ?", cible="toutes les cibles", sujet="coulisses, confiance",
    objectif="créer du lien, messages privés",
    slides=[
        S("photo", img="piquenique", pos="50% 85%", title=["Qui est derrière", "trophytracker ?"], sub="Une personne. Je développe l'appli, je la teste sur la route, et je réponds moi-même à chaque message."),
    ],
    legende="""Derrière trophytracker, il n'y a pas une grosse boîte. Il y a moi.

Je développe l'appli, je la teste sur la route, et c'est moi qui te réponds quand tu écris au compte. Je l'ai faite pour une raison simple : un road trip mérite mieux qu'un « je t'écris ce soir ». Ceux qu'on aime devraient pouvoir le vivre avec nous, en direct.

Une question, une idée, un bug ? Écris-moi en message, je réponds à tout.""",
    tags="#roadtrip #coulisses #startup #voyage",
))

# ───────────── modèles sans date (à sortir quand l'occasion se présente) ─────────────

P(dict(
    id=29, date=None, heure="19h", slug="modele-road-trip-de-la-semaine",
    titre="MODÈLE · Le road trip de la semaine", cible="toutes les cibles", sujet="repartage d'un vrai voyageur",
    objectif="preuve sociale réelle",
    remarque="[À COMPLÉTER] avec un vrai voyageur qui a partagé sa page et accepté d'être mis en avant. Remplacer la 2ᵉ slide par une vraie capture de sa page.",
    slides=[
        S("type", kicker="road trip de la semaine · n°[X]", title=["[Nom du road trip]"], red=[], sub="[d'où] → [où] · [voiture / raid / entre potes / van]", align="bottom"),
        S("type", bg="paper", kicker="sa réponse", title=["« [Pourquoi ce voyage ? En une phrase, ses mots] »"], red=[], align="center"),
    ],
    legende="""Cette semaine, on part avec [@compte] : [d'où → où, en quoi, un détail qu'il t'a donné].

[Une phrase sur son voyage, avec ses mots.]

Tu veux être le prochain road trip de la semaine ? Partage ta page ou ton replay en story et tague @trophytracker.fr.""",
    tags="#roadtrip #roadtripdelasemaine #voyage #trophytracker",
))

P(dict(
    id=30, date=None, heure="19h", slug="modele-avis-reel",
    titre="MODÈLE · Un vrai retour", cible="toutes les cibles", sujet="citation réelle d'un voyageur ou d'un proche",
    objectif="preuve sociale réelle",
    remarque="[À COMPLÉTER] uniquement avec une citation réelle, avec l'accord de la personne. Jamais de faux avis.",
    slides=[
        S("type", bg="paper", kicker="retour réel", title=["« [CITATION RÉELLE] »"], red=[], sub="— [qui : ex. la mère d'un voyageur, un sponsor]", align="center"),
    ],
    legende="""[Contexte en une phrase : qui, quel voyage.]

« [CITATION RÉELLE] »

Envoie ce post à la personne qui va te suivre pendant ton prochain road trip.""",
    tags="#roadtrip #voyage #avis #famille",
))

P(dict(
    id=31, date=None, heure="19h", slug="modele-nouveau-cest-en-ligne",
    titre="MODÈLE · Nouveau : c'est en ligne", cible="toutes les cibles", sujet="annonce d'une nouvelle fonctionnalité",
    objectif="montrer que l'appli vit",
    remarque="[À COMPLÉTER] uniquement pour une fonctionnalité réellement en ligne. Ajouter une vraie capture si possible.",
    slides=[
        S("type", bg="red", pill="nouveau · en ligne", title=["[Nom de la fonctionnalité]"], red=[], sub="Déjà dans ta page.", align="center"),
    ],
    legende="""Nouveau sur trophytracker : [fonctionnalité].

[Une phrase : à quoi ça sert, pour le voyageur ou pour ceux qui le suivent.]

C'est déjà dans ta page, rien à faire de ton côté. Lien en bio.""",
    tags="#roadtrip #nouveaute #voyage #raid",
))

for _p in POSTS:
    _p["dossier"] = f"{_p['date'].isoformat() if _p['date'] else 'modele'}_{_p['slug']}"
    _n = len(_p["slides"])
    _p["format"] = "post simple" if _n == 1 else f"carrousel {_n} visuels"
    assert len(_p["tags"].split()) <= 4, _p["id"]
