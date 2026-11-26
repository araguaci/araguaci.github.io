---
layout: post
title: "Sessão do AnyDesk caiu ao aplicar ajustes, e só o cruzamento de logs por horário mostrou o momento"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-191"
description: "Aplicar 41 ajustes recomendados do Labmini por AnyDesk derrubou a sessão remota por cerca de um minuto, sem que nenhum item do catálogo tocasse rede. O diário passou a gravar hora e duração de cada operação, e o plano passou a avisar que sessões remotas podem cair."
date: 2026-11-26 00:00:00-03:00
categories: devlog
category: windows
tags: [anydesk, acesso-remoto, diagnostico, logs, windows-11]
---

# Sessão do AnyDesk caiu ao aplicar ajustes, e só o cruzamento de logs por horário mostrou o momento

> [!NOTE]
> **Resumo Executivo (DEV-2026-191)**: Aplicar 41 ajustes recomendados do Labmini por AnyDesk derrubou a sessão remota por cerca de um minuto, sem que nenhum item do catálogo tocasse rede. O diário passou a gravar hora e duração de cada operação, e o plano passou a avisar que sessões remotas podem cair.

---

### 🚨 O Desafio Técnico / Contexto
Às 14:41:29 o Labmini 0.1.0 gravou o backup e começou o lote, com ponto de restauração. Às 14:41:33 o serviço do AnyDesk perdeu a conexão com o relay. O lote terminou às 14:41:57 com todos os itens ok, a sessão expirou às 14:42:15 e o acesso voltou sozinho às 14:42:34. O serviço do AnyDesk continuou rodando e com início automático. O diário do Labmini tinha uma linha por lote, então não dava para saber qual operação rodava na hora da queda. Os suspeitos são Checkpoint-Computer (VSS) e Remove-AppxPackage dos apps Xbox.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Os logs do AnyDesk ficam em UTC: ad_svc.trace em %ProgramData%\AnyDesk e ad.trace em %APPDATA%\AnyDesk. Converta o fuso antes de cruzar com logs em horário local.
* 💡 Uma linha por lote não serve para diagnóstico. exec.ps1 passou a devolver startedAt (ISO 8601 com fuso) e durationMs por operação, como campos opcionais para os backups antigos continuarem abrindo.
* 💡 Procurar um item culpado no catálogo não resolveu. O que mostrou o momento da queda foi cruzar, por horário, o diário do Labmini com o trace do AnyDesk.
* 💡 Ponto de restauração e remoção de pacotes Appx bastam para derrubar uma sessão remota por alguns segundos, mesmo sem nenhum ajuste de rede. O plano agora avisa isso antes de aplicar.
* 💡 Com o Git Credential Manager falhando no wincredman e o token do gh vencido, gh auth login seguido de gh auth setup-git fez o Git usar o gh como helper para o github.com.

---

### 🛠️ Especificação Técnica & Código-Chave
```bash
git -c credential.helper= -c 'credential.helper=!gh auth git-credential' push
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Na próxima queda, o Diário do Labmini mostra o passo que rodava naquele segundo, e quem aplica por acesso remoto é avisado antes.

* **Projetos Relacionados**: `labmini`
* **Registro de Origem**: `_data/daily.dev-30.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
