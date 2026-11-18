---
layout: post
title: "A verificação de limite existia e tinha teste, mas só o teste a chamava"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-116"
description: "Parecia haver um erro na conta do limite de uso contratado. Ao procurar quem usava aquela função, o problema era maior: nenhum código de produção a chamava."
date: 2026-11-04 00:00:00-03:00
categories: devlog
category: arquitetura
tags: [licenca, testes, laravel, revisao]
---

# A verificação de limite existia e tinha teste, mas só o teste a chamava

> [!NOTE]
> **Resumo Executivo (DEV-2026-116)**: Parecia haver um erro na conta do limite de uso contratado. Ao procurar quem usava aquela função, o problema era maior: nenhum código de produção a chamava.

---

### 🚨 O Desafio Técnico / Contexto
Os métodos de limite de usuários, campanhas e uso simultâneo estavam prontos e cobertos por testes unitários. Nenhum controller, middleware ou serviço os chamava, então nenhum limite era aplicado.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Teste unitário prova que a função funciona, e não que ela é usada. A cobertura pode estar alta com a regra desligada.
* 💡 Ao corrigir uma função, procure quem a chama. Se só os testes aparecem, a correção não muda nada para o usuário.
* 💡 Teste de regra de negócio precisa partir da ação do usuário: tentar passar do limite e ver a recusa.
* 💡 Ligar uma regra que nunca valeu é mudança de comportamento. Pode bloquear quem já passou do limite, então vale medir e avisar antes de bloquear.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
# Quem chama, fora a própria definição?
grep -rn "checkUserLimit" app resources routes tests | grep -v "public function"
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A aplicação dos limites virou uma decisão explícita de negócio, em vez de uma suposição de que já funcionava.

* **Projetos Relacionados**: `sistema-de-atendimento`
* **Registro de Origem**: `_data/daily.dev-19.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
