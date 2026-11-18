---
layout: post
title: "Asterisk AMI Originate exige atendimento da perna A no ramal e sincronização de CDR pede carga histórica idempotente"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-133"
description: "O disparo de chamadas pelo discador parecia congelar após o envio bem-sucedido do comando AMI e os relatórios de CDR permaneciam zerados. Descobrimos que a originação por ramal aguarda o operador atender a perna A antes de discar para o cliente e que a API de CDR filtrava entregas já confirmadas."
date: 2026-11-07 00:00:00-03:00
categories: devlog
category: telefonia
tags: [asterisk, ami, pjsip, cdr, webrtc, telefonia]
---

# Asterisk AMI Originate exige atendimento da perna A no ramal e sincronização de CDR pede carga histórica idempotente

> [!NOTE]
> **Resumo Executivo (DEV-2026-133)**: O disparo de chamadas pelo discador parecia congelar após o envio bem-sucedido do comando AMI e os relatórios de CDR permaneciam zerados. Descobrimos que a originação por ramal aguarda o operador atender a perna A antes de discar para o cliente e que a API de CDR filtrava entregas já confirmadas.

---

### 🚨 O Desafio Técnico / Contexto
Ao clicar em discar no discador automático, a API retornava sucesso mas a chamada não chegava ao telefone externo. Paralelamente, o PABX acumulava chamadas em banco mas o CRM continuava sem nenhum registro de atendimento para exibir nos relatórios.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 No comando AMI Originate com Channel e Exten, o Asterisk toca primeiro o ramal do operador e só inicia a perna externa quando o ramal atende.
* 💡 O operador precisa estar com o ramal PJSIP ou softphone WebRTC registrado e ativo no navegador para receber o toque preparatório.
* 💡 Rotinas de consumo de CDR com filtro pending=1 ignoram registros previamente confirmados (acked), necessitando de uma flag para sincronização histórica idempotente.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
// Asterisk AMI Originate: disca callerExt primeiro, depois destination
state.amiClient.sendAction({
  Action: 'Originate',
  Channel: `PJSIP/${callerExt}`,
  Exten: destination,
  Context: 'from-internal',
  Priority: '1',
  Async: 'true',
});
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O console de discagem passou a instruir o operador com clareza sobre o atendimento prévio e os relatórios passaram a puxar o histórico completo de chamadas.

* **Projetos Relacionados**: `triade-artesdosul`, `ecosul`, `iplive`
* **Registro de Origem**: `_data/daily.dev-21.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
