---
layout: post
title: "Service Worker exige Response valida em respondWith para evitar ERR_FAILED na Vercel"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-071"
description: "Ao implementar cache PWA, o metodo respondWith do Service Worker quebrou assets estaticos na Vercel por receber undefined. Passou a valer a regra de nunca resolver promises sem Response valida e desativar preload de fontes nao renderizadas de imediato."
date: 2026-10-07 00:00:00+00:00
categories: devlog
category: frontend
tags: [pwa, service-worker, astro, vercel, cache]
---

# Service Worker exige Response valida em respondWith para evitar ERR_FAILED na Vercel

> [!NOTE]
> **Resumo Executivo (DEV-2026-071)**: Ao implementar cache PWA, o metodo respondWith do Service Worker quebrou assets estaticos na Vercel por receber undefined. Passou a valer a regra de nunca resolver promises sem Response valida e desativar preload de fontes nao renderizadas de imediato.

---

### 🚨 O Desafio Técnico / Contexto
Apos deploy na Vercel, fontes .woff2 e scripts hoisted do Astro falharam com net::ERR_FAILED e TypeError: Failed to convert value to Response no sw.js, travando o carregamento da aplicacao.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O metodo event.respondWith() no sw.js exige estritamente uma instancia de Response; retornar undefined no fallback de caches.match ou no catch bloqueia a requisicao do navegador com net::ERR_FAILED.
* 💡 Requisicoes com Stale-While-Revalidate devem buscar na rede quando ausentes no cache e retornar Response explicita em caso de falha de conexao, nunca deixando a promise resolver vazia.
* 💡 Preload de fontes (preload: true) so deve ser mantido para tipografias ativamente renderizadas no primeiro viewport; fontes secundarias devem usar preload: false para evitar warnings no console.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
// public/sw.js - Garantir sempre Response valida no respondWith
event.respondWith(
  caches.match(event.request).then((cached) => {
    if (cached) return cached;
    return fetch(event.request).catch(() => {
      return new Response('', { status: 408, statusText: 'Request failed' });
    });
  })
);
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Eliminacao completa das falhas de rede na Vercel e restauracao do carregamento offline seguro dos assets.

* **Projetos Relacionados**: `portfolio-astro`
* **Registro de Origem**: `_data/daily.dev-10.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
