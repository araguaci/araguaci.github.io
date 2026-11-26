---
layout: post
title: "Na pesquisa, número curto, telefone, valor e dia de vencimento não são a mesma busca"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-175"
description: "Um campo só precisava achar rua, casa, nome, telefone, contrato, código, vencimento e valor. Tratar tudo como LIKE juntava o dia do mês com telefone e com dinheiro."
date: 2026-11-25 00:00:00-03:00
categories: devlog
category: backend
tags: [laravel, sql, busca, telefone]
---

# Na pesquisa, número curto, telefone, valor e dia de vencimento não são a mesma busca

> [!NOTE]
> **Resumo Executivo (DEV-2026-175)**: Um campo só precisava achar rua, casa, nome, telefone, contrato, código, vencimento e valor. Tratar tudo como LIKE juntava o dia do mês com telefone e com dinheiro.

---

### 🚨 O Desafio Técnico / Contexto
O termo 10 pode ser casa, código ou dia de vencimento. 80,00 é mensalidade. Um telefone com máscara não é igual aos dígitos digitados. Uma letra só, ou um número de um ou dois dígitos passado em LIKE, devolve gente demais. A rota também não pode entregar o cadastro a quem está em campo.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 GlobalSearch::clients trata termo só de dígitos com menos de 3 caracteres como id, legacy_id ou number do imóvel. A partir de 3, entra o LIKE em nome, endereço, rua, bairro e telefone. Uma letra não busca: longEnough pede dois caracteres quando não é número puro.
* 💡 O telefone compara os dígitos com REPLACE aninhado em espaço, hífen, parênteses e ponto, e só se há pelo menos 3 dígitos. O valor vira decimal com ponto: vírgula troca o separador e o ponto de milhar sai. Se o termo tem ponto ou vírgula e o valor fechou, esses dígitos não vão para o telefone. Mais de 8 dígitos não é valor.
* 💡 O dia usa a expressão dia ou vencimento, opcional, mais um ou dois dígitos de 1 a 31. O SQL é DAY(COALESCE(billing_date, start_date)). O contrato também compara contract_number, id e legacy_id.
* 💡 Client usa BelongsToCompany, e CompanyScope filtra company_id de quem está logado. Sem empresa, a consulta vira whereRaw 1 = 0. RestrictMonitorAccess não lista search.index, então o perfil de campo recebe 403.
* 💡 A rota /busca tem throttle de 60 por minuto. A página pede 30 linhas, o JSON pede 8 e a saída csv, ficha ou checklist pede 200. O CSV grava BOM EF BB BF e separa com ponto e vírgula.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
$phoneDigits = ($amount !== null && preg_match('/[.,]/', $term)) ? '' : $digits;
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O mesmo campo acha a casa, o telefone mascarado, o valor e o dia, sem misturar um no outro.

* **Projetos Relacionados**: `monitoramento-app`
* **Registro de Origem**: `_data/daily.dev-33.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
