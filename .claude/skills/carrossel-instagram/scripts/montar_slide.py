"""Compoe as laminas finais 1080x1350 de um carrossel a partir de um slides.json.

Uso:
  python montar_slide.py caminho/do/slides.json

Suporta 2 modelos ("modelo": 1 ou 2 no topo do json; pode sobrepor por lamina):

MODELO 1 (Vitrine, centralizado) — campos por lamina:
  arquivo, kicker, titulo [{texto, destaque}], subtitulo, imagem,
  caixa {titulo, url, passos, nota}, lista [[rotulo, detalhe], ...], rodape_extra

MODELO 2 (Imersivo, full-bleed, texto a esquerda) — campos por lamina:
  arquivo, kicker (pilula), titulo [{texto, destaque}]  (destaque = marca-texto),
  url (pilula), beneficio, paragrafos [..], passos [..] (numerados),
  dica (caixa com raio), botao (pilula da capa), proximo (teaser "Proximo: ... >>"),
  lista [[nome, desc, url], ...] (recap), imagem (fundo inteiro)

Json comum: tema, handle, marca, saida, paleta {fundo, titulo, destaque,
destaque_claro, texto, nota}, sombra_texto (Modelo 2: intensidade da sombra atras
do texto; padrao 1.0, ex.: 1.3 = mais escura, 0.6 = mais sutil, 0 = sem sombra).
Caminhos relativos ao proprio json.

Limites e regras:
- caixa.passos: no maximo 2 linhas renderizadas; caixa.nota: 1 linha (o excedente e cortado).
- NAO use emoji nos textos das laminas — as fontes nao renderizam (viram quadrados).
- Se a cor de destaque for escura (some no preto), os TEXTOS de destaque usam
  automaticamente destaque_claro; preenchimentos mantem a cor original.
- Modelo 1: a imagem cobre a largura toda do card, sem escurecimento (gere em paisagem,
  1536x1024). Modelo 2: a imagem cobre a lamina inteira (gere em retrato, 1024x1536).
"""

import json
import os
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1080, 1350
MARGEM = 70
LARG_UTIL = W - 2 * MARGEM

# Anton = tudo que e impactante (titulos, kickers M2, numeros, pilulas de destaque).
# DM Sans = escritas secundarias (subtitulos, paragrafos, notas, rodape).
# Ambas vem na pasta fonts/ da skill; o resto e fallback de sistema.
FONTES_TITULO = ["anton-regular.ttf", "anton.ttf", "archivoblack.ttf", "impact.ttf",
                 "ariblk.ttf", "arialbd.ttf", "dejavusans-bold.ttf",
                 "liberationsans-bold.ttf"]
FONTES_CORPO_BOLD = ["dmsans-semibold.ttf", "dmsans-bold.ttf", "seguisb.ttf",
                     "segoeuib.ttf", "arialbd.ttf", "helvetica.ttc",
                     "dejavusans-bold.ttf", "liberationsans-bold.ttf"]
FONTES_CORPO = ["dmsans-regular.ttf", "dmsans-medium.ttf", "segoeui.ttf", "arial.ttf",
                "helvetica.ttc", "dejavusans.ttf", "liberationsans-regular.ttf"]
FONTES_MONO = ["consolab.ttf", "consola.ttf", "courbd.ttf", "cour.ttf", "menlo.ttc",
               "dejavusansmono-bold.ttf", "liberationmono-bold.ttf"]

_INDICE_FONTES = None


def _indice_fontes():
    """Indexa fontes da pasta fonts/ da skill e das pastas do sistema (Win/Mac/Linux)."""
    global _INDICE_FONTES
    if _INDICE_FONTES is not None:
        return _INDICE_FONTES
    dirs = [os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "fonts")]
    windir = os.environ.get("WINDIR")
    if windir:
        dirs.append(os.path.join(windir, "Fonts"))
    dirs += ["/usr/share/fonts", "/usr/local/share/fonts",
             os.path.expanduser("~/.fonts"), os.path.expanduser("~/.local/share/fonts"),
             os.path.expanduser("~/Library/Fonts"), "/Library/Fonts",
             "/System/Library/Fonts"]
    _INDICE_FONTES = {}
    for d in dirs:
        if not os.path.isdir(d):
            continue
        for raiz, _, arquivos in os.walk(d):
            for a in arquivos:
                if a.lower().endswith((".ttf", ".otf", ".ttc")):
                    _INDICE_FONTES.setdefault(a.lower(), os.path.join(raiz, a))
    return _INDICE_FONTES


