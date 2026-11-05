---
layout: post
title: "A importação do legado era lenta porque o id vinha vazio, e todas as linhas atualizavam o mesmo registro"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-127"
description: "A migração de um sistema VB6 com Access parecia presa, e a primeira suspeita foram as chaves estrangeiras. A causa era a coluna de id vazia na origem, e a identidade passou a ser um hash do conteúdo com o número da ocorrência."
date: 2026-11-04 00:00:00-03:00
categories: devlog
category: backend
tags: [laravel, migracao, access, legado, importacao, mysql]
---

# A importação do legado era lenta porque o id vinha vazio, e todas as linhas atualizavam o mesmo registro

> [!NOTE]
> **Resumo Executivo (DEV-2026-127)**: A migração de um sistema VB6 com Access parecia presa, e a primeira suspeita foram as chaves estrangeiras. A causa era a coluna de id vazia na origem, e a identidade passou a ser um hash do conteúdo com o número da ocorrência.

---

### 🚨 O Desafio Técnico / Contexto
O upsert por id de origem tratava todas as linhas como o mesmo pagamento, porque a coluna existia e estava vazia. O processo ficava lento e o total não fechava. Desligar as chaves estrangeiras não era a solução, e elas continuaram ligadas.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Coluna com nome de chave não é chave. Antes de usar um id de origem, conte quantos valores distintos ele tem.
* 💡 Sem chave confiável, use um hash do conteúdo somado ao número da ocorrência. Duas linhas iguais continuam sendo dois pagamentos, e reimportar não duplica nada.
* 💡 Compare os totais com a origem no final da importação. Foram 12 conferências contra o Access, e divergência desfaz a transação inteira.
* 💡 A importação correta levou 39 segundos para 147 mil pagamentos, com as chaves estrangeiras ligadas. Desligá-las teria escondido o erro sem resolver a causa.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
// A segunda linha idêntica recebe outra identidade e fica marcada para conferência.
$ocorrencia = $vistos[$conteudo] ?? 0;
$vistos[$conteudo] = $ocorrencia + 1;
$id = hexdec(substr(sha1($conteudo."|{$ocorrencia}"), 0, 15)) + (1 << 60);
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A migração passou a poder ser ensaiada quantas vezes for preciso, com o resultado conferido contra a origem.

* **Projetos Relacionados**: `monitor-laravel`
* **Registro de Origem**: `_data/daily.dev-20.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
