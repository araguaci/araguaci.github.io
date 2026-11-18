---
layout: post
title: "Laravel Sanctum statefulApi força verificação de CSRF e quebra SPAs desacopladas com HTTP 419"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-135"
description: "Ao configurar o Laravel 11/12 para servir uma SPA React em localhost, requisições de login falhavam com HTTP 419 misterioso. Descobrimos que o método statefulApi ativa validação de CSRF para origens locais mesmo quando a SPA utiliza autenticação por Bearer Token."
date: 2026-11-08 00:00:00-03:00
categories: devlog
category: backend
tags: [laravel, sanctum, csrf, spa, react, autenticacao]
---

# Laravel Sanctum statefulApi força verificação de CSRF e quebra SPAs desacopladas com HTTP 419

> [!NOTE]
> **Resumo Executivo (DEV-2026-135)**: Ao configurar o Laravel 11/12 para servir uma SPA React em localhost, requisições de login falhavam com HTTP 419 misterioso. Descobrimos que o método statefulApi ativa validação de CSRF para origens locais mesmo quando a SPA utiliza autenticação por Bearer Token.

---

### 🚨 O Desafio Técnico / Contexto
O frontend Vite chamava POST /api/auth/login via proxy e recebia HTTP 419. Como a aplicação React armazena e envia Bearer Token via header Authorization e não mantém sessão por cookies, o middleware EnsureFrontendRequestsAreStateful exigia um token CSRF inexistente.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O método statefulApi() no bootstrap/app.php injeta o middleware de verificação de CSRF em rotas de API para domínios listados em SANCTUM_STATEFUL_DOMAINS.
* 💡 SPAs desacopladas que usam Personal Access Tokens (Bearer Token) não devem usar statefulApi(), pois não realizam o handshake com /sanctum/csrf-cookie.
* 💡 A correção consiste em remover statefulApi(), configurar validateCsrfTokens(except: ['api/*']) e publicar o config/cors.php liberando origens do dev server.

---

### 🛠️ Especificação Técnica & Código-Chave
```cpp
// bootstrap/app.php
->withMiddleware(function (Middleware $middleware): void {
    $middleware->validateCsrfTokens(except: ['api/*']);
    $middleware->api(prepend: [
        \Illuminate\Http\Middleware\HandleCors::class,
    ]);
})
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Eliminação imediata do erro HTTP 419 e garantia de autenticação Bearer pura e sem atrito no ciclo de desenvolvimento local e produção.

* **Projetos Relacionados**: `00-ZapDisparador`
* **Registro de Origem**: `_data/daily.dev-22.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
