---
layout: post
title: "Com a documentação pública desligada, a raiz da API aponta para o console"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-057"
description: "O Swagger aberto na internet depende de AGENTS_DOCS. Com o valor 0, /docs e /openapi.json somem e o campo docs da raiz passa a ser /console/docs."
date: 2026-08-17 00:00:00+00:00
categories: devlog
category: backend
tags: [fastapi, openapi, oauth, agentes]
---

# Com a documentação pública desligada, a raiz da API aponta para o console

> [!NOTE]
> **Resumo Executivo (DEV-2026-057)**: O Swagger aberto na internet depende de AGENTS_DOCS. Com o valor 0, /docs e /openapi.json somem e o campo docs da raiz passa a ser /console/docs.

---

### 🚨 O Desafio Técnico / Contexto
O FastAPI publicava /docs sozinho. Desligar o Swagger no construtor não bastava: a raiz continuava anunciando /docs, e o esquema ficava anônimo.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 main.py cria o FastAPI com docs_url, redoc_url e openapi_url nulos. As rotas /docs, /redoc e /openapi.json são manuais.
* 💡 _docs_public lê AGENTS_DOCS. Diferente de 0, /openapi.json responde 404. GET / então devolve docs igual a /console/docs.
* 💡 /console/openapi.json exige sessão Google ou X-API-Key. Anônimo em /console/docs recebe redirect 302 para /login.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
docs_url = None
# AGENTS_DOCS=0 → /openapi.json 404
# GET / → {"docs": "/console/docs", "docs_public": false}
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O catálogo HTTP deixou de entregar o Swagger anônimo quando a documentação pública está desligada.

* **Projetos Relacionados**: `_agents`
* **Registro de Origem**: `_data/daily.dev-05.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
