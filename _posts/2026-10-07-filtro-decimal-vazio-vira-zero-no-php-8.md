---
layout: post
title: "No PHP 8 um filtro decimal vazio vira comparação com zero"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-068"
description: "O reset da lista de clientes montava WHERE de faturamento igual a zero dos dois lados, sem ninguém ter digitado filtro. No PHP 8, converter null com ew_StrToFloat devolve 0, e 0 diferente de string vazia passa a ser verdadeiro."
date: 2026-10-07 00:00:00+00:00
categories: devlog
category: backend
tags: [php, php8, sql, adodb]
---

# No PHP 8 um filtro decimal vazio vira comparação com zero

> [!NOTE]
> **Resumo Executivo (DEV-2026-068)**: O reset da lista de clientes montava WHERE de faturamento igual a zero dos dois lados, sem ninguém ter digitado filtro. No PHP 8, converter null com ew_StrToFloat devolve 0, e 0 diferente de string vazia passa a ser verdadeiro.

---

### 🚨 O Desafio Técnico / Contexto
sac_clientelist.php?cmd=resetall gerava WHERE (ISNULL(Faturamento, 0) = 0 AND ISNULL(Faturamento, 0) = 0) ORDER BY NomeCli. SearchValue vinha de um GET ausente e SearchValue2 nem é carregado na lista: os dois eram null. Faturamento é ADO 131 (adNumeric), então ew_GetSearchSql chama ew_StrToFloat. Essa função devolve inteiro 0 para null. O teste antigo 0 <> "" descartava o campo vazio no PHP 5.6, porque lá 0 == "" é verdadeiro. No PHP 8.2 essa comparação é falsa, então 0 <> "" entra no SQL. O operador vazio vira "=" e a condição vira AND. Refatorar em sac_clienteinfo.php só troca [Faturamento] = por ISNULL(Faturamento, 0) =. Com o WHERE preenchido, o comando virava search e a sessão gravava SearchWhere. Um load seguinte, sem resetall, restaurava o filtro.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 ew_StrToFloat(null) devolve 0. No PHP 8, 0 <> "" é verdadeiro. A conversão só pode rodar depois de recusar null e string vazia.
* 💡 Digitar 0 ainda tem de gerar [Faturamento] = 0. O ISNULL é a busca real por zero, não a origem do filtro fantasma.
* 💡 resetall limpa a sessão, mas o bug nascia de novo em AdvancedSearchWhere. O WHERE gravado só explica a página sem cmd=resetall.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
// phpfn9.php — ew_GetSearchSql, campo float/numeric
if (!is_null($FldVal) && $FldVal !== "")
    $FldVal = ew_StrToFloat($FldVal);
if (!is_null($FldVal2) && $FldVal2 !== "")
    $FldVal2 = ew_StrToFloat($FldVal2);
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Reset da lista deixa de filtrar faturamento igual a zero quando os dois lados do campo estão vazios.

* **Projetos Relacionados**: `supervisor`
* **Registro de Origem**: `_data/daily.dev-09.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
