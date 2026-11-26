---
layout: post
title: "Compilar app Tauri para Windows a partir do Linux pede windres, gcc mingw e o WebView2Loader.dll ao lado do exe"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-189"
description: "O cargo check do app Tauri para x86_64-pc-windows-gnu falhava no build script com NotAttempted(x86_64-w64-mingw32-windres). Com binutils e gcc mingw instalados, o build cruzado gerou um exe funcional, mas que depende de WebView2Loader.dll na mesma pasta."
date: 2026-11-26 00:00:00-03:00
categories: devlog
category: devops
tags: [tauri, rust, cross-compile, mingw, webview2]
---

# Compilar app Tauri para Windows a partir do Linux pede windres, gcc mingw e o WebView2Loader.dll ao lado do exe

> [!NOTE]
> **Resumo Executivo (DEV-2026-189)**: O cargo check do app Tauri para x86_64-pc-windows-gnu falhava no build script com NotAttempted(x86_64-w64-mingw32-windres). Com binutils e gcc mingw instalados, o build cruzado gerou um exe funcional, mas que depende de WebView2Loader.dll na mesma pasta.

---

### 🚨 O Desafio Técnico / Contexto
O tauri-build embute ícone e manifesto com tauri-winres, que chama x86_64-w64-mingw32-windres. Sem o binário, o build script entra em pânico. Com só o binutils instalado, o windres falha com "preprocessing failed", porque usa o gcc do mingw como pré-processador. O exe gerado pelo alvo gnu importa WebView2Loader.dll dinamicamente, ao contrário do build MSVC, que o liga estaticamente.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Para o alvo windows-gnu no Ubuntu: rustup target add x86_64-pc-windows-gnu e apt install binutils-mingw-w64-x86-64 gcc-mingw-w64-x86-64. Os dois pacotes são necessários.
* 💡 x86_64-w64-mingw32-objdump -p labmini.exe | grep 'DLL Name' mostra a dependência de WebView2Loader.dll. A DLL fica em target/x86_64-pc-windows-gnu/release/ e tem que ir junto no zip.
* 💡 O build cruzado serve para validar compilação e entregar uma prévia rápida. O instalador definitivo (NSIS e MSI) sai de npm run tauri build com MSVC, no Windows ou no runner windows-latest do GitHub Actions.
* 💡 O núcleo em Rust separado do app Tauri, com um trait Runner único para executar comandos, permite rodar 58 testes no Linux com saídas reais gravadas como fixtures.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
rustup target add x86_64-pc-windows-gnu
apt-get install -y binutils-mingw-w64-x86-64 gcc-mingw-w64-x86-64
cargo build --release --target x86_64-pc-windows-gnu -p labmini
x86_64-w64-mingw32-objdump -p target/x86_64-pc-windows-gnu/release/labmini.exe | grep 'DLL Name'
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O app passou a compilar e ser verificado para Windows num container Linux, antes de existir qualquer toolchain na máquina de destino.

* **Projetos Relacionados**: `labmini`
* **Registro de Origem**: `_data/daily.dev-30.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
