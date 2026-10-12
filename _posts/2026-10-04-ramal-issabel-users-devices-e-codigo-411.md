---
layout: post
title: "Ramal que só existe em arquivo de peer não aparece na lista do Issabel"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-064"
description: "Peers em arquivo customizado registram no Asterisk e não entram na tela de extensões. A lista lê users, devices e sip, e o ramal 411 ainda colidia com o código de facilidade da lista telefônica."
date: 2026-10-04 00:00:00+00:00
categories: devlog
category: telefonia
tags: [asterisk, issabel, sip, php, chan-sip]
---

# Ramal que só existe em arquivo de peer não aparece na lista do Issabel

> [!NOTE]
> **Resumo Executivo (DEV-2026-064)**: Peers em arquivo customizado registram no Asterisk e não entram na tela de extensões. A lista lê users, devices e sip, e o ramal 411 ainda colidia com o código de facilidade da lista telefônica.

---

### 🚨 O Desafio Técnico / Contexto
A tela de extensões estava vazia mesmo com peers no sip show peers. O cadastro em sip_lab_peers.conf e sip_ura_peers.conf não cria linha em users. core_users_add imprimia ERROR: this state should not exist duas vezes por ramal. Em Feature Codes aparecia o aviso de conflito entre código de facilidade e número de ramal.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 A GUI do Issabel lista users + devices + sip. Peer só em sip_*_custom.conf existe para o Asterisk e não para o pbxadmin.
* 💡 core_users_add exige ringtimer inteiro (0, não string vazia). callwaiting e pinless têm de ser enabled ou disabled. Sem isso a função escreve ERROR: this state should not exist.
* 💡 Um lote seguinte que só atualiza o nome não entra de novo em core_users_add, então não corrige callwaiting já gravado vazio.
* 💡 O conflito era o defaultcode 411 de pbdirectory (app-pbdirectory) contra o ramal 411. featurecodeadmin usa customcode quando preenchido. customcode *411 libera o ramal e mantém a lista telefônica.
* 💡 O bootstrap do script é require de /etc/issabelpbx.conf com issabelpbx_auth desligado. Senha de ramal fica em arquivo modo 600 e não sai no stdout.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
UPDATE featurecodes
SET customcode = '*411'
WHERE modulename = 'pbdirectory'
  AND featurename = 'app-pbdirectory';
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Os ramais do laboratório passam a aparecer em Extensões, e o aviso de conflito de código de facilidade some sem renumerar o ramal 411.

* **Projetos Relacionados**: `lorentz-vps-stack`
* **Registro de Origem**: `_data/daily.dev-08.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
