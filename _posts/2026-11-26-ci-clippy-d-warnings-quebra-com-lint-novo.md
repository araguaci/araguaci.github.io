---
layout: post
title: "CI com clippy -D warnings e toolchain stable quebra quando o Rust ganha lint novo"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-190"
description: "O primeiro push do Labmini falhou no CI porque o Rust 1.100 trouxe o lint chunks_exact_to_as_chunks e o runner usava stable mais recente que o ambiente local. Corrigir o código, atualizar a toolchain local e fixar as dependências de teste deixou Linux e Windows verdes."
date: 2026-11-26 00:00:00-03:00
categories: devlog
category: devops
tags: [rust, clippy, github-actions, vitest, playwright]
---

# CI com clippy -D warnings e toolchain stable quebra quando o Rust ganha lint novo

> [!NOTE]
> **Resumo Executivo (DEV-2026-190)**: O primeiro push do Labmini falhou no CI porque o Rust 1.100 trouxe o lint chunks_exact_to_as_chunks e o runner usava stable mais recente que o ambiente local. Corrigir o código, atualizar a toolchain local e fixar as dependências de teste deixou Linux e Windows verdes.

---

### 🚨 O Desafio Técnico / Contexto
Localmente o clippy passava limpo. No GitHub Actions, dtolnay/rust-toolchain@stable instalou a versão do dia, e -D warnings transformou o lint novo em erro nos dois jobs. Na mesma rodada, o e2e falhou com MODULE_NOT_FOUND porque o script fazia require('playwright') de uma instalação global que só existia no container de desenvolvimento. Atualizar o vitest para 5.x, para zerar o npm audit, removeu a chave test do defineConfig do Vite.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Rode rustup update stable antes de confiar num clippy local quando o CI usa @stable. Para .chunks_exact(2) com tamanho constante, o lint pede .as_chunks::<2>().0.iter().
* 💡 Campo em [workspace.package] que nenhum crate herda gera o aviso unused_workspace_package_fields. Herde com repository.workspace = true.
* 💡 Dependência usada pelo script de teste vai no devDependencies com versão exata. Aqui foi playwright 1.63.0, igual à versão do navegador já instalado, para não quebrar o ambiente local.
* 💡 Com vitest 5, a configuração test: {...} saiu do tipo do defineConfig do Vite. Remova a chave ou use vitest.config.ts.

---

### 🛠️ Especificação Técnica & Código-Chave


---

### 📈 Impacto no Ecossistema & Valor Prático
O CI roda no Windows real o teste de ida e volta e gera o instalador como artefato a cada push, verde nos dois sistemas.

* **Projetos Relacionados**: `labmini`
* **Registro de Origem**: `_data/daily.dev-30.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
