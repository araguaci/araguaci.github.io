---
layout: post
title: "Resolução de Conflitos no GitHub Actions: Modernização de Ruby 2.6 para 3.3 e a Falha da Gem FFI"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-001"
description: "Diagnóstico profundo e correção definitiva de falha em pipeline de CI no GitHub Actions decorrente do uso de containers legados com Ruby 2.6 incompatíveis com gems modernas."
date: 2026-10-01 00:00:00+00:00
categories: devlog
category: devops
tags: [github-actions, ruby, jekyll, ffi, ci-cd, bundler]
---

# Resolução de Conflitos no GitHub Actions: Modernização de Ruby 2.6 para 3.3 e a Falha da Gem FFI

> [!NOTE]
> **Resumo Executivo (DEV-2026-001)**: Diagnóstico profundo e correção definitiva de falha em pipeline de CI no GitHub Actions decorrente do uso de containers legados com Ruby 2.6 incompatíveis com gems modernas.

---

### 🚨 O Desafio Técnico / Contexto
O workflow de CI rodava o container 'jekyll/builder:3.8' (com Ruby 2.6.3p62). O Bundler falhou ao instalar a gem 'ffi-1.17.4', que exige estritamente Ruby >= 3.0, quebrando o pull request com Exit Code 5.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Imagens Docker antigas de construtores de Jekyll congelam versões descontinuadas do Ruby e quebram quando o Rubygems resolve dependências transitivas contemporâneas.
* 💡 O padrão moderno oficial para Jekyll no GitHub Actions dispensa Docker e usa a action nativa 'ruby/setup-ruby@v1' com 'bundler-cache: true'.
* 💡 A migração para 'actions/checkout@v4' e Ruby 3.3 reduziu o tempo médio de compilação da pipeline de 3 minutos para apenas 17 segundos.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
# .github/workflows/ci.yml moderno
name: Beautiful Jekyll CI
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.3'
          bundler-cache: true
      - run: bundle exec jekyll build --future
        env:
          JEKYLL_ENV: production

```

---

### 📈 Impacto no Ecossistema & Valor Prático
Pipeline de CI 100% verde, eliminando alertas de depreciação do Node e blindando o repositório contra dependências que exigem Ruby 3+.

* **Projetos Relacionados**: `artesdosul.github.io`, `araguaci.github.io`
* **Registro de Origem**: `_data/daily.dev-01.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
