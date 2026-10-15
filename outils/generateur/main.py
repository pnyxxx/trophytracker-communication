import os, sys
from common import date_fr
from posts1 import POSTS as A
from posts2 import POSTS as B
from stories import STORIES
from hashtags import HASHTAGS
OUT = sys.argv[1]
SEP = "━━━━━━━━"
def w(path, txt):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(txt.rstrip() + "\n")
for p in A + B:
    dt = p["date"].isoformat() if p["date"] else "modele"
    folder = f"{OUT}/posts/P{p['id']:02d}_{dt}_{p['slug']}"
    L = [f"P{p['id']:02d} · {p['titre'].upper()}", "",
         f"Date     : {date_fr(p['date'])} · {p['heure']}",
         f"Cible    : {p['cible']}", f"Sujet    : {p['sujet']}",
         f"Format   : {p['format']} · 4:5, PNG 2160 × 2700 · importer dans l'ordre",
         f"Objectif : {p['objectif']}"]
    if p.get("remarque"): L.append(f"Remarque : {p['remarque']}")
    L += ["", f"{SEP} VISUELS {SEP}", ""]
    for role, txt, vis in p["slides"]:
        L += [role, "Texte sur l'image :", txt, "Visuel : " + vis, ""]
    L += [f"{SEP} LÉGENDE À COPIER {SEP}", "", p["legende"].strip(), "", HASHTAGS[p["id"]]]
    w(f"{folder}/post.txt", "\n".join(L))
for s in STORIES:
    dt = s["date"].isoformat() if s["date"] else ("a-la-une" if s["permanent"] else "modele")
    folder = f"{OUT}/stories/S{s['id']:02d}_{dt}_{s['slug']}"
    L = [f"S{s['id']:02d} · {s['titre'].upper()}", "",
         f"Date   : {'permanente (story à la une)' if s['permanent'] else date_fr(s['date'])} · {s['heure']}",
         f"Cible  : {s['cible']}",
         f"Format : {len(s['ecrans'])} écran(s) · 9:16, PNG 2160 × 3840, sans bandeau de l'interface Instagram"]
    if s.get("remarque"): L.append(f"Remarque : {s['remarque']}")
    L += ["", f"{SEP} ÉCRANS {SEP}", ""]
    for lab, txt, st, vis in s["ecrans"]:
        L += [f"ÉCRAN {lab}", "Texte : " + txt, "Sticker : " + st, "Visuel : " + vis, ""]
    w(f"{folder}/story.txt", "\n".join(L))
print(len(A+B), "posts,", len(STORIES), "stories")
