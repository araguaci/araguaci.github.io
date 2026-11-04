---
layout: post
title: "Quando o formulário de contato só recebe spam, a saída pode ser retirá-lo"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-103"
description: "Praticamente todas as mensagens que chegavam pelo site eram spam de robôs. Em vez de mais uma camada de filtro, o site trocou o formulário por caminhos que já qualificam o contato."
date: 2026-11-03 00:00:00-03:00
categories: devlog
category: arquitetura
tags: [formularios, spam, jekyll, suporte]
---

# Quando o formulário de contato só recebe spam, a saída pode ser retirá-lo

> [!NOTE]
> **Resumo Executivo (DEV-2026-103)**: Praticamente todas as mensagens que chegavam pelo site eram spam de robôs. Em vez de mais uma camada de filtro, o site trocou o formulário por caminhos que já qualificam o contato.

---

### 🚨 O Desafio Técnico / Contexto
Os formulários do site enchiam a caixa de entrada de mensagens automáticas, e o contato real quase não aparecia. Manter o formulário exigiria filtrar para sempre um canal que trazia pouco.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Antes de reforçar a proteção, olhe o que o canal entrega. Se quase nada presta, o problema é o canal, e não o filtro.
* 💡 /contact/ e o layout do showcase passaram a levar ao simulador do Studio e a /suporte/, caminhos em que a pessoa já diz o que quer.
* 💡 A retirada precisa ir até o fim: o último formulário ativo só saiu no dia seguinte, junto com o contato.php, e os endpoints nos serviços externos ainda precisam ser desativados.

---

### 🛠️ Especificação Técnica & Código-Chave


---

### 📈 Impacto no Ecossistema & Valor Prático
O site parou de oferecer um canal que só trazia spam, e o contato passou pelo simulador e pelo suporte.

* **Projetos Relacionados**: `artesdosul`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
