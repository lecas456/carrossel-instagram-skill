# Estilo Visual — calibrado em 2 carrosséis reais de alto engajamento

Referências que originaram os modelos:
- **Modelo 1 — "Vitrine"**: "7 sites que fazem assuntos difíceis ficarem visíveis"
  (@caminhotec — 699 likes, 322 compartilhamentos)
- **Modelo 2 — "Imersivo"**: "As histórias da sua família não precisam se perder"
  (@caminhotec — 463 likes, 309 compartilhamentos)

Se o diretório de trabalho tiver pastas com os screenshots originais (ex.:
`Carrossel Vencedor` e `Carrossel Vencedor 02`), consulte as imagens — mas este guia
já contém tudo o que é necessário para reproduzir os estilos.

## Princípios comuns (replicar sempre, nos dois modelos)

1. Capa com gancho forte: promessa numerada OU dor emocional + palavra/linha destacada em cor.
2. Uma ideia por lâmina, com kicker de contexto no topo.
3. Utilidade imediata gera salvamento: URL + passos curtos + nota honesta
   ("Grátis, mas pede cadastro", "Site em inglês").
4. Penúltima lâmina = recap em lista; última = CTA da marca + pergunta de engajamento.
5. TODAS as imagens do carrossel com a mesma luz e atmosfera → parece uma coleção.
6. Selo fino "Ilustração" quando a imagem for de IA (honestidade visual).

---

## MODELO 1 — Vitrine (centralizado, utilidade)

Quando usar: ferramentas, listas práticas, tutoriais, "N sites/apps/dicas que...".

### Anatomia (1080x1350, de cima para baixo, tudo centralizado)

| Zona | Conteúdo | Especificação |
|---|---|---|
| Kicker | `NN • NOME DA COISA` | caps, letter-spacing largo, ~26px |
| Título | 2 linhas MAIÚSCULAS | condensado ultra-bold, ~110-130px; 1 linha clara + 1 linha na COR DE DESTAQUE |
| Subtítulo | 1-2 frases de apoio | ~40px, semibold, branco suave |
| Imagem | render 3D central | miolo da lâmina; fundo preto da imagem funde com o canvas |
| Caixa info | "COMO ABRIR"/"COMO FAZER" | pill do título no destaque, URL grande bold, passos curtos, nota fina; borda arredondada |
| Rodapé | hairline + @handle + marca | handle esquerda ~24px, marca central bold |

Capa leva `Arraste e descubra →`. Recap = "SALVE ESTE POST" com lista rótulo→detalhe.

### Estrutura narrativa

| # | Papel | Fórmula |
|---|---|---|
| 1 | Capa — curiosidade | número + promessa + palavra destacada. `Arraste e descubra →` |
| 2..N-2 | Conteúdo | kicker numerado; título = benefício visual; sub = o que fazer; caixa prática |
| N-1 | Recap | "SALVE ESTE POST" + lista item→nome |
| N | CTA | SIGA @handle / produto / link + pergunta de engajamento |

---

## MODELO 2 — Imersivo (full-bleed, esquerda, storytelling)

Quando usar: temas emocionais/narrativos — histórias, memória, transformação, antes/depois,
lifestyle. O carrossel vira uma "jornada" e cada lâmina puxa a próxima.

### Anatomia (1080x1350; imagem cobre TUDO; texto em coluna à esquerda ~55%)

| Zona | Conteúdo | Especificação |
|---|---|---|
| Fundo | imagem cinematográfica full-bleed | terço esquerdo escurecido (scrim) para o texto |
| Kicker | pílula PREENCHIDA na cor destaque | `TEMA · SUBTEMA`, caps, texto contrastante, topo-esquerda |
| Título | 1-2 linhas à esquerda | condensado ultra-bold ~90-110px, creme; linha com `destaque` vira TEXTO ESCURO SOBRE CAIXA PREENCHIDA (efeito marca-texto) |
| Pílula URL | retângulo preenchido | URL em fonte mono bold, logo abaixo do título |
| Benefício | 1 linha na cor destaque clara | "Ache o batismo do seu bisavô", bold ~38px |
| Corpo | 2-3 parágrafos curtos OU passos numerados (1,2,3 em círculos) | branco ~34px, separados por linhas finas |
| Caixa dica | pílula preenchida com ⚡ | conselho prático de 1-2 linhas, texto contrastante bold |
| Rodapé | @handle + pílula `Próximo: <teaser> »` + marca | o teaser é o GANCHO BINGE — obrigatório em toda lâmina de conteúdo |
| Progresso | barra segmentada na base | N segmentos, preenchidos até a lâmina atual |

### Estrutura narrativa

| # | Papel | Fórmula |
|---|---|---|
| 1 | Capa — dor/desejo emocional | "AS HISTÓRIAS DA SUA FAMÍLIA / NÃO PRECISAM / [SE PERDER]" + sub com número em destaque + botão `Arraste pro lado »` |
| 2..N-2 | Conteúdo | kicker tema·subtema; título = NOME da coisa; pílula URL; benefício; 2-3 parágrafos ou passos; dica ⚡; teaser `Próximo:` |
| N-1 | Recap | título-cenário ("SALVA ANTES DO PRÓXIMO ALMOÇO DE FAMÍLIA") + lista nome→desc→pílula URL + caixa pedindo COMPARTILHAMENTO ("Manda pra quem...") |
| N | CTA | "CONTINUA NO @MARCA" + o que tem lá + URL em pílula + pergunta de engajamento com 👇 |

