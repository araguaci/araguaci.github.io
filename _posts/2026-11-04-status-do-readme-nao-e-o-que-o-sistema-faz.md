---
layout: post
title: "O status escrito no README não é o que o sistema faz: confira no código antes de apresentar"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-123"
description: "O README marcava canais como implementados, e uma apresentação feita a partir dele prometeria o que não existe. Conferir o código mudou o slide de situação e um relatório de decisões."
date: 2026-11-04 00:00:00-03:00
categories: devlog
category: conteudo
tags: [documentacao, apresentacao, produto, revisao]
---

# O status escrito no README não é o que o sistema faz: confira no código antes de apresentar

> [!NOTE]
> **Resumo Executivo (DEV-2026-123)**: O README marcava canais como implementados, e uma apresentação feita a partir dele prometeria o que não existe. Conferir o código mudou o slide de situação e um relatório de decisões.

---

### 🚨 O Desafio Técnico / Contexto
O documento listava telefonia, WhatsApp, chat e e-mail com sinal de pronto. No código, a chamada era só registrada, o WhatsApp comercial só gravava a mensagem, o e-mail não enviava e iniciar campanha só mudava o status.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Pronto precisa dizer pronto para quê. Separar tela e regra de tráfego real muda a conversa com quem compra.
* 💡 Para cada frase de capacidade, procure no código a chamada que faz acontecer: o cliente HTTP, o envio, a discagem.
* 💡 Ao revisar o texto final, procure o que afirma mais do que foi conferido. Eu escrevi que uma falha impedia acessos, e o certo era que podia estar impedindo, porque a confirmação ainda faltava.
* 💡 Escolha prints que mostrem a tela como ela é, com aviso de dados de demonstração. Tela com número errado fica de fora e entra na lista de defeitos.
* 💡 Notas do apresentador ficam no código da página. Em site público, qualquer um as lê.
* 💡 Errar e corrigir por escrito vale mais do que ajustar em silêncio: quem decide precisa saber qual afirmação mudou.

---

### 🛠️ Especificação Técnica & Código-Chave


---

### 📈 Impacto no Ecossistema & Valor Prático
O material passou a separar o que está pronto do que vem, e cada afirmação tem de onde veio.

* **Projetos Relacionados**: `sistema-de-atendimento`
* **Registro de Origem**: `_data/daily.dev-19.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
