---
layout: post
title: "A descrição do dossiê saturava o ranking porque alcance e sinergia liam o mesmo texto"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-148"
description: "O primeiro passe do ranking de showcase pôs quase todo dossiê longo acima de 85. A descrição repetia as mesmas palavras de alcance e de ecossistema, e a nota automática deixou de ler esse parágrafo."
date: 2026-11-10 00:00:00-03:00
categories: devlog
category: conteudo
tags: [python, ranking, corpus, showcase]
---

# A descrição do dossiê saturava o ranking porque alcance e sinergia liam o mesmo texto

> [!NOTE]
> **Resumo Executivo (DEV-2026-148)**: O primeiro passe do ranking de showcase pôs quase todo dossiê longo acima de 85. A descrição repetia as mesmas palavras de alcance e de ecossistema, e a nota automática deixou de ler esse parágrafo.

---

### 🚨 O Desafio Técnico / Contexto
rank_showcase_candidates.py aplica os pesos editoriais de 2026-10-08: prontidão 20%, diferenciação 20%, alcance 25%, sinergia 20% e profundidade 15%. No primeiro passe, o texto corrido do HTML entrava no alcance e na sinergia ao mesmo tempo. O lead repete Brasil e global, então peça pronta e ensaio parecido recebiam a mesma força.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 score_alcance usa só o conjunto de tokens do slug, do título e das tags. A descrição fica de fora porque o lead saturava o eixo.
* 💡 cluster_for escolhe o cluster com mais acertos de palavra. O slug pesa três, e título e tags pesam um. O corpo do HTML não vota.
* 💡 ecosystem_hits, que alimenta a sinergia, lê o mesmo trio. Um dossiê longo deixa de parecer ligado a todos os nós só porque o parágrafo cita o ecossistema.
* 💡 O que já está em portfolio.json ou em portfolio-todos.json sai da fila. A força automática é proxy de arquivo e fica abaixo da nota editorial, que leu o dossiê inteiro.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
alcance_tokens = tokens(" ".join([item["slug"], title, *tag_text]))
cluster = cluster_for(item["slug"], title, tag_text)
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O ranking volta a separar card novo de ensaio parecido, e a fila deixa de fora o que o showcase já publicou.

* **Projetos Relacionados**: `gosurf.site`
* **Registro de Origem**: `_data/daily.dev-25.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
