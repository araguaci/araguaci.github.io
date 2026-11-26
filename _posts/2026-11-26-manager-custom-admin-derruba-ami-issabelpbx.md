---
layout: post
title: "Uma seção [admin] no manager_custom.conf derruba o AMI do próprio IssabelPBX"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-182"
description: "Para o CTI entrar no AMI, um script acrescentava [admin] com outra senha no manager_custom.conf. O IssabelPBX usa esse mesmo usuário, e o retrieve_conf passou a falhar."
date: 2026-11-26 00:00:00-03:00
categories: devlog
category: infraestrutura
tags: [asterisk, ami, issabel, cti]
---

# Uma seção [admin] no manager_custom.conf derruba o AMI do próprio IssabelPBX

> [!NOTE]
> **Resumo Executivo (DEV-2026-182)**: Para o CTI entrar no AMI, um script acrescentava [admin] com outra senha no manager_custom.conf. O IssabelPBX usa esse mesmo usuário, e o retrieve_conf passou a falhar.

---

### 🚨 O Desafio Técnico / Contexto
O CTI precisa do AMI do Asterisk a partir da rede do Docker. O script da stack gravava no manager_custom.conf uma seção com o usuário do CTI, a senha do .env e o permit da rede. Com o usuário padrão admin e uma senha gerada para o laboratório, a seção nova tomou o lugar da senha que o IssabelPBX lê do amportal.conf. O CTI conectou, mas o retrieve_conf e o botão Aplicar do painel passaram a dar "Cannot connect to Asterisk Manager". Na VPS o script usava a senha padrão, por isso nunca quebrou.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O usuário admin do AMI pertence ao IssabelPBX. Integração externa ganha usuário próprio, com permit restrito à rede dela.
* 💡 No Asterisk, uma seção repetida em arquivo incluído depois vale sobre a anterior. Acrescentar não é inofensivo.
* 💡 O script passou a recusar admin com senha diferente da AMPMGRPASS do Issabel, e o deploy do laboratório recusa o .env com o CTI no admin.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
LORENTZ_CTI_AMI_USER=lorentzcti
# manager show connected: lorentzcti vindo da rede do Docker,
# e o retrieve_conf do Issabel volta a funcionar
```

---

### 📈 Impacto no Ecossistema & Valor Prático
CTI e IssabelPBX usam o AMI ao mesmo tempo, sem um derrubar o outro.

* **Projetos Relacionados**: `lorentz-vps-stack`, `lorentz-cti`
* **Registro de Origem**: `_data/daily.dev-34.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
