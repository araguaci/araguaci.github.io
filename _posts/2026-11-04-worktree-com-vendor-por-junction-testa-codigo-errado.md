---
layout: post
title: "Worktree com vendor por junction testa o código da pasta original, e a comparação sai falsa"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-118"
description: "Para comparar testes antes e depois de uma correção, usei uma worktree com o vendor ligado por junction. Os testes da falha passaram mesmo com a correção removida, o que revelou que a cópia rodava o código de outra pasta."
date: 2026-11-04 00:00:00-03:00
categories: devlog
category: devops
tags: [git, worktree, composer, php, windows, testes]
---

# Worktree com vendor por junction testa o código da pasta original, e a comparação sai falsa

> [!NOTE]
> **Resumo Executivo (DEV-2026-118)**: Para comparar testes antes e depois de uma correção, usei uma worktree com o vendor ligado por junction. Os testes da falha passaram mesmo com a correção removida, o que revelou que a cópia rodava o código de outra pasta.

---

### 🚨 O Desafio Técnico / Contexto
A comparação mostrou 60 falhas antes e depois, e eu a chamei de válida. O autoload do Composer resolve o caminho real do vendor, então as classes vinham da pasta original, com as correções, e só os testes vinham da worktree. O número real era 64.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Copie o vendor de verdade ao criar a worktree. No Windows, robocopy com /MT é rápido.
* 💡 Confira de onde a classe é carregada antes de confiar no resultado, com ReflectionClass e getFileName.
* 💡 Um teste de controle tem que falhar: rode o teste novo sem a correção. Se ele passar, o método está errado, e não o código.
* 💡 Duas coisas que eu não sabia explicar eram sintomas do mesmo erro. Quando um número não fecha, vale investigar antes de seguir.
* 💡 O projeto antigo usava MyISAM nesta máquina. Ajustes só para o teste rodar devem ser revertidos antes do commit, e uma trava no script evita o descuido.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
New-Item -ItemType Junction ...  # autoload aponta para a pasta original
robocopy .\vendor $wt\vendor /E /MT:16  # autoload aponta para a worktree

php -r "require 'vendor/autoload.php'; echo (new ReflectionClass('App\Models\X'))->getFileName();"
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A comparação com a base passou a provar o que diz, e a medição anterior foi refeita e corrigida.

* **Projetos Relacionados**: `sistema-de-atendimento`
* **Registro de Origem**: `_data/daily.dev-19.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
