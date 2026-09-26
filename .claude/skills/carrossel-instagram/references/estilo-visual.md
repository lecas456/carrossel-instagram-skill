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
7. **Imagem grande e VIVA**: a imagem ocupa boa parte da lâmina, com cores ricas e bem
   iluminada. NUNCA escurecer nem encolher a imagem para "caber" — o script já corta e
   esfuma as bordas. Texto por cima da imagem é permitido, desde que continue legível
   (o layout garante o fundo escuro atrás do texto onde precisa).
8. **A imagem ilustra o card ao pé da letra**: "custa caro" → etiqueta de preço rasgada;
   curso online de enfermagem → notebook exibindo a aula. Nada de imagem genérica.
9. **Sem contador de páginas** ("1/10"): nas referências ele era da interface do
   Instagram (eram prints), NÃO faz parte da arte. Não desenhar.
10. **Sem emoji nos textos das lâminas** — as fontes não renderizam (viram quadrados).
    Emoji só na legenda do post.
11. **Recap sempre com imagem**: uma composição reunindo todos os objetos do carrossel;
    lista sozinha deixa a lâmina vazia.

---

## MODELO 1 — Vitrine (centralizado, utilidade)

Quando usar: ferramentas, listas práticas, tutoriais, "N sites/apps/dicas que...".

### Anatomia (1080x1350, de cima para baixo, tudo centralizado)

| Zona | Conteúdo | Especificação |
|---|---|---|
| Kicker | `NN • NOME DA COISA` | caps, letter-spacing largo, ~26px |
| Título | 2 linhas MAIÚSCULAS | condensado ultra-bold, ~110-130px; 1 linha clara + 1 linha na COR DE DESTAQUE |
| Subtítulo | 1-2 frases de apoio | ~40px, semibold, branco suave |
| Imagem | cena horizontal viva | cobre a LARGURA TODA do card (gerar em paisagem 1536x1024); o script corta o excesso de altura e esfuma as bordas; nunca escurecer |
| Caixa info | "COMO ABRIR"/"COMO FAZER" | pill do título no destaque, URL grande bold, passos curtos (MÁX. 2 linhas), nota fina (MÁX. 1 linha — o script corta além disso); borda arredondada |
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
| Fundo | imagem cinematográfica full-bleed | terço esquerdo escurecido (scrim) + o script desenha um painel de sombra preta seguindo o contorno do texto, na frente da imagem, para legibilidade — intensidade via `sombra_texto` no json (1.0 padrão; maior = mais escuro; 0 = desliga) |
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
| N | CTA | "CONTINUA NO @MARCA" + o que tem lá + URL em pílula + pergunta de engajamento (sem emoji — fontes não renderizam) |

Diferenças-chave vs Modelo 1: teasers "Próximo:" encadeando as lâminas; recap pede
compartilhar (não salvar); tom emocional; texto à esquerda; cor de destaque usada em
ELEMENTOS PREENCHIDOS (pílulas/caixas), não só em letras.

---

## MODELO 3 — Post Único (estilo tweet, opinião/autoridade)

Quando usar: opinião forte, posicionamento, frase de autoridade, reação a notícia do
nicho. É UMA arte só, sem imagem de IA — o poder está no texto. Referência: posts de
"print de tweet" com alto compartilhamento.

### Anatomia (1080x1350, fundo BRANCO #FFFFFF)

| Zona | Conteúdo | Especificação |
|---|---|---|
| Cabeçalho | foto de perfil circular + nome + @usuario | avatar ~128px no topo-esquerda; nome bold escuro; @ em cinza |
| Texto | a mensagem | DM Sans regular, GRANDE (~64px, auto-ajuste), preto #111 sobre branco, alinhado à esquerda |
| Punchline | último parágrafo, separado por linha em branco | 1 linha seca que fecha o raciocínio ("Aqui se faz, aqui se paga.") |

Sem rodapé, sem logo, sem hashtag, sem emoji — a força do formato é parecer um
pensamento cru, não uma arte produzida.

### Fórmula de escrita

1. **Afirmação forte e específica** (3-6 linhas curtas na arte): um fato ou opinião
   que o público do nicho sente mas não verbaliza. Números concretos aumentam o peso
   ("apostou 30 milhões", "curso com certificado de graça").
