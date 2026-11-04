---
layout: post
title: "O comando ares que fala com a TV autentica só no terminal do usuário"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-096"
description: "O mesmo comando de instalação na TV falhava no shell do agente e funcionava na aba do usuário. A autenticação depende de uma passphrase que o shell isolado não enxerga, então o fluxo foi dividido em duas etapas."
date: 2026-10-23 00:00:00-03:00
categories: devlog
category: devops
tags: [webos, lg, ares, terminal, sandbox]
---

# O comando ares que fala com a TV autentica só no terminal do usuário

> [!NOTE]
> **Resumo Executivo (DEV-2026-096)**: O mesmo comando de instalação na TV falhava no shell do agente e funcionava na aba do usuário. A autenticação depende de uma passphrase que o shell isolado não enxerga, então o fluxo foi dividido em duas etapas.

---

### 🚨 O Desafio Técnico / Contexto
ares-install e ares-launch falhavam com 'All configured authentication methods failed' quando rodados pelo shell do agente. O dispositivo estava configurado, e o mesmo comando funcionava no terminal do usuário.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 A passphrase gravada com ares-setup-device --modify não fica visível para o PowerShell isolado do agente.
* 💡 O empacotamento não fala com a TV, então npm run build roda em qualquer um dos shells.
* 💡 Instalação e abertura ficam no terminal do usuário: node scripts/deploy.js ou npm run launch.
* 💡 A mensagem de falha fala em autenticação, mas chave e dispositivo estavam certos. A diferença estava em qual shell executava o comando.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
# Shell do agente: só empacota
npm run build
# Terminal do usuário: fala com a TV
node scripts/deploy.js
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O deploy na TV deixou de falhar por causa do shell, com cada etapa no lugar em que funciona.

* **Projetos Relacionados**: `querencia`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
