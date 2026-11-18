---
layout: post
title: "Merge na pasta que o servidor lê derruba a tela com marcadores de conflito"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-119"
description: "Durante um merge, quem usava o sistema recebeu ParseError com unexpected token '<<'. O servidor de desenvolvimento lia os arquivos com os marcadores de conflito no disco."
date: 2026-11-04 00:00:00-03:00
categories: devlog
category: devops
tags: [git, merge, php, desenvolvimento]
---

# Merge na pasta que o servidor lê derruba a tela com marcadores de conflito

> [!NOTE]
> **Resumo Executivo (DEV-2026-119)**: Durante um merge, quem usava o sistema recebeu ParseError com unexpected token '<<'. O servidor de desenvolvimento lia os arquivos com os marcadores de conflito no disco.

---

### 🚨 O Desafio Técnico / Contexto
O merge parou com conflito em um serviço PHP, e o php artisan serve lia essa mesma pasta. Enquanto os testes rodavam, com o conflito já resolvido mas o merge ainda aberto, a pessoa já tinha visto o erro numa tela que não tinha relação com o assunto.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 PHP não tem etapa de build: o que está no disco é o que roda. Merge com conflito em pasta servida quebra o sistema na hora.
* 💡 Faça merge com conflito esperado em uma worktree separada, e traga o resultado pronto.
* 💡 git merge-tree --write-tree simula o merge sem tocar nos arquivos e lista os conflitos.
* 💡 O merge limpo também merece leitura: o automático juntou duas regras para a mesma chave em um array PHP. Funcionou, porque a última vence, mas uma das linhas virou código morto.
* 💡 Depois de um merge, confira marcadores, sintaxe, a suíte e as telas, nessa ordem.

---

### 🛠️ Especificação Técnica & Código-Chave
```bash
# Simula, sem mexer na pasta de trabalho
git merge-tree --write-tree --name-only meu-branch main
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Merge com conflito esperado passou a ser feito fora da pasta que o servidor usa.

* **Projetos Relacionados**: `sistema-de-atendimento`
* **Registro de Origem**: `_data/daily.dev-19.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
