---
layout: post
title: "No Carbon 3, diffInSeconds tem sinal e casas decimais, e a duração negativa foi parar no banco"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-112"
description: "Uma tela mostrava pausa de -34,10325 segundos, o que parecia erro de exibição. A causa era a mudança do Carbon 3, e o mesmo cálculo gravava duração negativa ao encerrar pausa, chamada e chat."
date: 2026-11-04 00:00:00-03:00
categories: devlog
category: backend
tags: [laravel, carbon, php, datas]
---

# No Carbon 3, diffInSeconds tem sinal e casas decimais, e a duração negativa foi parar no banco

> [!NOTE]
> **Resumo Executivo (DEV-2026-112)**: Uma tela mostrava pausa de -34,10325 segundos, o que parecia erro de exibição. A causa era a mudança do Carbon 3, e o mesmo cálculo gravava duração negativa ao encerrar pausa, chamada e chat.

---

### 🚨 O Desafio Técnico / Contexto
O código fazia now()->diffInSeconds($inicio), que no Carbon 2 devolvia um inteiro positivo. No Carbon 3, que vem com o Laravel 12, o intervalo tem sinal e é decimal: do presente para o passado, o resultado é negativo.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O sentido passou a importar. Escreva sempre do mais antigo para o mais novo: $inicio->diffInSeconds(now()).
* 💡 O retorno é float. Se a coluna ou a tela espera inteiro, faça o cast com (int).
* 💡 Uma atualização de framework pode não dar erro nenhum e ainda assim gravar dado errado. Depois de atualizar, procure todos os diffIn no código, e não só o que apareceu na tela.
* 💡 A busca achou o mesmo erro em cinco pontos, três deles gravando no banco. Corrigir o cálculo não conserta o que já foi gravado, e esses dados precisam de conferência à parte.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
// Carbon 3: negativo e decimal
now()->diffInSeconds($pause->started_at);   // -34.10325

// Do passado para o presente, como inteiro
(int) $pause->started_at->diffInSeconds(now());   // 34
```

---

### 📈 Impacto no Ecossistema & Valor Prático
As durações passaram a ser positivas e inteiras, e os registros antigos ficaram marcados para conferência.

* **Projetos Relacionados**: `sistema-de-atendimento`
* **Registro de Origem**: `_data/daily.dev-19.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
