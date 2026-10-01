---
layout: post
title: "Cartografia de Saúde Holística & Medicina Integrativa: O PWA Mapa da Cura e Frequências Rife"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-021"
description: "Construção de bússola terapêutica interativa em SVG para fitoterapia, biofísica e frequências sonoras integrativas com compartilhamento social via WhatsApp."
date: 2026-09-27 00:00:00+00:00
categories: devlog
category: frontend
tags: [pwa, medicina-integrativa, svg, tooltips, saude-digital]
---

# Cartografia de Saúde Holística & Medicina Integrativa: O PWA Mapa da Cura e Frequências Rife

> [!NOTE]
> **Resumo Executivo (DEV-2026-021)**: Construção de bússola terapêutica interativa em SVG para fitoterapia, biofísica e frequências sonoras integrativas com compartilhamento social via WhatsApp.

---

### 🚨 O Desafio Técnico / Contexto
A navegação em manuais extensos de práticas integrativas gerava fadiga no paciente e impossibilidade de prescrição compartilhada rápida com familiares.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Cálculo de coordenadas polares (raio, seno, cosseno) para posicionamento de nós em rosa-dos-ventos SVG garante escalabilidade visual matemática perfeita.
* 💡 Tooltips desacoplados com position: fixed e cálculo de bounding-rect previnem cortes causados por wrappers com overflow: hidden.
* 💡 Codificação direta de roteiros e prescrições em URLs wa.me viabiliza encaminhamento de guias de saúde sem intermediários ou bancos de dados.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
// Posicionamento trigonométrico em SVG da Rosa da Cura
function getPointOnCircle(cx, cy, r, angleInDegrees) {
  const rad = (angleInDegrees - 90) * Math.PI / 180.0;
  return {
    x: cx + (r * Math.cos(rad)),
    y: cy + (r * Math.sin(rad))
  };
}
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Democratização do acesso a guias de autocuidado e conexão direta de pacientes com abordagens de bem-estar natural.

* **Projetos Relacionados**: `cura.artesdosul.com`, `gaia.artesdosul.com`
* **Registro de Origem**: `_data/daily.dev-02.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
