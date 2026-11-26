---
layout: post
title: "Catálogo de tema copiava a cor crua e o cockpit pintava status com o destaque"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-167"
description: "O gerador do catálogo gravava as cores do JSON sem piso, e o cockpit usava a cor de destaque para sucesso, erro e texto de apoio. O piso passou a valer nos dois fundos, e o texto apagado passou a sair do texto principal."
date: 2026-11-23 00:00:00-03:00
categories: devlog
category: frontend
tags: [css, contraste, temas, wcag]
---

# Catálogo de tema copiava a cor crua e o cockpit pintava status com o destaque

> [!NOTE]
> **Resumo Executivo (DEV-2026-167)**: O gerador do catálogo gravava as cores do JSON sem piso, e o cockpit usava a cor de destaque para sucesso, erro e texto de apoio. O piso passou a valer nos dois fundos, e o texto apagado passou a sair do texto principal.

---

### 🚨 O Desafio Técnico / Contexto
Em tools/scripts/build-theme-catalog.py o catálogo copiava o JSON do tema como estava. No ui-cockpit, apply.ts punha foreground.secondary em --straw e foreground.muted em --sio-muted e --fog. Num tema escuro de mar, o secundário é o verde de sucesso, então o rótulo saía verde. theme.css mandava text-emerald, text-rose e text-amber para --sio-accent, e o hover misturava o destaque com --sio-fg. A mistura de 78% do texto com o fundo da página deixava o texto apagado do tema de faroeste em 4,27:1 sobre o cartão, que usa background.secondary.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O piso é medido em background.primary e em background.secondary. Texto, aviso e destaque ficam em 4,5:1. Sucesso, erro e perigo ficam em 5:1. O gerador recusa o catalog.json se algum par ficar abaixo.
* 💡 Texto de apoio não usa a cor semântica. --sio-muted e --fog saem de color-mix com 80% de --sio-fg sobre --sio-bg. Com 78% um cartão ficava em 4,27:1. Com 80% os 22 temas passaram de 4,5:1 na página e no cartão.
* 💡 Sucesso, erro e aviso têm token próprio. Se o piso cola o sucesso no destaque, o gerador empurra o matiz e mede de novo. O hover do botão mistura o destaque com preto ou branco conforme a luminância da tinta, não com a cor do texto da página.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
const muted = "color-mix(in srgb, var(--sio-fg) 80%, var(--sio-bg))";
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Erro, ok e destaque deixam de sair na mesma cor, e o texto de apoio deixa de herdar o verde do tema.

* **Projetos Relacionados**: `sio-ecosystem`
* **Registro de Origem**: `_data/daily.dev-31.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
