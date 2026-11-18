---
layout: post
title: "Modal em branco no Tailwind 4: o fundo ficou opaco e cobriu o painel, sem nenhum erro no console"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-113"
description: "Clicar em um botão deixava a tela inteira de uma cor só, e o console não mostrava erro. Duas classes do Tailwind 3 tinham deixado de existir, e isso atingia todos os modais do sistema."
date: 2026-11-04 00:00:00-03:00
categories: devlog
category: frontend
tags: [tailwind, vue, css, modal]
---

# Modal em branco no Tailwind 4: o fundo ficou opaco e cobriu o painel, sem nenhum erro no console

> [!NOTE]
> **Resumo Executivo (DEV-2026-113)**: Clicar em um botão deixava a tela inteira de uma cor só, e o console não mostrava erro. Duas classes do Tailwind 3 tinham deixado de existir, e isso atingia todos os modais do sistema.

---

### 🚨 O Desafio Técnico / Contexto
O modal usava bg-gray-500 bg-opacity-75 no fundo, e o painel dependia da classe transform para ficar na frente. No Tailwind 4, bg-opacity-* não existe e o fundo ficou opaco. O fundo fixo também passou a ser desenhado sobre o painel, que não tinha posição.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Classe removida não dá erro: o CSS simplesmente não é gerado. Página em branco sem erro de JavaScript pede para olhar qual elemento está na frente, com document.elementFromPoint.
* 💡 A sintaxe nova é a cor com barra: bg-gray-500/75. O mesmo vale para ring-opacity-*, e flex-shrink-* virou shrink-*.
* 💡 Elemento fixo fica acima de conteúdo sem posição. Dê position: relative ao painel, em vez de contar com um efeito colateral de transform.
* 💡 O defeito estava em um componente compartilhado. Corrigir só a tela em que foi visto deixaria as outras quebradas, então a busca deve ser pela classe, em todo o projeto.

---

### 🛠️ Especificação Técnica & Código-Chave
```html
<!-- Antes -->
<div class="fixed inset-0 bg-gray-500 bg-opacity-75" />
<div class="inline-block transform">

<!-- Depois -->
<div class="fixed inset-0 bg-gray-500/75" @click="$emit('close')" />
<div class="relative inline-block">
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Os modais voltaram a aparecer em todas as telas, e o fundo e o Esc passaram a fechá-los.

* **Projetos Relacionados**: `sistema-de-atendimento`
* **Registro de Origem**: `_data/daily.dev-19.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
