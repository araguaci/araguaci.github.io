---
layout: post
title: "O motor de alertas já estava no banco, e faltava só agendar e notificar"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-082"
description: "A primeira tentativa de automatizar alertas de consumo reimplementou em PHP o que uma migration já tinha criado. Ao reaproveitar o que existia, a entrega ficou reduzida a um script de agendamento e notificação."
date: 2026-06-15 00:00:00-03:00
categories: devlog
category: backend
tags: [mysql, php, stored-procedure, alertas, phpmaker]
---

# O motor de alertas já estava no banco, e faltava só agendar e notificar

> [!NOTE]
> **Resumo Executivo (DEV-2026-082)**: A primeira tentativa de automatizar alertas de consumo reimplementou em PHP o que uma migration já tinha criado. Ao reaproveitar o que existia, a entrega ficou reduzida a um script de agendamento e notificação.

---

### 🚨 O Desafio Técnico / Contexto
O pedido era a fase A da automação: alertas e relatórios sobre as faturas já importadas. A tabela e as regras novas ficaram redundantes e em conflito com scripts/migration_relatorios_executivos.sql, já aplicada no banco local.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Antes de escrever regra de negócio, procure também em migrations, procedures e views. O motor estava em sp_gera_alertas() e sp_processa_executivo(), fora do PHP.
* 💡 A tabela alerta já evitava duplicidade com UNIQUE(idfilial, tipo, competencia) e tinha o ciclo ABERTO, NOTIFICADO, RESOLVIDO e IGNORADO.
* 💡 O que faltava coube no monitor.php: chamar o orquestrador, enviar o resumo por e-mail e marcar NOTIFICADO, com --dry-run e --notify.
* 💡 Para o setup Docker funcionar, o ewcfg.php passou a ler as credenciais por getenv(), com o .env fora do Git.

---

### 🛠️ Especificação Técnica & Código-Chave


---

### 📈 Impacto no Ecossistema & Valor Prático
As regras de alerta continuam em um lugar só, e o dashboard executivo segue lendo a mesma tabela.

* **Projetos Relacionados**: `lorentz-energy`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
