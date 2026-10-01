---
layout: post
title: "Hub novo no Ecossistema Selva só aparece quando o nome do cache muda"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-060"
description: "O service worker entrega a lista de hubs do cache antes da rede. Incluir um hub no JSON não chega ao visitante enquanto CACHE_NAME for o mesmo."
date: 2026-09-12 00:00:00+00:00
categories: devlog
category: frontend
tags: [service-worker, pwa, cache]
---

# Hub novo no Ecossistema Selva só aparece quando o nome do cache muda

> [!NOTE]
> **Resumo Executivo (DEV-2026-060)**: O service worker entrega a lista de hubs do cache antes da rede. Incluir um hub no JSON não chega ao visitante enquanto CACHE_NAME for o mesmo.

---

### 🚨 O Desafio Técnico / Contexto
O hub Arquivo Vivo entrou em ecosystem.json e no app, e a página antiga continuava no cache. O install guarda a lista inteira, e o fetch devolve essa cópia.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 sw.js precacheia /data/ecosystem.json, /app.js e /index.html sob CACHE_NAME.
* 💡 O fetch responde caches.match primeiro. Sem rede por cima, o JSON novo não substitui o antigo.
* 💡 No activate, caches com outro nome são apagados. A troca registrada em 12/09 foi selva-hub-v3.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
const CACHE_NAME = 'selva-hub-v3';
// install: cache.addAll inclui /data/ecosystem.json
// fetch: cache primeiro; activate apaga os nomes antigos
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Publicar um hub novo passou a exigir outro CACHE_NAME, senão o visitante permanece na lista em cache.

* **Projetos Relacionados**: `ecosistema-selva.vercel.app`
* **Registro de Origem**: `_data/daily.dev-05.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
