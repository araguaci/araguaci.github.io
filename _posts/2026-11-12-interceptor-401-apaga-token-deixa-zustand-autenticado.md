---
layout: post
title: "Interceptor 401 que apaga só o token deixa o Zustand autenticado e pula a Landing Page"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-154"
description: "Visitantes com sessão expirada iam direto para /login ao abrir a raiz do site em vez de verem a Landing Page pública. O interceptor Axios removia fieldflow_token do localStorage, mas deixava isAuthenticated como true no objeto fieldflow-auth persistido pelo Zustand."
date: 2026-11-12 00:00:00-03:00
categories: devlog
category: frontend
tags: [react, zustand, axios, auth, localstorage]
---

# Interceptor 401 que apaga só o token deixa o Zustand autenticado e pula a Landing Page

> [!NOTE]
> **Resumo Executivo (DEV-2026-154)**: Visitantes com sessão expirada iam direto para /login ao abrir a raiz do site em vez de verem a Landing Page pública. O interceptor Axios removia fieldflow_token do localStorage, mas deixava isAuthenticated como true no objeto fieldflow-auth persistido pelo Zustand.

---

### 🚨 O Desafio Técnico / Contexto
Em 2026-11-12, abrir a raiz pública do ProntOS sem sessão válida redirecionava imediatamente para /login. A rota / usava PublicHome, que lia isAuthenticated do authStore (Zustand persist em fieldflow-auth). Quando uma sessão anterior recebia HTTP 401, api.ts apagava apenas fieldflow_token.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Em frontend/src/lib/api.ts, localStorage.removeItem('fieldflow_token') no interceptor de erro 401 não limpava a chave fieldflow-auth gravada pelo middleware persist do Zustand.
* 💡 Na visita seguinte à raiz /, PublicHome lia isAuthenticated === true do fieldflow-auth, redirecionava para /dashboard via Navigate, disparava fetchUser() sem token e caía no redirect para /login.
* 💡 No onRehydrateStorage de frontend/src/stores/authStore.ts, validar se localStorage.getItem('fieldflow_token') existe antes de aceitar state.isAuthenticated = true impede que um estado órfão finja sessão ativa.
* 💡 No interceptor 401 de api.ts, remover tanto fieldflow_token quanto fieldflow-auth e redirecionar para /login apenas quando window.location.pathname não for /, /landing, /login ou /register preserva a vitrine pública.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
onRehydrateStorage: () => (state) => {
  if (state && !localStorage.getItem('fieldflow_token')) {
    state.user = null;
    state.token = null;
    state.isAuthenticated = false;
  }
}
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Visitantes deslogados ou com token expirado passaram a ver a Landing Page na raiz / sem redirecionamento indevido para /login.

* **Projetos Relacionados**: `30-FieldFlow`
* **Registro de Origem**: `_data/daily.dev-27.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
