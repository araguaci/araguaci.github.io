---
layout: post
title: "Uma pasta que parece cópia pode ser junction do mesmo repositório"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-087"
description: "Em 2026-06-21, a pasta supervisor parecia um checkout independente, mas apontava para supervisor-php733. Quem ignora isso supõe duas árvores de trabalho onde só existe uma."
date: 2026-06-21 00:00:00-03:00
categories: devlog
category: windows
tags: [windows, junction, git, checkout]
---

# Uma pasta que parece cópia pode ser junction do mesmo repositório

> [!NOTE]
> **Resumo Executivo (DEV-2026-087)**: Em 2026-06-21, a pasta supervisor parecia um checkout independente, mas apontava para supervisor-php733. Quem ignora isso supõe duas árvores de trabalho onde só existe uma.

---

### 🚨 O Desafio Técnico / Contexto
Duas pastas com o mesmo conteúdo sugeriam dois checkouts. Na verdade, supervisor era uma junction do Windows para supervisor-php733, com o mesmo .git e o mesmo HEAD.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O atributo DL em Get-ChildItem indica diretório com reparse point. O nome e o conteúdo da pasta não mostram isso.
* 💡 Mudar de branch em uma das pastas muda também a outra, porque as duas compartilham o HEAD.
* 💡 Esse tipo de fato envelhece: naquele dia era uma junction, e em 2026-11-04 supervisor já era um repositório comum e supervisor-php733 não existia mais na máquina. Confira antes de confiar na anotação.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
Get-ChildItem D:\projeto | Where-Object { $_.Attributes -match 'ReparsePoint' }
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Conferir o tipo da pasta passou a vir antes de qualquer decisão sobre qual checkout é o canônico.

* **Projetos Relacionados**: `lorentz-supervisor`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
