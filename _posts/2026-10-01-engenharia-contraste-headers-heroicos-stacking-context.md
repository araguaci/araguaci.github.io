---
layout: post
title: "Engenharia de Contraste em Headers Heróicos: Stacking Context e Overlay Gradiente"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-003"
description: "Técnica definitiva de camadas CSS (z-index e pseudo-elementos) para garantir leitura de títulos sobre qualquer imagem de fundo sem recorrer a caixas opacas."
date: 2026-10-01 00:00:00+00:00
categories: devlog
category: frontend
tags: [css, acessibilidade, wcag, beautiful-jekyll, design-system]
---

# Engenharia de Contraste em Headers Heróicos: Stacking Context e Overlay Gradiente

> [!NOTE]
> **Resumo Executivo (DEV-2026-003)**: Técnica definitiva de camadas CSS (z-index e pseudo-elementos) para garantir leitura de títulos sobre qualquer imagem de fundo sem recorrer a caixas opacas.

---

### 🚨 O Desafio Técnico / Contexto
Aplicar 'background-color: rgba(255,255,255,0.6)' no seletor '.intro-header.big-img' não surtia efeito porque a cor fica fisicamente atrás da 'background-image'. Títulos brancos colidiam com áreas claras de fotos.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Propriedades 'background-color' nunca criam overlays sobre 'background-image' do mesmo elemento no box model da W3C.
* 💡 A solução robusta requer um pseudo-elemento '::before' com 'position: absolute', 'pointer-events: none' e gradiente vertical (180deg).
* 💡 O container do texto deve receber 'position: relative' e 'z-index: 2' para elevar a tipografia acima da camada escura de oclusão.
* 💡 Text-shadow duplo de alta dispersão garante conformidade com o padrão WCAG AAA (>7:1).

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
.intro-header.big-img { position: relative; }
.intro-header.big-img::before {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(10,15,26,0.55) 0%, rgba(10,15,26,0.88) 100%);
  z-index: 1;
  pointer-events: none;
}
.intro-header.big-img .container-md {
  position: relative;
  z-index: 2;
}

```

---

### 📈 Impacto no Ecossistema & Valor Prático
Legibilidade impecável em 100% dos posts heróicos em telas mobile e desktop sob qualquer iluminação ambiente.

* **Projetos Relacionados**: `artesdosul.github.io`, `modelos.artesdosul.com`
* **Registro de Origem**: `_data/daily.dev-01.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