2. **Punchline de UMA linha** como parágrafo final: fecho seco, quase provérbio.
3. Tom de conversa, primeira pessoa opcional, zero jargão institucional.

### JSON (lâmina)

```json
{
  "arquivo": "post.png", "modelo": 3,
  "nome": "Nome de Exibição", "usuario": "@usuario",
  "avatar": "avatar.jpg",
  "texto": "Afirmação forte em poucas linhas.\n\nPunchline de uma linha."
}
```

Sem `avatar`, o script desenha um círculo na cor de destaque com a inicial do nome.

---

## Paleta

| Papel | Vencedores (referência) | Padrão desta skill |
|---|---|---|
| Fundo | preto texturizado | **preto puro #000000** (vinheta sutil do script; nada de cinza) |
| Título linha clara | creme #F5EFE6 | #F5EFE6 |
| Destaque | dourado #F2C14E / amarelo #F5B301 | **vinho #7A1F2D** (troque pela cor da marca do usuário) |
| Destaque claro (textos) | — | #C8374F |
| Corpo/subtítulo | branco #EDEDED | #EDEDED |
| Nota fina | cinza #9A9A9A | #9A9A9A |

Contraste — regra prática: cores de destaque ESCURAS (vinho #7A1F2D, bordô #6B1F2E)
somem no fundo preto quando usadas em TEXTO, inclusive em título. Sempre cheque a
luminância antes de fechar a paleta e proponha ao usuário uma versão mais acesa para
textos (ex.: bordô #6B1F2E → #C8374F), mantendo a escura em preenchimentos se ele quiser.
O `montar_slide.py` já se protege sozinho: se `destaque` for escuro, os textos de
destaque usam `destaque_claro` automaticamente; e em pílulas preenchidas ele decide a
cor do texto (claro sobre vinho, escuro sobre amarelo) pela luminância do preenchimento.

## Tipografia

- **Anton** (incluída em `fonts/`) em TUDO que é impactante: títulos, kickers do Modelo 2,
  números dos passos, pílulas de destaque, URLs grandes.
- **DM Sans** (incluída em `fonts/`) nas escritas secundárias: subtítulos, parágrafos,
  notas, rodapé, kicker do Modelo 1.
- Pílula de URL do Modelo 2 fica em fonte mono (estilo "endereço digitável").
- O script resolve tudo sozinho pela pasta `fonts/`; não é preciso instalar nada.

## Templates de prompt de imagem (inglês, SEM texto na imagem)

### Modelo 1 — Vitrine (gerar em PAISAGEM, `--size 1536x1024`)

```
Photorealistic cinematic scene on a dark wooden table: {OBJETOS} — several objects
directly related to {ASSUNTO}, arranged naturally and filling most of the frame,
brightly lit with warm {COR_LUZ} light, rich vivid colors. Dark background with a
blurred bookshelf fading into black at the edges. Shallow depth of field, hyper-detailed,
8k editorial product photography. No text, no letters, no watermark. HORIZONTAL
landscape composition.
```

- Cena, não objeto isolado: NADA de "um objeto num pedestal com fundo preto absoluto" —
  isso deixa a lâmina vazia e apagada. Vários objetos do assunto, sobre mesa/bancada,
  ocupando boa parte do quadro.
- Se a lâmina cita um site/app, um dos objetos é um notebook ou celular exibindo uma
  interface genérica desfocada ("blurred generic interface, no readable text").

### Modelo 2 — Imersivo (gerar em RETRATO, `--size 1024x1536`)

```
Cinematic photorealistic scene filling the entire frame: {CENA} on a {SUPERFICIE} —
{OBJETOS}, with the main subjects placed right of center. Warm {COR_LUZ} practical
lighting, emotional atmosphere, rich vivid textures, shallow depth of field, 8k
editorial photography. No text, no letters, no watermark. Vertical portrait composition.
```

- A cena pode ocupar o quadro inteiro — o script escurece a área do texto (scrim), então
  não é preciso deixar o lado esquerdo vazio; basta os assuntos principais tenderem à direita.

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
  "sombra_texto": 1.0,
  "paleta": {
    "fundo": "#000000", "titulo": "#F5EFE6", "destaque": "#7A1F2D",
    "destaque_claro": "#C8374F", "texto": "#EDEDED", "nota": "#9A9A9A"
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
