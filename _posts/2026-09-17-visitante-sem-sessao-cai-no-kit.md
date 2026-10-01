---
layout: post
title: "Visitante sem sessão no Content Factory cai no /kit, não no login"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-056"
description: "A vitrine do pacote é pública. Quem entra na raiz sem sessão é mandado para /kit, e /comprar continua fora desse guard."
date: 2026-09-17 00:00:00+00:00
categories: devlog
category: frontend
tags: [react, router, content-factory, auth]
---

# Visitante sem sessão no Content Factory cai no /kit, não no login

> [!NOTE]
> **Resumo Executivo (DEV-2026-056)**: A vitrine do pacote é pública. Quem entra na raiz sem sessão é mandado para /kit, e /comprar continua fora desse guard.

---

### 🚨 O Desafio Técnico / Contexto
A raiz exigia login e escondia o catálogo. O pedido PIX ficava misturado com a biblioteca autenticada, então visitante e comprador caíam no mesmo destino.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 App.tsx: Guard lê isAuthenticated e, se falhar, faz Navigate para /kit.
* 💡 As rotas /kit, /login, /about e /comprar ficam fora do Guard. O pedido não exige sessão.
* 💡 A rota * também redireciona para /kit. Caminho desconhecido não abre o cockpit.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
function Guard({ children }) {
  const ok = useAuthStore((s) => s.isAuthenticated);
  if (!ok) return <Navigate to="/kit" replace />;
  return children;
}
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A raiz pública passou a mostrar o catálogo, e o pedido ficou numa rota própria.

* **Projetos Relacionados**: `sio-ecosystem`
* **Registro de Origem**: `_data/daily.dev-04.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
