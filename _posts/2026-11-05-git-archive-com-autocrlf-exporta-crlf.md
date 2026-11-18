---
layout: post
title: "O git archive com autocrlf ligado exporta o texto em CRLF"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-149"
description: "O pacote enviado ao servidor chegou com fim de linha do Windows em 29 arquivos de texto. git archive obedece core.autocrlf, e só o que o .gitattributes fixa em LF escapa."
date: 2026-11-05 00:00:00-03:00
categories: devlog
category: devops
tags: [git, autocrlf, crlf, deploy]
---

# O git archive com autocrlf ligado exporta o texto em CRLF

> [!NOTE]
> **Resumo Executivo (DEV-2026-149)**: O pacote enviado ao servidor chegou com fim de linha do Windows em 29 arquivos de texto. git archive obedece core.autocrlf, e só o que o .gitattributes fixa em LF escapa.

---

### 🚨 O Desafio Técnico / Contexto
Em 2026-11-05 o envio para o servidor de deploy saiu da máquina em que core.autocrlf está true. O checkout local parecia certo, e o que chegou tinha CR.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 core.autocrlf=true faz o git archive converter o texto para CRLF na exportação. O arquivo no disco de trabalho não mostra esse CR.
* 💡 O que o .gitattributes fixa em LF continua em LF. O resto do texto vai com o fim de linha do Windows.
* 💡 A cópia que segue para o servidor passa por tr -d '\r' antes do envio. O .gitattributes só protege o arquivo que ele marca.
* 💡 A conferência é no arquivo que chegou, não no exit code do archive.

---

### 🛠️ Especificação Técnica & Código-Chave
```bash
git config --get core.autocrlf
tr -d '\r' < arquivo.txt > arquivo-lf.txt
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O envio passou a tirar o CR antes de chegar no servidor, e a conferência olha o arquivo recebido.

* **Projetos Relacionados**: `lorentz-vps-stack`
* **Registro de Origem**: `_data/daily.dev-26.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
