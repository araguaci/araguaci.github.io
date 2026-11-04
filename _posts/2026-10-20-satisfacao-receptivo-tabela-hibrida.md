---
layout: post
title: "A satisfação do receptivo é o código IdSatisfacao na tabela híbrida de status"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-079"
description: "As procedures do painel receptivo calculavam a média em SAC_SATISFACAO.Nota, tabela que este banco não tem. A nota é SAC_ATENDIMENTO.IdSatisfacao e o rótulo está em SAC_ATENDIMENTO_STATUS, na linha em que Tabela vale IdSatisfacao."
date: 2026-10-20 00:00:00-03:00
categories: devlog
category: backend
tags: [sqlserver, php, supervisor, crm]
---

# A satisfação do receptivo é o código IdSatisfacao na tabela híbrida de status

> [!NOTE]
> **Resumo Executivo (DEV-2026-079)**: As procedures do painel receptivo calculavam a média em SAC_SATISFACAO.Nota, tabela que este banco não tem. A nota é SAC_ATENDIMENTO.IdSatisfacao e o rótulo está em SAC_ATENDIMENTO_STATUS, na linha em que Tabela vale IdSatisfacao.

---

### 🚨 O Desafio Técnico / Contexto
O painel crm.html chama crm_data.php, que executa sp_Receptivo_Dashboard_KPIs e sp_Receptivo_PerformanceAgentes. O SQL original fazia LEFT JOIN em SAC_SATISFACAO e a média de s.Nota. Essa tabela não está no catálogo PHPMaker. O cadastro resolve IdSatisfacao com o filtro Tabela = 'IdSatisfacao' em SAC_ATENDIMENTO_STATUS. No script CREATE_MISSING_OBJECTS.sql, a view vw_atendimentos ligava o alias SATISFACAO por A.IdStatus, que é a situação do atendimento, não o código de satisfação.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Não há SAC_SATISFACAO. O rótulo é SAC_ATENDIMENTO_STATUS.Status, com Tabela = 'IdSatisfacao' e IdStatus igual a SAC_ATENDIMENTO.IdSatisfacao. A mesma tabela guarda IdStatus, IdSuporte e IdCobrar, separados pela coluna Tabela.
* 💡 MediaSatisfacao é a média do inteiro IdSatisfacao. A coluna Status é texto e não entra na média. crm_data.php lê o campo; crm.html não desenha o número.
* 💡 home_api.php só cria a procedure se sysobjects ainda não tem o nome. Mudar o texto no PHP não altera a cópia já instalada. É preciso DROP, ou o script api/scripts/sp_Receptivo_Dashboard_Procedures.sql, que apaga e recria.
* 💡 O lookup em sac_atendimentoview.php filtra [Tabela] = 'IdSatisfacao' e compara IdStatus com o valor de IdSatisfacao. Esse filtro é o vínculo, não um nome de tabela inventado.

---

### 🛠️ Especificação Técnica & Código-Chave
```sql
-- rótulo em SAC_ATENDIMENTO_STATUS, código em SAC_ATENDIMENTO
LEFT JOIN SAC_ATENDIMENTO_STATUS s
  ON s.IdStatus = a.IdSatisfacao
 AND s.Tabela = 'IdSatisfacao'
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A média do painel passa a usar o código que o cadastro grava, e a view de atendimentos deixa de buscar o rótulo na situação.

* **Projetos Relacionados**: `supervisor-php564`
* **Registro de Origem**: `_data/daily.dev-16.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
