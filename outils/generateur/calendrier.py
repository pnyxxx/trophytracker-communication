import datetime as dt
from common import date_court
from posts1 import POSTS as A
from posts2 import POSTS as B
from stories import STORIES
P = [p for p in A+B if p["date"]]
S = {s["date"]: s for s in STORIES if s["date"]}
def lien(p): return f"[P{p['id']:02d} · {p['titre']}](posts/P{p['id']:02d}_{p['date'].isoformat()}_{p['slug']}/post.txt)"
def lien_s(s): return f"[S{s['id']:02d} · {s['titre']}](stories/S{s['id']:02d}_{s['date'].isoformat()}_{s['slug']}/story.txt)"
semaines = {}
for p in P:
    lundi = p["date"] - dt.timedelta(days=p["date"].weekday())
    semaines.setdefault(lundi, []).append(p)
for lundi in sorted(semaines):
    fin = lundi + dt.timedelta(days=6)
    print(f"\n### Semaine du {lundi.day:02d}/{lundi.month:02d} au {fin.day:02d}/{fin.month:02d}\n")
    print("| | Date | Heure | Post | Cible | Stories du jour |\n|---|---|---|---|---|---|")
    for p in sorted(semaines[lundi], key=lambda x:(x["date"], x["heure"])):
        st = lien_s(S[p["date"]]) if p["date"] in S else "repartage du post (S27)"
        print(f"| [ ] | {date_court(p['date'])} | {p['heure']} | {lien(p)} | {p['cible']} | {st} |")
