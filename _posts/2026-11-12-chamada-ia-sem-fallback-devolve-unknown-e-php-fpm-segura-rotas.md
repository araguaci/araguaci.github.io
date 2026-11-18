---
layout: post
title: "Chamada de IA sem fallback devolve intent desconhecido e rota nova pede reinício do PHP-FPM"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-157"
description: "O simulador de IA respondia sempre unknown e a rota de importação recém-adicionada dava 404. A API externa falhava por modelo não provisionado sem acionar o classificador heurístico, e os processos PHP-FPM retidos em memória serviam o catálogo antigo de rotas."
date: 2026-11-12 00:00:00-03:00
categories: devlog
category: backend
tags: [ia, laravel, php-fpm, opcache, webhooks]
---

# Chamada de IA sem fallback devolve intent desconhecido e rota nova pede reinício do PHP-FPM

> [!NOTE]
> **Resumo Executivo (DEV-2026-157)**: O simulador de IA respondia sempre unknown e a rota de importação recém-adicionada dava 404. A API externa falhava por modelo não provisionado sem acionar o classificador heurístico, e os processos PHP-FPM retidos em memória serviam o catálogo antigo de rotas.

---

### 🚨 O Desafio Técnico / Contexto
Em 2026-11-12, ao testar o webhook de IA em /integrations, o endpoint retornava detected_intent: unknown. Simultaneamente, a rota POST /api/integrations/orcamento/import respondia HTTP 404 no navegador mesmo constando na listagem do artisan route:list.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Em app/Services/ClaudeService.php, quando o provedor externo responde erro (ex: not_found_error ou cota), retornar 'unknown' descarta a inteligência da aplicação. O fluxo precisa acionar imediatamente um classificador NLP semântico local em português.
* 💡 No webhook de entrada, ler $request->input('data.message.conversation') ?? $request->input('message') ?? $request->getContent() garante suporte tanto ao formato nativo da Evolution API quanto a chamadas JSON do Axios ou payloads brutos.
* 💡 Adicionar rotas no routes/api.php de um container PHP-FPM em produção não tem efeito imediato se houver routes-v7.php compilado ou OPcache ativo. php artisan route:clear seguido de docker restart recicla os workers e ativa os novos endpoints.

---

### 🛠️ Especificação Técnica & Código-Chave
```bash
/* Fallback resiliente no ClaudeService */
if ($response->failed()) {
    return $this->fallbackIntentDetection($message);
}
/* Reciclagem do FPM */
docker restart fieldflow_app
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A detecção de intenções passou a responder instantaneamente com alta precisão e a rota de importação foi ativada em produção.

* **Projetos Relacionados**: `30-FieldFlow`
* **Registro de Origem**: `_data/daily.dev-27.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
