"""Images disponibles pour les visuels.
PHOTOS : vraies photos de la page j4l-club (photos-j4l/, téléchargées depuis la page), utilisées telles quelles.
CAPS : captures de la page j4l-club (captures-j4l/, refaites par captures-j4l.mjs).
  F_ = vraie page (trace en France) · D_ = mise en scène dans les dunes · N_ = mise en scène dans les dunes, hors réseau depuis 2 h.
« d » sert à décrire le visuel dans les post.txt."""

PHOTOS = {
    "dunes": dict(f="cover.jpg", pos="45% 60%", d="la voiture de l'équipage lancée sur une piste de sable, palmiers derrière (photo de couverture de la page)"),
    "sponsor": dict(f="05_classic.jpg", pos="50% 30%", d="gros plan d'un autocollant de sponsor sur la carrosserie, une disqueuse posée au sol"),
    "piquenique": dict(f="06_classic.jpg", pos="50% 55%", d="pique-nique sur une table pliante à côté de la voiture, sur une aire de station-service"),
    "moteur": dict(f="07_classic.jpg", pos="50% 45%", d="deux paires de mains penchées sur le moteur, capot ouvert"),
    "feu": dict(f="08_classic.jpg", pos="50% 60%", d="feu de camp la nuit au bivouac, des silhouettes autour"),
    "bivouac": dict(f="09_classic.jpg", pos="50% 70%", d="la voiture au bivouac au coucher du soleil, tentes autour"),
    "camp": dict(f="10_classic.jpg", pos="50% 75%", d="le flanc de la voiture couvert d'autocollants de sponsors, le camp derrière"),
    "village": dict(f="11_classic.jpg", pos="50% 35%", d="le toit de la voiture (jerricans, roues de secours) et le camp animé derrière"),
    "pompe": dict(f="12_classic.jpg", pos="50% 60%", d="une pompe à essence isolée la nuit, un jerrican rouge au pied"),
    "chameau": dict(f="13_classic.jpg", pos="50% 70%", d="étendue de désert caillouteux sous un ciel bleu, un chameau au loin"),
    "echappement": dict(f="14_classic.jpg", pos="50% 50%", d="le pot d'échappement arraché qui pend sous la voiture"),
    "station360": dict(f="03_panorama.jpg", pos="50% 62%", d="photo 360° (vue à plat) d'une station-service pleine de voitures de rallye colorées"),
}

CAPS = {
    # vraie page j4l-club
    "F_ecran_haut": dict(f="F_ecran_haut.png", d="écran de téléphone : le haut de la vraie page j4l-club (photo de couverture, nom, carte)"),
    "F_ecran_carte": dict(f="F_ecran_carte.png", d="écran de téléphone : la carte satellite de la vraie page avec la trace en France et le tableau de bord"),
    "F_carte": dict(f="F_carte.png", d="la carte satellite de la vraie page j4l-club"),
    "F_sponsors": dict(f="F_sponsors.png", crop=(0, .56), d="la vitrine « ils soutiennent ce voyage » de la vraie page (logos des sponsors)"),
    "F_photos": dict(f="F_photos.png", crop=(0, .62), d="la galerie photos de la vraie page, avec les photos 360°"),
    "F_replay": dict(f="F_replay_bloc.png", d="le bloc « revivre en 3D » de la vraie page (Lancer le replay, Exporter en vidéo)"),
    # mise en scène dans les dunes
    "D_ecran_carte": dict(f="D_ecran_carte.png", d="écran de téléphone : la page avec la carte satellite sur les dunes, la trace et la balise en direct"),
    "D_ecran_relief": dict(f="D_ecran_relief.png", d="écran de téléphone : la page en relief 3D sur les dunes"),
    "D_ecran_haut": dict(f="D_ecran_haut.png", d="écran de téléphone : le haut de la page, pastille « en direct · à l'instant »"),
    "D_carte": dict(f="D_carte.png", d="la carte satellite sur les dunes, trace rouge et balise en direct"),
    "D_relief": dict(f="D_relief3d.png", d="la carte en relief 3D sur les dunes, trace et balise"),
    "D_meteo": dict(f="D_meteo.png", d="le bloc « Météo sur place » (vraie météo à la position, sous les dunes)"),
    "D_tableau": dict(f="D_tableau_de_bord.png", d="le tableau de bord : distance, vitesse, altitude, dénivelé, jour, temps au volant, batterie"),
    "D_profil": dict(f="D_profil_altitude.png", d="le profil d'altitude de la journée"),
    "D_etapes": dict(f="D_carnet.png", crop=(0, .25), d="le carnet de route, onglet Étapes (bivouac au pied des dunes, le bout de la piste)"),
    "D_journal": dict(f="D_carnet_journal.png", crop=(0, .37), d="le carnet de route, onglet Journal : une page de carnet écrite par l'IA (texte d'exemple)"),
    "D_mur": dict(f="D_mur.png", crop=(.71, 1), d="le mur d'encouragements : « Laisse un mot aux voyageurs, ils le liront au bivouac. »"),
    # hors réseau
    "N_ecran_haut": dict(f="N_ecran_haut.png", d="écran de téléphone : la page hors réseau, carte « Pas de réseau, c'est normal. Dernière position, il y a 2 h. »"),
    "N_ecran_carte": dict(f="N_ecran_carte.png", d="écran de téléphone : la carte, « Dernière position · il y a 2 h »"),
}
