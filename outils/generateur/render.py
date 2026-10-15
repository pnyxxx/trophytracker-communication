"""Construit une page HTML par slide (posts 1080×1350, stories 1080×1920) à partir des données des posts et stories,
dans la charte du site. Les captures réelles de la page d'exemple sont dans captures/ (captures.mjs les refait).
Sortie : .html/... + jobs.json (liste {html, png, w, h}) pour shoot.mjs."""
import html, json, os, re, sys
from posts1 import POSTS as A
from posts2 import POSTS as B
from stories import STORIES

ROOT = os.path.dirname(os.path.abspath(__file__))
R = ROOT
CAP = os.path.join(R, "captures")
OUT_REPO = sys.argv[1] if len(sys.argv) > 1 else None
ONLY = set(sys.argv[2].split(",")) if len(sys.argv) > 2 and sys.argv[2] else None

E = html.escape
def Q(s):
    """Citations « … » de premier niveau (gère les « » imbriqués)."""
    out, depth, cur = [], 0, ""
    for ch in s:
        if ch == "«":
            if depth: cur += ch
            depth += 1
        elif ch == "»" and depth:
            depth -= 1
            if depth: cur += ch
            else: out.append(cur.strip()); cur = ""
        elif depth: cur += ch
    return out

SYMBOLE = open(os.path.join(ROOT, "symbole.svg")).read()

# Captures disponibles (code du plan → fichier, recadrage vertical en fraction : (haut, bas))
CAPS = {
    "C1": ("C1_couverture.png", (0, 1)), "C19": ("C1_couverture.png", (0, 1)),
    "C2": ("C2_carte_trace.png", (0, 1)), "C3": ("C3_relief3d.png", (0, 1)),
    "C4": ("C4_tableau_de_bord.png", (0, 1)), "C5": ("C5_meteo.png", (0, 1)),
    "C6": ("C6_profil_altitude.png", (0, 1)), "C7": ("C7_carnet_journal.png", (0, 0.42)),
    "C11": ("C11_replay.png", (0, 1)), "C12": ("C12_mur.png", (0.42, 1)),
    "C18": ("C18_sponsors.png", (0, 0.33)), "C21": ("C21_photos.png", (0.62, 1)),
}
EXEMPLE_CAPS = set(CAPS)


def capture_for(vis):
    v = vis
    m = re.findall(r"\bC(\d{1,2})\b", v)
    for n in m:
        k = "C" + n
        if k in CAPS and os.path.exists(os.path.join(CAP, CAPS[k][0])):
            return k
    low = v.lower()
    if "page d'exemple" in low or "page d’exemple" in low:
        if "carnet" in low: return "C7"
        if "relief" in low or "col" in low: return "C3"
        if "météo" in low: return "C5"
        if "couverture" in low: return "C1"
        return "C2"
    if "photos sur la carte" in low or "photos" in low and "capture" in low: return "C21"
    if "mur d'encouragements" in low and "capture" in low: return "C12"
    return None


def cap_img(k, cls="cap"):
    f, (a, b) = CAPS[k]
    path = os.path.join(CAP, f)
    # recadrage vertical via object-position + aspect
    from PIL import Image
    w, h = Image.open(path).size
    hh = h * (b - a)
    ratio = w / hh
    pos = 0 if b - a >= 1 else (a / (1 - (b - a)) * 100 if (1 - (b - a)) else 0)
    pill = '<span class="pill pill-ex">road trip d’exemple</span>' if k in EXEMPLE_CAPS and k not in ("C1", "C19") else ""
    if cls == "cap" and pill:
        return (f'{pill}<div class="{cls}" style="aspect-ratio:{ratio:.4f};width:min(100cqw, calc((100cqh - 70px) * {ratio:.4f}))">'
                f'<img src="file://{path}" style="object-position:50% {pos:.1f}%"></div>')
    return (f'<div class="{cls}" style="aspect-ratio:{ratio:.4f};width:min(100cqw, calc(100cqh * {ratio:.4f}))">'
            f'<img src="file://{path}" style="object-position:50% {pos:.1f}%">{pill}</div>')


