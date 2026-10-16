"""Construit une page HTML par slide (posts 1080×1350, stories 1080×1920) à partir de posts.py et stories.py.
Chaque slide déclare son gabarit (clé « t ») : photo, bleed, screen, widget, type, list, chat, timeline, bingo.
Photos : photos-j4l/ (photos de la page j4l-club, telles quelles). Captures : captures-j4l/ (captures-j4l.mjs).
Sortie : .html/... + jobs.json (liste {html, png, w, h}) pour shoot.mjs.
Usage : python3 render.py ../../publications-instagram [P01,S03]"""
import html, json, os, sys
from PIL import Image
from posts import POSTS
from stories import STORIES
from assets import PHOTOS, CAPS

R = os.path.dirname(os.path.abspath(__file__))
OUT_REPO = sys.argv[1] if len(sys.argv) > 1 else None
ONLY = set(sys.argv[2].split(",")) if len(sys.argv) > 2 and sys.argv[2] else None
E = html.escape
SYMBOLE = open(os.path.join(R, "symbole.svg")).read()
CSS = open(os.path.join(R, "render.css")).read()
LOGO = f'<div class="logo">{SYMBOLE}<span class="wm"><b>TROPHY</b><i>TRACKER</i></span></div>'


def photo_url(k):
    return "file://" + os.path.join(R, "photos-j4l", PHOTOS[k]["f"])


def cap_html(k, crop=None, phone=False, pill=True, cls=""):
    """Capture réelle recadrée verticalement (crop = (haut, bas) en fractions), dans un cadre de téléphone ou une carte."""
    f = CAPS[k]["f"]
    path = os.path.join(R, "captures-j4l", f)
    w, h = Image.open(path).size
    a, b = crop or CAPS[k].get("crop", (0, 1))
    ratio = w / (h * (b - a))
    img = (f'<img src="file://{path}" style="position:absolute;left:0;width:100%;height:{100 / (b - a):.3f}%;'
           f'top:{-a / (b - a) * 100:.3f}%">')
    tag = '<span class="pill pill-ex">road trip d’exemple</span>' if pill else ""
    kind = "phone" if phone else "card"
    return (f'<div class="capzone {cls}">{tag}<div class="{kind}" style="aspect-ratio:{ratio:.4f};'
            f'width:min(100cqw, calc((100cqh - {70 if pill else 0}px) * {ratio:.4f}))">{img}</div></div>')


def title_html(lines, red=None, cls="title"):
    """lines : liste de lignes ; la dernière en rouge par défaut (red = liste d'indices, ou [] pour aucune)."""
    if not lines: return ""
    red = [len(lines) - 1] if red is None and len(lines) > 1 else (red or [])
    parts = [f'<span class="red">{E(l)}</span>' if i in red else E(l) for i, l in enumerate(lines)]
    return f'<h1 class="{cls} fit">{"<br>".join(parts)}</h1>'


def common(s):
    """Petits éléments partagés : étiquette du haut, pastille, sous-titre, liste à puces, « glisse »."""
    out = dict(
        kicker=f'<div class="kicker">{E(s["kicker"])}</div>' if s.get("kicker") else "",
        pill=f'<span class="pill{" live" if s.get("live") else ""}">{E(s["pill"])}</span>' if s.get("pill") else "",
        sub="".join(f'<p class="sub">{E(x)}</p>' for x in ([s["sub"]] if isinstance(s.get("sub"), str) else s.get("sub", []))),
        bullets=('<ul class="bullets">' + "".join(f"<li>{E(x)}</li>" for x in s["bullets"]) + "</ul>") if s.get("bullets") else "",
        mono=f'<div class="monoline">{E(s["mono"])}</div>' if s.get("mono") else "",
        swipe=f'<div class="swipe">{E(s["swipe"])}</div>' if s.get("swipe") else "",
        num=f'<div class="num">{E(s["num"])}</div>' if s.get("num") else "",
        reserve='<div class="reserve"></div>' if s.get("sticker") else "",
    )
    return out


