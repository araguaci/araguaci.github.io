---
layout: post
title: "Regra de validação em closure não roda com valor nulo, e o campo obrigatório nunca foi exigido"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-120"
description: "O motivo da desqualificação devia ser obrigatório, e a regra estava escrita. Como ela era um closure sobre um campo nullable, nunca rodava justamente quando o campo vinha vazio."
date: 2026-11-04 00:00:00-03:00
categories: devlog
category: backend
tags: [laravel, validacao, formularios]
---

# Regra de validação em closure não roda com valor nulo, e o campo obrigatório nunca foi exigido

> [!NOTE]
> **Resumo Executivo (DEV-2026-120)**: O motivo da desqualificação devia ser obrigatório, e a regra estava escrita. Como ela era um closure sobre um campo nullable, nunca rodava justamente quando o campo vinha vazio.

---

### 🚨 O Desafio Técnico / Contexto
A regra conferia se o motivo estava vazio, mas o Laravel não executa regra comum em valor nulo de campo nullable. Além disso, o motivo era anexado às notas e, logo depois, as notas do formulário sobrescreviam o texto.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Para campo obrigatório sob condição, use required_if. Essa regra roda com valor vazio.
* 💡 Se precisar de closure para exigir valor, ela tem que ser uma regra implícita. Um teste com o campo vazio mostra a diferença na hora.
* 💡 Duas gravações na mesma coluna na mesma requisição: a última vence. Altere os dados antes da gravação final, e não em uma gravação à parte.
* 💡 Atributo required na tela não é validação. O servidor precisa recusar sozinho.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
// Nunca executa quando o valor vem nulo
'reason' => ['nullable', 'string', function ($attribute, $value, $fail) { /* ... */ }],

// Roda também com o campo vazio
'reason' => 'nullable|required_if:status,not_qualified|string|max:500',
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O motivo passou a ser exigido e a ficar guardado nas notas.

* **Projetos Relacionados**: `sistema-de-atendimento`
* **Registro de Origem**: `_data/daily.dev-19.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