def fonte(candidatas, tamanho):
    indice = _indice_fontes()
    for nome in candidatas:
        caminho = indice.get(nome.lower())
        if caminho:
            try:
                return ImageFont.truetype(caminho, tamanho)
            except OSError:
                continue
    return ImageFont.load_default(tamanho)


def larg(draw, texto, f):
    caixa = draw.textbbox((0, 0), texto, font=f)
    return caixa[2] - caixa[0]


def alt(draw, texto, f):
    caixa = draw.textbbox((0, 0), texto, font=f)
    return caixa[3] - caixa[1]


def fonte_ajustada(draw, texto, candidatas, tam_max, larg_max):
    tam = tam_max
    while tam > 20:
        f = fonte(candidatas, tam)
        if larg(draw, texto, f) <= larg_max:
            return f
        tam -= 4
    return fonte(candidatas, 20)


def quebrar(draw, texto, f, larg_max):
    linhas, atual = [], ""
    for palavra in texto.split():
        teste = (atual + " " + palavra).strip()
        if larg(draw, teste, f) <= larg_max or not atual:
            atual = teste
        else:
            linhas.append(atual)
            atual = palavra
    if atual:
        linhas.append(atual)
    return linhas


def texto_espacado(draw, cx, y, texto, f, cor, espaco=6):
    largs = [larg(draw, ch, f) for ch in texto]
    total = sum(largs) + espaco * (len(texto) - 1)
    x = cx - total / 2
    for ch, lg in zip(texto, largs):
        draw.text((x, y), ch, font=f, fill=cor)
        x += lg + espaco


def _luminancia(hex_cor):
    h = hex_cor.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return 0.299 * r + 0.587 * g + 0.114 * b


def cor_contraste(hex_cor):
    """Texto escuro sobre preenchimento claro; texto claro sobre escuro."""
    return "#141414" if _luminancia(hex_cor) > 150 else "#F5EFE6"


def cor_destaque_texto(pal):
    """Cor de destaque para TEXTO sobre fundo escuro: se a cor for escura demais
    (some no preto), usa a versao acesa (destaque_claro). Preenchimentos continuam
    usando a cor original."""
    if _luminancia(pal["destaque"]) < 100:
        return pal.get("destaque_claro", pal["destaque"])
    return pal["destaque"]


def fundo_texturizado(cor_hex):
    """Fundo preto puro com vinheta central MUITO sutil (sem acinzentar)."""
    base = Image.new("RGB", (W, H), cor_hex)
    vin = Image.new("L", (W, H), 0)
    dv = ImageDraw.Draw(vin)
    dv.ellipse([-W * 0.4, -H * 0.25, W * 1.4, H * 1.05], fill=13)
    vin = vin.filter(ImageFilter.GaussianBlur(180))
    claro = Image.new("RGB", (W, H), "#141110")
    return Image.composite(claro, base, vin)


def desenhar_raio(d, x, y, h, cor):
    pts = [(0.62, 0.0), (0.08, 0.58), (0.40, 0.58), (0.30, 1.0), (0.92, 0.40), (0.52, 0.40)]
    d.polygon([(x + px * h * 0.75, y + py * h) for px, py in pts], fill=cor)


def pilula(d, x, y, texto, f, preenchimento, cor_texto, pad_x=26, pad_y=12):
    """Desenha pilula preenchida com canto arredondado; retorna (largura, altura)."""
    lg, at = larg(d, texto, f), alt(d, texto, f)
    w, h = lg + 2 * pad_x, at + 2 * pad_y
    d.rounded_rectangle([x, y, x + w, y + h], radius=h / 2 - 2, fill=preenchimento)
    d.text((x + pad_x, y + pad_y - 4), texto, font=f, fill=cor_texto)
    return w, h


