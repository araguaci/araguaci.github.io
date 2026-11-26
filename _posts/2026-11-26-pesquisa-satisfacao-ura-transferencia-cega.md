---
layout: post
title: "Pesquisa de satisfação pela URA exige transferência cega"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-184"
description: "Na chamada de prova, a terceira pergunta da pesquisa não aceitava resposta. O agente tinha feito transferência assistida, e as duas primeiras perguntas tocaram para ele."
date: 2026-11-26 00:00:00-03:00
categories: devlog
category: arquitetura
tags: [ura, dtmf, asterisk, call-center]
---

# Pesquisa de satisfação pela URA exige transferência cega

> [!NOTE]
> **Resumo Executivo (DEV-2026-184)**: Na chamada de prova, a terceira pergunta da pesquisa não aceitava resposta. O agente tinha feito transferência assistida, e as duas primeiras perguntas tocaram para ele.

---

### 🚨 O Desafio Técnico / Contexto
O fluxo é: cliente liga para a URA de entrada, escolhe a fila, o agente atende e transfere para a URA de satisfação. A pergunta 3 travava. O log de DTMF do Asterisk mostrou que, depois da transferência, nenhum dígito vinha do cliente. A chamada direta do cliente para a URA de satisfação passava inteira. O agente tinha consultado a URA antes de completar a transferência: as perguntas 1 e 2 tocaram no telefone dele, e só a 3 chegou ao cliente.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 As perguntas 1 e 2 tinham espera de 5 s e avançavam sem dígito. A pergunta 3 não tinha prazo e ficava parada para sempre. Uma árvore sem timeout em todos os nós de dígito pode prender a chamada.
* 💡 Separar o problema com duas chamadas (direta e transferida) e um canal de log só de DTMF no Asterisk mostrou em minutos de que lado o dígito sumia.
* 💡 Para pesquisa pela URA, o agente usa transferência cega. A assistida coloca o próprio agente na URA.

---

### 🛠️ Especificação Técnica & Código-Chave
```bash
asterisk -rx "logger add channel dtmf-lab.log dtmf,notice,warning"
# DTMF begin '5' received on SIP/410-...  (chamada direta)
# nenhum dígito do cliente depois da transferência assistida
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A pesquisa fechou as três respostas, e o procedimento do agente entrou no roteiro do laboratório.

* **Projetos Relacionados**: `lorentz-ura-impacta`, `lorentz-vps-stack`
* **Registro de Origem**: `_data/daily.dev-34.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
