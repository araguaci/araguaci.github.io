---
layout: post
title: "Meia-noite em UTC com o site em São Paulo publica o artigo um dia antes"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-111"
description: "O gerador do diário gravava a data à meia-noite em UTC, e o site usa o fuso de São Paulo, então a URL e a data exibida recuavam um dia. A data passou a ser gravada com o fuso do site, e as URLs já publicadas viraram redirecionamentos."
date: 2026-11-04 00:00:00-03:00
categories: devlog
category: devops
tags: [jekyll, timezone, redirect, github-pages]
---

# Meia-noite em UTC com o site em São Paulo publica o artigo um dia antes

> [!NOTE]
> **Resumo Executivo (DEV-2026-111)**: O gerador do diário gravava a data à meia-noite em UTC, e o site usa o fuso de São Paulo, então a URL e a data exibida recuavam um dia. A data passou a ser gravada com o fuso do site, e as URLs já publicadas viraram redirecionamentos.

---

### 🚨 O Desafio Técnico / Contexto
O arquivo do artigo tinha o nome 2026-10-12-... e o site respondia em /2026-10-11-..., com 'Posted on October 11'. O nome do arquivo e o YAML estavam certos, por isso o erro só apareceu ao olhar a URL gerada no build.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O Jekyll usa a data do front matter, e não a do nome do arquivo, para montar o :day do permalink. O valor 00:00:00+00:00 convertido para America/Sao_Paulo cai às 21h do dia anterior.
* 💡 Gravar 00:00:00-03:00 mantém o dia nas duas pontas. O teste precisa olhar a URL gerada, porque validar o YAML e o nome do arquivo não pega esse erro.
* 💡 Corrigir a data muda URLs já publicadas. O jekyll-redirect-from mantém as antigas respondendo, e a página de redirecionamento não entra no sitemap.
* 💡 O gerador regrava os artigos, então a correção também precisa estar nele. Se ficasse só nos arquivos, uma nova importação desfaria o ajuste.
* 💡 Só os artigos que já estavam no ar ganharam redirecionamento. Os ainda não publicados não têm URL antiga a preservar.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
date: 2026-10-01 00:00:00-03:00
redirect_from: /2026-09-30-armadilha-vendor-bundle-jekyll-exclude/
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A URL e a data exibida passam a mostrar o dia do aprendizado, sem quebrar os links já publicados.

* **Projetos Relacionados**: `araguaci.github.io`
* **Registro de Origem**: `_data/daily.dev-18.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
