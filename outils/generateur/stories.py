"""Stories (refonte du 16/10/2026). Mêmes gabarits que les posts (render.py), au format 1080×1920.
Chaque écran : S(gabarit, …, label="1/3" ou une heure, sticker="…" ou absent). Les stickers se posent dans Instagram :
sur l'image, on laisse seulement l'emplacement. Jamais de moto. Exemple : la page j4l-club."""
from common import d
from posts import S

EX = "https://trophytracker.fr/road-trip/j4l-club"
LIEN_EX = f"sticker LIEN → {EX} (texte du sticker : « voir l'exemple »)"
LIEN_SITE = "sticker LIEN → https://trophytracker.fr (texte du sticker : « trophytracker.fr »)"

STORIES = []
A = STORIES.append

# ───────────── stories à la une (permanentes) ─────────────

A(dict(id=1, date=None, permanent=True, heure="à mettre en place le 17/10", slug="a-la-une-cest-quoi", titre="À la une « trophytracker » (c'est quoi)",
       cible="toutes les cibles", remarque="Couverture : symbole du logo sur fond encre.",
       ecrans=[
           S("photo", label="1/3", img="dunes", pos="40% 60%", kicker="trophytracker", title=["Ton road trip,", "en direct."], sub="Tu roules. Ceux que tu invites te suivent."),
           S("screen", label="2/3", bg="paper", title=["Une page privée,", "rien qu'à toi."], sub="Sans compte et sans appli pour ceux qui suivent.", cap="D_ecran_carte"),
           S("type", label="3/3", bg="red", title=["Va voir", "un vrai road trip."], red=[], sub="La page d'exemple, ouverte comme tes proches l'ouvriraient.", sticker=LIEN_EX),
       ]))

A(dict(id=2, date=None, permanent=True, heure="à mettre en place le 17/10", slug="a-la-une-comment-ca-marche", titre="À la une « Comment ça marche »",
       cible="toutes les cibles", remarque="Couverture : « 1·2·3 » en DM Mono rouge.",
       ecrans=[
           S("type", label="1/4", giant="5 min", accent="pour tout préparer.", sub="Zéro prise de tête."),
           S("photo", label="2/4", img="piquenique", num="1", title=["Tu crées ta page."], red=[], sub="Un nom, une photo, tes compagnons, d'où à où, quand. L'itinéraire est facultatif."),
           S("type", label="3/4", bg="paper", num="2", title=["Tu scannes", "un QR code."], sub="Avec l'appli gratuite Traccar Client (Android, iPhone), ou un boîtier GPS compatible."),
           S("screen", label="4/4", num="3", title=["Tu envoies ton lien.", "Et tu pars."], cap="F_ecran_haut", sticker=LIEN_SITE),
       ]))

A(dict(id=3, date=None, permanent=True, heure="à mettre en place le 17/10", slug="a-la-une-carnet-ia", titre="À la une « Carnet IA »",
       cible="toutes les cibles", remarque="Couverture : bouton micro rouge.",
       ecrans=[
           S("photo", label="1/3", img="feu", title=["Le soir, tu racontes.", "L'IA écrit."]),
           S("type", label="2/3", bg="paper", items=[("1", "Tu racontes au micro.", "Ou tu écris."), ("2", "L'IA fait la page.", "Tes anecdotes, sans les « euh », avec km et altitude."), ("3", "Tu relis, tu publies.", None)]),
           S("widget", label="3/3", title=["Sans rien inventer."], red=[], cap="D_journal", sticker=LIEN_EX),
       ]))

A(dict(id=4, date=None, permanent=True, heure="à mettre en place le 17/10", slug="a-la-une-proches", titre="À la une « Proches »",
       cible="les proches", remarque="Story à envoyer directement aux proches. Couverture : un petit cœur papier sur fond rouge.",
       ecrans=[
           S("type", label="1/3", bg="red", title=["Quelqu'un que tu aimes", "part en road trip ?"], red=[], sub="Voilà comment le suivre."),
           S("widget", label="2/3", bg="paper", title=["Tu ouvres son lien.", "C'est tout."], sub="Pas de compte, pas d'appli. La carte, la météo là-bas, ses photos.", cap="D_meteo"),
           S("type", label="3/3", title=["Et chaque soir,", "le résumé par e-mail."], sub="Tu peux aussi lui laisser un mot sur son mur d'encouragements.", sticker=LIEN_EX),
       ]))