# ───────────── analyse du texte d'une slide ─────────────
def parse(texte):
    d = dict(pill=None, top=[], title=[], giant=None, accent=None, head=None, body=[], items=[], mono=[],
             swipe=None, placeholder=None, bubble=None, bubble_meta=None, dashed=None, bingo=[], bigNum=None, quote=None)
    pending_num = None
    d["msgs"] = []
    next_quote = False
    seen_main = False
    lines = texte.split("\n")
    i = 0
    while i < len(lines):
        l = lines[i].strip(); i += 1
        if not l: continue
        q = Q(l)
        low = l.lower()
        if "[à complét" in low:
            d["placeholder"] = re.sub(r"^\[|\]$", "", l.strip()); continue
        if l.startswith("Grille"):
            while i < len(lines) and Q(lines[i]) and not lines[i].strip().startswith("En bas"):
                d["bingo"] += Q(lines[i]); i += 1
            continue
        if next_quote and q:
            d["quote"] = q[0]; next_quote = False; seen_main = True; continue
        if l.startswith("Texte") and not q:
            next_quote = True; continue
        if ("titre :" in low and q) or (len(q) >= 2 and re.search(r"»\s*/\s*«", l) and l.startswith("«")):
            d["title"] = q; seen_main = True; continue
        if q and l.startswith("«") and len(q) == 1 and " — " in q[0]:
            d["msgs"].append(q[0]); seen_main = True; continue
        if l.startswith("Titre"):
            d["title"] = q; seen_main = True; continue
        if l.startswith("Chrono"):
            continue
        if "pastille" in low and q and not l.startswith("Gabarit"):
            d["pill"] = q[0] if q else None; continue
        if ("swipe" in low or "glisse" in low or "touche pour" in low) and q:
            d["swipe"] = q[0]; continue
        if l.startswith("En très grand"):
            d["giant"] = q[0]; seen_main = True; continue
        if l.startswith("Dessous"):
            d["accent"] = q[0] if q else None; continue
        if l.startswith(("Sous le titre", "Sous-titre")) and q:
            d["body"].append(q[0]); continue
        if l.startswith("Un cadre en pointillés"):
            d["dashed"] = q[0] if q else "Ton logo ici"; continue
        if "bulle de message" in low:
            d["bubble"] = q[0] if q else None; d["bubble_meta"] = q[1] if len(q) > 1 else None; continue
        if l.startswith(("Logo", "Petit logo")) or (l.startswith("En bas") and "DM Mono" not in l):
            continue
        if "DM Mono" in l and q:
            txt = " · ".join(q) if not l.startswith("DM Mono, deux") else None
            if txt:
                (d["mono"] if seen_main else d["top"]).append(txt)
            continue
        if q and (l.startswith("«") or l.startswith("Texte")):
            if l.startswith("Texte"):
                d["quote"] = q[0]; seen_main = True; continue
            for t in q:
                if re.fullmatch(r"\d+", t):
                    d["bigNum"] = t; seen_main = True; continue
                m = re.match(r"^(\d+)\.\s+(.*)$", t)
                if m:
                    d["items"].append([m.group(1), m.group(2), None]); seen_main = True; continue
                if d["items"] and d["items"][-1][2] is None:
                    d["items"][-1][2] = t; continue
                if d["head"] is None and not d["title"]:
                    d["head"] = t; seen_main = True
                else:
                    d["body"].append(t)
            continue
        if q:  # autres préfixes (« Au milieu, en rouge… », « Trois lignes… »)
            (d["mono"] if seen_main else d["top"]).extend(q)
    return d


def esc_nl(t):
    return E(t)


LOGO = f'<div class="logo">{SYMBOLE}<span class="wm"><b>TROPHY</b><i>TRACKER</i></span></div>'


def title_html(parts, cls="title"):
    if not parts: return ""
    if len(parts) == 1:
        return f'<h1 class="{cls} fit">{E(parts[0])}</h1>'
    return f'<h1 class="{cls} fit">{"<br>".join(E(p) for p in parts[:-1])}<br><span class="red">{E(parts[-1])}</span></h1>'


# ───────────── fonds et illustrations ─────────────
def art_for(vis, d, story=False):
    low = vis.lower()
    if any(k in low for k in ["désert", "dunes", "piste"]): return "dunes"
    if any(k in low for k in ["lacet", "épingle", "route de col", "drone"]): return "lacets"
    if any(k in low for k in ["nuit", "lampe frontale", "étoiles"]): return "nuit"
    if any(k in low for k in ["table de cuisine", "table de fête", "téléphone posé"]): return "phone"
    if any(k in low for k in ["satellite", "relief", "carte", "vallée", "côte", "van", "mosaïque", "forêt", "route"]): return "sat"
    return "contours"


