---
layout: post
title: "Auditoria Jurimétrica de Supersalários e Captura Institucional com Corpus CC0"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-009"
description: "Mineração de dados de remuneração de magistrados, quebra de 'penduricalhos' indenizatórios e disponibilização de base aberta sob Creative Commons Zero."
date: 2026-08-15 00:00:00+00:00
categories: devlog
category: osint
tags: [jurimetria, dados-abertos, cc0, judiciario, transparência]
---

# Auditoria Jurimétrica de Supersalários e Captura Institucional com Corpus CC0

> [!NOTE]
> **Resumo Executivo (DEV-2026-009)**: Mineração de dados de remuneração de magistrados, quebra de 'penduricalhos' indenizatórios e disponibilização de base aberta sob Creative Commons Zero.

---

### 🚨 O Desafio Técnico / Contexto
Tribunais brasileiros mascaram supersalários por meio de dezenas de rubricas indenizatórias obscuras (folgas compensatórias, acúmulo de acervo), dificultando a fiscalização cidadã.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 A divisão entre 'remuneração paradigma' (subteto) e 'vantagens eventuais' é o mecanismo padrão de dreno orçamentário.
* 💡 O cálculo da mediana regional de rendimentos em cotejo com a folha dos tribunais revela disparidades superiores a 40x o salário mínimo.
* 💡 Bases em JSON tipado disponibilizadas em repositórios abertos garantem perenidade contra remoção de portais públicos.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
// Cálculo de Excesso de Teto Constitucional
interface Contracheque {
  subsidio: number;
  indenizatorias: number;
  retencaoTeto: number;
}
function calcularLiquidoReal(c: Contracheque): number {
  return (c.subsidio - c.retencaoTeto) + c.indenizatorias;
}

```

---

### 📈 Impacto no Ecossistema & Valor Prático
Base de apoio para pesquisadores cívicos e jornalistas independentes com dados irrefutáveis (JusMonitor).

* **Projetos Relacionados**: `jusmonitor.vercel.app`, `observatorio-civil-br.vercel.app`
* **Registro de Origem**: `_data/daily.dev-01.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
