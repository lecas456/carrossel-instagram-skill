"""Gera uma imagem via API OpenAI (gpt-image-1) usando apenas a stdlib.

Uso:
  python gerar_imagem.py --prompt "..." --out saida.png
  python gerar_imagem.py --prompt-file prompt.txt --out saida.png [--size 1024x1536]
                         [--quality medium] [--env-file caminho/.env]

Chave: OPENAI_API_KEY no ambiente, ou em --env-file, ou em ./.env
Sai com código 0 em sucesso; != 0 e mensagem no stderr em falha (sem vazar a chave).
"""

import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.request

API_URL = "https://api.openai.com/v1/images/generations"


def carregar_chave(env_file: str | None) -> str | None:
    chave = os.environ.get("OPENAI_API_KEY")
    if chave:
        return chave.strip()
    candidatos = [env_file] if env_file else []
    candidatos.append(os.path.join(os.getcwd(), ".env"))
    for caminho in candidatos:
        if not caminho or not os.path.isfile(caminho):
            continue
        try:
            with open(caminho, "r", encoding="utf-8-sig") as f:
                for linha in f:
                    linha = linha.strip()
                    if linha.startswith("OPENAI_API_KEY"):
                        _, _, valor = linha.partition("=")
                        valor = valor.strip().strip('"').strip("'")
                        if valor:
                            return valor
        except OSError:
            continue
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    grupo = ap.add_mutually_exclusive_group(required=True)
    grupo.add_argument("--prompt")
    grupo.add_argument("--prompt-file")
    ap.add_argument("--out", required=True)
    ap.add_argument("--size", default="1024x1536",
                    choices=["1024x1024", "1024x1536", "1536x1024"])
    ap.add_argument("--quality", default="low",
                    choices=["low", "medium", "high"])
    ap.add_argument("--model", default="gpt-image-1")
    ap.add_argument("--env-file")
    args = ap.parse_args()

    prompt = args.prompt
    if args.prompt_file:
        with open(args.prompt_file, "r", encoding="utf-8-sig") as f:
            prompt = f.read().strip()
    if not prompt:
        print("ERRO: prompt vazio.", file=sys.stderr)
        return 2

    chave = carregar_chave(args.env_file)
    if not chave:
        print("ERRO: OPENAI_API_KEY nao encontrada (ambiente ou .env).", file=sys.stderr)
        return 3

    corpo = json.dumps({
        "model": args.model,
        "prompt": prompt,
        "size": args.size,
        "quality": args.quality,
        "n": 1,
    }).encode("utf-8")
    req = urllib.request.Request(
        API_URL,
        data=corpo,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {chave}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            dados = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detalhe = ""
        try:
            detalhe = json.loads(e.read().decode("utf-8")).get("error", {}).get("message", "")
        except Exception:
            pass
        print(f"ERRO: API retornou {e.code}. {detalhe}", file=sys.stderr)
        return 4
    except urllib.error.URLError as e:
        print(f"ERRO: falha de rede: {e.reason}", file=sys.stderr)
        return 5

    try:
        b64 = dados["data"][0]["b64_json"]
    except (KeyError, IndexError):
        print("ERRO: resposta sem imagem.", file=sys.stderr)
        return 6

    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "wb") as f:
        f.write(base64.b64decode(b64))
    print(f"OK: {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
