---
layout: post
title: "DTMF de celular na URA e o dispositivo de áudio que o PJSIP não abria"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-036"
description: "Dígito de celular some quando a URA espera tom na faixa de voz e o tronco entrega RFC 2833. No laboratório, o softphone falha se o PJSIP foi compilado sem o host de áudio do Windows."
date: 2026-08-11 00:00:00+00:00
categories: devlog
category: telefonia
tags: [dtmf, ura, pjsip, asterisk, panasonic]
---

# DTMF de celular na URA e o dispositivo de áudio que o PJSIP não abria

> [!NOTE]
> **Resumo Executivo (DEV-2026-036)**: Dígito de celular some quando a URA espera tom na faixa de voz e o tronco entrega RFC 2833. No laboratório, o softphone falha se o PJSIP foi compilado sem o host de áudio do Windows.

---

### 🚨 O Desafio Técnico / Contexto
Em campo, menus e transferências da URA não recebiam o dígito vindo de celular. No lab, o PJSIP 2.12.1 não abria o dispositivo de som. Os dois sintomas pareciam a mesma falha e não eram.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Antes de alterar o menu da URA, confirmar se o dígito chega como RFC 2833, SIP INFO ou tom in-band.
* 💡 A captura no trecho do PABX mostra o evento de telefonia que o log da URA não registra.
* 💡 No Windows, o pjproject de teste local precisa do host de áudio WMME. Sem isso o softphone sobe e não há áudio.

---

### 🛠️ Especificação Técnica & Código-Chave
```bash
# Separar as duas falhas
# 1) Sinalização: o INVITE/RTP traz telephone-event (RFC 2833)?
# 2) Laboratório: o build do PJSIP incluiu o host WMME?

# Conferir no Asterisk se o dígito chegou ao canal
asterisk -rx "core show channel <canal>"
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O diagnóstico de campo separa falha de sinalização DTMF de falha de compilação do softphone de teste.

* **Projetos Relacionados**: `omnichannel`, `ura`, `_lab`
* **Registro de Origem**: `_data/daily.dev-03.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
