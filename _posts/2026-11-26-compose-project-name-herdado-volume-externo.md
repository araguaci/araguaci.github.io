---
layout: post
title: "COMPOSE_PROJECT_NAME exportado de outro .env troca o nome dos volumes externos"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-181"
description: "O deploy do PABX criava volumes com prefixo fixo, e o compose montava o nome com COMPOSE_PROJECT_NAME. Rodado de um script que exportava o .env da stack, o compose procurou volumes que não existiam."
date: 2026-11-26 00:00:00-03:00
categories: devlog
category: devops
tags: [docker-compose, volumes, bash]
---

# COMPOSE_PROJECT_NAME exportado de outro .env troca o nome dos volumes externos

> [!NOTE]
> **Resumo Executivo (DEV-2026-181)**: O deploy do PABX criava volumes com prefixo fixo, e o compose montava o nome com COMPOSE_PROJECT_NAME. Rodado de um script que exportava o .env da stack, o compose procurou volumes que não existiam.

---

### 🚨 O Desafio Técnico / Contexto
deploy-issabel.sh criava os volumes como issabel_*. O compose do Issabel declara o nome como ${COMPOSE_PROJECT_NAME:-issabel}_issabel-spool. O script do laboratório carregava o .env da stack com set -a, que define COMPOSE_PROJECT_NAME=lorentz, e chamava o deploy do Issabel. A variável exportada venceu o padrão, e o compose parou em "external volume lorentz_issabel-spool not found", depois de montar uma imagem de 4,7 GB com o nome errado.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 set -a seguido de source .env exporta tudo para os processos filhos, inclusive variáveis que o compose de outro projeto lê, como COMPOSE_PROJECT_NAME.
* 💡 Quem cria volume com nome fixo e depois chama um compose que monta o nome com variável precisa fixar a variável na chamada.
* 💡 Na VPS o problema não aparecia porque o deploy do PABX rodava sem o .env da stack exportado. Só a combinação dos dois scripts mostrou.

---

### 🛠️ Especificação Técnica & Código-Chave
```bash
# os volumes são issabel_*: o projeto do compose tem de bater
COMPOSE_PROJECT_NAME=issabel bash ./scripts/deploy-production.sh
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O PABX passou a subir com o .env da stack carregado, e a imagem órfã deixou de ocupar disco.

* **Projetos Relacionados**: `lorentz-vps-stack`, `issabel4-docker`
* **Registro de Origem**: `_data/daily.dev-34.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
