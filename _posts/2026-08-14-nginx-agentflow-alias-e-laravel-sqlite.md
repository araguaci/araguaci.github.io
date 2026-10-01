---
layout: post
title: "O Nginx do AgentFlow procura um alias que o nome do container não é"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-053"
description: "O PHP-FPM escuta no alias agentflow_api, não no container_name. Sem DB_CONNECTION no ambiente, o Laravel 11 sobe em sqlite."
date: 2026-08-14 00:00:00+00:00
categories: devlog
category: devops
tags: [nginx, docker, laravel, agentflow]
---

# O Nginx do AgentFlow procura um alias que o nome do container não é

> [!NOTE]
> **Resumo Executivo (DEV-2026-053)**: O PHP-FPM escuta no alias agentflow_api, não no container_name. Sem DB_CONNECTION no ambiente, o Laravel 11 sobe em sqlite.

---

### 🚨 O Desafio Técnico / Contexto
O Nginx registrava host not found in upstream agentflow_api. A fila caía porque o Laravel, sem a variável, usava sqlite em vez do Postgres do compose.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 agentflow-api.conf faz fastcgi_pass agentflow_api:9000. O container_name na VPS é agentflow-api.
* 💡 O serviço api no compose da VPS declara o alias de rede agentflow_api. Sem esse alias o upstream não resolve.
* 💡 O comentário do compose diz que o Laravel 11 cai em sqlite se DB_CONNECTION não vier. O anchor laravel-env fixa DB_CONNECTION: pgsql.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
# deployments/ainativo/agentflow/docker-compose.yml
networks:
  internal:
    aliases:
      - agentflow_api
# x-laravel-env: DB_CONNECTION: pgsql
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A API do AgentFlow passou a resolver o PHP-FPM e a usar o Postgres do stack.

* **Projetos Relacionados**: `sio-ecosystem`
* **Registro de Origem**: `_data/daily.dev-04.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
