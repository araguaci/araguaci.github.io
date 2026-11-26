---
layout: post
title: "Subir a versão nos três manifestos antes do build, senão o MSI não atualiza a instalação existente"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-167"
description: "O Labmini 0.1.0 foi distribuído sem tag, e gerar um instalador novo com a mesma versão faz o MSI não ser tratado como atualização. A 0.1.1 saiu com versão atualizada em Cargo.toml, package.json e tauri.conf.json, tag anotada e release no GitHub com os dois instaladores."
date: 2026-11-26 00:00:00-03:00
categories: devlog
category: devops
tags: [tauri, release, msi, versionamento, github-releases]
---

# Subir a versão nos três manifestos antes do build, senão o MSI não atualiza a instalação existente

> [!NOTE]
> **Resumo Executivo (DEV-2026-167)**: O Labmini 0.1.0 foi distribuído sem tag, e gerar um instalador novo com a mesma versão faz o MSI não ser tratado como atualização. A 0.1.1 saiu com versão atualizada em Cargo.toml, package.json e tauri.conf.json, tag anotada e release no GitHub com os dois instaladores.

---

### 🚨 O Desafio Técnico / Contexto
Um app Tauri carrega a versão em três lugares: [workspace.package] do Cargo.toml, package.json e src-tauri/tauri.conf.json. O build gera Labmini_<versão>_x64-setup.exe (NSIS) e Labmini_<versão>_x64_en-US.msi (WiX). A 0.1.0 nunca foi marcada com tag, e um MSI reconstruído com a mesma versão não substitui a instalação de quem já tem o app.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Atualize a versão nos três manifestos antes do build de distribuição. O MSI decide se é atualização pela versão do produto.
* 💡 cargo update -w atualiza o Cargo.lock só para os crates do workspace, sem puxar versões novas das dependências. npm install --package-lock-only --ignore-scripts faz o mesmo no package-lock.json.
* 💡 Toda versão publicada ganha uma tag anotada vX.Y.Z (git tag -a) e um gh release create com o .exe e o .msi anexados.
* 💡 Instaladores sem assinatura fazem o SmartScreen alertar no download e na instalação. Isso ficou como pendência registrada já no release.

---

### 🛠️ Especificação Técnica & Código-Chave
```bash
cargo update -w
npm install --package-lock-only --ignore-scripts
npm run tauri build
git tag -a v0.1.1 -m "Labmini 0.1.1"
git push origin main v0.1.1
gh release create v0.1.1 target/release/bundle/nsis/*.exe target/release/bundle/msi/*.msi
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A 0.1.1 é o primeiro release público e com tag, e quem instala o MSI novo recebe uma atualização em vez de uma instalação paralela.

* **Projetos Relacionados**: `labmini`
* **Registro de Origem**: `_data/daily.dev-30.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
