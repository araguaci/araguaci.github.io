---
layout: post
title: "Dois checkouts do mesmo produto divergiram em 1.425 arquivos, e só o hash mostrou"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-090"
description: "Duas pastas do Supervisor pareciam variações pequenas uma da outra. Com a comparação por hash, ficou claro que nenhuma das duas podia ser tratada como cópia da outra."
date: 2026-07-15 00:00:00-03:00
categories: devlog
category: devops
tags: [git, php, checkout, hash]
---

# Dois checkouts do mesmo produto divergiram em 1.425 arquivos, e só o hash mostrou

> [!NOTE]
> **Resumo Executivo (DEV-2026-090)**: Duas pastas do Supervisor pareciam variações pequenas uma da outra. Com a comparação por hash, ficou claro que nenhuma das duas podia ser tratada como cópia da outra.

---

### 🚨 O Desafio Técnico / Contexto
Havia dois checkouts paralelos do Supervisor e dúvida sobre qual usar. Nomes de pasta e branch não diziam o que cada um continha.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 A comparação por MD5 achou cerca de 4.332 arquivos em comum, 1.425 deles com conteúdo diferente.
* 💡 Cada lado tinha funcionalidades que o outro não recebeu, então adotar um e apagar o outro perderia trabalho.
* 💡 O relatório entrou no repositório e as regras do agente passaram a apontar para ele, para evitar a repetição da dúvida a cada sessão.

---

### 🛠️ Especificação Técnica & Código-Chave


---

### 📈 Impacto no Ecossistema & Valor Prático
A escolha do checkout passou a ser feita com um relatório na mão, e não pelo nome da pasta.

* **Projetos Relacionados**: `lorentz-supervisor`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
