---
layout: post
title: "Compilar Zig em /mnt (9p) falha no .zig-cache e GtkGLArea sem GPU exige NANOUI_RENDERER=cpu"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-164"
description: "Compilar projetos Zig sob /mnt no WSL2 falhava com AccessDenied ao renomear .zig-cache, e abrir o wslpanel em máquina sem GPU fechava a janela no GtkGLArea. Mover ZIG_LOCAL_CACHE_DIR para o filesystem Linux e usar NANOUI_RENDERER=cpu resolveu compilação e execução em ambientes headless ou sem EGL."
date: 2026-11-18 00:00:00-03:00
categories: devlog
category: devops
tags: [zig, wsl, 9p, gtk3, opengl, build]
---

# Compilar Zig em /mnt (9p) falha no .zig-cache e GtkGLArea sem GPU exige NANOUI_RENDERER=cpu

> [!NOTE]
> **Resumo Executivo (DEV-2026-164)**: Compilar projetos Zig sob /mnt no WSL2 falhava com AccessDenied ao renomear .zig-cache, e abrir o wslpanel em máquina sem GPU fechava a janela no GtkGLArea. Mover ZIG_LOCAL_CACHE_DIR para o filesystem Linux e usar NANOUI_RENDERER=cpu resolveu compilação e execução em ambientes headless ou sem EGL.

---

### 🚨 O Desafio Técnico / Contexto
Durante os testes de compilação e instalação do wslpanel no WSL2 e no servidor labmini (2026-11-18), o sistema de arquivos 9p montado em /mnt recusava a operação de rename dentro de .zig-cache com AccessDenied. Na instalação manual do Zig 0.17.0 como root, tar -C "$HOME/.local" falhava quando /root/.local ainda não existia. Ao executar o binário em máquina sem GPU, GtkGLArea exigia OpenGL 3.0+, emitia libEGL com fd -1 e ZINK: failed to choose pdev e fechava sem fallback automático. Além disso, zig fetch --save gravava .path em vez de .url + hash no build.zig.zon.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Em diretórios montados sob /mnt (9p do Windows), exportar ZIG_LOCAL_CACHE_DIR="$HOME/.cache/wslpanel-zig" evita erro AccessDenied no rename do cache enquanto o binário em zig-out grava normalmente.
* 💡 Executar mkdir -p "$HOME/.local" antes de tar -C garante a extração do Zig mesmo sob conta root onde /root/.local não existe.
* 💡 Quando não há GPU/EGL disponível (erros libEGL fd -1 e ZINK: failed to choose pdev), GtkGLArea não faz fallback silencioso: é necessário executar com NANOUI_RENDERER=cpu e DISPLAY definido.
* 💡 No Zig 0.17, zig fetch --save pode registrar .path no build.zig.zon em vez de .url + hash; além disso, c.print exige formato conhecido em comptime (frases traduzidas saem de std.fmt.allocPrint) e _ = param gera erro se o parâmetro também for usado.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
export ZIG_LOCAL_CACHE_DIR="$HOME/.cache/wslpanel-zig"
mkdir -p "$HOME/.local"
zig build -Doptimize=ReleaseSafe
NANOUI_RENDERER=cpu ./zig-out/bin/wslpanel
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Compilação e execução do wslpanel passaram a funcionar de forma reproduzível tanto em WSL2 sob /mnt quanto em máquinas Linux sem aceleração GPU.

* **Projetos Relacionados**: `wslpanel`
* **Registro de Origem**: `_data/daily.dev-30.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
