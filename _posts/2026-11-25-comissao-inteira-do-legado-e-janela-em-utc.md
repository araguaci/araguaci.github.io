---
layout: post
title: "A comissão do legado é um inteiro no funcionário, e zero não é zero por cento"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-177"
description: "A comissão já existia no cadastro antigo como inteiro, e zero significava que não havia comissão. A consulta do monitor passou a somar o valor confirmado no período local, com o fim do dia exclusivo."
date: 2026-11-25 00:00:00-03:00
categories: devlog
category: backend
tags: [laravel, mysql, comissao, fuso]
---

# A comissão do legado é um inteiro no funcionário, e zero não é zero por cento

> [!NOTE]
> **Resumo Executivo (DEV-2026-177)**: A comissão já existia no cadastro antigo como inteiro, e zero significava que não havia comissão. A consulta do monitor passou a somar o valor confirmado no período local, com o fim do dia exclusivo.

---

### 🚨 O Desafio Técnico / Contexto
Somar a mensalidade, ou o mês civil em UTC, erra o total de quem trabalha em São Paulo. Um percentual 0 gravado como número ainda aparece como comissão. Pagamento de outro monitor, ou de fora do intervalo, não pode entrar na soma.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 No Access o campo é Funcionario.Comissao, inteiro. LegacyImporter grava commission_percent só de 1 a 100; fora disso fica null. A migration 2026_11_25_000900_add_monitor_commission_percent.php copia o mesmo recorte do JSON em legacy_records, source_table Funcionario, com CAST e BETWEEN 1 AND 100.
* 💡 No formulário, 0 vira null antes da validação. A regra é nullable, integer, min 1, max 100. Sem isso o zero não passa no mínimo e a tela trata ausência como erro.
* 💡 collectedReport lê de e ate. Se o fim é anterior ao início, troca os dois. O padrão é o dia 1 do mês até hoje, no fuso config('app.display_timezone'), que cai em America/Sao_Paulo. O início é startOfDay convertido para UTC. O fim é o dia seguinte, também startOfDay em UTC, e a comparação de confirmed_at é maior ou igual e menor.
* 💡 O total é a soma de confirmed_amount, arredondada em duas casas. A comissão é essa soma vezes o percentual, dividida por 100, também arredondada. Percentual vazio não gera valor. A consulta filtra monitor_id, então o recebimento de outro monitor fica de fora.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
$start = Carbon::createFromFormat('Y-m-d', $de, $timezone)->startOfDay()->utc();
$end = Carbon::createFromFormat('Y-m-d', $ate, $timezone)->addDay()->startOfDay()->utc();
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O percentual vem do cadastro antigo, zero continua sem comissão, e o período fecha na meia-noite local.

* **Projetos Relacionados**: `monitoramento-app`
* **Registro de Origem**: `_data/daily.dev-33.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
