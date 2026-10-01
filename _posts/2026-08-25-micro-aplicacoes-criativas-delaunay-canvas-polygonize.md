---
layout: post
title: "Engenharia de Micro-Aplicações Criativas: Algoritmos de Delaunay e Canvas Generativo (Polygonize 3D)"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-024"
description: "Geração procedimental de malhas poligonais e arte computacional no cliente com Triangulação de Delaunay e otimização de renderização com TypedArrays."
date: 2026-08-25 00:00:00+00:00
categories: devlog
category: frontend
tags: [canvas, delaunay, procedural, web-graphics, math, javascript]
---

# Engenharia de Micro-Aplicações Criativas: Algoritmos de Delaunay e Canvas Generativo (Polygonize 3D)

> [!NOTE]
> **Resumo Executivo (DEV-2026-024)**: Geração procedimental de malhas poligonais e arte computacional no cliente com Triangulação de Delaunay e otimização de renderização com TypedArrays.

---

### 🚨 O Desafio Técnico / Contexto
Renderizar dezenas de milhares de polígonos interativos a partir de fotografias do usuário diretamente no browser provocava travamento da thread principal e alto consumo de memória.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 A Triangulação de Delaunay sobre pontos distribuídos por algoritmo de Poisson Disk produz malhas orgânicas sem arestas agudas e finas indesejadas.
* 💡 O uso de TypedArrays (Float32Array) para coordenadas e Uint32Array para índices reduz o overhead de alocação de objetos em mais de 75%.
* 💡 O cálculo de cor média por centróide do triângulo amostrando diretamente a imagem de fundo via getImageData viabiliza exportação vetorial de fidelidade artística.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
// Renderização otimizada de triângulos Delaunay em Canvas 2D
function renderMesh(ctx, vertices, triangles, colors) {
  for (let i = 0; i < triangles.length; i += 3) {
    const p0 = triangles[i] * 2, p1 = triangles[i+1] * 2, p2 = triangles[i+2] * 2;
    ctx.fillStyle = colors[i / 3];
    ctx.beginPath();
    ctx.moveTo(vertices[p0], vertices[p0 + 1]);
    ctx.lineTo(vertices[p1], vertices[p1 + 1]);
    ctx.lineTo(vertices[p2], vertices[p2 + 1]);
    ctx.closePath();
    ctx.fill();
  }
}
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Suíte de webapps criativos aberta, fluida e com processamento 100% no navegador sem envio de fotos a servidores remotos.

* **Projetos Relacionados**: `polygonize-3d`, `chromamesh`, `glitchlab`
* **Registro de Origem**: `_data/daily.dev-02.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
