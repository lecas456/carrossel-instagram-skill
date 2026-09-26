"""Baixa a foto de perfil publica de um usuario do Instagram (sem login, so stdlib).

Uso:
  python baixar_avatar.py <usuario_ou_url> --out avatar.jpg

Tenta 2 caminhos, nesta ordem:
  1. API web publica do Instagram (web_profile_info) — retorna a foto em alta;
  2. og:image da pagina do perfil.
Sai com codigo 0 e imprime OK em sucesso. Se o Instagram bloquear (comum em
alguns IPs/horarios), sai com codigo != 0 — nesse caso peca a foto ao usuario.
"""

import argparse
import json
import re
import sys
import urllib.error
import urllib.request

UA_NAVEGADOR = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")


def limpar_usuario(entrada):
    m = re.search(r"instagram\.com/([A-Za-z0-9._]+)", entrada)
    usuario = m.group(1) if m else entrada
    return usuario.strip().strip("/@")


def baixar(url, headers, timeout=30):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def via_api(usuario):
    url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={usuario}"
    corpo = baixar(url, {
        "User-Agent": UA_NAVEGADOR,
        "x-ig-app-id": "936619743392459",
        "Accept": "*/*",
    })
    dados = json.loads(corpo.decode("utf-8"))
    u = dados.get("data", {}).get("user") or {}
    return u.get("profile_pic_url_hd") or u.get("profile_pic_url")


def via_og_image(usuario):
    html = baixar(f"https://www.instagram.com/{usuario}/", {
        "User-Agent": UA_NAVEGADOR,
        "Accept": "text/html",
    }).decode("utf-8", "ignore")
    m = (re.search(r'property="og:image"\s+content="([^"]+)"', html)
         or re.search(r'"profile_pic_url_hd":"([^"]+)"', html)
         or re.search(r'"profile_pic_url":"([^"]+)"', html))
    if not m:
        return None
    url = m.group(1)
    url = url.replace("\\u0026", "&").replace("&amp;", "&")
    return url


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("usuario", help="usuario do Instagram ou URL do perfil")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    usuario = limpar_usuario(args.usuario)

    for tentativa in (via_api, via_og_image):
        try:
            url_foto = tentativa(usuario)
            if not url_foto:
                continue
            imagem = baixar(url_foto, {"User-Agent": UA_NAVEGADOR})
            if len(imagem) < 1000:  # resposta suspeita (pagina de erro/placeholder)
                continue
            with open(args.out, "wb") as f:
                f.write(imagem)
            print(f"OK: {args.out} (@{usuario})")
            return 0
        except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError,
                TimeoutError, OSError):
            continue

    print(f"ERRO: nao consegui obter a foto publica de @{usuario} "
          "(Instagram costuma bloquear acesso anonimo). Peca a foto ao usuario "
          "ou siga com o avatar de inicial.", file=sys.stderr)
    return 3


if __name__ == "__main__":
    sys.exit(main())
