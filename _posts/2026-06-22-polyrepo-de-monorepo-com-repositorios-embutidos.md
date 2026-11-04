---
layout: post
title: "Polyrepo a partir de um monorepo com 25 repositórios embutidos pede dois caminhos"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-089"
description: "O monorepo local não tinha remoto próprio e guardava cerca de 25 repositórios embutidos sem .gitmodules. A migração usou subtree split para o que estava rastreado direto e renomeação para o que já tinha repositório."
date: 2026-06-22 00:00:00-03:00
categories: devlog
category: devops
tags: [git, subtree, filter-repo, polyrepo, github]
---

# Polyrepo a partir de um monorepo com 25 repositórios embutidos pede dois caminhos

> [!NOTE]
> **Resumo Executivo (DEV-2026-089)**: O monorepo local não tinha remoto próprio e guardava cerca de 25 repositórios embutidos sem .gitmodules. A migração usou subtree split para o que estava rastreado direto e renomeação para o que já tinha repositório.

---

### 🚨 O Desafio Técnico / Contexto
Desktop VB.NET e C++, web PHP e Laravel e infraestrutura conviviam na mesma pasta, com necessidades de acesso diferentes. Faltava repartir por domínio sem perder histórico e sem misturar projetos de terceiros.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Pasta rastreada direto sai com git subtree split e push para o repositório novo. Repositório embutido só precisa ser renomeado no GitHub, o que preserva histórico e cria redirecionamento.
* 💡 git filter-repo limpou o histórico do cliente desktop antes da publicação, removendo uma biblioteca de 77 MB.
* 💡 O nome desejado pode estar ocupado por um fork antigo na própria conta. Renomeie o fork antes, para liberar o nome ao servidor real.
* 💡 Projetos de terceiros não entram nos repositórios próprios nem são renomeados.
* 💡 Repositórios antigos sobrepostos ficam para decisão humana. Definir qual é o canônico não é tarefa de automação.

---

### 🛠️ Especificação Técnica & Código-Chave
```bash
git subtree split --prefix=<pasta> -b export/<repo>
git push https://github.com/<conta>/<repo>.git export/<repo>:main
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Cada componente passou a ter repositório privado próprio, com acesso controlado por domínio.

* **Projetos Relacionados**: `lorentz-client`, `lorentz-omnichannel`, `lorentz-docs`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
