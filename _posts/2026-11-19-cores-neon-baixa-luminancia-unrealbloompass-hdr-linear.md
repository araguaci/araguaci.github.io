---
layout: post
title: "Cores neon de baixa luminância perdem o brilho no UnrealBloomPass sem compensação HDR linear"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-165"
description: "No palco 3D dos 5 Sólidos Platônicos com UnrealBloomPass (threshold 0.85), tons como violeta (#b5179e) e coral (#ff2a6d) ficavam apagados após conversão sRGB para linear no Three.js r170. Calibrar o multiplicador HDR pela luminância linear de cada cor e adicionar OutputPass garantiu glow uniforme em todos os sólidos."
date: 2026-11-19 00:00:00-03:00
categories: devlog
category: frontend
tags: [threejs, webgl, glsl, bloom, color-management]
---

# Cores neon de baixa luminância perdem o brilho no UnrealBloomPass sem compensação HDR linear

> [!NOTE]
> **Resumo Executivo (DEV-2026-165)**: No palco 3D dos 5 Sólidos Platônicos com UnrealBloomPass (threshold 0.85), tons como violeta (#b5179e) e coral (#ff2a6d) ficavam apagados após conversão sRGB para linear no Three.js r170. Calibrar o multiplicador HDR pela luminância linear de cada cor e adicionar OutputPass garantiu glow uniforme em todos os sólidos.

---

### 🚨 O Desafio Técnico / Contexto
Ao construir o palco 3D dos 5 Sólidos Platônicos em Three.js r170 com ACESFilmicToneMapping e UnrealBloomPass configurado em threshold 0.85, strength 1.2 e radius 0.6, um multiplicador fixo (2.5x) ativava fortemente o brilho em ciano (#00f5d4) e verde (#05ffa1), mas deixava o Icosaedro violeta (#b5179e) abaixo do limiar de bloom porque sua luminância linear (0.299*R + 0.587*G + 0.114*B) é de apenas ~0.182. Sem OutputPass ao final do EffectComposer, a conversão sRGB e o tone mapping também ficavam desalinhados com o render padrão.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 No Three.js r170 com gerenciamento de cores ativo, THREE.Color converte hex sRGB para espaço linear; matizes saturados de baixa luminância (violeta, coral) exigem multiplicador HDR proporcional a targetLuma / max(luma, 0.12) com toneMapped: false para ultrapassar threshold 0.85.
* 💡 Usar THREE.EdgesGeometry(geometry, 1) com detail = 0 remove diagonais internas nas faces quadradas do Hexaedro e pentagonais do Dodecaedro, preservando arestas limpas para o bloom.
* 💡 Adicionar OutputPass após UnrealBloomPass no EffectComposer assegura a aplicação correta de ACESFilmicToneMapping e saída SRGBColorSpace.
* 💡 Reutilizar um THREE.Vector3 pré-alocado fora do loop requestAnimationFrame evita dezenas de alocações por frame em interpolações de escala (group.scale.lerp).

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
function createEmissiveHDRColor(colorInt, targetLuma = 2.4) {
  const c = new THREE.Color(colorInt);
  const luma = 0.299 * c.r + 0.587 * c.g + 0.114 * c.b;
  return c.multiplyScalar(Math.max(2.2, targetLuma / Math.max(luma, 0.12)));
}
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Todos os 5 Sólidos Platônicos em geometria.artesdosul.com/platonicos.html exibem brilho neon equilibrado sem estourar o fundo nem perder nitidez.

* **Projetos Relacionados**: `geometria.artesdosul.com`, `artesdosul`
* **Registro de Origem**: `_data/daily.dev-30.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
