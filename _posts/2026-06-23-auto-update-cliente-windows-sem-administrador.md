---
layout: post
title: "Atualizar o cliente Windows sem pedir administrador"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-047"
description: "O instalador gravava em Arquivos de Programas e o atualizador falhava para o operador sem elevação. A pasta do aplicativo passou a permitir modificação pelos usuários, e o INI da empresa saiu do Git."
date: 2026-06-23 00:00:00+00:00
categories: devlog
category: windows
tags: [inno-setup, dotnet, atualizacao, seguranca]
---

# Atualizar o cliente Windows sem pedir administrador

> [!NOTE]
> **Resumo Executivo (DEV-2026-047)**: O instalador gravava em Arquivos de Programas e o atualizador falhava para o operador sem elevação. A pasta do aplicativo passou a permitir modificação pelos usuários, e o INI da empresa saiu do Git.

---

### 🚨 O Desafio Técnico / Contexto
Cada build novo pedia UAC porque o updater não conseguia trocar o exe em Program Files. O script de publicação ainda esbarrava no lock do compartilhamento de rede, e um INI com dados da empresa tinha caído na árvore versionada.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Permissão Modify para Users na pasta {app} deixa o updater trocar exe e dll sem elevação.
* 💡 O publish recusa gravar de novo a mesma versão. Isso evita manifesto apontando para binário trocado em silêncio.
* 💡 A pasta deploy, com o INI da empresa, fica no gitignore.
* 💡 Lock no share de rede pede nova tentativa no script, não um segundo clique manual.

---

### 🛠️ Especificação Técnica & Código-Chave
```ini
; Inno Setup: a pasta do app pode ser atualizada pelo operador
[Dirs]
Name: "{app}"; Permissions: users-modify

; Não versionar
; deploy/
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A estação recebe a build nova sem UAC e a configuração da empresa deixa o repositório.

* **Projetos Relacionados**: `omnichannel`, `LorentzCliente`
* **Registro de Origem**: `_data/daily.dev-03.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
