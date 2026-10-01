---
layout: post
title: "Arquivar o mês de chamadas com T-SQL, sem arquivo de backup"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-044"
description: "Montar Base Histórica deixou de ser BACKUP e RESTORE em arquivo. O worker copia tabela a tabela entre bases da mesma instância e grava o que fez."
date: 2026-07-11 00:00:00+00:00
categories: devlog
category: backend
tags: [sql-server, dotnet, cti, arquivamento]
---

# Arquivar o mês de chamadas com T-SQL, sem arquivo de backup

> [!NOTE]
> **Resumo Executivo (DEV-2026-044)**: Montar Base Histórica deixou de ser BACKUP e RESTORE em arquivo. O worker copia tabela a tabela entre bases da mesma instância e grava o que fez.

---

### 🚨 O Desafio Técnico / Contexto
O utilitário antigo gerava arquivo de backup e restaurava em outra base. No Docker isso exige volume, permissão de arquivo e um passo manual. Uma falha no meio do mês não dizia qual tabela já tinha saído da base quente.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O contrato é INSERT na base histórica, conferir a contagem e só então DELETE na base quente.
* 💡 Não há desfazer automático se a tabela seguinte falhar. O histórico auditável marca até onde o lote chegou.
* 💡 O agendamento mora em tabela de configuração. A tela PHP só chama a API. O motor é o worker .NET 9.

---

### 🛠️ Especificação Técnica & Código-Chave
```sql
-- Mesma instância SQL Server, duas bases
INSERT INTO LorentzHistorico.dbo.CTI_CHAMADA
SELECT * FROM LorentzCTI.dbo.CTI_CHAMADA
WHERE DataInicio >= @ini AND DataInicio < @fim;

-- Só apaga na quente depois de a contagem bater
-- O lote fica em CTI_BASEHISTORICA_HISTORICO
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O arquivamento mensal roda como serviço, com rastro do que já foi movido.

* **Projetos Relacionados**: `omnichannel`, `lorentz-vps-stack`, `supervisor`
* **Registro de Origem**: `_data/daily.dev-03.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
