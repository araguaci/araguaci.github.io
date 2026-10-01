---
layout: post
title: "Trocar o repositório do PBX na VPS sem perder o firstboot local"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-040"
description: "A VPS ainda apontava para o fork antigo do Issabel. O pull só fechou depois de descartar o firstboot alterado no servidor e alinhar o remote canônico."
date: 2026-07-21 00:00:00+00:00
categories: devlog
category: devops
tags: [git, issabel, docker, asterisk]
---

# Trocar o repositório do PBX na VPS sem perder o firstboot local

> [!NOTE]
> **Resumo Executivo (DEV-2026-040)**: A VPS ainda apontava para o fork antigo do Issabel. O pull só fechou depois de descartar o firstboot alterado no servidor e alinhar o remote canônico.

---

### 🚨 O Desafio Técnico / Contexto
Scripts de primeiro boot editados direto na VPS divergiam do Git e bloqueavam a atualização. No Asterisk 18 o schema de call center esperado pelo bootstrap também podia não existir, e o script abortava o boot inteiro.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Cópia local de script de boot no servidor não é fonte da verdade. O descarte consciente vem antes do pull.
* 💡 ISSABEL_REPO, a imagem e a tag de firstboot mudam juntos. Trocar só o remote deixa o container no fluxo antigo.
* 💡 A árvore anterior fica em backup no host antes de um re-clone.
* 💡 Se a tabela de call center não existe no Asterisk 18, o bootstrap pula esse passo em vez de falhar.

---

### 🛠️ Especificação Técnica & Código-Chave
```bash
# Na VPS, o firstboot local bloqueia o pull
git -C "$ISSABEL_DIR" status --short
# backup da árvore, depois alinhar origin e descartar o script divergente
git checkout -- issabel-firstboot
git pull

# Asterisk 18: schema de call center ausente não pode abortar o boot
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A troca de fork do PBX na VPS deixa de parar no primeiro arquivo editado à mão.

* **Projetos Relacionados**: `issabel4-docker`, `lorentz-vps-stack`
* **Registro de Origem**: `_data/daily.dev-03.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
