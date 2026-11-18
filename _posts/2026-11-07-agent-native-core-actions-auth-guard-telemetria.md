---
layout: post
title: "Actions do Agent-Native rodam em prefixo próprio e exigem requiresAuth false para telemetria pública"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-132"
description: "Tentativas de liberar rotas públicas de actions pelo caminho convencional da API resultavam em erro 401 silencioso no frontend. Descobrimos que o framework despacha sob o prefixo interno /_agent-native/actions e exige flag declarativa na definição da action para contornar o guard."
date: 2026-11-07 00:00:00-03:00
categories: devlog
category: backend
tags: [agent-native, nitro, h3, auth, api, typescript]
---

# Actions do Agent-Native rodam em prefixo próprio e exigem requiresAuth false para telemetria pública

> [!NOTE]
> **Resumo Executivo (DEV-2026-132)**: Tentativas de liberar rotas públicas de actions pelo caminho convencional da API resultavam em erro 401 silencioso no frontend. Descobrimos que o framework despacha sob o prefixo interno /_agent-native/actions e exige flag declarativa na definição da action para contornar o guard.

---

### 🚨 O Desafio Técnico / Contexto
O indicador de status da telefonia e o seletor de temas no cabeçalho apareciam desconectados para usuários sem sessão logada. As requisições de telemetria recebiam HTTP 401 do middleware runAuthGuard, mesmo com tentativas de liberação em /api/actions/* no arquivo de rotas.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Actions do @agent-native/core são registradas sob o prefixo /_agent-native/actions e não em /api/actions/.
* 💡 Para expor uma action sem exigir cookie de sessão, deve-se declarar requiresAuth: false e http: { method: 'GET' } no defineAction.
* 💡 O registerAuthPublicPaths deve incluir o caminho exato do framework para que o middleware H3 libere a rota sem interceptação.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
export default defineAction({
  description: "Telemetria de saúde da malha",
  requiresAuth: false,
  http: { method: "GET" },
  readOnly: true,
  schema: z.object({}),
  run: async () => ({ online: true }),
});
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Telemetria de infraestrutura e temas visuais passaram a responder 200 OK imediatamente para qualquer visitante, eliminando telas falsas de desconexão.

* **Projetos Relacionados**: `triade-artesdosul`, `ecosul`
* **Registro de Origem**: `_data/daily.dev-21.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
