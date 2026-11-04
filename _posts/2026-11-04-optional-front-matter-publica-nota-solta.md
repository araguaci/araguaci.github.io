---
layout: post
title: "Com jekyll-optional-front-matter, nota solta no repositório pode virar página pública"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-110"
description: "O plugin faz o Jekyll tratar arquivo Markdown sem front matter como página. Por isso, as notas pessoais ficaram numa pasta fora do repositório do site."
date: 2026-11-04 00:00:00-03:00
categories: devlog
category: devops
tags: [jekyll, privacidade, markdown, notas]
---

# Com jekyll-optional-front-matter, nota solta no repositório pode virar página pública

> [!NOTE]
> **Resumo Executivo (DEV-2026-110)**: O plugin faz o Jekyll tratar arquivo Markdown sem front matter como página. Por isso, as notas pessoais ficaram numa pasta fora do repositório do site.

---

### 🚨 O Desafio Técnico / Contexto
Era preciso decidir onde guardar as notas de trabalho, e o repositório do site era um lugar possível. No site, com jekyll-optional-front-matter ativo, um .md solto pode sair publicado como página, ainda que não tenha cabeçalho.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Não ter front matter não torna um arquivo privado: com o plugin, o .md vira página renderizada. Só o que está no exclude ou fora da pasta fica de fora do build.
* 💡 A pasta de notas foi para fora do repositório. Depender de uma lista exclude é arriscado, porque um novo arquivo fora da lista já seria publicado.
* 💡 Antes de guardar texto privado em um repositório de site, confira os plugins ativos no _config.yml.

---

### 🛠️ Especificação Técnica & Código-Chave


---

### 📈 Impacto no Ecossistema & Valor Prático
As notas ficam fora do alcance do build do site, sem depender de uma lista de exclusão.

* **Projetos Relacionados**: `artesdosul`, `segundo-cerebro`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
