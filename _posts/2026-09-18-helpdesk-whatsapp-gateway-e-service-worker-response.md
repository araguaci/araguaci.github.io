---
layout: post
title: "Helpdesk com três modos de WhatsApp e o service worker que invalidava a resposta"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-035"
description: "Portal de suporte com token de acompanhamento e um único gateway WhatsApp (log, WAHA ou Meta), depois de corrigir cache do service worker, assets do Vite e o e-mail de senha em inglês."
date: 2026-09-18 00:00:00+00:00
categories: devlog
category: arquitetura
tags: [laravel, whatsapp, service-worker, vite, smtp]
---

# Helpdesk com três modos de WhatsApp e o service worker que invalidava a resposta

> [!NOTE]
> **Resumo Executivo (DEV-2026-035)**: Portal de suporte com token de acompanhamento e um único gateway WhatsApp (log, WAHA ou Meta), depois de corrigir cache do service worker, assets do Vite e o e-mail de senha em inglês.

---

### 🚨 O Desafio Técnico / Contexto
O service worker em cache agressivo quebrava o preload com 'Failed to convert value to Response'. O nginx servia um manifest do Vite de outro build. Módulos respondiam HTTP 500 porque o schema ainda não tinha colunas que o código já lia. O reset de senha saía em inglês.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Um gateway com modos log, waha e meta evita três integrações paralelas enquanto o canal ainda está em prova.
* 💡 Cache-first em aplicação Laravel com assets versionados pelo Vite dessincroniza o preload. Estático pode cachear; o manifest, não.
* 💡 Reparar migrations que ficaram para trás faz parte do deploy. O seeder assume colunas que um banco antigo não tem.
* 💡 E-mail de redefinição pede notificação própria e lang pt_BR. O template padrão do framework não traduz sozinho.

---

### 🛠️ Especificação Técnica & Código-Chave
```bash
# Modos do gateway (segredo fica no .env, não na tela de Settings)
# WHATSAPP_GATEWAY=log|waha|meta

# Conferir schema antes de culpar a rota
php scripts/repair-migrations.php
php scripts/smoke-modules.php
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Chamado público com protocolo e WhatsApp de primeiro nível no mesmo app, com assets que batem com o build.

* **Projetos Relacionados**: `omnichannel-system`, `lorentz-vps-stack`
* **Registro de Origem**: `_data/daily.dev-03.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