def bg_html(kind):
    if kind == "dunes":
        return '''<svg class="bgart" viewBox="0 0 1080 1350" preserveAspectRatio="xMidYMax slice"><defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#15161A"/><stop offset=".55" stop-color="#3a1d14"/><stop offset="1" stop-color="#6b3418"/></linearGradient>
<linearGradient id="d1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E8A33D"/><stop offset="1" stop-color="#7a4114"/></linearGradient>
<linearGradient id="d2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b9672a"/><stop offset="1" stop-color="#2a160e"/></linearGradient></defs>
<rect width="1080" height="1350" fill="url(#sky)"/><circle cx="780" cy="560" r="90" fill="#E8A33D" opacity=".55"/>
<path d="M0 760 C 200 640 360 700 520 650 S 860 560 1080 640 V1350 H0Z" fill="url(#d1)" opacity=".55"/>
<path d="M0 880 C 220 780 420 860 640 780 S 940 760 1080 800 V1350 H0Z" fill="url(#d2)" opacity=".85"/>
<path d="M0 1010 C 260 930 520 1020 760 950 S 1000 940 1080 960 V1350 H0Z" fill="#1d120d"/>
<path d="M120 1350 C 260 1180 380 1080 560 990 S 820 860 900 760" fill="none" stroke="#E8A33D" stroke-width="6" stroke-dasharray="4 18" stroke-linecap="round" opacity=".9"/>
<path d="M900 760 C 940 720 960 700 990 690" fill="none" stroke="#E1262C" stroke-width="7" stroke-linecap="round"/>
<circle cx="992" cy="688" r="26" fill="none" stroke="#E1262C" stroke-width="4" opacity=".45"/><circle cx="992" cy="688" r="13" fill="#E1262C" stroke="#F5F1EA" stroke-width="5"/></svg>'''
    if kind == "lacets":
        pts = []
        y = 1350; x = 260; d = 1
        path = f"M {x} {y}"
        for k in range(9):
            y2 = y - 110
            x2 = 820 if d == 1 else 260
            path += f" C {x} {y-60} {x2} {y-50} {x2} {y2}"
            x, y, d = x2, y2, -d
        return f'''<svg class="bgart" viewBox="0 0 1080 1350" preserveAspectRatio="xMidYMid slice">
<rect width="1080" height="1350" fill="#15161A"/>{contours_svg(.10)}
<path d="{path}" fill="none" stroke="#2b2c33" stroke-width="46" stroke-linecap="round"/>
<path d="{path}" fill="none" stroke="#E8A33D" stroke-width="8" stroke-linecap="round" opacity=".85"/>
<circle cx="{x}" cy="{y}" r="30" fill="none" stroke="#E1262C" stroke-width="4" opacity=".45"/><circle cx="{x}" cy="{y}" r="15" fill="#E1262C" stroke="#F5F1EA" stroke-width="5"/></svg>'''
    if kind == "nuit":
        import random
        rnd = random.Random(7)
        stars = "".join(f'<circle cx="{rnd.randint(0,1080)}" cy="{rnd.randint(0,900)}" r="{rnd.choice([1.5,2,2.5,3])}" fill="#F5F1EA" opacity="{rnd.uniform(.3,.9):.2f}"/>' for _ in range(120))
        return f'''<svg class="bgart" viewBox="0 0 1080 1350" preserveAspectRatio="xMidYMid slice"><defs>
<linearGradient id="n" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0e0f12"/><stop offset="1" stop-color="#1f2026"/></linearGradient></defs>
<rect width="1080" height="1350" fill="url(#n)"/>{stars}
<path d="M0 1050 L 180 900 L 300 980 L 470 820 L 640 960 L 800 860 L 1080 1010 V1350 H0Z" fill="#111215"/></svg>'''
    if kind == "sat":
        return f'<div class="bgsat" style="background-image:url(file://{os.path.join(CAP, "C3_relief3d.png")})"></div>'
    if kind == "phone":
        return f'''<div class="bgphone"><div class="phone">{cap_img("C1", "cap phonecap")}</div></div>'''
    return f'<svg class="bgart" viewBox="0 0 1080 1350" preserveAspectRatio="xMidYMid slice"><rect width="1080" height="1350" fill="#15161A"/>{contours_svg(.12)}</svg>'


def contours_svg(op):
    import math
    out = []
    for k, (cx, cy) in enumerate([(860, 260), (180, 1150)]):
        for r in range(60, 700, 46):
            pts = []
            for a in range(0, 361, 10):
                t = math.radians(a)
                rr = r * (1 + 0.08 * math.sin(3 * t + k + r / 90) + 0.05 * math.cos(5 * t + r / 70))
                pts.append(f"{cx + rr * math.cos(t):.0f},{cy + rr * math.sin(t):.0f}")
            out.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="#F5F1EA" stroke-width="1.6" opacity="{op}"/>')
    return "".join(out)


