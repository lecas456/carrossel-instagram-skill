---
name: carrossel-instagram
description: Roteiro completo para criar carrosséis profissionais de Instagram (7 a 9 lâminas 1080x1350) em dois modelos visuais — Vitrine (imagem central estilo museu) e Imersivo (imagem de fundo inteira com texto à esquerda). Use quando o usuário pedir para criar um carrossel, post em carrossel, sequência de slides para Instagram, ou mencionar "roteiro de carrossel". Cobre paleta, tema com pesquisa de tendências, estrutura de engajamento, prompts de imagem, geração via OpenAI (gpt-image-1) e montagem final com Pillow.
---

# Carrossel de Instagram — Roteiro de Execução

Você vai executar este roteiro de ponta a ponta. Siga os passos NA ORDEM. Antes de começar,
leia `references/estilo-visual.md` (anatomia dos DOIS modelos visuais e templates de prompt,
calibrados em carrosséis reais de alto engajamento). Se existir no diretório de trabalho
uma pasta de exemplos com screenshots de carrosséis de referência (ex.: `Carrossel Vencedor*`),
consulte as imagens para calibrar ainda mais o estilo — mas a skill funciona sem ela.

Scripts desta skill (rodar com `python`):
- `scripts/gerar_imagem.py` — gera 1 imagem via API OpenAI (gpt-image-1), só stdlib.
- `scripts/montar_slide.py` — compõe as lâminas finais 1080x1350 (Pillow) a partir de um
  `slides.json`. Suporta os dois modelos (`"modelo": 1` ou `2`).

## Passo 0 — Contexto do perfil (antes de qualquer padrão)

Procure no diretório de trabalho arquivos de contexto/estratégia do perfil
(`CONTEXTO*`, `briefing*`, `estrategia*`, manual de marca, `CLAUDE.md` com dados do perfil).
Se existirem, leia ANTES de tudo: paleta, tom de voz e roteiro definidos ali têm
PRIORIDADE sobre os padrões desta skill. Só ofereça os padrões abaixo no que o contexto
não cobrir.

## Passo 1 — Paleta de cores

