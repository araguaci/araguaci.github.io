---
layout: post
title: "Taxa de atendimento de 0% com mil chamadas: a métrica procurava um status que os dados não usam"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-115"
description: "O painel mostrava 0% de atendimento e nenhuma chamada ativa, enquanto a lista exibia chamadas atendidas. Cada tela tinha a própria definição de atendida e de em andamento, e nenhuma foi conferida contra os dados."
date: 2026-11-04 00:00:00-03:00
categories: devlog
category: backend
tags: [metricas, laravel, sql, dashboard]
---

# Taxa de atendimento de 0% com mil chamadas: a métrica procurava um status que os dados não usam

> [!NOTE]
> **Resumo Executivo (DEV-2026-115)**: O painel mostrava 0% de atendimento e nenhuma chamada ativa, enquanto a lista exibia chamadas atendidas. Cada tela tinha a própria definição de atendida e de em andamento, e nenhuma foi conferida contra os dados.

---

### 🚨 O Desafio Técnico / Contexto
O painel contava só o status completed, mas os dados tinham apenas answered e abandoned. Outra tela procurava in_progress, que a validação nem aceita. E um indicador novo contava answered como em andamento sem olhar se a chamada já tinha terminado.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Antes de escrever uma métrica, agrupe os dados reais por status. A consulta de um minuto teria mostrado o problema.
* 💡 Regra de negócio repetida em cada consulta acaba divergindo. Definir atendida e em andamento em um só lugar, com scopes no model, faz as telas concordarem.
* 💡 Em andamento depende de dois campos: o status e a data de encerramento vazia.
* 💡 Confira o número novo contra outro independente. Atendidas de 73,54% e abandono de 26,18% somam cerca de 100%, o que dá mais confiança do que o teste passar.
* 💡 O dado de demonstração revelou o erro, mas também pode confundir: uma pausa aberta há 8.504 horas é conta certa sobre um dado antigo, e não um defeito.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
public function scopeAttended($query)
{
    return $query->whereIn('status', ['answered', 'completed']);
}

public function scopeOngoing($query)
{
    return $query->whereIn('status', ['ringing', 'answered'])->whereNull('ended_at');
}
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Painel, monitoramento e tela inicial passaram a usar a mesma definição e a mostrar números que fecham entre si.

* **Projetos Relacionados**: `sistema-de-atendimento`
* **Registro de Origem**: `_data/daily.dev-19.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
