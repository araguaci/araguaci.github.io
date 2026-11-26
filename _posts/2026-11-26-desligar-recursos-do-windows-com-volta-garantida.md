---
layout: post
title: "Desligar recursos do Windows com volta garantida exige gravar o estado anterior antes de mudar"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-187"
description: "Scripts de debloat costumam gravar valores fixos e não sabem voltar ao estado de antes. No Labmini, cada ajuste passou a ser sondado, planejado com as operações de reversão calculadas a partir do valor real e gravado em backup antes da primeira alteração."
date: 2026-11-26 00:00:00-03:00
categories: devlog
category: arquitetura
tags: [windows, registro, servicos, backup, rust]
---

# Desligar recursos do Windows com volta garantida exige gravar o estado anterior antes de mudar

> [!NOTE]
> **Resumo Executivo (DEV-2026-187)**: Scripts de debloat costumam gravar valores fixos e não sabem voltar ao estado de antes. No Labmini, cada ajuste passou a ser sondado, planejado com as operações de reversão calculadas a partir do valor real e gravado em backup antes da primeira alteração.

---

### 🚨 O Desafio Técnico / Contexto
Desativar Xbox, widgets, telemetria e apps pré-instalados mexe em quatro tipos de alvo: serviço, valor de registro, tarefa agendada e pacote Appx. Uma reversão genérica do tipo "volta para Automático" ou "apaga a chave" erra quando o serviço era Automático com atraso, quando o valor era ExpandString ou quando o valor nem existia antes. Também não dá para confiar num plano montado minutos antes pela interface, porque o estado pode ter mudado.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Serviço: guarde StartMode e DelayedAutoStart do Win32_Service e se estava rodando. Reverter é sc.exe config NOME start= auto, delayed-auto ou demand, e Start-Service só se estava rodando.
* 💡 Registro: guarde se o valor existia, o tipo (GetValueKind) e o valor lido com 'DoNotExpandEnvironmentNames'. Se não existia, reverter é apagar o valor, não gravar zero. Tipos que você não sabe regravar (Binary, MultiString) ficam fora do plano.
* 💡 O backup vai para o disco antes da primeira operação, com escrita atômica (arquivo temporário e rename). Assim, mesmo se o PowerShell cair no meio, existe como voltar.
* 💡 O backend recebe só os ids e sonda de novo na hora de aplicar. Um plano velho vindo da interface nunca é executado.
* 💡 Cada operação roda em try/catch próprio e devolve um resultado. A falha de um item não derruba os outros e fica registrada no backup.
* 💡 A primeira sondagem grava um baseline.json que nunca é sobrescrito, com o retrato de como o Windows veio.

---

### 🛠️ Especificação Técnica & Código-Chave


---

### 📈 Impacto no Ecossistema & Valor Prático
41 ajustes aplicados de uma vez no PC real podem ser revertidos tudo ou item a item, e o teste de ida e volta confirmou estado final idêntico ao inicial, inclusive tipo ExpandString.

* **Projetos Relacionados**: `labmini`
* **Registro de Origem**: `_data/daily.dev-30.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
