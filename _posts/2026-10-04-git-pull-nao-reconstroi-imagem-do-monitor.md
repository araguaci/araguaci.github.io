---
layout: post
title: "git pull na VPS não troca a imagem do monitor que já está no ar"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-067"
description: "O site mostrava a versão antiga do monitor com o Git já à frente. A imagem copia o código na build, e um pull com árvore suja nem chega a atualizar os arquivos."
date: 2026-10-04 00:00:00+00:00
categories: devlog
category: devops
tags: [docker, git, monitor, vps]
---

# git pull na VPS não troca a imagem do monitor que já está no ar

> [!NOTE]
> **Resumo Executivo (DEV-2026-067)**: O site mostrava a versão antiga do monitor com o Git já à frente. A imagem copia o código na build, e um pull com árvore suja nem chega a atualizar os arquivos.

---

### 🚨 O Desafio Técnico / Contexto
O painel em produção continuava na versão anterior depois que o repositório remoto já tinha os commits novos. git pull abortou porque arquivos rastreados estavam modificados e arquivos não rastreados seriam sobrescritos. O rodapé exibia a data do arquivo VERSION da stack, não a versão do monitor.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O Dockerfile do monitor copia Python, templates, estáticos e o arquivo VERSION na build. git pull no host não entra no container que já está rodando.
* 💡 A atualização do painel é docker compose up -d --build monitor, depois do pull ter concluído.
* 💡 A data do rodapé é o mtime do VERSION da stack. A versão do monitor é outro arquivo, copiado para a imagem.
* 💡 Pull com modificação local e untracked no mesmo caminho aborta. Dá para descartar o que é só cópia antiga do Git. .env, token e config do portal ficam de fora do reset.

---

### 🛠️ Especificação Técnica & Código-Chave
```bash
git pull --ff-only
docker compose up -d --build monitor
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O monitor em produção só muda de versão quando a imagem é reconstruída, e o pull deixa de ser bloqueado pelos arquivos que a VPS precisa manter.

* **Projetos Relacionados**: `lorentz-vps-stack`
* **Registro de Origem**: `_data/daily.dev-08.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