def illus(vis, d):
    low = vis.lower()
    if "micro" in low:
        return '''<div class="ill mic"><svg viewBox="0 0 400 400"><g fill="none" stroke="#E8A33D" stroke-width="6" stroke-linecap="round" opacity=".8">
<path d="M70 200 v0"/><path d="M95 170 v60"/><path d="M120 140 v120"/><path d="M280 140 v120"/><path d="M305 170 v60"/><path d="M330 200 v0"/></g>
<circle cx="200" cy="200" r="92" fill="#E1262C"/><circle cx="200" cy="200" r="118" fill="none" stroke="#E1262C" stroke-width="4" opacity=".35"/>
<rect x="178" y="140" width="44" height="78" rx="22" fill="#F5F1EA"/><path d="M160 196 a40 40 0 0 0 80 0" fill="none" stroke="#F5F1EA" stroke-width="9" stroke-linecap="round"/><path d="M200 236 v22" stroke="#F5F1EA" stroke-width="9" stroke-linecap="round"/></svg></div>'''
    if "chrono" in low:
        return '<div class="ill chrono"><span>05:00</span></div>'
    if "calendrier" in low:
        mois = ["jan", "fév", "mar", "avr", "mai", "juin", "juil", "août", "sep", "oct", "nov", "déc"]
        return '<div class="ill cal">' + "".join(f'<span class="{"on" if m == "juil" else ""}">{m}</span>' for m in mois) + "</div>"
    if "vue du dessus" in low and "sièges" in low:
        return '<div class="ill seats">' + "".join('<span>3,75 €</span>' for _ in range(4)) + "</div>"
    if "carte bancaire" in low:
        return '<div class="ill ccard"><div class="chip"></div><div class="num">•••• •••• •••• ••••</div><div class="lock">🔒</div></div>'
    if "initiales" in low:
        return '<div class="ill initials">' + "".join(f'<span style="background:{c}">{t}</span>' for t, c in [("L", "#E1262C"), ("S", "#F5F1EA"), ("M", "#E8A33D"), ("T", "#3a3b42")]) + "</div>"
    if "ticket" in low:
        return '<div class="ill ticket"><span>TT-XXXX-XXXX</span></div>'
    if "enveloppe" in low or "e-mail" in low and "capture" not in low:
        return '<div class="ill env">✉︎ ✉︎ ✉︎</div>'
    if "« ton logo ici »" in low or "cadres « logo »" in low or "cadres « logo » en pointillés" in low or "3 cadres" in low:
        return '<div class="ill logos"><span>logo</span><span>logo</span><span>logo</span></div>'
    if "barres de réseau" in low:
        return '<div class="ill bars"><span style="height:30%"></span><span style="height:55%"></span><span style="height:80%"></span><span style="height:100%"></span><b>0</b></div>'
    if "bandeau" in low:
        return '<div class="ill banner">● pas de réseau, c’est normal</div>'
    if "interrupteur" in low:
        return '<div class="ill switch"><span></span></div>'
    return ""


CSS = open(os.path.join(ROOT, "render.css")).read()


def page(inner, w, h, extra_cls=""):
    return f'''<!doctype html><html lang="fr"><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Big+Shoulders+Display:wght@900&family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=DM+Mono:wght@400;500&display=block" rel="stylesheet">
<style>:root{{--W:{w}px;--H:{h}px}}{CSS}</style></head><body><div class="cv {extra_cls}" style="width:{w}px;height:{h}px">{inner}</div>
<script>{FITJS}</script></body></html>'''


FITJS = """
document.fonts.ready.then(()=>{
 document.querySelectorAll('.fit').forEach(el=>{
   let fs=parseFloat(getComputedStyle(el).fontSize); const max=el.dataset.max?+el.dataset.max:9999;
   const box=el.closest('.fitbox')||el.parentElement;
   let guard=0;
   while((el.scrollWidth>el.clientWidth+1 || box.scrollHeight>box.clientHeight+1) && fs>20 && guard++<200){fs-=2; el.style.fontSize=fs+'px';}
 });
 document.body.dataset.ready='1';
});"""


