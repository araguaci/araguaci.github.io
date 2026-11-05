---
layout: post
title: "O commit falhou, o script seguiu em frente, e a tag da versão nova foi publicada no commit da versão anterior"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-130"
description: "Um único comando encadeava commit, tag e push, sem conferir o resultado de cada passo. A tag da versão foi parar no commit errado, e os passos de publicação passaram a depender do sucesso do anterior."
date: 2026-11-04 00:00:00-03:00
categories: devlog
category: devops
tags: [git, powershell, release, automacao]
---

# O commit falhou, o script seguiu em frente, e a tag da versão nova foi publicada no commit da versão anterior

> [!NOTE]
> **Resumo Executivo (DEV-2026-130)**: Um único comando encadeava commit, tag e push, sem conferir o resultado de cada passo. A tag da versão foi parar no commit errado, e os passos de publicação passaram a depender do sucesso do anterior.

---

### 🚨 O Desafio Técnico / Contexto
A mensagem foi passada com here-string para git commit -F -, e o Git tratou o texto como caminho de arquivo. O commit falhou com erro de pathspec, mas o PowerShell executou as linhas seguintes. A tag nova ficou no commit da versão anterior e foi enviada ao remoto. Conferi o arquivo VERSION dentro da tag e ele mostrava o número antigo.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 No PowerShell, um comando nativo que falha não interrompe o script. Confira $LASTEXITCODE depois de cada passo que vale a pena proteger.
* 💡 Grave a mensagem em um arquivo e use git commit -F arquivo. Não depende das regras de aspas do shell.
* 💡 Depois de publicar, confira o conteúdo da tag: git show v1.2.3:VERSION mostra o erro na hora.
* 💡 Corrigir tag publicada exige push --force, e essa decisão ficou com o responsável pelo repositório. Apagar e recriar teria o mesmo efeito, então também não é atalho.

---

### 🛠️ Especificação Técnica & Código-Chave
```bash
git commit -q -F $arquivoDaMensagem
if ($LASTEXITCODE -ne 0) { "commit falhou"; exit 1 }
git tag -a v1.2.3 -m "v1.2.3"
if ($LASTEXITCODE -ne 0) { "tag falhou"; exit 1 }
git show v1.2.3:VERSION
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A tag só é criada depois de um commit confirmado, e a conferência do conteúdo virou parte da publicação.

* **Projetos Relacionados**: `monitor-laravel`
* **Registro de Origem**: `_data/daily.dev-20.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