A(dict(id=5, date=None, permanent=True, heure="à mettre en place le 17/10", slug="a-la-une-raid-et-sponsors", titre="À la une « Raid & sponsors »",
       cible="raid / rallye", remarque="Couverture : drapeau à damier stylisé ambre (pas de logo d'événement).",
       ecrans=[
           S("photo", label="1/3", img="camp", title=["Raid, rallye :", "tout l'équipage en direct."]),
           S("widget", label="2/3", title=["Tes sponsors,", "à côté de la carte."], sub="Et ta cagnotte sur la même page.", cap="F_sponsors"),
           S("type", label="3/3", bg="paper", title=["À l'arrivée :"], red=[], bullets=["Les statistiques de visibilité", "Un rapport PDF pour tes sponsors", "Des autocollants QR pour la voiture"], sticker=LIEN_SITE),
       ]))

A(dict(id=6, date=None, permanent=True, heure="à mettre en place le 17/10", slug="a-la-une-tarif", titre="À la une « Tarif »",
       cible="toutes les cibles", remarque="Un seul prix. Couverture : « 15 € » papier sur fond rouge.",
       ecrans=[
           S("type", label="1/1", bg="paper", giant="15 €", accent="par road trip.", bullets=["Payé une seule fois", "Pas d'abonnement", "Gratuit pour ceux qui te suivent"], sticker=LIEN_SITE),
       ]))

A(dict(id=7, date=None, permanent=True, heure="à mettre en place le 17/10", slug="a-la-une-faq", titre="À la une « FAQ »",
       cible="toutes les cibles", remarque="L'écran 2 (pas un outil de sécurité ni de navigation) est à garder en permanence. Les réponses de la boîte à questions (S17) viennent enrichir cette story. Couverture : « ? » rouge.",
       ecrans=[
           S("type", label="1/2", bg="paper", items=[("?", "Mes proches doivent installer une appli ?", "Non : un lien, sans compte."), ("?", "Il faut un boîtier GPS ?", "Non : ton téléphone et Traccar Client (gratuit)."), ("?", "Et sans réseau ?", "Tout est gardé et envoyé dès que ça capte.")]),
           S("type", label="2/2", items=[("?", "Ça sert à s'orienter, ou en cas de pépin ?", "Non. Ce n'est ni un outil de navigation, ni un outil de sécurité. C'est fait pour partager ton voyage."), ("?", "Qui voit ma page ?", "Ceux qui ont ton lien. Jamais sur Google.")]),
       ]))

# ───────────── stories datées ─────────────

A(dict(id=8, date=d("2026-10-17"), permanent=False, heure="12h → 19h05", slug="relance-du-compte", titre="Relance du compte : « Ton road trip, en direct. »",
       cible="toutes les cibles", remarque="Le jour du premier post. Ne pas expliquer le changement : on présente, c'est tout. Partage aussi depuis ton compte perso.",
       ecrans=[
           S("type", label="12h", title=["Ton prochain road trip,", "c'est…"], sticker="sticker SONDAGE, 4 options : « En voiture » · « Raid ou rallye » · « Entre amis » · « En van »"),
           S("bleed", label="17h", cap="D_relief", pos="45% 75%", size="320%", title=["Va voir une page", "en direct."], sticker=LIEN_EX),
           S("type", label="19h05", bg="red", title=["Ton road trip,", "en direct."], red=[], sub="Nouveau post ↓", sticker="repartage du post P01 (bouton avion › « Ajouter à la story »)"),
       ]))

A(dict(id=9, date=d("2026-10-21"), permanent=False, heure="18h", slug="ca-capte-la-bas", titre="Ça capte, là-bas ?",
       cible="raid / rallye", remarque="Le jour du post P04.",
       ecrans=[
           S("photo", label="1/2", img="chameau", title=["Le pire endroit sans réseau", "où tu as roulé ?"], red=[], sticker="sticker QUESTION « Raconte »"),
           S("widget", label="2/2", bg="ink", title=["Sur ta page,", "c'est prévu."], sub="« Pas de réseau, c'est normal. »", cap="N_ecran_haut", crop=(.655, .955), sticker="repartage du post P04"),
       ]))

