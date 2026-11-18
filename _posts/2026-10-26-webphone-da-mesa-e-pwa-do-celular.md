---
layout: post
title: "O webphone da mesa e o PWA do celular entram por hosts e logins diferentes"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-141"
description: "Os dois falam com o mesmo PABX e o mesmo CTI, e mesmo assim não são o mesmo posto. Um é o telefone da mesa embutido no Operador Web. O outro é o aplicativo do celular publicado dentro do PBX."
date: 2026-10-26 00:00:00-03:00
categories: devlog
category: telefonia
tags: [webphone, webrtc, cti, pwa, supervisor]
---

# O webphone da mesa e o PWA do celular entram por hosts e logins diferentes

> [!NOTE]
> **Resumo Executivo (DEV-2026-141)**: Os dois falam com o mesmo PABX e o mesmo CTI, e mesmo assim não são o mesmo posto. Um é o telefone da mesa embutido no Operador Web. O outro é o aplicativo do celular publicado dentro do PBX.

---

### 🚨 O Desafio Técnico / Contexto
A pergunta era se o host público do softphone opera como o caminho /mobile/. Os dois são WebRTC no navegador. O da mesa vive num container próprio e entra pela sessão do Operador Web. O do celular é outro aplicativo, publicado dentro do PBX, com login próprio.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O da mesa é o Lorentz Webphone (fork 008, SIP.js), container próprio, embutido no Operador Web. A voz sai pelo WebSocket descrito na configuração desse aplicativo.
* 💡 O do celular é o Lorentz Mobile, PWA com JsSIP, arquivos em /mobile/ dentro do PBX. A voz sai por wss na porta 443, no caminho /mobile/ws.
* 💡 No CTI os dois usam web_agent. O celular autentica com sub próprio. Tratar os dois como um atalho só mistura host, login e estado do ramal.
* 💡 cli_GetWebphonePublicUrl, com a página em HTTPS e host no formato supervisor.<resto>, monta o softphone em https://phone.<resto>/. Isso não aponta para /mobile/.

---

### 🛠️ Especificação Técnica & Código-Chave


---

### 📈 Impacto no Ecossistema & Valor Prático
Embed, suporte e login passam a tratar mesa e celular como postos distintos, cada um com o seu host.

* **Projetos Relacionados**: `lorentz-webphone`, `supervisor`, `lorentz-vps-stack`
* **Registro de Origem**: `_data/daily.dev-24.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