def body_html(d):
    h = ""
    if d.get("msgs"):
        h += '<div class="msgs">' + "".join(f'<div class="msg">{E(m.rsplit(" — ",1)[0])}<small>{E(m.rsplit(" — ",1)[1])}</small></div>' for m in d["msgs"]) + "</div>"
    if d["bigNum"]:
        h += f'<div class="bignum">{E(d["bigNum"])}</div>'
    if d["quote"]:
        h += f'<div class="rawquote">{E(d["quote"])}</div>'
    if d["head"]:
        h += f'<h2 class="head fit">{E(d["head"])}</h2>'
    for it in d["items"]:
        h += f'<div class="item"><span class="n">{E(it[0])}</span><div><div class="ih">{E(it[1])}</div>' + (f'<div class="ib">{E(it[2])}</div>' if it[2] else "") + "</div></div>"
    for b in d["body"]:
        h += f'<p class="body">{E(b)}</p>'
    return h


def slide_html(role, texte, vis, w, h, story=False, sticker=""):
    d = parse(texte)
    kind = role.split("·")[-1].strip().upper() if "·" in role else role.upper()
    capk = capture_for(vis)
    cls = "story" if story else "post"
    top = "".join(f'<div class="mono top">{E(t)}</div>' for t in d["top"])
    pill = f'<span class="pill">{E(d["pill"])}</span>' if d["pill"] else ""
    mono = "".join(f'<div class="mono">{E(t)}</div>' for t in d["mono"])
    swipe = f'<div class="mono swipe">{E(d["swipe"])}</div>' if d["swipe"] else ""
    ph = f'<div class="placeholder">{E(d["placeholder"])}</div>' if d["placeholder"] else ""
    ill = illus(vis, d)
    stick = sticker.upper() if sticker else ""
    reserve = ""
    if story and stick and stick != "AUCUN":
        if "REPARTAGE" in stick: reserve = '<div class="reserve big"></div>'
        elif any(k in stick for k in ["SONDAGE", "QUIZ", "QUESTION", "CURSEUR", "COMPTE À REBOURS", "LIEN", "MENTION"]): reserve = '<div class="reserve"></div>'

    # Gabarits
    if d["bingo"]:
        cells = "".join(f'<div class="cell{" mid" if j == 4 else ""}">{E(t)}</div>' for j, t in enumerate(d["bingo"][:9]))
        inner = f'<div class="wrap paper">{title_html(d["title"] or [d["head"] or ""], "title dark")}<div class="bingo">{cells}</div>{mono}<div class="foot">{LOGO}</div></div>'
        return page(inner, w, h, cls)
    if "DERNIÈRE" in kind:
        inner = f'''<div class="halo"></div><div class="wrap cta fitbox"><div class="ctalogo">{LOGO}</div>
<h2 class="head big fit">{E(d["head"] or " ".join(d["title"]))}</h2>{"".join(f'<p class="body">{E(b)}</p>' for b in d["body"])}
<div class="mono url">trophytracker.fr · lien en bio</div><span class="pill red">15 € par road trip · sans abonnement</span></div>'''
        return page(inner, w, h, cls)
    if d["giant"]:
        inner = f'''<div class="halo"></div>{bg_html("contours")}<div class="wrap giantw fitbox">{pill}<div class="spacer"></div><div class="giant">{E(d["giant"])}</div>
<div class="accent red">{E(d["accent"] or "")}</div>{mono}{"".join(f'<p class="body">{E(b)}</p>' for b in d["body"])}<div class="spacer"></div><div class="foot">{LOGO}</div></div>'''
        return page(inner, w, h, cls)
    if d["bubble"]:
        inner = f'''<div class="halo"></div><div class="wrap fitbox"><div class="bubble">{E(d["bubble"])}<small>{E(d["bubble_meta"] or "")}</small></div>
{"".join(f'<div class="mono redmono">{E(t)}</div>' for t in d["top"] + d["mono"])}<div class="spacer"></div>{title_html(d["title"])}<div class="foot">{LOGO}</div></div>'''
        return page(inner, w, h, cls)
    if kind in ("COUVERTURE", "VISUEL UNIQUE", "PHOTO") or (story and d["title"] and not capk):
        if capk and kind != "PHOTO" and ("capture" in vis.lower() and ("en grand" in vis.lower() or "c1" in vis.lower() or "(c" in vis.lower())) and not any(k in vis.lower() for k in ["photo :", "photo d", "photo vue", "photo de"]):
            # couverture avec capture en avant
            inner = f'''<div class="halo"></div><div class="wrap coverwrap fitbox">{pill}{top}<div class="capzone">{cap_img(capk)}</div>
{title_html(d["title"]) if d["title"] else (f'<h2 class="head fit">{E(d["head"])}</h2>' if d["head"] else "")}{"".join(f'<p class="body">{E(b)}</p>' for b in d["body"])}{mono}{swipe}{reserve}<div class="foot">{LOGO}</div></div>'''
            return page(inner, w, h, cls)
        art = art_for(vis, d, story)
        inner = f'''{bg_html(art)}<div class="shade"></div><div class="halo"></div><div class="wrap cover fitbox">{pill}{top}{ill}<div class="spacer"></div>
{title_html(d["title"]) if d["title"] else (f'<h2 class="head big fit">{E(d["head"])}</h2>' if d["head"] else "")}
{f'<div class="accent">{E(d["accent"])}</div>' if d["accent"] else ""}{"".join(f'<p class="body">{E(b)}</p>' for b in d["body"])}{"".join(f'<div class="item"><span class="n">{E(it[0])}</span><div><div class="ih">{E(it[1])}</div>' + (f'<div class="ib">{E(it[2])}</div>' if it[2] else "") + "</div></div>" for it in d["items"])}{mono}{ph}{reserve}{swipe}<div class="foot">{LOGO}</div></div>'''
        return page(inner, w, h, cls)
    if capk and ("ÉCRAN" in kind or "capture" in vis.lower() or story):
        inner = f'''<div class="halo"></div><div class="wrap ecran fitbox">{pill}{top}{title_html(d["title"]) if d["title"] else ""}{body_html(d)}
<div class="capzone">{cap_img(capk)}</div>{mono}{ph}{reserve}{swipe}<div class="foot">{LOGO}</div></div>'''
        return page(inner, w, h, cls)
    # TEXTE (et AVANT/APRÈS, ÉCRAN sans capture disponible, VIDÉO)
    paper = "paper" if ("fond papier" in vis.lower() or "AVANT" in kind and False) else ""
    inner = f'''<div class="halo"></div>{bg_html("contours") if not paper else ""}<div class="wrap texte {paper} fitbox">{pill}{top}{title_html(d["title"], "title" + (" dark" if paper else "")) if d["title"] else ""}
{body_html(d)}{ill}{ph}{mono}{reserve}{swipe}<div class="foot">{LOGO}</div></div>'''
    return page(inner, w, h, cls)


