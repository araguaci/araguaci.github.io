---
layout: post
title: "O piloto do assistente de IA começa pelo suporte do próprio sistema"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-088"
description: "Um assistente de IA exposto logo a clientes externos arrisca errar no domínio deles. O piloto usa o suporte do próprio Lorentz, e a fase de voz só abre quando os indicadores chegam ao valor definido."
date: 2026-06-21 00:00:00-03:00
categories: devlog
category: ia
tags: [ia, whatsapp, rag, suporte, piloto]
---

# O piloto do assistente de IA começa pelo suporte do próprio sistema

> [!NOTE]
> **Resumo Executivo (DEV-2026-088)**: Um assistente de IA exposto logo a clientes externos arrisca errar no domínio deles. O piloto usa o suporte do próprio Lorentz, e a fase de voz só abre quando os indicadores chegam ao valor definido.

---

### 🚨 O Desafio Técnico / Contexto
A fase 4 do plano da URA para o WhatsApp precisava validar passagem de contexto, IA por texto e escalonamento. Era preciso escolher um domínio de baixo risco, em que a equipe conseguisse avaliar se a resposta estava certa.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Instalação, configuração, administração e troubleshooting são um domínio que a equipe domina, logo o erro aparece rápido e o valor interno é imediato.
* 💡 A base de perguntas é ancorada na configuração real, e a matriz de escalonamento define quando a IA para e passa para uma pessoa.
* 💡 Toda conversa escalada vira candidata a nova FAQ, com curadoria quinzenal. O piloto evolui com chamados reais.
* 💡 A passagem de fase tem número: voz só com autoatendimento de pelo menos 40% e precisão de triagem de pelo menos 85%. São metas do roteiro, ainda sem medição do piloto.

---

### 🛠️ Especificação Técnica & Código-Chave


---

### 📈 Impacto no Ecossistema & Valor Prático
O avanço do assistente passou a depender de critério escrito, e não de impressão sobre a qualidade das respostas.

* **Projetos Relacionados**: `omnichannel`, `lorentz-supervisor`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
