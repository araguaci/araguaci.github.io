---
layout: post
title: "A chave SSH no agente do Windows não funciona pelo ssh do Git Bash"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-098"
description: "Na mesma máquina há três ambientes de shell, e cada um enxerga coisas diferentes. A conexão só funciona pelo OpenSSH do Windows, e o bash chamado do PowerShell não é o Git Bash."
date: 2026-10-30 00:00:00-03:00
categories: devlog
category: windows
tags: [ssh, windows, git-bash, wsl, crlf]
---

# A chave SSH no agente do Windows não funciona pelo ssh do Git Bash

> [!NOTE]
> **Resumo Executivo (DEV-2026-098)**: Na mesma máquina há três ambientes de shell, e cada um enxerga coisas diferentes. A conexão só funciona pelo OpenSSH do Windows, e o bash chamado do PowerShell não é o Git Bash.

---

### 🚨 O Desafio Técnico / Contexto
A chave com passphrase está carregada no ssh-agent do Windows, mas o ssh do Git Bash não consegue usá-la. No PowerShell, chamar bash abria o WSL, e o git de lá apontava alterações em arquivos que ninguém tinha mudado.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O ssh do MSYS não usa o agente do Windows. Dentro do Git Bash, chame /c/Windows/System32/OpenSSH/ssh.exe pelo caminho completo.
* 💡 No PowerShell, bash resolve para System32/bash.exe, ou seja, para o WSL. Confira qual executável está sendo chamado antes de culpar o script.
* 💡 O git do WSL vê o CRLF do checkout do Windows como alteração. Os arquivos estão iguais, e o que difere é a ferramenta.
* 💡 Um script de deploy em PowerShell fixa o caminho certo, e ninguém precisa lembrar disso a cada conexão.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
# Dentro do Git Bash, usando a chave do agente do Windows
/c/Windows/System32/OpenSSH/ssh.exe minha-vps
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A conexão e o deploy passaram a seguir um caminho conhecido, sem falso alarme de arquivo alterado.

* **Projetos Relacionados**: `iplive`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
