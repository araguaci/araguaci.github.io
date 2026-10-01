---
layout: post
title: "O histórico do agente guarda metadados sempre e o prompt só com opt-in"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-058"
description: "Cada execução grava quem rodou, qual agente e o status. O texto do prompt e da saída só entra no SQLite se o pedido pedir e a retenção for maior que zero."
date: 2026-08-17 00:00:00+00:00
categories: devlog
category: seguranca
tags: [sqlite, fastapi, lgpd, agentes]
---

# O histórico do agente guarda metadados sempre e o prompt só com opt-in

> [!NOTE]
> **Resumo Executivo (DEV-2026-058)**: Cada execução grava quem rodou, qual agente e o status. O texto do prompt e da saída só entra no SQLite se o pedido pedir e a retenção for maior que zero.

---

### 🚨 O Desafio Técnico / Contexto
O console precisava de histórico sem arquivar prompt por padrão. Upload em base64 também não podia ir parar na mesma tabela.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 history.record grava a linha sempre. prompt e output só são preenchidos se store for verdadeiro e retention_days for maior que zero.
* 💡 _wants_store_body aceita o header x-agents-store-body ou a query store_body com 1, true, yes ou on.
* 💡 AGENTS_HISTORY_BODY_DAYS vale 30 se não vier número. O valor fica entre 0 e 365. expire_bodies zera prompt e output vencidos.
* 💡 sanitize_params descarta as chaves file_bytes, arquivo_b64 e arquivo. O log de acesso não grava query nem body.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
# Sem o header, prompt e output ficam NULL.
# X-Agents-Store-Body: 1  → grava, até AGENTS_HISTORY_BODY_DAYS
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Rodar um agente passou a deixar rastro operacional sem guardar o texto do pedido por padrão.

* **Projetos Relacionados**: `_agents`
* **Registro de Origem**: `_data/daily.dev-05.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
