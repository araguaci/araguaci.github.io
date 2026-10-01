---
layout: post
title: "O limite de execução do agente é por processo e lê o primeiro IP encaminhado"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-059"
description: "POST /agent tem um teto por minuto. O contador vive na memória daquele processo e a chave é o primeiro endereço de X-Forwarded-For."
date: 2026-08-16 00:00:00+00:00
categories: devlog
category: backend
tags: [fastapi, rate-limit, agentes]
---

# O limite de execução do agente é por processo e lê o primeiro IP encaminhado

> [!NOTE]
> **Resumo Executivo (DEV-2026-059)**: POST /agent tem um teto por minuto. O contador vive na memória daquele processo e a chave é o primeiro endereço de X-Forwarded-For.

---

### 🚨 O Desafio Técnico / Contexto
Várias chamadas seguidas no mesmo agente não tinham teto. Um limite só no processo também não acompanha outro worker, e o IP visto pelo app não é o da conexão quando há proxy.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 RateLimitMiddleware só olha POST cujo path é /agent ou começa com /agent/. Acima do teto responde 429 com Retry-After 60.
* 💡 AGENTS_RATE_LIMIT default 60 por janela de 60 segundos. Valor 0 desliga. O deque está em memória: um processo, um contador.
* 💡 client_ip usa o primeiro trecho de X-Forwarded-For. Sem esse header, usa request.client.host.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
# POST /agent/{id}
# AGENTS_RATE_LIMIT=60  → 429 depois do teto
# AGENTS_RATE_LIMIT=0   → sem limite
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A execução do agente passou a ter teto por IP naquele processo, com desligamento explícito no ambiente.

* **Projetos Relacionados**: `_agents`
* **Registro de Origem**: `_data/daily.dev-05.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
