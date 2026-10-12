---
layout: post
title: "A chamada SIP atende sem voz quando o SDP fica no IP local"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-076"
description: "O ramal registrou, a chamada atendeu e o microfone chegou ao Janus, mas a faixa remota ficou muda. O Contact público não corrige o endereço de mídia: sem sdp_ip o c= do SDP continua no IP local, e o comedia só aprende o caminho depois do primeiro RTP."
date: 2026-10-12 00:00:00+00:00
categories: devlog
category: telefonia
tags: [janus, asterisk, sip, rtp, nat]
---

# A chamada SIP atende sem voz quando o SDP fica no IP local

> [!NOTE]
> **Resumo Executivo (DEV-2026-076)**: O ramal registrou, a chamada atendeu e o microfone chegou ao Janus, mas a faixa remota ficou muda. O Contact público não corrige o endereço de mídia: sem sdp_ip o c= do SDP continua no IP local, e o comedia só aprende o caminho depois do primeiro RTP.

---

### 🚨 O Desafio Técnico / Contexto
O discador de teste usa o binário Janus 1.3.3 já instalado, sem recompilar, com API HTTP na porta 8088. Este build não tem transporte WebSocket. O ramal que completou a chamada é chan_sip, não PJSIP: o driver PJSIP estava carregado só com um endpoint fictício. No par, force rport, symmetric RTP e directmedia desligado já estavam ligados, e os codecs do par eram ulaw e alaw. O navegador ouviu o tom DTMF gerado na página e o Janus recebeu o microfone. A voz do PABX não voltou. Um socket UDP preso numa porta local chegou ao PABX com outra porta em rport, então anunciar o IP público com a porta local também erra o destino.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 behind_nat no janus.plugin.sip.jcfg faz o Sofia reescrever o Contact pelo rport. O c= do SDP é outro campo: sem sdp_ip, janus_sip_sdp_manipulate grava o IP local.
* 💡 sip show peers e pjsip show endpoints dizem o driver. NAT de chan_sip (nat=force_rport,comedia e directmedia=no) não é o de PJSIP (rtp_symmetric, force_rport, rewrite_contact, direct_media).
* 💡 Chamada atendida já negociou codec. Oferta com codec pcmu é ulaw. Falta de Opus não explica silêncio depois do 200 OK; um codec recusado cai com 488 antes do atendimento.
* 💡 Symmetric RTP só troca o destino depois que o primeiro pacote entra. A faixa a liberar no firewall é a de rtp show settings, neste Asterisk UDP 10000-20000, não a porta 5060 do Contact.
* 💡 Tom DTMF local prova o alto-falante. Faixa remota sem nível prova que o RTP do PABX não chegou ao navegador. A prova no servidor é rtp set debug on: Got RTP e o IP do Sent RTP.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
# janus.plugin.sip.jcfg — Contact e mídia não andam juntos
behind_nat = true
rtp_port_range = "20000-40000"
# sdp_ip ausente: o c= do SDP fica no IP local
```

---

### 📈 Impacto no Ecossistema & Valor Prático
No próximo discador, o checklist começa pelo driver do ramal, pelo c= do SDP e pelo debug RTP, não por codec novo nem pela porta de registro.

* **Projetos Relacionados**: `janus`
* **Registro de Origem**: `_data/daily.dev-13.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
