import datetime as dt

HANDLE = "@trophytracker.fr"
EXEMPLE = "trophytracker.fr/road-trip/j4l-club"

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
