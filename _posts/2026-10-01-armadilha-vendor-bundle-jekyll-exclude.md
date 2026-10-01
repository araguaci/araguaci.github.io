---
layout: post
title: "A Armadilha do 'vendor/bundle' no Jekyll: Exclusão Obrigatória no _config.yml"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-002"
description: "Como evitar que o Jekyll tente processar arquivos de template internos das gems instaladas como se fossem posts do próprio blog."
date: 2026-10-01 00:00:00+00:00
categories: devlog
category: devops
tags: [jekyll, bundler, config-yml, debugging, ruby]
---

# A Armadilha do 'vendor/bundle' no Jekyll: Exclusão Obrigatória no _config.yml

> [!NOTE]
> **Resumo Executivo (DEV-2026-002)**: Como evitar que o Jekyll tente processar arquivos de template internos das gems instaladas como se fossem posts do próprio blog.

---

### 🚨 O Desafio Técnico / Contexto
Ao ativar 'bundler-cache: true', as gems são instaladas no caminho local 'vendor/bundle'. O Jekyll tentou processar 'vendor/bundle/.../jekyll-3.10.0/.../_posts/0000-00-00-welcome-to-jekyll.markdown.erb' como post, falhando com erro fatal de data inválida em tag ERB.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Quando a diretiva 'exclude:' é declarada no '_config.yml', o Jekyll substitui totalmente sua lista padrão de exclusões.
* 💡 Se 'vendor/' não for recolocado explicitamente em 'exclude:', o Jekyll fará varredura recursiva em todo o código-fonte das gems instaladas.
* 💡 Arquivos de exemplo e geradores internos de gems com extensão '.markdown.erb' quebram o parser de frontmatter do Jekyll.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
# _config.yml - Exclusão obrigatória de artefatos de build
exclude:
  - vendor/
  - .bundle/
  - .sass-cache/
  - .jekyll-cache/
  - Gemfile
  - Gemfile.lock

```

---

### 📈 Impacto no Ecossistema & Valor Prático
Zero falsos positivos de compilação em ambientes de integração contínua (GitHub Actions e Vercel).

* **Projetos Relacionados**: `artesdosul.github.io`, `araguaci.github.io`
* **Registro de Origem**: `_data/daily.dev-01.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
