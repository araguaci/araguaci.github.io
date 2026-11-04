---
layout: post
title: "O ID válido da licença é o que o executável daquela máquina grava, não o da ferramenta do lab"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-093"
description: "Na visita a campo, a licença gerada com a ferramenta do laboratório foi recusada, embora o procedimento estivesse certo. O binário em produção era de outro build e calculava outro ID."
date: 2026-08-01 00:00:00-03:00
categories: devlog
category: telefonia
tags: [ura, licenca, vbnet, campo]
---

# O ID válido da licença é o que o executável daquela máquina grava, não o da ferramenta do lab

> [!NOTE]
> **Resumo Executivo (DEV-2026-093)**: Na visita a campo, a licença gerada com a ferramenta do laboratório foi recusada, embora o procedimento estivesse certo. O binário em produção era de outro build e calculava outro ID.

---

### 🚨 O Desafio Técnico / Contexto
A URA instalada registrou 'Licença inválida ID Local' com uma licença gerada a partir do ID impresso pela ferramenta do lab. O executável em produção tinha gravado no INI um ID começando em 1970, diferente do valor que a ferramenta mostrava.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Gerada de novo com o ID que aquele executável gravou no INI, a licença passou a mostrar 'Licença OK' no log.
* 💡 ID de máquina começando em 19700101 é sintoma de data de instalação zerada ou anormal naquele build.
* 💡 Ferramenta de apoio e produto precisam vir do mesmo build. Em campo, consulte a versão e o tamanho do binário instalado antes de gerar a licença.
* 💡 Na versão seguinte, data zerada ou ausente passou a dar falha explícita, em vez de gerar um ID enganoso, e o código morto de WMIC saiu.

---

### 🛠️ Especificação Técnica & Código-Chave


---

### 📈 Impacto no Ecossistema & Valor Prático
A licença de campo passou a ser gerada a partir do que o binário instalado informa.

* **Projetos Relacionados**: `ura`, `ura-dtmf-lab`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
