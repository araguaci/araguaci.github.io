---
layout: post
title: "Capacidade de IoT se define em patamares, antes do primeiro cliente em produção"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-094"
description: "O desenho inicial dizia o que construir, mas não até quantos dispositivos ele aguentaria. O plano de expansão fixou três patamares, com limites e o que precisa estar pronto para passar de um ao outro."
date: 2026-08-06 00:00:00-03:00
categories: devlog
category: arquitetura
tags: [iot, capacidade, teste-de-carga, planejamento]
---

# Capacidade de IoT se define em patamares, antes do primeiro cliente em produção

> [!NOTE]
> **Resumo Executivo (DEV-2026-094)**: O desenho inicial dizia o que construir, mas não até quantos dispositivos ele aguentaria. O plano de expansão fixou três patamares, com limites e o que precisa estar pronto para passar de um ao outro.

---

### 🚨 O Desafio Técnico / Contexto
Um laboratório com poucos dispositivos não diz nada sobre uma pousada inteira ou uma rede delas. Sem limites escritos, o primeiro cliente real seria também o primeiro teste de carga.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 L0, laboratório: até 10 dispositivos. L1, uma pousada: até 80 dispositivos e 20 req/s de ingestão. L2, rede: até 500 dispositivos e 100 req/s. São metas de projeto, ainda não medidas.
* 💡 O limite inclui latência: p95 de ingestão abaixo de 200 ms em L1 e de 300 ms em L2, para um servidor lento não passar por aprovado.
* 💡 O bloqueio seguinte ficou explícito: limite de requisições, token por dispositivo e retenção, depois MariaDB, e teste de carga antes da primeira pousada.

---

### 🛠️ Especificação Técnica & Código-Chave


---

### 📈 Impacto no Ecossistema & Valor Prático
A ida para produção passou a ter uma condição verificável, e não uma estimativa de que deve aguentar.

* **Projetos Relacionados**: `lorentz-iot`, `lorentz-hotel`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