def T_photo(s, story):
    c = common(s)
    pos = s.get("pos", PHOTOS[s["img"]].get("pos", "50% 50%"))
    zoom = s.get("zoom", 1)
    top = s.get("align") == "top"
    card = ""
    if s.get("card"):
        cd = s["card"]
        card = f'<div class="floatcard {cd.get("where", "top")}">{cap_html(cd["cap"], cd.get("crop"), phone=cd.get("phone", False), pill=cd.get("pill", True))}</div>'
    items = "".join(f'<div class="item"><span class="n">{E(n)}</span><div><div class="ih">{E(h)}</div>' + (f'<div class="ib">{E(b)}</div>' if b else "") + "</div></div>" for n, h, b in s.get("items", []))
    inner = (f'<div class="bgimg" style="background-image:url(&quot;{photo_url(s["img"])}&quot;);background-position:{pos};transform:scale({zoom});transform-origin:{pos}"></div>'
             f'<div class="grad {"gtop" if top else "gbot"}"></div>{card}'
             f'<div class="wrap {"top" if top else "bottom"} fitbox">{c["pill"]}{c["kicker"]}{c["num"]}{title_html(s.get("title"), s.get("red"))}{c["sub"]}{items}{c["bullets"]}{c["mono"]}{c["reserve"]}{c["swipe"]}</div>')
    return inner, "dark"


def T_bleed(s, story):
    """Capture en plein cadre (carte satellite ou relief 3D), titre par-dessus."""
    c = common(s)
    f = os.path.join(R, "captures-j4l", CAPS[s["cap"]]["f"])
    inner = (f'<div class="bgimg" style="background-image:url(&quot;file://{f}&quot;);background-position:{s.get("pos", "50% 50%")};background-size:{s.get("size", "cover")}"></div>'
             f'<div class="grad gbot"></div><span class="pill pill-ex abs">road trip d’exemple</span>'
             f'<div class="wrap bottom fitbox">{c["pill"]}{c["kicker"]}{title_html(s.get("title"), s.get("red"))}{c["sub"]}{c["mono"]}{c["reserve"]}{c["swipe"]}</div>'
             f'<div class="credit">Imagerie © Esri, Maxar, Earthstar Geographics</div>')
    return inner, "dark"


def T_screen(s, story):
    c = common(s)
    inner = (f'<div class="wrap screen fitbox">{c["pill"]}{c["kicker"]}{c["num"]}{title_html(s.get("title"), s.get("red"))}{c["sub"]}'
             f'{cap_html(s["cap"], s.get("crop"), phone=True, pill=s.get("expill", True), cls="tilt" if s.get("tilt") else "")}{c["mono"]}{c["reserve"]}{c["swipe"]}</div>')
    return inner, s.get("bg", "ink")


def T_widget(s, story):
    c = common(s)
    below = s.get("below", False)
    capz = cap_html(s["cap"], s.get("crop"), phone=False, pill=s.get("expill", True))
    head = f'{c["pill"]}{c["kicker"]}{title_html(s.get("title"), s.get("red"))}{c["sub"]}'
    inner = f'<div class="wrap widget fitbox">{capz + head if below else head + capz}{c["bullets"]}{c["mono"]}{c["reserve"]}{c["swipe"]}</div>'
    return inner, s.get("bg", "ink")


def T_type(s, story):
    c = common(s)
    giant = f'<div class="giant fit">{E(s["giant"])}</div>' if s.get("giant") else ""
    accent = f'<div class="accent">{E(s["accent"])}</div>' if s.get("accent") else ""
    items = "".join(f'<div class="item"><span class="n">{E(n)}</span><div><div class="ih">{E(h)}</div>' + (f'<div class="ib">{E(b)}</div>' if b else "") + "</div></div>" for n, h, b in s.get("items", []))
    if s.get("cols"): items = f'<div class="items2">{items}</div>'
    inner = (f'<div class="wrap type {s.get("align", "center")} fitbox">{c["pill"]}{c["kicker"]}{giant}{accent}'
             f'{title_html(s.get("title"), s.get("red"))}{c["sub"]}{items}{c["bullets"]}{c["mono"]}{c["reserve"]}{c["swipe"]}</div>')
    return inner, s.get("bg", "ink")


def T_chat(s, story):
    c = common(s)
    msgs = "".join(f'<div class="bubble {side}"><span>{E(t)}</span>' + (f"<small>{E(m)}</small>" if m else "") + "</div>" for side, t, m in s["msgs"])
    inner = (f'<div class="wrap chat fitbox">{c["kicker"]}<div class="msgs">{msgs}</div><div class="spacer"></div>'
             f'{title_html(s.get("title"), s.get("red"))}{c["sub"]}{c["reserve"]}{c["swipe"]}</div>')
    return inner, s.get("bg", "ink")


