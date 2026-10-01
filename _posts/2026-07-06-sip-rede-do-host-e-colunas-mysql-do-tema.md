---
layout: post
title: "SIP pede a rede do host, e o tema do Issabel lia a coluna errada"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-046"
description: "Registro e áudio não fecham bem atrás do NAT da bridge. Em produção o PBX usa a rede do host. O tema escuro quebrava porque a consulta de variáveis globais do MySQL pedia colunas com outro nome."
date: 2026-07-06 00:00:00+00:00
categories: devlog
category: telefonia
tags: [sip, docker, issabel, mysql, rtp]
---

# SIP pede a rede do host, e o tema do Issabel lia a coluna errada

> [!NOTE]
> **Resumo Executivo (DEV-2026-046)**: Registro e áudio não fecham bem atrás do NAT da bridge. Em produção o PBX usa a rede do host. O tema escuro quebrava porque a consulta de variáveis globais do MySQL pedia colunas com outro nome.

---

### 🚨 O Desafio Técnico / Contexto
Softphone externo registrava e a mídia não voltava, típico de RTP atrás do NAT do Docker. No painel do Issabel, a instalação do tema falhava ao ler globals: o PHP esperava aliases que o SHOW VARIABLES não devolve.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 SIP e RTP do PBX em produção usam a rede do host. A bridge serve para o que não precisa de mídia direta.
* 💡 SHOW GLOBAL VARIABLES devolve Variable e Value. O código do tema tem que ler esses nomes, não um alias inventado.
* 💡 O webphone fica num profile opcional enquanto o código-fonte ainda não foi clonado.
* 💡 Instalar tema por REPLACE INTO, com arquivos em /var/www/html, evita pipe e base64 frágeis numa sessão SSH.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
# PBX com SIP/RTP na rede do host
services:
  issabel:
    network_mode: host

# MySQL: os nomes reais da saída
SHOW GLOBAL VARIABLES;
# colunas: Variable, Value
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O ramal externo volta a ter áudio e o tema do painel instala sem quebrar na leitura do MySQL.

* **Projetos Relacionados**: `issabel4-docker`, `lorentz-vps-stack`, `lorentz-webphone`
* **Registro de Origem**: `_data/daily.dev-03.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
