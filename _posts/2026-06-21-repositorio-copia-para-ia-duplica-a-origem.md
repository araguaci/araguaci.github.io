---
layout: post
title: "Repositório-cópia para a IA duplica código que já tem origem própria"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-086"
description: "Um repositório focado foi criado para trabalhar o WhatsApp com o claude.ai e logo passou a duplicar código. A decisão foi conectar a ferramenta aos repositórios reais e descontinuar a cópia."
date: 2026-06-21 00:00:00-03:00
categories: devlog
category: devops
tags: [git, github, claude, repositorios]
---

# Repositório-cópia para a IA duplica código que já tem origem própria

> [!NOTE]
> **Resumo Executivo (DEV-2026-086)**: Um repositório focado foi criado para trabalhar o WhatsApp com o claude.ai e logo passou a duplicar código. A decisão foi conectar a ferramenta aos repositórios reais e descontinuar a cópia.

---

### 🚨 O Desafio Técnico / Contexto
O repositório lorentz-whatsapp reunia num só lugar o que interessava à integração. Esse código já tinha origem própria em dois repositórios, então cada ajuste passaria a existir em dois lugares.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Com uma fonte única da verdade, a ferramenta enxerga o histórico real e o trabalho não precisa de um passo de sincronização.
* 💡 Antes de conectar um repositório, confira o que há nele: chave de terceiro em documento e arquivo de configuração versionado saem antes.
* 💡 A decisão vale para os dois lados: a pasta local foi removida e o repositório remoto, que ficou redundante, foi marcado para exclusão.

---

### 🛠️ Especificação Técnica & Código-Chave


---

### 📈 Impacto no Ecossistema & Valor Prático
O trabalho do canal voltou a acontecer nos repositórios que vão para produção.

* **Projetos Relacionados**: `omnichannel-system`, `lorentz-supervisor`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