# ---------------------------------------------------------------- MODELO 1

def colar_imagem(canvas, caminho, topo, base):
    """Cobre a LARGURA TODA do card entre topo e base: escala para cobrir, corta o
    excesso de altura e esfuma so as bordas superior/inferior para fundir no fundo.
    A imagem NUNCA e escurecida — ela deve ficar viva e colorida."""
    try:
        img = Image.open(caminho).convert("RGB")
    except OSError:
        return topo
    alt_disp = max(base - topo, 100)
    img = cobrir(img, W, alt_disp)
    masc = Image.new("L", img.size, 255)
    dm = ImageDraw.Draw(masc)
    borda = 80
    for i in range(borda):
        opac = int(255 * i / borda)
        dm.line([(0, i), (img.width, i)], fill=opac)
        dm.line([(0, img.height - 1 - i), (img.width, img.height - 1 - i)], fill=opac)
    canvas.paste(img, (0, topo), masc)
    return topo + alt_disp


def montar_m1(spec, pal, meta, dir_base):
    canvas = fundo_texturizado(pal["fundo"])
    d = ImageDraw.Draw(canvas)
    cx = W / 2
    y = 84

    kicker = spec.get("kicker", "").upper()
    if kicker:
        f = fonte(FONTES_CORPO_BOLD, 26)
        texto_espacado(d, cx, y, kicker, f, pal["texto"])
        y += 62

    for linha in spec.get("titulo", []):
        txt = linha["texto"].upper()
        f = fonte_ajustada(d, txt, FONTES_TITULO, 128, LARG_UTIL)
        cor = cor_destaque_texto(pal) if linha.get("destaque") else pal["titulo"]
        d.text((cx, y), txt, font=f, fill=cor, anchor="ma")
        y += alt(d, txt, f) + 26
    y += 12

    sub = spec.get("subtitulo")
    if sub:
        f = fonte(FONTES_CORPO_BOLD, 40)
        for ln in quebrar(d, sub, f, LARG_UTIL - 60):
            d.text((cx, y), ln, font=f, fill=pal["texto"], anchor="ma")
            y += 54
        y += 10

    base_rodape = H - 120
    y_reservado = base_rodape - 24
    caixa = spec.get("caixa")
    lista = spec.get("lista")
    extra = spec.get("rodape_extra")
    if extra:
        y_reservado -= 56
    alt_caixa = 0
    caixa_passos = []
    caixa_nota = None
    if caixa:
        if caixa.get("passos"):
            caixa_passos = quebrar(d, caixa["passos"], fonte(FONTES_CORPO_BOLD, 30),
                                   LARG_UTIL - 60)[:2]  # limite: 2 linhas
        if caixa.get("nota"):
            caixa_nota = quebrar(d, caixa["nota"], fonte(FONTES_CORPO, 26),
                                 LARG_UTIL - 60)[0]  # limite: 1 linha
        alt_caixa = (44 + (62 if caixa.get("url") else 0)
                     + 40 * len(caixa_passos) + (44 if caixa_nota else 0) + 14)
        y_reservado -= alt_caixa + 30

    if lista:
        f_rot = fonte(FONTES_CORPO_BOLD, 34)
        f_det = fonte(FONTES_CORPO, 28)
        alt_item = 116
        y_l = y + 20
        for item in lista:
            if y_l + alt_item > y_reservado:
                break
            d.rounded_rectangle([MARGEM, y_l, W - MARGEM, y_l + 100],
                                radius=16, outline=pal["nota"], width=2)
            d.text((MARGEM + 30, y_l + 14), item[0], font=f_rot, fill=pal["titulo"])
            d.text((MARGEM + 30, y_l + 58), item[1], font=f_det, fill=pal["nota"])
            y_l += alt_item
        if spec.get("imagem"):
            colar_imagem(canvas, os.path.join(dir_base, spec["imagem"]), y_l + 10, y_reservado)
    elif spec.get("imagem"):
        colar_imagem(canvas, os.path.join(dir_base, spec["imagem"]), y, y_reservado)
        f = fonte(FONTES_CORPO, 20)
        d.text((W - MARGEM, y_reservado - 8), "Ilustração", font=f, fill=pal["nota"], anchor="rs")

    if caixa:
        topo_cx = y_reservado + 30
        d.rounded_rectangle([MARGEM, topo_cx, W - MARGEM, topo_cx + alt_caixa],
                            radius=18, outline=pal["destaque_claro"], width=3)
        f_pill = fonte(FONTES_TITULO, 30)
        pill_txt = caixa.get("titulo", "COMO FAZER").upper()
        pill_l = larg(d, pill_txt, f_pill) + 48
        d.rounded_rectangle([MARGEM + 30, topo_cx - 22, MARGEM + 30 + pill_l, topo_cx + 26],
                            radius=10, fill=pal["destaque"])
        d.text((MARGEM + 54, topo_cx - 16), pill_txt, font=f_pill,
               fill=cor_contraste(pal["destaque"]))
        yc = topo_cx + 44
        if caixa.get("url"):
            f = fonte(FONTES_TITULO, 44)
            d.text((MARGEM + 30, yc), caixa["url"], font=f, fill=pal["destaque_claro"])
            yc += 62
        if caixa_passos:
            f = fonte(FONTES_CORPO_BOLD, 30)
            for ln in caixa_passos:
                d.text((MARGEM + 30, yc), ln, font=f, fill=pal["texto"])
                yc += 40
        if caixa_nota:
            f = fonte(FONTES_CORPO, 26)
            d.text((MARGEM + 30, yc + 4), caixa_nota, font=f, fill=pal["nota"])

    if extra:
        f = fonte(FONTES_CORPO_BOLD, 28)
        texto_espacado(d, cx, base_rodape - 60, extra, f, pal["texto"], espaco=3)

    d.line([MARGEM, base_rodape, W - MARGEM, base_rodape], fill="#3a3a3a", width=2)
    f = fonte(FONTES_CORPO, 26)
    d.text((MARGEM, base_rodape + 28), meta.get("handle", ""), font=f, fill=pal["nota"])
    f = fonte(FONTES_CORPO_BOLD, 34)
    d.text((cx, base_rodape + 22), meta.get("marca", ""), font=f,
           fill=pal["titulo"], anchor="ma")
    return canvas