Diferenças-chave vs Modelo 1: teasers "Próximo:" encadeando as lâminas; recap pede
compartilhar (não salvar); tom emocional; texto à esquerda; cor de destaque usada em
ELEMENTOS PREENCHIDOS (pílulas/caixas), não só em letras.

---

## Paleta

| Papel | Vencedores (referência) | Padrão desta skill |
|---|---|---|
| Fundo | preto texturizado #0A0A0A | #0A0A0A |
| Título linha clara | creme #F5EFE6 | #F5EFE6 |
| Destaque | dourado #F2C14E / amarelo #F5B301 | **vinho #7A1F2D** (troque pela cor da marca do usuário) |
| Destaque claro (texto pequeno) | — | #A83245 |
| Corpo/subtítulo | branco #EDEDED | #EDEDED |
| Nota fina | cinza #9A9A9A | #9A9A9A |

Contraste: vinho #7A1F2D sobre preto funciona em texto GRANDE; em texto pequeno use
#A83245 ou branco. Em pílulas preenchidas o `montar_slide.py` decide sozinho a cor do
texto (claro sobre vinho, escuro sobre amarelo) pela luminância do preenchimento.

## Templates de prompt de imagem (inglês, SEM texto na imagem)

### Modelo 1 — Vitrine

```
Photorealistic 3D render, premium museum-exhibit style: {OBJETO} displayed on a round
dark pedestal on a dark reflective surface, {DETALHE}. Pure black background, dramatic
{COR_LUZ} rim lighting and soft under-glow, subtle floor reflections, shallow depth of
field, cinematic contrast, hyper-detailed, 8k product photography look. No text, no
letters, no watermark. Vertical composition with empty dark space at top and bottom.
```

### Modelo 2 — Imersivo

```
Cinematic photorealistic scene filling the entire frame: {CENA} arranged on the RIGHT
side of a {SUPERFICIE} — {OBJETOS}. Warm {COR_LUZ} practical lighting, nostalgic
emotional atmosphere, rich textures, shallow depth of field, 8k editorial photography.
The LEFT third of the frame is dark, clean and out of focus, reserved as negative space.
No text, no letters, no watermark. Vertical portrait composition.
```

- `{COR_LUZ}`: paleta dourada → `amber-gold` | paleta vinho → `deep burgundy wine-toned`
- Modelo 2, `{OBJETOS}`: inclua um celular/notebook mostrando a interface citada quando a
  lâmina fala de um app/site (sem texto legível — "blurred generic interface").
- Capa M2: cena-símbolo da dor/desejo. Recap M2: todos os objetos do carrossel reunidos.
  CTA M2: mesa da marca (notebook + caderno + caneca).

## Exemplo de slides.json (campos por modelo)

```json
{
  "tema": "Nome do Tema", "handle": "@perfil", "marca": "Marca",
  "modelo": 2, "saida": "finais",
  "paleta": {
    "fundo": "#0A0A0A", "titulo": "#F5EFE6", "destaque": "#7A1F2D",
    "destaque_claro": "#A83245", "texto": "#EDEDED", "nota": "#9A9A9A"
  },
  "slides": [
    {
      "arquivo": "01.png",
      "titulo": [
        {"texto": "SUAS RECEITAS DE FAMÍLIA", "destaque": false},
        {"texto": "NÃO PRECISAM", "destaque": false},
        {"texto": "SE PERDER", "destaque": true}
      ],
      "subtitulo": "7 jeitos de guardar e contar essa história.",
      "botao": "Arraste pro lado »",
      "imagem": "imagens/01.png"
    },
    {
      "arquivo": "02.png",
      "kicker": "ORIGEM · REGISTROS",
      "titulo": [{"texto": "FAMILYSEARCH", "destaque": false}],
      "url": "familysearch.org",
      "beneficio": "Ache o batismo do seu bisavô",
      "paragrafos": [
        "Registros antigos de batismo, casamento e óbito.",
        "Tudo digitalizado, com busca por nome."
      ],
      "dica": "Comece pelo nome e pela cidade de quem você procura.",
      "proximo": "quem chegou de navio",
      "imagem": "imagens/02.png"
    },
    {
      "arquivo": "03.png",
      "kicker": "DOCUMENTOS · IA",
      "titulo": [{"texto": "TRANSKRIBUS", "destaque": false}],
      "url": "transkribus.org",
      "beneficio": "Lê aquela letra que ninguém entende",
      "passos": [
        "Manda a foto da carta ou documento.",
        "A IA transcreve a caligrafia em texto.",
        "Site em inglês. Cadastro grátis."
      ],
      "dica": "Confira o resultado com o original.",
      "proximo": "dá cor à foto",
      "imagem": "imagens/03.png"
    },
    {
      "arquivo": "08.png",
      "titulo": [
        {"texto": "SALVA ANTES DO PRÓXIMO", "destaque": false},
        {"texto": "ALMOÇO DE FAMÍLIA", "destaque": false}
      ],
      "lista": [
        ["FamilySearch", "batismos antigos", "familysearch.org"],
        ["Transkribus", "lê letra antiga", "transkribus.org"]
      ],
      "dica": "Manda pra quem guarda as fotos da família.",
      "proximo": "continua na marca",
      "imagem": "imagens/08.png"
    }
  ]
}
```

Campos do Modelo 1 (com `"modelo": 1` no topo): `kicker`, `titulo`, `subtitulo`, `imagem`,
`caixa {titulo,url,passos,nota}`, `lista [[rotulo,detalhe],...]`, `rodape_extra`.
`modelo` também pode ser definido por lâmina (sobrepõe o global).
