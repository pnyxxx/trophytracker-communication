"""Écrit les post.txt et story.txt à partir de posts.py et stories.py.
Usage : python3 main.py ../../publications-instagram"""
import os, sys
from common import date_fr
from posts import POSTS
from stories import STORIES
from assets import PHOTOS, CAPS

OUT = sys.argv[1]
SEP = "━━━━━━━━"
FOND = {"ink": "fond encre avec halo rouge", "paper": "fond papier", "red": "fond rouge trophytracker", "dark": "fond encre"}


def w(path, txt):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(txt.rstrip() + "\n")


def texte(s):
    """Le texte tel qu'il apparaît sur l'image, ligne par ligne."""
    L = []
    for k in ("pill", "kicker"):
        if s.get(k): L.append(f"[{s[k]}]")
    if s.get("num"): L.append(s["num"])
    if s.get("giant"): L.append(s["giant"])
    if s.get("accent"): L.append(s["accent"])
    if s.get("msgs"): L += [f"« {t} »" + (f" ({m})" if m else "") for _, t, m in s["msgs"]]
    if s.get("title"):
        red = s.get("red")
        red = [len(s["title"]) - 1] if red is None and len(s["title"]) > 1 else (red or [])
        L += [t + (" (en rouge)" if i in red else "") for i, t in enumerate(s["title"])]
    if s.get("rows"): L += [f"{h} : {t}" for h, t in s["rows"]]
    sub = s.get("sub")
    if sub: L += [sub] if isinstance(sub, str) else sub
    for n, h, b in s.get("items", []): L.append((f"{n} " if n == "?" else f"{n}. ") + h + (f" ({b})" if b else ""))
    L += [f"• {b}" for b in s.get("bullets", [])]
    if s.get("cells"): L.append("Grille : " + " · ".join(s["cells"]))
    for k in ("mono", "swipe"):
        if s.get(k): L.append(s[k])
    return "\n".join(L)


def visuel(s):
    t = s["t"]
    if t == "photo":
        v = f"Photo plein cadre (page j4l-club) : {PHOTOS[s['img']]['d']}, dégradé encre pour le texte."
        if s.get("card"): v += f" Par-dessus, en haut : capture réelle, {CAPS[s['card']['cap']]['d']}."
        return v
    if t == "bleed": return f"Capture en plein cadre : {CAPS[s['cap']]['d']}, dégradé encre en bas pour le titre."
    if t == "screen": return f"{FOND[s.get('bg', 'ink')].capitalize()}, téléphone avec une capture : {CAPS[s['cap']]['d']}."
    if t == "widget": return f"{FOND[s.get('bg', 'ink')].capitalize()}, capture de la page : {CAPS[s['cap']]['d']}."
    if t == "chat": return "Fond encre, bulles de messages (envoyé en rouge, réponse en papier), titre en bas."
    if t == "timeline": return f"{FOND[s.get('bg', 'paper')].capitalize()}, chronologie verticale (heures en DM Mono, dernière ligne en rouge)."
    if t == "bingo": return "Fond papier, grille de bingo 3 × 3 en cases encre, case du milieu en rouge."
    return f"{FOND[s.get('bg', 'ink')].capitalize()}, typographie seule."


for p in POSTS:
    folder = f"{OUT}/posts/P{p['id']:02d}_{p['dossier']}"
    n = len(p["slides"])
    L = [f"P{p['id']:02d} · {p['titre'].upper()}", "",
         f"Date     : {date_fr(p['date'])} · {p['heure']}",
         f"Cible    : {p['cible']}", f"Sujet    : {p['sujet']}",
         f"Format   : {p['format']} · 4:5, PNG 2160 × 2700 · importer dans l'ordre",
         f"Objectif : {p['objectif']}"]
    if p.get("remarque"): L.append(f"Remarque : {p['remarque']}")
    L += ["", f"{SEP} VISUELS {SEP}", ""]
    for i, s in enumerate(p["slides"], 1):
        L += [f"{i}/{n}" if n > 1 else "VISUEL UNIQUE", "Texte sur l'image :", texte(s), "Visuel : " + visuel(s), ""]
    L += [f"{SEP} LÉGENDE À COPIER {SEP}", "", p["legende"].strip(), "", p["tags"]]
    w(f"{folder}/post.txt", "\n".join(L))

for s in STORIES:
    folder = f"{OUT}/stories/S{s['id']:02d}_{s['dossier']}"
    L = [f"S{s['id']:02d} · {s['titre'].upper()}", "",
         f"Date   : {'permanente (story à la une)' if s['permanent'] else date_fr(s['date'])} · {s['heure']}",
         f"Cible  : {s['cible']}",
         f"Format : {len(s['ecrans'])} écran(s) · 9:16, PNG 2160 × 3840, sans bandeau de l'interface Instagram"]
    if s.get("remarque"): L.append(f"Remarque : {s['remarque']}")
    L += ["", f"{SEP} ÉCRANS {SEP}", ""]
    for e in s["ecrans"]:
        L += [f"ÉCRAN {e['label']}", "Texte :", texte(e), "Sticker : " + e.get("sticker", "aucun"), "Visuel : " + visuel(e), ""]
    w(f"{folder}/story.txt", "\n".join(L))

print(len(POSTS), "posts,", len(STORIES), "stories")