def T_timeline(s, story):
    c = common(s)
    rows = "".join(f'<div class="tl"><div class="tlh">{E(h)}</div><div class="tlt{" red" if i == len(s["rows"]) - 1 else ""}">{E(t)}</div></div>' for i, (h, t) in enumerate(s["rows"]))
    inner = f'<div class="wrap timeline fitbox">{c["kicker"]}{title_html(s.get("title"), s.get("red"))}<div class="tls">{rows}</div>{c["sub"]}{c["reserve"]}</div>'
    return inner, s.get("bg", "paper")


def T_bingo(s, story):
    c = common(s)
    cells = "".join(f'<div class="cell{" mid" if j == 4 else ""}">{E(t)}</div>' for j, t in enumerate(s["cells"][:9]))
    inner = f'<div class="wrap bingo fitbox">{title_html(s.get("title"), s.get("red"))}<div class="grid">{cells}</div>{c["mono"]}</div>'
    return inner, "paper"


TPL = dict(photo=T_photo, bleed=T_bleed, screen=T_screen, widget=T_widget, type=T_type, chat=T_chat, timeline=T_timeline, bingo=T_bingo)

FITJS = """
document.fonts.ready.then(()=>{
 const box=document.querySelector('.fitbox');
 const fits=[...document.querySelectorAll('.fit')];
 let guard=0;
 const over=()=>box && (box.scrollHeight>box.clientHeight+1 || fits.some(el=>el.scrollWidth>el.clientWidth+1));
 while(over() && guard++<120){
   fits.forEach(el=>{const fs=parseFloat(getComputedStyle(el).fontSize); if(fs>40) el.style.fontSize=(fs*0.96)+'px';});
   document.querySelectorAll('.sub,.ib,.bullets li').forEach(el=>{const fs=parseFloat(getComputedStyle(el).fontSize); if(fs>30) el.style.fontSize=(fs*0.98)+'px';});
 }
 const imgs=[...document.images]; Promise.all(imgs.map(i=>i.complete?1:new Promise(r=>{i.onload=i.onerror=r;}))).then(()=>{document.body.dataset.ready='1';});
});"""


def page(inner, bg, w, h, story):
    logo = "" if bg == "paper-nologo" else f'<div class="foot">{LOGO}</div>'
    return f'''<!doctype html><html lang="fr"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Big+Shoulders+Display:wght@900&family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=DM+Mono:wght@400;500&display=block" rel="stylesheet">
<style>{CSS}</style></head><body><div class="cv bg-{bg} {"story" if story else "post"}" style="width:{w}px;height:{h}px">
{'<div class="halo"></div>' if bg == "ink" else ""}{inner}{logo}</div><script>{FITJS}</script></body></html>'''


def slide_html(s, w, h, story=False):
    inner, bg = TPL[s["t"]](s, story)
    return page(inner, bg, w, h, story)


def main():
    jobs = []
    out_html = os.path.join(R, ".html")
    groups = [(f"P{p['id']:02d}", p, "posts", p["slides"], 1350) for p in POSTS] + \
             [(f"S{s['id']:02d}", s, "stories", s["ecrans"], 1920) for s in STORIES]
    for key, item, kind, slides, H in groups:
        if ONLY and key not in ONLY: continue
        folder = f"{kind}/{key}_{item['dossier']}"
        n = len(slides)
        for i, s in enumerate(slides, 1):
            hp = os.path.join(out_html, folder, f"{i}.html")
            os.makedirs(os.path.dirname(hp), exist_ok=True)
            open(hp, "w").write(slide_html(s, 1080, H, story=(kind == "stories")))
            name = f"{key}.png" if n == 1 else f"{key}_{i}-sur-{n}.png"
            jobs.append(dict(html=hp, png=os.path.join(OUT_REPO, folder, name) if OUT_REPO else hp[:-5] + ".png", w=1080, h=H))
    json.dump(jobs, open(os.path.join(R, "jobs.json"), "w"), ensure_ascii=False, indent=0)
    print(len(jobs), "visuels à rendre")


if __name__ == "__main__":
    main()
