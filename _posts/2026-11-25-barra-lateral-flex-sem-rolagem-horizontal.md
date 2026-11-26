---
layout: post
title: "A barra lateral abre rolagem horizontal quando o item flex não encolhe"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-174"
description: "A lista do menu passava da largura da barra e a página ganhava rolagem para o lado. A barra ficou com altura da janela, a lista é o único trecho que rola, e só na vertical."
date: 2026-11-25 00:00:00-03:00
categories: devlog
category: frontend
tags: [css, flexbox, sidebar, tipografia]
---

# A barra lateral abre rolagem horizontal quando o item flex não encolhe

> [!NOTE]
> **Resumo Executivo (DEV-2026-174)**: A lista do menu passava da largura da barra e a página ganhava rolagem para o lado. A barra ficou com altura da janela, a lista é o único trecho que rola, e só na vertical.

---

### 🚨 O Desafio Técnico / Contexto
No computador a barra é uma coluna flex. O corpo do offcanvas pedia min-height 100% e o item flex, por padrão, não encolhe abaixo do conteúdo. Letra grande alarga a barra para 280px e a máxima para 320px. Contraída, ela tem 72px e o texto longo continuava empurrando a largura.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 A partir de 768px, em scripts/theme-rules.css, .sidebar é sticky, height e max-height 100vh, flex column. .offcanvas-body fica flex 1 1 auto, min-height 0 com !important e overflow hidden.
* 💡 .nav fica flex 1 1 auto, min-width 0, min-height 0, overflow-x hidden e overflow-y auto. .nav-link e .nav-texto também têm min-width 0. Sem isso o mínimo do flex é o tamanho do texto e a barra abre rolagem horizontal.
* 💡 Usuário, tamanho da letra, botão de contrair e versão têm flex-shrink 0, para a lista ceder o espaço e esses blocos permanecerem no fim.
* 💡 html[data-text=grande] alarga a barra para 280px e maxima para 320px. O estado contraido força 72px mesmo com essas letras. O texto some com o recorte de 1px, e o link ganha title com o nome.
* 💡 reading.js grava a escolha em app_text neste aparelho, antes de pintar: menor 16px, grande 20px, maxima 24px, padrão grande, em documentElement.style.fontSize. Os três botões usam grid com minmax(0, 1fr).

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
.sidebar .nav { min-width: 0; min-height: 0; overflow-x: hidden; overflow-y: auto; }
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A página não rola mais para o lado por causa do menu. Só a lista de itens desce.

* **Projetos Relacionados**: `monitoramento-app`
* **Registro de Origem**: `_data/daily.dev-33.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
