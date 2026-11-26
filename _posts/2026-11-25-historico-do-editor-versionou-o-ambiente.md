---
layout: post
title: "O histórico do editor versionou o ambiente porque o ignore só cobria o nome .env"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-178"
description: "O commit da versão 0.12.9 levou cópias do arquivo de ambiente feitas pelo histórico local do editor. A regra que ignora .env não alcança um nome com carimbo na frente da extensão, dentro de outra pasta."
date: 2026-11-25 00:00:00-03:00
categories: devlog
category: seguranca
tags: [git, gitignore, ambiente, editor]
---

# O histórico do editor versionou o ambiente porque o ignore só cobria o nome .env

> [!NOTE]
> **Resumo Executivo (DEV-2026-178)**: O commit da versão 0.12.9 levou cópias do arquivo de ambiente feitas pelo histórico local do editor. A regra que ignora .env não alcança um nome com carimbo na frente da extensão, dentro de outra pasta.

---

### 🚨 O Desafio Técnico / Contexto
.gitignore lista .env, .env.backup e .env.production. O editor gravou cópias em .history com o nome .env seguido de um carimbo numérico. Esse caminho não é o arquivo .env, então o git add incluiu as três cópias no commit bdad9f6.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Um padrão sem barra, como .env, casa com esse nome de arquivo em qualquer pasta. Não casa com .env_ e um carimbo. .env.backup também não cobre esse sufixo.
* 💡 A pasta .history não estava no ignore. Três caminhos .history/.env_ mais carimbo passaram a ser rastreados. O conteúdo não entra neste registro.
* 💡 A regra que fecha o buraco é ignorar a pasta .history/. Apagar só a cópia de trabalho não tira o arquivo do commit em que ele já entrou.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
.history/
```

---

### 📈 Impacto no Ecossistema & Valor Prático
As três cópias continuam no commit até saírem do índice do git. Ignorar .env não as alcança.

* **Projetos Relacionados**: `monitoramento-app`
* **Registro de Origem**: `_data/daily.dev-33.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
