---
layout: post
title: "Modernizar sem parar o legado muda como se projeta cada integração nova"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-084"
description: "Novos clientes passaram a exigir WhatsApp enquanto a base instalada segue no stack legado. A regra passou a ser projetar a integração para funcionar no legado e servir também à plataforma moderna."
date: 2026-06-21 00:00:00-03:00
categories: devlog
category: arquitetura
tags: [legado, whatsapp, modernizacao, strangler-fig]
---

# Modernizar sem parar o legado muda como se projeta cada integração nova

> [!NOTE]
> **Resumo Executivo (DEV-2026-084)**: Novos clientes passaram a exigir WhatsApp enquanto a base instalada segue no stack legado. A regra passou a ser projetar a integração para funcionar no legado e servir também à plataforma moderna.

---

### 🚨 O Desafio Técnico / Contexto
O negócio precisa fechar contratos novos sem quebrar quem já roda CTI, URA, cliente desktop e Supervisor em produção. Desenvolver o canal só na plataforma nova deixaria esses clientes de fora, e desenvolvê-lo só no legado obrigaria a refazer tudo depois.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Modernizar e manter o legado são duas frentes simultâneas: o legado continua recebendo as soluções novas.
* 💡 A integração precisa encaixar no Supervisor e no CTI legados e ao mesmo tempo servir de base para a plataforma moderna.
* 💡 Listar nominalmente os projetos em produção evita tratar como descartável algo de que um cliente ainda depende.

---

### 🛠️ Especificação Técnica & Código-Chave


---

### 📈 Impacto no Ecossistema & Valor Prático
O planejamento do WhatsApp passou a considerar o legado e a plataforma moderna desde o início.

* **Projetos Relacionados**: `omnichannel-system`, `lorentz-supervisor`, `lorentz-cti`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
