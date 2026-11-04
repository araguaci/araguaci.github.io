---
layout: post
title: "Em VPS compartilhada, todo comando fica restrito ao projeto"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-099"
description: "O serviço novo entrou numa VPS de produção que já roda dezenas de outros containers. Qualquer comando global de limpeza derrubaria os vizinhos, então toda operação ficou limitada ao projeto."
date: 2026-10-30 00:00:00-03:00
categories: devlog
category: infraestrutura
tags: [docker, compose, nginx, fail2ban, vps]
---

# Em VPS compartilhada, todo comando fica restrito ao projeto

> [!NOTE]
> **Resumo Executivo (DEV-2026-099)**: O serviço novo entrou numa VPS de produção que já roda dezenas de outros containers. Qualquer comando global de limpeza derrubaria os vizinhos, então toda operação ficou limitada ao projeto.

---

### 🚨 O Desafio Técnico / Contexto
O deploy do iplive divide a máquina com outros produtos em produção. O serviço também precisa de backup, proteção contra força bruta e um jeito público de checar a saúde, sem atingir o que já estava lá.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Nada de down nem prune globais. Use um nome de projeto no Compose e só comandos com esse escopo.
* 💡 O Nginx é compartilhado: rode nginx -t antes de cada reload. Um erro em um site impede o reload de todos.
* 💡 O serviço escuta só em 127.0.0.1, e o Nginx faz a publicação.
* 💡 A jail do fail2ban para Asterisk usa a chain DOCKER-USER, porque tráfego de porta publicada passa pelo FORWARD. O protocol=all faz o bloqueio valer além do TCP.
* 💡 Backup diário por cron e um /healthz público fecham o mínimo de operação sem depender dos vizinhos.

---

### 🛠️ Especificação Técnica & Código-Chave
```bash
docker compose -p iplive up -d
nginx -t && systemctl reload nginx
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O serviço entrou em produção com backup, proteção e checagem de saúde, sem comandos que alcançassem os outros containers.

* **Projetos Relacionados**: `iplive`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
