import datetime as dt

HANDLE = "@trophytracker.fr"
EXEMPLE = "trophytracker.fr/road-trip/exemple"

JOURS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août",
        "septembre", "octobre", "novembre", "décembre"]


def d(s):
    return dt.date.fromisoformat(s)


def date_fr(x):
    if x is None:
        return "pas de date fixe (modèle à utiliser au bon moment)"
    return f"{JOURS[x.weekday()]} {x.day}{'er' if x.day == 1 else ''} {MOIS[x.month - 1]} {x.year}"


def date_court(x):
    if x is None:
        return "—"
    return f"{JOURS[x.weekday()][:3]}. {x.day:02d}/{x.month:02d}"


# Hashtags (aucun lié à un événement précis)
H = {
    "rt": "#roadtrip #roadtripfrance #roadtripper #voyageenvoiture #carnetdevoyage #trophytracker",
    "raid": "#raid #rallye #raidaventure #rallyeraid #equipage #desert #trophytracker",
    "moto": "#moto #roadtripmoto #balademoto #motovoyage #cols #motard #trophytracker",
    "amis": "#roadtripentreamis #entrepotes #voyageentreamis #roadtrip #souvenirs #trophytracker",
    "proches": "#famille #roadtrip #voyage #nouvelles #grandsparents #trophytracker",
    "sponsors": "#sponsoring #partenariat #dossiersponsor #raid #rallye #trophytracker",
    "van": "#vanlife #vanamenage #campingcar #roadtrip #voyage #trophytracker",
    "tdm": "#tourdumonde #voyage #roadtrip #carnetdevoyage #grandvoyage #trophytracker",
    "alpes": "#routedesgrandesalpes #grandesalpes #cols #roadtrip #moto #trophytracker",
    "prix": "#roadtrip #sansabonnement #voyage #petitbudget #trophytracker",
}

CTA_FINAL = (
    "Visuel : gabarit DERNIÈRE SLIDE. Fond encre #15161A avec halo rouge en haut à droite, logo "
    "TROPHYTRACKER centré en haut, la phrase en Bricolage Grotesque, puis « trophytracker.fr · lien en bio » "
    "en DM Mono et la pastille « 15 € par road trip · sans abonnement »."
)
