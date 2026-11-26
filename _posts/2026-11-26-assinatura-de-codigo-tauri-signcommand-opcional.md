---
layout: post
title: "Assinatura de código no Tauri com chave em nuvem e signCommand opcional por variável de ambiente"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-168"
description: "Desde 2023 a chave de assinatura de código precisa ficar em hardware, então não existe mais o caminho de um .pfx num secret do CI. O Labmini passou a assinar pelo bundle.windows.signCommand do Tauri com um script que só assina quando há um thumbprint configurado, e o fluxo foi validado com um certificado descartável."
date: 2026-11-26 00:00:00-03:00
categories: devlog
category: seguranca
tags: [code-signing, tauri, signtool, smartscreen, powershell]
---

# Assinatura de código no Tauri com chave em nuvem e signCommand opcional por variável de ambiente

> [!NOTE]
> **Resumo Executivo (DEV-2026-168)**: Desde 2023 a chave de assinatura de código precisa ficar em hardware, então não existe mais o caminho de um .pfx num secret do CI. O Labmini passou a assinar pelo bundle.windows.signCommand do Tauri com um script que só assina quando há um thumbprint configurado, e o fluxo foi validado com um certificado descartável.

---

### 🚨 O Desafio Técnico / Contexto
Os instaladores da 0.1.1 saíam sem assinatura e o SmartScreen alertava. A escolha foi o Certum Open Source Code Signing com a chave no cofre SimplySign. O Azure Artifact Signing tem restrições para pessoa física, OV e EV de outras autoridades custam mais (EV não dá mais reputação imediata) e um certificado autoassinado não remove o alerta. O build precisava continuar funcionando no CI e em máquinas sem certificado.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 bundle.windows.signCommand em tauri.conf.json chama 'powershell -File ../scripts/sign.ps1 %1'. O caminho é relativo a src-tauri/, que é onde o Tauri executa o comando.
* 💡 Sem LABMINI_SIGN_THUMBPRINT o script sai com 0 e não assina. Com ela, confere o certificado em Cert:\CurrentUser\My, acha o signtool e assina em SHA-256 com carimbo RFC 3161. O thumbprint nunca entra no repositório.
* 💡 O Tauri chama o signCommand para o labmini.exe, para as DLLs de plugin do NSIS e para os dois instaladores. Com SimplySign, a sessão precisa ficar ativa durante todo o build.
* 💡 O labmini.exe solto em target/release fica sem assinatura, provavelmente porque o Tauri grava o tipo de pacote no executável depois de assinar. Confira pela cópia dentro do instalador, por exemplo com msiexec /a numa pasta temporária.
* 💡 PowerShell 5.1 lê .ps1 sem BOM como ANSI. Script com acentos precisa ser gravado em UTF-8 com BOM.
* 💡 Teste o fluxo inteiro com um certificado autoassinado de 1 dia. Get-AuthenticodeSignature mostra UnknownError, que é o esperado sem raiz confiável. Depois apague o certificado e refaça o build sem assinatura.

---

### 🛠️ Especificação Técnica & Código-Chave
```bash
"bundle": { "windows": { "signCommand": "powershell -File ../scripts/sign.ps1 %1" } }
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O mesmo repositório gera instaladores assinados na máquina com certificado e sem assinatura no CI, sem nenhum segredo versionado.

* **Projetos Relacionados**: `labmini`
* **Registro de Origem**: `_data/daily.dev-30.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
