---
layout: post
title: "Remodelar cenas Three.js para Mobile-First exige 100dvh, drawer colapsável e câmera adaptativa"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-166"
description: "A versão desktop da Coluna dos 7 Chakras empilhava seletores de áudio, jornada e HUD lateral sobre o canvas WebGL em telas pequenas, obstruindo a cena e disparando cliques acidentais no raycaster. Aplicar CSS Mobile-First com 100dvh, drawer colapsável, bottom sheet e enquadramento de câmera responsivo tornou o app utilizável como PWA em qualquer tela."
date: 2026-11-19 00:00:00-03:00
categories: devlog
category: frontend
tags: [mobile-first, pwa, threejs, css, web-audio, ux]
---

# Remodelar cenas Three.js para Mobile-First exige 100dvh, drawer colapsável e câmera adaptativa

> [!NOTE]
> **Resumo Executivo (DEV-2026-166)**: A versão desktop da Coluna dos 7 Chakras empilhava seletores de áudio, jornada e HUD lateral sobre o canvas WebGL em telas pequenas, obstruindo a cena e disparando cliques acidentais no raycaster. Aplicar CSS Mobile-First com 100dvh, drawer colapsável, bottom sheet e enquadramento de câmera responsivo tornou o app utilizável como PWA em qualquer tela.

---

### 🚨 O Desafio Técnico / Contexto
No artefato original de 7 Chakras com sintetizador Solfeggio e ondas binaurais (geometria.artesdosul.com), a barra superior quebrava em múltiplas linhas no celular, o card HUD lateral colidia com o guia de respiração e o uso de 100vh sofria recorte pela barra dinâmica de endereço em navegadores móveis. Além disso, tocar nos controles disparava o raycaster do Three.js e a distância fixa da câmera (z = 16.5 com offset horizontal x = 0.38) cortava os chakras extremos em telas retrato.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Usar 100dvh com viewport-fit=cover, env(safe-area-inset-*) e touch-action: none no container WebGL evita cortes da barra de endereço móvel e conflitos de scroll/pull-to-refresh durante a órbita 3D.
* 💡 Agrupar controles avançados (onda binaural, timbre, volume, link e botão de instalação PWA) num drawer colapsável no mobile que vira barra inline em min-width: 1024px preserva todos os IDs do DOM sem duplicar estado JS.
* 💡 No raycaster (pointerup), filtrar cliques vindos de header e #controls-drawer via e.target.closest impede selecionar um objeto 3D por trás dos botões.
* 💡 Em telas retrato (< 768px), recuar DEFAULT_CAM_POS no eixo Z (19.6 vs 16.5) e zerar o deslocamento horizontal do foco quando o HUD vira bottom sheet mantém o objeto 3D centralizado e visível.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
function getDefaultCamPos() {
  const isCompact = window.innerWidth < 768;
  return new THREE.Vector3(0, isCompact ? 5.9 : 6.2, isCompact ? 19.6 : 16.5);
}
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O portal geometria.artesdosul.com passou a operar como PWA instalável Mobile-First com alvos táteis >= 44px, suporte offline e câmera 3D adaptada para retrato e paisagem.

* **Projetos Relacionados**: `geometria.artesdosul.com`, `artesdosul`
* **Registro de Origem**: `_data/daily.dev-30.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