A(dict(id=10, date=d("2026-10-23"), permanent=False, heure="12h", slug="vacances-de-la-toussaint", titre="Vacances de la Toussaint : tu pars ?",
       cible="road trip", remarque="Début des vacances scolaires.",
       ecrans=[
           S("type", label="1/1", bg="red", kicker="vacances de la toussaint", title=["Tu pars ?"], red=[], sticker="sticker SONDAGE : « Oui, je roule » / « Non, canapé »"),
       ]))

A(dict(id=11, date=d("2026-10-30"), permanent=False, heure="18h", slug="raid-ta-galere-sponsors", titre="Raid : ta galère n°1 avec les sponsors",
       cible="raid / rallye", remarque="Le jour du post P08. Les réponses nourrissent le post P12 (5 phrases pour convaincre un sponsor).",
       ecrans=[
           S("photo", label="1/2", img="sponsor", title=["Ta galère n°1", "avec les sponsors ?"], sticker="sticker QUESTION « Dis-nous »"),
           S("type", label="2/2", bg="paper", title=["Sur ta page,", "ils ont leur vitrine."], sub="Logo à côté de la carte, et un rapport PDF à l'arrivée.", sticker="repartage du post P08"),
       ]))

A(dict(id=12, date=d("2026-11-05"), permanent=False, heure="18h", slug="replay-3d", titre="Le replay 3D en story",
       cible="toutes les cibles", remarque="Le jour du post P10. [À COMPLÉTER] si possible : un vrai export vidéo story du replay (Exporter en vidéo › story) à la place de l'écran 1.",
       ecrans=[
           S("bleed", label="1/2", cap="D_relief", pos="45% 75%", size="320%", title=["Ton voyage,", "rejoué en 3D."]),
           S("type", label="2/2", title=["En vidéo story,", "prête à poster."], sticker="repartage du post P10"),
       ]))

A(dict(id=13, date=d("2026-11-12"), permanent=False, heure="18h", slug="proches-tu-stresses", titre="Proches : tu stresses quand ils partent ?",
       cible="proches", remarque="Le jour du post P13.",
       ecrans=[
           S("timeline", label="1/2", kicker="toi, quand ils partent", rows=[("jour 1", "Ça va."), ("jour 2, 22 h", "Pas de nouvelles…")], sticker="sticker CURSEUR « Ton niveau de stress » 😬"),
           S("type", label="2/2", bg="red", title=["Avec leur lien,", "tu vois où ils en sont."], red=[], sticker="repartage du post P13"),
       ]))

A(dict(id=14, date=d("2026-11-24"), permanent=False, heure="18h", slug="mur-dencouragements", titre="Le mur d'encouragements",
       cible="proches, raid / rallye", remarque="Le jour du post P18.",
       ecrans=[
           S("widget", label="1/1", title=["Un mot de chez toi,", "lu au bivouac."], cap="D_mur", expill=False, sticker="sticker QUESTION « Le message que tu aimerais recevoir au bivouac »"),
       ]))

A(dict(id=15, date=d("2026-12-10"), permanent=False, heure="12h → 19h", slug="concours", titre="Concours (stories d'accompagnement)",
       cible="toutes les cibles", remarque="Le jour du post P25, puis rappel le 17/12 à 18h (écran 2). Résultat du tirage le 18/12 en story.",
       ecrans=[
           S("photo", label="10/12", img="bivouac", pos="50% 60%", pill="concours", title=["Ton prochain road trip,", "on te l'offre."], sticker="repartage du post P25"),
           S("type", label="17/12", bg="red", title=["Dernier jour", "pour participer."], red=[], sub="Fin ce soir à 23h59.", sticker="sticker COMPTE À REBOURS « Fin du concours » (17/12, 23h59)"),
       ]))

