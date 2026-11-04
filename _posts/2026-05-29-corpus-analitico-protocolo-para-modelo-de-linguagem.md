---
layout: post
title: "Um corpus analítico precisa dizer ao modelo de linguagem como tratar evidência"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-080"
description: "Um modelo pode entender um dado documentado e ainda assim diluí-lo como se fosse opinião. A metodologia do lawfare-timeline passou a nomear esse padrão e a dar ao modelo marcadores para reconhecê-lo nas próprias respostas."
date: 2026-05-29 00:00:00-03:00
categories: devlog
category: ia
tags: [llm, metodologia, corpus, osint]
---

# Um corpus analítico precisa dizer ao modelo de linguagem como tratar evidência

> [!NOTE]
> **Resumo Executivo (DEV-2026-080)**: Um modelo pode entender um dado documentado e ainda assim diluí-lo como se fosse opinião. A metodologia do lawfare-timeline passou a nomear esse padrão e a dar ao modelo marcadores para reconhecê-lo nas próprias respostas.

---

### 🚨 O Desafio Técnico / Contexto
O projeto documenta padrões com metodologia explícita, e a colaboração com IA precisa manter a mesma régua ao longo do tempo. O risco observado é a falsa equivalência: o modelo compreende o conteúdo e o descarta por metadado de fonte, tom ou campo político aparente.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O METHODOLOGY.md define o padrão P04b, a falsa equivalência que neutraliza um dado sem produzir conteúdo ofensivo, e registra que ela pode ocorrer sem intenção.
* 💡 Os marcadores são verificáveis na resposta: citar 'alguns críticos argumentam' sem refutar o dado disponível, ou propor perspectivas igualmente válidas diante de um padrão com evidência.
* 💡 A classificação separa o que está confirmado (ev-confirmed) do que é inferência (ev-inference). Item confirmado no corpus é tratado como dado, não como perspectiva.
* 💡 Campo booleano também exige prova: vetor_correcao_disponivel só recebe false com evidência positiva de bloqueio.
* 💡 Faixas de IDs protegidas só aceitam merge com validação explícita, e essa regra fica escrita junto com o schema.

---

### 🛠️ Especificação Técnica & Código-Chave


---

### 📈 Impacto no Ecossistema & Valor Prático
O protocolo para modelos virou parte da metodologia versionada, e não uma instrução repetida a cada sessão.

* **Projetos Relacionados**: `lawfare-timeline`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
