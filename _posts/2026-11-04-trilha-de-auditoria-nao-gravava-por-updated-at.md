---
layout: post
title: "A trilha de auditoria não gravava porque o Eloquent preenchia uma coluna que a tabela não tem"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-107"
description: "O model AuditLog existia, mas gravar por ele falhava, porque o Eloquent tentava preencher updated_at. Só o primeiro teste que dependia de um registro de auditoria expôs o defeito."
date: 2026-11-04 00:00:00-03:00
categories: devlog
category: backend
tags: [laravel, eloquent, auditoria, testes]
---

# A trilha de auditoria não gravava porque o Eloquent preenchia uma coluna que a tabela não tem

> [!NOTE]
> **Resumo Executivo (DEV-2026-107)**: O model AuditLog existia, mas gravar por ele falhava, porque o Eloquent tentava preencher updated_at. Só o primeiro teste que dependia de um registro de auditoria expôs o defeito.

---

### 🚨 O Desafio Técnico / Contexto
A tabela audit_logs só tem created_at, e faz sentido, porque a trilha não muda depois de gravada. O model mantinha o comportamento padrão do Eloquent e preenchia updated_at em todo insert.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 UPDATED_AT = null no model desliga só essa coluna e mantém o created_at.
* 💡 A existência do model não prova que o recurso funciona. A prova é um teste que grava e lê o registro.
* 💡 Esse defeito só apareceu quando a tela de perfis passou a gravar na trilha. Hoje ela é a única a usar AuditLog::create, então os outros eventos sensíveis ainda não têm registro por esse caminho.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
class AuditLog extends Model
{
    // A trilha não muda depois de gravada: a tabela só tem created_at
    public const UPDATED_AT = null;
}
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A configuração de perfis passou a ficar registrada na trilha, e ficou claro o quanto ainda falta cobrir.

* **Projetos Relacionados**: `omnichannel-system`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