Padrão da skill: **fundo preto (#0A0A0A) + destaque vinho (#7A1F2D)**. Se o usuário tiver
logomarca ou manual de marca, ofereça extrair a cor de destaque dela. SEMPRE confirme com
AskUserQuestion antes de seguir:

1. **(Recomendado)** Cor da marca como destaque + off-white (#F5EFE6) no restante do título —
   equivale ao papel do dourado nos carrosséis de referência e garante leitura no feed.
2. Tudo na cor de destaque (avise do contraste se ela for escura).
3. Outra paleta (usuário informa).

**Cheque o contraste antes de fechar:** cores de destaque escuras (vinho #7A1F2D,
bordô #6B1F2E) somem no fundo preto quando usadas em TEXTO. Se a cor escolhida for
escura, avise e proponha uma versão mais acesa para os textos (ex.: #6B1F2E → #C8374F),
definindo-a como `destaque_claro` no slides.json — os preenchimentos podem manter a
cor original. O `montar_slide.py` também aplica essa troca automaticamente por segurança.

Guarde a paleta escolhida; ela entra no `slides.json` e nos prompts de imagem
(se a luz da cena deve ser dourada ou em tons vinho/borgonha). Nos elementos PREENCHIDOS
do Modelo 2 (pílulas, caixas), o script escolhe sozinho texto claro ou escuro pelo contraste.

## Passo 2 — Tema do carrossel

1. Se ainda não souber, pergunte qual é a empresa/nicho do usuário e o @ do perfil.
2. Pesquise na internet (WebSearch) ANTES de sugerir: assuntos em alta no nicho,
   datas comemorativas próximas (use a data de hoje), campanhas sazonais
   (ex.: saúde → Outubro Rosa, Novembro Azul, Dia Mundial da Saúde).
3. Sugira 2–3 temas com uma linha de justificativa cada ("em alta porque...") e
   deixe o usuário escolher ou propor outro (AskUserQuestion, com sua sugestão
   principal marcada como recomendada).

## Passo 3 — Modelo visual e estrutura das lâminas

**3a. Escolha do modelo** (AskUserQuestion, recomende conforme o tema):

- **Modelo 1 — Vitrine:** texto centralizado, imagem 3D "peça de museu" no meio da lâmina,
  caixa de instrução "COMO FAZER". Melhor para temas de UTILIDADE: ferramentas, dicas,
  listas práticas, tutoriais.
- **Modelo 2 — Imersivo:** imagem cinematográfica cobrindo a lâmina INTEIRA, texto em coluna
  à esquerda, pílulas preenchidas, teaser "Próximo: ... »" no rodapé e barra de progresso.
  Melhor para temas EMOCIONAIS/narrativos: histórias, transformação, nostalgia, lifestyle.

Use UM modelo por carrossel (consistência é parte do que faz os vencedores funcionarem).

**3b. Objetivo:** pergunte (AskUserQuestion, multiSelect): ganhar seguidores / vender /
gerar salvamentos / compartilhamentos / levar para link. Isso define as 2 últimas lâminas.

**3c. Estrutura — 7 a 9 lâminas** (detalhes e fórmulas em `references/estilo-visual.md`):

- **Lâmina 1 (capa):** gancho de CURIOSIDADE (promessa numerada, dor ou pergunta).
  Modelo 1: "Arraste e descubra →". Modelo 2: dor emocional + botão "Arraste pro lado »".
- **Lâminas 2 a N-2 (conteúdo):** 1 ideia por lâmina. No Modelo 2, TODA lâmina termina
  com o teaser da próxima ("Próximo: ... »") — escreva esses ganchos com cuidado.
- **Lâmina N-1 (recap):** lista-resumo. Modelo 1 pede SALVAR; Modelo 2 pede COMPARTILHAR
  ("Manda pra quem...").
- **Lâmina N (CTA):** conforme o objetivo — seguir, comprar, acessar link.
  Termina com pergunta de engajamento.

Regras de texto: SEM emoji nos textos das lâminas (as fontes do script não renderizam —
viram quadrados; emoji só na legenda do post) e sem contador de páginas tipo "1/10"
(nas referências ele era da interface do Instagram, não da arte).

Apresente o roteiro completo (título + subtítulo/corpo de cada lâmina + teasers) em texto
e valide com o usuário antes de gerar qualquer imagem.

## Passo 4 — Prompts de imagem

Para cada lâmina, gere um prompt em INGLÊS usando o template do modelo escolhido em
`references/estilo-visual.md` (seção "Templates de prompt"). Regras de ouro:

- **Modelo 1 (PAISAGEM, `--size 1536x1024`):** CENA viva sobre mesa/bancada — vários
  objetos ligados ao assunto, bem iluminados, cores ricas, ocupando boa parte do quadro;
  fundo escuro com estante desfocada sumindo no preto nas bordas. NADA de objeto isolado
  em pedestal com fundo preto absoluto (fica vazio e apagado). A imagem cobre a largura
  toda do card, sem escurecimento.
- **Modelo 2 (RETRATO, `--size 1024x1536`):** cena cinematográfica FULL-FRAME (vira o
  fundo inteiro da lâmina), assuntos principais tendendo à direita — o script escurece a
  área do texto, então a cena pode ocupar o quadro todo.
- **A imagem ilustra o card ao pé da letra**: "custa caro" → etiqueta de preço rasgada;
  curso online → notebook exibindo a aula. Telas de celular/notebook mostram interface
  genérica desfocada, sem texto legível.
- **Recap:** composição reunindo todos os objetos do carrossel (lista sem imagem fica vazia).
- Cor da luz conforme a paleta do Passo 1 (dourado âmbar OU vinho/borgonha).
- A imagem NÃO deve conter texto — todo texto é aplicado depois pelo `montar_slide.py`.

Salve todos os prompts em `<pasta do tema>/prompts.md` (um bloco por lâmina, numerado).

## Passo 5 — Geração das imagens

1. Procure a chave: variável de ambiente `OPENAI_API_KEY`, depois arquivo `.env` no diretório
   de trabalho (linha `OPENAI_API_KEY=...`). NUNCA imprima a chave no chat.
2. Se não achar, peça ao usuário para colar a chave num `.env` (explique: criar arquivo `.env`
   com `OPENAI_API_KEY=sk-...`). Se ele não quiser, siga SEM imagens (Modelo 1 aguenta
   lâminas só tipográficas; no Modelo 2 o fundo vira o preto texturizado).
3. **Qualidade: use `low` (o padrão do script).** Low dá conta desde que o prompt peça
   cena viva e colorida (imagem apagada vem de prompt ruim/escurecimento, não da
   qualidade). Só suba para `medium` se o usuário pedir mais qualidade — e nesse caso
   proponha a troca informando os preços médios (gpt-image-1): low ≈ US$ 0,016/imagem
   (carrossel de 9 ≈ US$ 0,14) e medium ≈ US$ 0,063/imagem (carrossel de 9 ≈ US$ 0,57).
4. **Lâmina-piloto ANTES do lote:** gere a imagem de UMA lâmina representativa
   (`--size 1536x1024` no Modelo 1, `1024x1536` no Modelo 2), monte-a com o
   `montar_slide.py` e mostre ao usuário para aprovar o visual. Só depois da aprovação
   gere as imagens das demais lâminas — isso evita queimar uma rodada inteira de
   imagens com um estilo errado.
5. Com chave e piloto aprovado, rode para cada lâmina restante:
   `python <skill>/scripts/gerar_imagem.py --prompt-file <arquivo.txt> --size <do modelo> --out "<tema>/imagens/NN.png"`
   (aceita `--env-file` para apontar o `.env` e `--quality medium` para o upgrade).
   Rode em série; se uma falhar, tente 1 vez de novo e siga em frente sem ela,
   avisando no final.

## Passo 6 — Montagem final

1. Escreva `<pasta do tema>/slides.json` com `"modelo"`, paleta, handle, marca e as lâminas
   (formato documentado no topo de `scripts/montar_slide.py` e exemplificado em
   `references/estilo-visual.md`).
2. Rode: `python <skill>/scripts/montar_slide.py "<tema>/slides.json"` —
   gera as artes finais 1080x1350 em `<tema>/finais/`.
3. Confira visualmente (Read nas PNGs geradas). Cheque: título não cortado, contraste ok,
   numeração/teasers certos, barra de progresso coerente (Modelo 2), imagem ocupando a
   largura do card sem ficar apagada (Modelo 1). Ajuste o JSON e rode de novo se preciso.
4. **Ao refazer lâminas já entregues**, preserve a versão anterior movendo-a para uma
   subpasta (`<tema>/v1/`, `v2/`...) antes de sobrescrever — o usuário pode querer comparar.

## Passo 7 — Verificação e entrega

1. **Verifique as informações citadas**: todo site, URL, preço ou passo a passo que
   aparece nas lâminas deve ser conferido na fonte oficial (WebFetch/WebSearch) antes
   da entrega — nada de instrução inventada.
2. Escreva `<tema>/legenda-e-fontes.md` com: a legenda sugerida do post (aqui SIM pode
   emoji) + hashtags do nicho + a lista das fontes consultadas na verificação.
3. Organize tudo em uma pasta com o nome do tema (no diretório de trabalho do usuário):

```
<Nome do Tema>/
  finais/               01.png ... NN.png  ← artes prontas para postar
  imagens/              NN.png             ← imagens brutas da IA
  prompts.md
  slides.json
  legenda-e-fontes.md
  v1/                   (versões anteriores, quando houver refação)
```

Liste para o usuário todos os arquivos gerados (caminhos clicáveis), na ordem de postagem.
