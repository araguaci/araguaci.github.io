---
layout: post
title: "A home não soma a API de agentes com o AgentFlow"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-055"
description: "São dois runtimes. A FastAPI é catálogo HTTP e o AgentFlow é orquestração. A home manda o visitante ao console, não ao JSON da raiz."
date: 2026-08-19 00:00:00+00:00
categories: devlog
category: arquitetura
tags: [apex, fastapi, agentflow, adr]
---

# A home não soma a API de agentes com o AgentFlow

> [!NOTE]
> **Resumo Executivo (DEV-2026-055)**: São dois runtimes. A FastAPI é catálogo HTTP e o AgentFlow é orquestração. A home manda o visitante ao console, não ao JSON da raiz.

---

### 🚨 O Desafio Técnico / Contexto
A landing somava contagens de origens diferentes e o atalho da home apontava para GET /, que devolve JSON. A pasta de HTML no git também não era a página publicada.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 ADR 0010 separa AgentFlow (8 agentes no Postgres) da API Agentes (35 no FastAPI). 47+ continua blueprint.
* 💡 O CTA do card é /console. A sonda usa GET /health. GET / não é interface.
* 💡 A página no ar sai de deployments/ainativo/apex/ para o volume do site. O HTML antigo no git não é essa página.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
# Contar cada runtime com rótulo. Não somar.
# FastAPI: GET /health
# AgentFlow: Agent::count() no container da API
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A home passou a apontar para o console e a citar cada frota com o runtime de onde o número saiu.

* **Projetos Relacionados**: `sio-ecosystem`
* **Registro de Origem**: `_data/daily.dev-04.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
