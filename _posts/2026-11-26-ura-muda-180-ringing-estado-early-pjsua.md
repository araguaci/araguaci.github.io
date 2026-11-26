---
layout: post
title: "URA muda porque o 180 Ringing tirava a chamada do estado que emitia o atendimento"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-179"
description: "A URA em Linux atendia, carregava a árvore e recebia dígitos, mas nunca tocava o menu. O evento de atendimento só saía no estado INCOMING, e o 180 enviado antes do 200 levava o INVITE para EARLY."
date: 2026-11-26 00:00:00-03:00
categories: devlog
category: infraestrutura
tags: [pjsip, sip, asterisk, ura, telefonia]
---

# URA muda porque o 180 Ringing tirava a chamada do estado que emitia o atendimento

> [!NOTE]
> **Resumo Executivo (DEV-2026-179)**: A URA em Linux atendia, carregava a árvore e recebia dígitos, mas nunca tocava o menu. O evento de atendimento só saía no estado INCOMING, e o 180 enviado antes do 200 levava o INVITE para EARLY.

---

### 🚨 O Desafio Técnico / Contexto
A porta Linux da URA (PJSIP) responde 180 Ringing no on_incoming_call e só depois atende com 200. O on_call_media_state emitia o Event_answer apenas quando o estado era PJSIP_INV_STATE_INCOMING. A versão Windows atende direto com 200, e nela o estado ainda é INCOMING quando a mídia fica ativa. Na versão Linux o estado já é EARLY. As árvores começam num nó "Atendimento" que espera esse evento, então a URA ficava parada no primeiro nó, em silêncio. Os áudios estavam no lugar, e o código nem chegava a chamar o player.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Depois de um 18x sem SDP o INVITE fica em EARLY, não em INCOMING. Um teste de estado escrito para quem atende direto com 200 deixa de valer quando alguém acrescenta o 180.
* 💡 O log mostrou o caminho: eventos 2 (chegou), 4096 (confirmado), 32 (dígito) e 8 (desligou), sem o 4 (atendeu) e sem nenhuma linha de reprodução. A ausência do evento apontou o código antes de qualquer suspeita de formato de áudio.
* 💡 Numa porta entre plataformas, cada diferença de protocolo (180 antes do 200) tem de ser comparada com a versão antiga linha a linha. A correção aceitou INCOMING ou EARLY, com o motivo comentado.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
if (call_info.state == PJSIP_INV_STATE_INCOMING ||
    call_info.state == PJSIP_INV_STATE_EARLY)
    Evento(call_info.acc_id, call_id, Event_answer, ev_vazio, ...);
```

---

### 📈 Impacto no Ecossistema & Valor Prático
As árvores que começam em Atendimento voltaram a tocar o menu e a pesquisa na URA em container.

* **Projetos Relacionados**: `lorentz-ura-impacta`, `lorentz-vps-stack`
* **Registro de Origem**: `_data/daily.dev-34.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
