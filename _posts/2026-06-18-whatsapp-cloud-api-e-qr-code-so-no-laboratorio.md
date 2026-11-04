---
layout: post
title: "Canal de WhatsApp em produção usa a Cloud API, e a solução por QR Code fica no laboratório"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-083"
description: "A primeira versão do plano apoiava o canal em WAHA, que não é a API oficial. A revisão contra o código trocou a base por Meta Cloud API e cortou o que não era necessário ao piloto."
date: 2026-06-18 00:00:00-03:00
categories: devlog
category: arquitetura
tags: [whatsapp, meta, waha, integracao]
---

# Canal de WhatsApp em produção usa a Cloud API, e a solução por QR Code fica no laboratório

> [!NOTE]
> **Resumo Executivo (DEV-2026-083)**: A primeira versão do plano apoiava o canal em WAHA, que não é a API oficial. A revisão contra o código trocou a base por Meta Cloud API e cortou o que não era necessário ao piloto.

---

### 🚨 O Desafio Técnico / Contexto
A versão 1.0 do plano previa WAHA self-hosted, custo zero de API, orquestrador Node.js e sincronização dupla entre SQL Server e MySQL. Comparada ao repositório, ela citava um passo de QR Code que não existe na API oficial e ignorava o que o código já tinha.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 WAHA, Evolution e Baileys ficam só para protótipo: não são a API oficial e carregam risco de banimento.
* 💡 Custo de API por conversa precisa estar no plano. O 'R$ 0' da versão anterior subestimava o gasto real na Meta.
* 💡 O orquestrador Node.js saiu porque a ponte PHP/Laravel existente basta. Stack extra sem necessidade também é custo de operação.
* 💡 A sincronização dupla virou opcional numa fase posterior. No piloto há uma única fonte operacional, o que reduz a complexidade.
* 💡 Revisar o plano contra o código revelou que o WhatsAppService só persistia localmente e não chamava a Meta.

---

### 🛠️ Especificação Técnica & Código-Chave


---

### 📈 Impacto no Ecossistema & Valor Prático
O plano passou a descrever o que pode ir para produção, com os estudos de WAHA isolados em projetos/.

* **Projetos Relacionados**: `omnichannel-system`, `lorentz-supervisor`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