# ---------------------------------------------------------------- MODELO 2

def cobrir(img, w, h):
    escala = max(w / img.width, h / img.height)
    img = img.resize((int(img.width * escala) + 1, int(img.height * escala) + 1),
                     Image.LANCZOS)
    x = (img.width - w) // 2
    y = (img.height - h) // 2
    return img.crop((x, y, x + w, y + h))


def aplicar_scrim(canvas):
    preto = Image.new("RGB", (W, H), "#000000")
    # esquerda -> direita (coluna de texto)
    g = Image.new("L", (W, 1), 0)
    for x in range(W):
        frac = max(0.0, 1 - x / (W * 0.66))
        g.putpixel((x, 0), int(235 * (frac ** 1.25)))
    canvas.paste(preto, (0, 0), g.resize((W, H)))
    # topo (kicker) e base (rodape/progresso)
    g = Image.new("L", (1, H), 0)
    for y in range(H):
        v = 0
        if y < 300:
            v = int(140 * (1 - y / 300))
        if y > H - 330:
            v = max(v, int(215 * (y - (H - 330)) / 330))
        g.putpixel((0, y), v)
    canvas.paste(preto, (0, 0), g.resize((W, H)))


def montar_m2(spec, pal, meta, dir_base, idx, total):
    caminho = spec.get("imagem")
    canvas = None
    if caminho:
        try:
            canvas = cobrir(Image.open(os.path.join(dir_base, caminho)).convert("RGB"), W, H)
        except OSError:
            canvas = None
    if canvas is None:
        canvas = fundo_texturizado(pal["fundo"])
    aplicar_scrim(canvas)
    # o conteudo e desenhado numa camada separada; o proprio desenho borrado vira
    # uma sombra preta sutil atras do texto (na frente da imagem), para legibilidade
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)

    X = 64
    COL = 620
    cor_pill_txt = cor_contraste(pal["destaque"])
    y = 84

    kicker = spec.get("kicker", "").upper()
    if kicker:
        f = fonte(FONTES_TITULO, 30)
        _, h = pilula(d, X, y, kicker, f, pal["destaque"], cor_pill_txt, pad_x=24, pad_y=12)
        y += h + 30

    for linha in spec.get("titulo", []):
        txt = linha["texto"].upper()
        f = fonte_ajustada(d, txt, FONTES_TITULO, 106, 880)
        at = alt(d, txt, f)
        if linha.get("destaque"):
            lg = larg(d, txt, f)
            d.rounded_rectangle([X - 6, y - 6, X + lg + 26, y + at + 22],
                                radius=8, fill=pal["destaque"])
            d.text((X + 10, y), txt, font=f, fill=cor_pill_txt)
        else:
            d.text((X, y), txt, font=f, fill=pal["titulo"])
        y += at + 30
    y += 6

    if spec.get("url"):
        f = fonte(FONTES_MONO, 42)
        _, h = pilula(d, X, y, spec["url"], f, pal["destaque"], cor_pill_txt,
                      pad_x=28, pad_y=14)
        y += h + 26

    if spec.get("beneficio"):
        f = fonte(FONTES_CORPO_BOLD, 38)
        for ln in quebrar(d, spec["beneficio"], f, COL):
            d.text((X, y), ln, font=f, fill=pal["destaque_claro"])
            y += 50
        y += 14

    sub = spec.get("subtitulo")
    if sub:
        f = fonte(FONTES_CORPO_BOLD, 40)
        for ln in quebrar(d, sub, f, COL):
            d.text((X, y), ln, font=f, fill=pal["texto"])
            y += 54
        y += 16

    paragrafos = spec.get("paragrafos", [])
    if paragrafos:
        f = fonte(FONTES_CORPO_BOLD, 33)
        for i, p in enumerate(paragrafos):
            for ln in quebrar(d, p, f, COL - 60):
                d.text((X, y), ln, font=f, fill=pal["texto"])
                y += 44
            if i < len(paragrafos) - 1:
                y += 12
                d.line([X, y, X + 300, y], fill="#6a6a6a", width=2)
                y += 22

    passos = spec.get("passos", [])
    if passos:
        f_num = fonte(FONTES_TITULO, 30)
        f_txt = fonte(FONTES_CORPO_BOLD, 32)
        for i, p in enumerate(passos, 1):
            linhas = quebrar(d, p, f_txt, COL - 120)
            d.ellipse([X, y + 2, X + 48, y + 50], fill=pal["destaque"])
            d.text((X + 24, y + 8), str(i), font=f_num, fill=cor_pill_txt, anchor="ma")
            yt = y
            for ln in linhas:
                d.text((X + 68, yt), ln, font=f_txt, fill=pal["texto"])
                yt += 42
            y = max(yt, y + 56) + 14

    lista = spec.get("lista", [])
    if lista:
        f_nome = fonte(FONTES_CORPO_BOLD, 34)
        f_desc = fonte(FONTES_CORPO, 27)
        f_url = fonte(FONTES_MONO, 26)
        y += 8
        for item in lista:
            if y > H - 330:
                break
            d.text((X, y), item[0], font=f_nome, fill=pal["titulo"])
            d.text((X, y + 42), item[1], font=f_desc, fill=pal["nota"])
            if len(item) > 2 and item[2]:
                lg = larg(d, item[2], f_url) + 40
                pilula(d, W - 64 - lg, y + 8, item[2], f_url,
                       pal["destaque"], cor_pill_txt, pad_x=20, pad_y=8)
            y += 88
        y += 8

    if spec.get("botao"):
        f = fonte(FONTES_CORPO_BOLD, 34)
        y += 10
        _, h = pilula(d, X, y, spec["botao"], f, pal["destaque"], cor_pill_txt,
                      pad_x=34, pad_y=16)
        y += h

    dica = spec.get("dica")
    if dica:
        f = fonte(FONTES_CORPO_BOLD, 31)
        linhas = quebrar(d, dica, f, COL - 130)
        box_h = len(linhas) * 42 + 34
        box_w = max(larg(d, ln, f) for ln in linhas) + 130
        y_d = min(max(y + 24, H - 480), H - 210 - box_h)
        d.rounded_rectangle([X, y_d, X + box_w, y_d + box_h],
                            radius=18, fill=pal["destaque"])
        desenhar_raio(d, X + 34, y_d + box_h / 2 - 19, 38, cor_pill_txt)
        yt = y_d + 18
        for ln in linhas:
            d.text((X + 92, yt), ln, font=f, fill=cor_pill_txt)
            yt += 42

    # rodape
    y_f = H - 152
    f = fonte(FONTES_CORPO, 26)
    d.text((X, y_f + 8), meta.get("handle", ""), font=f, fill=pal["texto"])
    if spec.get("proximo"):
        f_p = fonte(FONTES_CORPO_BOLD, 27)
        txt = f"Próximo: {spec['proximo']} »"
        lg = larg(d, txt, f_p) + 52
        pilula(d, min(W * 0.40, W - 74 - lg - 260), y_f - 4, txt, f_p,
               pal["destaque"], cor_pill_txt, pad_x=26, pad_y=11)
    f = fonte(FONTES_CORPO_BOLD, 30)
    d.text((W - X, y_f + 4), meta.get("marca", ""), font=f, fill=pal["titulo"], anchor="ra")
    if caminho:
        f = fonte(FONTES_CORPO, 20)
        d.text((W - X, y_f - 26), "Ilustração", font=f, fill=pal["nota"], anchor="rs")

    # barra de progresso
    if total > 1:
        gap = 8
        seg = (W - 2 * X - gap * (total - 1)) / total
        y_b = H - 68
        for i in range(total):
            x0 = X + i * (seg + gap)
            cor = pal["destaque"] if i <= idx else "#4a4a4a"
            d.rounded_rectangle([x0, y_b, x0 + seg, y_b + 12], radius=6, fill=cor)

    # sombra seguindo o contorno do conteudo: dilata alem das letras (painel
    # continuo atras do bloco de texto), borra e escurece — legivel sem apagar a
    # cena. Intensidade ajustavel via "sombra_texto" no json (padrao 1.0).
    forca = float(meta.get("sombra_texto", 1.0))
    if forca > 0:
        teto = min(230, int(175 * forca))
        sombra = overlay.split()[3].filter(ImageFilter.MaxFilter(21))
        sombra = sombra.filter(ImageFilter.GaussianBlur(30))
        sombra = sombra.point(lambda a: min(teto, int(a * 1.1 * forca)))
        canvas.paste(Image.new("RGB", (W, H), "#000000"), (0, 0), sombra)
    canvas.paste(overlay, (0, 0), overlay)
    return canvas


