---
layout: post
title: "O header X-Tenant-Id que diverge do JWT devolve 403"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-051"
description: "No CRM do ImobHub o tenant da sessão é o companyId do JWT. Um X-Tenant-Id diferente não troca a imobiliária: a API responde 403."
date: 2026-09-03 00:00:00+00:00
categories: devlog
category: backend
tags: [jwt, tenant, express, imobhub]
---

# O header X-Tenant-Id que diverge do JWT devolve 403

> [!NOTE]
> **Resumo Executivo (DEV-2026-051)**: No CRM do ImobHub o tenant da sessão é o companyId do JWT. Um X-Tenant-Id diferente não troca a imobiliária: a API responde 403.

---

### 🚨 O Desafio Técnico / Contexto
Listar e gravar imóvel e lead filtrava por company_id, mas um header podia apontar outro tenant. Sem a checagem, a sessão e o header divergiam em silêncio.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 auth.middleware.ts grava req.user.companyId e req.tenantId a partir do JWT verificado.
* 💡 tenant.middleware.ts, se já há sessão e o header X-Tenant-Id difere, responde 403 com tenant_id não confere com a sessão.
* 💡 Sem sessão, o header ainda preenche req.tenantId. Com sessão, o companyId do token é o que vale.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
if (sessionTenant && headerTenant && headerTenant !== sessionTenant) {
  return res.status(403).json({ error: 'tenant_id não confere com a sessão' });
}
req.tenantId = sessionTenant;
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Consulta e escrita do CRM ficaram presas à imobiliária do token, não ao header.

* **Projetos Relacionados**: `sio-ecosystem`
* **Registro de Origem**: `_data/daily.dev-04.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