A(dict(id=16, date=d("2026-12-21"), permanent=False, heure="18h", slug="noel", titre="Noël : tes road trips 2027",
       cible="toutes les cibles", remarque="Le jour du post P28.",
       ecrans=[
           S("type", label="1/1", bg="red", kicker="2027", title=["Ton road trip 2027,", "c'est où ?"], red=[], sticker="sticker QUESTION « Ta destination »"),
       ]))

# ───────────── stories du quotidien (modèles) ─────────────

A(dict(id=17, date=None, permanent=False, heure="1 fois par semaine (le jeudi)", slug="quotidien-boite-a-questions", titre="Quotidien · Boîte à questions",
       cible="toutes les cibles", remarque="Les réponses vont ensuite dans la story à la une « FAQ » (S07). Répondre à chacune en story, une par écran.",
       ecrans=[S("type", label="1/1", title=["Une question", "sur trophytracker ?"], sub="Pose-la ici, on répond à tout.", sticker="sticker QUESTION « Ta question »")]))

A(dict(id=18, date=None, permanent=False, heure="à chaque fois qu'un voyageur tague le compte", slug="quotidien-repartage-voyageur", titre="Quotidien · Repartage d'un voyageur",
       cible="toutes les cibles", remarque="[À COMPLÉTER] à chaque fois. Seulement les stories où le compte est tagué (donc publiques). Ne jamais repartager une page privée sans accord.",
       ecrans=[S("type", label="1/1", bg="red", title=["Bonne route", "[@compte] !"], red=[], sticker="repartage de sa story + sticker MENTION du voyageur")]))

A(dict(id=19, date=None, permanent=False, heure="de temps en temps", slug="quotidien-coulisses", titre="Quotidien · Coulisses",
       cible="toutes les cibles", remarque="[À COMPLÉTER] : une vraie photo de ton écran et une vraie amélioration en cours. Jamais annoncer une fonctionnalité qui n'existe pas encore comme si elle était là.",
       ecrans=[S("type", label="1/1", kicker="coulisses · [heure]", title=["Ce soir, je travaille sur", "[amélioration réelle]."], sticker="sticker SONDAGE facultatif : « Hâte ! » / « Ça sert à quoi ? »")]))

A(dict(id=20, date=None, permanent=False, heure="1 fois par semaine (le mardi)", slug="quotidien-fonction-de-la-semaine", titre="Quotidien · La fonction de la semaine",
       cible="toutes les cibles", remarque="Faire tourner : météo sur place · nuits floutées · profil d'altitude · import GPX · photos 360° · mur d'encouragements · résumé du soir · couper / effacer sa trace · plusieurs road trips par compte · connexion par code reçu par e-mail.",
       ecrans=[
           S("type", label="1/2", bg="paper", kicker="la fonction de la semaine", title=["[Nom de la fonction]"], red=[]),
           S("type", label="2/2", title=["[À quoi elle sert,", "en une phrase]"], sticker="sticker QUIZ facultatif (« Tu savais ? » Oui / Non) + " + LIEN_SITE),
       ]))

A(dict(id=21, date=None, permanent=False, heure="chaque vendredi vers 17h", slug="quotidien-ce-week-end-tu-roules", titre="Quotidien · Ce week-end, tu roules ?",
       cible="toutes les cibles", remarque="Rendez-vous du vendredi.",
       ecrans=[S("photo", label="1/1", img="bivouac", pos="50% 60%", title=["Ce week-end,", "tu roules ?"], sticker="sticker SONDAGE : « Oui, ça roule » / « Canapé »")]))

A(dict(id=22, date=None, permanent=False, heure="le jour de chaque post", slug="quotidien-repartage-dun-post", titre="Quotidien · Repartage du post du jour",
       cible="toutes les cibles", remarque="Habillage générique pour chaque nouveau post.",
       ecrans=[S("type", label="1/1", align="top", title=["Nouveau post ↓"], red=[], sticker="repartage du post (bouton avion › « Ajouter à la story »)")]))

for _s in STORIES:
    _s["dossier"] = _s["date"].isoformat() if _s["date"] else ("a-la-une" if _s["permanent"] else "modele")
    _s["dossier"] += "_" + _s["slug"]
