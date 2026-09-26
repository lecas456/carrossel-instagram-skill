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

## Passo 1 — Paleta de cores

Padrão da skill: **fundo preto (#0A0A0A) + destaque vinho (#7A1F2D)**. Se o usuário tiver
logomarca ou manual de marca, ofereça extrair a cor de destaque dela. SEMPRE confirme com
AskUserQuestion antes de seguir:

1. **(Recomendado)** Cor da marca como destaque + off-white (#F5EFE6) no restante do título —
   equivale ao papel do dourado nos carrosséis de referência e garante leitura no feed.
   Cores escuras em texto pequeno sobre preto têm contraste baixo.
2. Tudo na cor de destaque (avise do contraste se ela for escura).
3. Outra paleta (usuário informa).

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

Apresente o roteiro completo (título + subtítulo/corpo de cada lâmina + teasers) em texto
e valide com o usuário antes de gerar qualquer imagem.

## Passo 4 — Prompts de imagem

Para cada lâmina, gere um prompt em INGLÊS usando o template do modelo escolhido em
`references/estilo-visual.md` (seção "Templates de prompt"). Regras de ouro:

- **Modelo 1:** objeto 3D em pedestal, fundo PRETO ABSOLUTO (funde com o canvas),
  luz dramática. A imagem ocupa só o miolo da lâmina.
- **Modelo 2:** cena cinematográfica FULL-FRAME (vira o fundo inteiro da lâmina),
  objetos principais à DIREITA, terço esquerdo escuro e limpo para receber o texto,
  atmosfera quente e emocional. Telas de celular/notebook podem mostrar a interface citada.
- Cor da luz conforme a paleta do Passo 1 (dourado âmbar OU vinho/borgonha).
- A imagem NÃO deve conter texto — todo texto é aplicado depois pelo `montar_slide.py`.
- Formato retrato 1024x1536.

Salve todos os prompts em `<pasta do tema>/prompts.md` (um bloco por lâmina, numerado).

## Passo 5 — Geração das imagens

1. Procure a chave: variável de ambiente `OPENAI_API_KEY`, depois arquivo `.env` no diretório
   de trabalho (linha `OPENAI_API_KEY=...`). NUNCA imprima a chave no chat.
2. Se não achar, peça ao usuário para colar a chave num `.env` (explique: criar arquivo `.env`
   com `OPENAI_API_KEY=sk-...`). Se ele não quiser, siga SEM imagens (Modelo 1 aguenta
   lâminas só tipográficas; no Modelo 2 o fundo vira o preto texturizado).
3. **Qualidade: use `low` (o padrão do script).** Só suba para `medium` se o usuário pedir
   mais qualidade — e nesse caso proponha a troca informando os preços médios (gpt-image-1,
   1024x1536): low ≈ US$ 0,016/imagem (carrossel de 9 ≈ US$ 0,14) e medium ≈ US$ 0,063/imagem
   (carrossel de 9 ≈ US$ 0,57). Dica de fluxo: rascunhe tudo em low e regenere em medium
   apenas as lâminas aprovadas.
4. Com chave, rode para cada lâmina:
   `python <skill>/scripts/gerar_imagem.py --prompt-file <arquivo.txt> --out "<tema>/imagens/NN.png"`
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
   numeração/teasers certos, barra de progresso coerente (Modelo 2). Ajuste o JSON e
   rode de novo se preciso.

## Passo 7 — Entrega

Organize tudo em uma pasta com o nome do tema (no diretório de trabalho do usuário):

```
<Nome do Tema>/
  finais/        01.png ... NN.png  ← artes prontas para postar
  imagens/       NN.png             ← imagens brutas da IA
  prompts.md
  slides.json
```

Liste para o usuário todos os arquivos gerados (caminhos clicáveis), na ordem de postagem,
e entregue de bônus uma sugestão de legenda com hashtags do nicho.
