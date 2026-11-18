---
layout: post
title: "O git no servidor não representa o que está rodando"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-150"
description: "A árvore no servidor estava em main com dezenas de arquivos alterados sem commit, inclusive o que atende. Sincronizar a pasta inteira apagaria ajuste que só existe lá."
date: 2026-11-05 00:00:00-03:00
categories: devlog
category: devops
tags: [git, deploy, drift, backup]
---

# O git no servidor não representa o que está rodando

> [!NOTE]
> **Resumo Executivo (DEV-2026-150)**: A árvore no servidor estava em main com dezenas de arquivos alterados sem commit, inclusive o que atende. Sincronizar a pasta inteira apagaria ajuste que só existe lá.

---

### 🚨 O Desafio Técnico / Contexto
Em 2026-11-05, lorentz-vps-stack no servidor apontava o HEAD para 33572d8 e o disco divergia desse commit. O git status de lá não era o inventário do que estava no ar.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 HEAD em main não significa árvore limpa. Havia dezenas de arquivos modificados sem commit, e parte deles era o que estava em uso.
* 💡 Antes de enviar, compare cada arquivo com a versão do lab e mande só o que precisa mudar.
* 💡 O backup vem antes da sobrescrita, e só segue quem confirma que o backup existe.
* 💡 A documentação entra na mesma comparação. Ajuste que está só no servidor se perde num envio completo.

---

### 🛠️ Especificação Técnica & Código-Chave
```bash
git -C ~/omnichannel/lorentz-vps-stack status --short
git -C ~/omnichannel/lorentz-vps-stack rev-parse --short HEAD
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O deploy deixou de tratar o git do servidor como cópia fiel e passou a comparar arquivo por arquivo.

* **Projetos Relacionados**: `lorentz-vps-stack`
* **Registro de Origem**: `_data/daily.dev-26.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
