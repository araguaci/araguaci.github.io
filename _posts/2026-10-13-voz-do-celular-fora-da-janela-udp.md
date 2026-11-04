---
layout: post
title: "O celular registra no PABX e a voz sai numa porta UDP que o firewall não entrega"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-078"
description: "O registro SIP e a chamada atendida usam o WebSocket na porta 443. A voz é outro fluxo, UDP, e o fim da faixa que o Asterisk obedece pode ficar acima da janela que o firewall entrega."
date: 2026-10-13 00:00:00-03:00
categories: devlog
category: telefonia
tags: [asterisk, webrtc, rtp, firewall, docker]
---

# O celular registra no PABX e a voz sai numa porta UDP que o firewall não entrega

> [!NOTE]
> **Resumo Executivo (DEV-2026-078)**: O registro SIP e a chamada atendida usam o WebSocket na porta 443. A voz é outro fluxo, UDP, e o fim da faixa que o Asterisk obedece pode ficar acima da janela que o firewall entrega.

---

### 🚨 O Desafio Técnico / Contexto
Dois celulares registraram e a chamada ficou atendida, sem áudio nos dois lados. O log do Asterisk repetia o estouro de tempo do DTLS e não havia pacote UDP na faixa de voz. O ajuste de um aparelho ainda apontava o WebSocket para 127.0.0.1 na porta 8445, porque o proxy entrega o PABX nesse host e o provisionamento copiou o Host do pedido.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O WebSocket do celular tem de usar o nome público, em wss na porta 443. O nome chega em X-Forwarded-Host. HTTP_HOST, nesse proxy, é 127.0.0.1:8445, e no aparelho esse endereço é o próprio celular, com o certificado do PABX.
* 💡 rtp.conf inclui rtp_additional.conf antes de rtp_custom.conf. A primeira atribuição de rtpend vale. O Issabel gravava 20000 no primeiro arquivo, então o valor 10100 do segundo não entrava em vigor.
* 💡 A voz WebRTC não volta pelo WebSocket. Com o fim em 20000 o Asterisk abriu a mídia acima de 10100. Um pacote de prova entrou em 10000, 10050 e 10100 e não entrou na porta alta. Sem esse UDP o DTLS não completa e os dois lados ficam mudos.
* 💡 Sem servidor STUN o navegador anuncia só o endereço privado da rede do aparelho. O PABX precisa anunciar o candidato ICE do endereço público, não o das pontes Docker.
* 💡 O Issabel também guarda rtpend na tabela sipsettings. Mudar só o arquivo volta atrás quando alguém aplica a configuração do PABX. O peer em 127.0.0.1 prova o soquete do WebSocket, não o caminho da voz.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
# A primeira atribuição é a que o Asterisk usa.
# rtp_additional.conf é incluído antes de rtp_custom.conf.
rtpstart=10000
rtpend=10100
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A chamada entre os dois celulares passou a ter voz quando o RTP ficou em 10000–10100 e o WebSocket deixou de apontar para o host interno.

* **Projetos Relacionados**: `lorentz-vps-stack`, `lorentz-mobile`
* **Registro de Origem**: `_data/daily.dev-15.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
