---
layout: post
title: "Rollover do Fator de Vencimento FEBRABAN pós-2025 e Linha Digitável de Boleto no PHP"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-137"
description: "O cálculo do Fator de Vencimento bancário da FEBRABAN ultrapassou o teto de 9999 dias em fevereiro de 2025. Implementamos o rollover para o novo ciclo de 1000 a 9999 garantindo código de barras e linha digitável válidos."
date: 2026-11-08 00:00:00-03:00
categories: devlog
category: backend
tags: [php, boleto, febraban, erp, pagamentos]
---

# Rollover do Fator de Vencimento FEBRABAN pós-2025 e Linha Digitável de Boleto no PHP

> [!NOTE]
> **Resumo Executivo (DEV-2026-137)**: O cálculo do Fator de Vencimento bancário da FEBRABAN ultrapassou o teto de 9999 dias em fevereiro de 2025. Implementamos o rollover para o novo ciclo de 1000 a 9999 garantindo código de barras e linha digitável válidos.

---

### 🚨 O Desafio Técnico / Contexto
A data base original da FEBRABAN (07/10/1997) gerava 10.000 dias decorridos em 22/02/2025. Ao converter datas posteriores para o fator de vencimento de 4 dígitos sem o tratamento de rollover, a string resultante continha 5 dígitos, estourando o código de barras de 44 posições para 45 caracteres e corrompendo a validação por Módulo 11.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O primeiro ciclo da FEBRABAN esgotou em 21/02/2025 (fator 9999); em 22/02/2025 reiniciou em 1000.
* 💡 O cálculo deve usar a diferença em dias a partir da data de corte 2025-02-22 acrescido do offset 1000.
* 💡 A linha digitável divide o código em três campos validados por Módulo 10, seguidos do dígito geral e fator/valor.
* 💡 A geração de barras I25 e QR Code PIX deve ser feita em SVG vetorial offline para evitar latência de APIs externas.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
if ($dueDate->gte(Carbon::parse('2025-02-22'))) {
    $base2025 = Carbon::parse('2025-02-22');
    $days = 1000 + $base2025->diffInDays($dueDate);
    return str_pad((string) ($days % 10000), 4, '0', STR_PAD_LEFT);
}
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Emissão de boletos bancários no ERP 100% aderente ao novo ciclo regulatório FEBRABAN sem quebra de código de barras.

* **Projetos Relacionados**: `laravel-ERP`
* **Registro de Origem**: `_data/daily.dev-23.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
