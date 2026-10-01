---
layout: post
title: "A triagem de saúde pula o tenant do ImobHub e ainda responde 200"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-052"
description: "O AgentFlow só classifica urgência para tenants da Saúde Livre. O tenant do ImobHub volta skipped, com HTTP 200, para o proxy de sugestão não virar 502."
date: 2026-08-20 00:00:00+00:00
categories: devlog
category: arquitetura
tags: [agentflow, brainos, webhook, tenant]
---

# A triagem de saúde pula o tenant do ImobHub e ainda responde 200

> [!NOTE]
> **Resumo Executivo (DEV-2026-052)**: O AgentFlow só classifica urgência para tenants da Saúde Livre. O tenant do ImobHub volta skipped, com HTTP 200, para o proxy de sugestão não virar 502.

---

### 🚨 O Desafio Técnico / Contexto
O mesmo webhook de triagem atendia conversas de imobiliária e de clínica. Recusar com erro fazia o suggest-reply do Omnichannel tratar o isolamento como falha.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 HealthcareVenture::allowsTenant lê blocked_tenants, padrão imobhub-sim, e a allowlist saude-livre-prod.
* 💡 SioOmnichannelTriage::fromConversation devolve skipped true, reason venture_isolation e urgency null.
* 💡 OmnichannelWebhookController::triage responde JSON desse resultado. O status padrão é 200, não erro.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
if (! HealthcareVenture::allowsTenant($tenant)) {
    return ['skipped' => true, 'reason' => 'venture_isolation', 'urgency' => null];
}
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Conversa do ImobHub deixou de entrar na classificação clínica sem derrubar o proxy.

* **Projetos Relacionados**: `sio-ecosystem`
* **Registro de Origem**: `_data/daily.dev-04.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