def main():
    jobs = []
    out_html = os.path.join(R, ".html")
    for p in A + B:
        key = f"P{p['id']:02d}"
        if ONLY and key not in ONLY: continue
        dt = p["date"].isoformat() if p["date"] else "modele"
        folder = f"posts/{key}_{dt}_{p['slug']}"
        n = len(p["slides"])
        for i, (role, texte, vis) in enumerate(p["slides"], 1):
            if "VIDÉO" in role: continue
            hp = os.path.join(out_html, folder, f"{i}.html")
            os.makedirs(os.path.dirname(hp), exist_ok=True)
            open(hp, "w").write(slide_html(role, texte, vis, 1080, 1350))
            name = f"{key}.png" if n == 1 else f"{key}_{i}-sur-{n}.png"
            jobs.append(dict(html=hp, png=os.path.join(OUT_REPO, folder, name) if OUT_REPO else hp[:-5] + ".png", w=1080, h=1350))
    for s in STORIES:
        key = f"S{s['id']:02d}"
        if ONLY and key not in ONLY: continue
        dt = s["date"].isoformat() if s["date"] else ("a-la-une" if s["permanent"] else "modele")
        folder = f"stories/{key}_{dt}_{s['slug']}"
        n = len(s["ecrans"])
        for i, (lab, txt, st, vis) in enumerate(s["ecrans"], 1):
            hp = os.path.join(out_html, folder, f"{i}.html")
            os.makedirs(os.path.dirname(hp), exist_ok=True)
            open(hp, "w").write(slide_html(lab, txt, vis, 1080, 1920, story=True, sticker=st))
            name = f"{key}.png" if n == 1 else f"{key}_{i}-sur-{n}.png"
            jobs.append(dict(html=hp, png=os.path.join(OUT_REPO, folder, name) if OUT_REPO else hp[:-5] + ".png", w=1080, h=1920))
    json.dump(jobs, open(os.path.join(R, "jobs.json"), "w"), ensure_ascii=False, indent=0)
    print(len(jobs), "visuels à rendre")


if __name__ == "__main__":
    main()
