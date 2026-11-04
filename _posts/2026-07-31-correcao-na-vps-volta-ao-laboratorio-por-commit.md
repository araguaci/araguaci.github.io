---
layout: post
title: "Correção feita às pressas na VPS volta ao laboratório por commit, sem perder o trabalho local"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-091"
description: "Para estabilizar a produção, houve ajustes feitos direto na VPS, enquanto o laboratório tinha centenas de arquivos em andamento. O caminho foi publicar pelo Git o que estava na VPS e guardar o trabalho local em branch antes de sincronizar."
date: 2026-07-31 00:00:00-03:00
categories: devlog
category: devops
tags: [git, vps, php, deploy, hotfix]
---

# Correção feita às pressas na VPS volta ao laboratório por commit, sem perder o trabalho local

> [!NOTE]
> **Resumo Executivo (DEV-2026-091)**: Para estabilizar a produção, houve ajustes feitos direto na VPS, enquanto o laboratório tinha centenas de arquivos em andamento. O caminho foi publicar pelo Git o que estava na VPS e guardar o trabalho local em branch antes de sincronizar.

---

### 🚨 O Desafio Técnico / Contexto
A jornada foi do laboratório a uma VPS, depois a um ambiente Docker no WSL, depois a outra VPS, e por fim de volta ao laboratório para consolidar. Na volta, o código em produção e o laboratório já tinham andado por caminhos diferentes.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Correção feita na VPS precisa virar commit lá e ir para o remoto. Fora do Git, a próxima atualização pode apagá-la.
* 💡 Antes de alinhar o laboratório com a produção, um branch guardou os 221 arquivos em andamento. Nada se perdeu no alinhamento.
* 💡 O produto não foi reescrito. É o mesmo código migrando de PHP 5.6.40 para 7.3.33, 7.4.33 e 8.2.26, e registrar essa linhagem evita tratar cada pasta como um sistema à parte.
* 💡 A regra ficou escrita: ajuste destinado à VPS nasce no checkout do laboratório, segue por push e chega ao servidor com git pull.

---

### 🛠️ Especificação Técnica & Código-Chave
```bash
git switch -c lab-wip-pre-pull
git add -A && git commit -m "wip: laboratório antes de alinhar com a VPS"
git switch lorentz-vps && git pull --ff-only
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O laboratório voltou a coincidir com a produção, com o trabalho anterior recuperável em branch próprio.

* **Projetos Relacionados**: `lorentz-supervisor`, `lorentz-vps-stack`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
