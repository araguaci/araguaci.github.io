---
layout: post
title: "Regra de banco no UFW não alcança porta que o Docker publicou"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-054"
description: "O Docker publica porta por FORWARD e DNAT e ignora o UFW no INPUT. O filtro de 3306, 6379 e 5432 fica na cadeia DOCKER-USER."
date: 2026-08-19 00:00:00+00:00
categories: devlog
category: infraestrutura
tags: [docker, ufw, iptables, postgres]
---

# Regra de banco no UFW não alcança porta que o Docker publicou

> [!NOTE]
> **Resumo Executivo (DEV-2026-054)**: O Docker publica porta por FORWARD e DNAT e ignora o UFW no INPUT. O filtro de 3306, 6379 e 5432 fica na cadeia DOCKER-USER.

---

### 🚨 O Desafio Técnico / Contexto
Trancar o banco no UFW não mudava o que estava publicado pelo compose. A regra nunca era consultada no caminho que o Docker usa para expor a porta.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 deployments/ainativo/RESTRINGIR_PORTAS_DB.md: a regra entra em DOCKER-USER, cadeia AINATIVO_DB_PORTS.
* 💡 restrict-db-ports.sh --persist instala o script em /usr/sbin e a unit restrict-db-ports.service depois do docker.service.
* 💡 Nesta VPS os bancos não têm ports no host. O script cobre o dia em que alguém publicar 5432 ou 6379.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
sudo /opt/ainativo/src/sio-ecosystem/tools/scripts/restrict-db-ports.sh --persist
sudo restrict-db-ports.sh --status
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Porta de banco publicada pelo Docker passou a depender da cadeia DOCKER-USER, não do UFW de entrada.

* **Projetos Relacionados**: `sio-ecosystem`
* **Registro de Origem**: `_data/daily.dev-04.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