# ---------------------------------------------------------------- principal

def main():
    if len(sys.argv) != 2:
        print("Uso: python montar_slide.py slides.json", file=sys.stderr)
        return 2
    caminho_json = os.path.abspath(sys.argv[1])
    dir_base = os.path.dirname(caminho_json)
    with open(caminho_json, "r", encoding="utf-8-sig") as f:
        spec = json.load(f)

    pal = {"fundo": "#000000", "titulo": "#F5EFE6", "destaque": "#7A1F2D",
           "destaque_claro": "#C8374F", "texto": "#EDEDED", "nota": "#9A9A9A"}
    pal.update(spec.get("paleta", {}))
    dir_saida = os.path.join(dir_base, spec.get("saida", "finais"))
    os.makedirs(dir_saida, exist_ok=True)

    slides = spec["slides"]
    modelo_padrao = spec.get("modelo", 1)
    gerados = []
    for idx, slide in enumerate(slides):
        modelo = slide.get("modelo", modelo_padrao)
        if modelo == 2:
            img = montar_m2(slide, pal, spec, dir_base, idx, len(slides))
        else:
            img = montar_m1(slide, pal, spec, dir_base)
        destino = os.path.join(dir_saida, slide["arquivo"])
        img.save(destino, "PNG")
        gerados.append(destino)
        print(f"OK: {destino}")
    print(f"{len(gerados)} lamina(s) gerada(s) em {dir_saida}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
