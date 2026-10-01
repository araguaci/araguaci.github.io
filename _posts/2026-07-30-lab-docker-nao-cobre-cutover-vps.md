---
layout: post
title: "O que o laboratório Docker não mostra na ida para a VPS"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-039"
description: "Compose verde no WSL não garante certificado, caminho de volume, driver SQL nem URL pública. O corte de ambiente quebrou em TLS, symlink e driver legado."
date: 2026-07-30 00:00:00+00:00
categories: devlog
category: devops
tags: [vps, tls, symlink, php, sql-server, caddy]
---

# O que o laboratório Docker não mostra na ida para a VPS

> [!NOTE]
> **Resumo Executivo (DEV-2026-039)**: Compose verde no WSL não garante certificado, caminho de volume, driver SQL nem URL pública. O corte de ambiente quebrou em TLS, symlink e driver legado.

---

### 🚨 O Desafio Técnico / Contexto
O laboratório aceita HTTP e certificado autoassinado. Em produção o navegador cobra HTTPS válido, o PBX já ocupa a porta 443, um atalho em /root mudava o caminho relativo do volume e o PHP 8.2 não tinha a extensão mssql antiga.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 URL pública antiga duplicada no .env vence no source do shell e aponta o stack para o host anterior.
* 💡 Um symlink de atalho altera ../supervisor. O volume monta uma pasta vazia e o site sobe sem código.
* 💡 No PHP 8.2 o driver é mssqlnative, com TrustServerCertificate quando o SQL ainda usa certificado interno. A extensão mssql legada não existe nesse runtime.
* 💡 ADOdb e a pasta adodb5 não são o mesmo caminho. Flags de debug do Supervisor ficam desligadas no host de produção.

---

### 🛠️ Especificação Técnica & Código-Chave
```bash
# Conferir para onde o relativo aponta antes do compose
readlink -f /root/lorentz
ls -la /root/omnichannel/supervisor/index.php

# .env: uma única URL pública. Duplicata antiga ganha no `source`.
# Driver no container: mssqlnative + TrustServerCertificate=true
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O checklist de corte passa a olhar certificado, caminho real do volume e driver SQL, além do compose.

* **Projetos Relacionados**: `lorentz-vps-stack`, `supervisor`
* **Registro de Origem**: `_data/daily.dev-03.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
