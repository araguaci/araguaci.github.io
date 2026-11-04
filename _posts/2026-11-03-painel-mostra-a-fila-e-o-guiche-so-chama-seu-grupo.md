---
layout: post
title: "O painel mostra a fila da unidade, e o guichê só chama os serviços do próprio grupo"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-102"
description: "O botão de chamar parecia quebrado enquanto o painel e o monitor mostravam senhas esperando. O código estava certo, e faltava a tela explicar a diferença entre as duas filas."
date: 2026-11-03 00:00:00-03:00
categories: devlog
category: frontend
tags: [laravel, atp, filas, ux, mensagens]
---

# O painel mostra a fila da unidade, e o guichê só chama os serviços do próprio grupo

> [!NOTE]
> **Resumo Executivo (DEV-2026-102)**: O botão de chamar parecia quebrado enquanto o painel e o monitor mostravam senhas esperando. O código estava certo, e faltava a tela explicar a diferença entre as duas filas.

---

### 🚨 O Desafio Técnico / Contexto
O atendente clicava em chamar e nada acontecia, com senhas visíveis no painel. As senhas eram de um serviço que o grupo dele não atende, e ninguém logado atendia aquele serviço.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Duas telas podem mostrar recortes diferentes da mesma fila. Se quem olha não vê a diferença, o comportamento correto parece defeito.
* 💡 A mensagem de fila vazia agora diz quais serviços têm gente esperando e quantas senhas: 'Aguardando em serviços que você não atende: Financeiro (2).'
* 💡 O monitor ganhou a coluna Atendentes (guichê aberto, fora de pausa, com o serviço no grupo) e o aviso 'sem atendente' quando há senha esperando e ninguém disponível.
* 💡 Diagnosticar antes de corrigir evitou mudar o distribuidor, que estava certo.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
// A fila da unidade pode ter senhas de serviços que o grupo não atende
$meus = array_keys(app(Distribuidor::class)->servicosDo($u));
$fora = Senha::with('servico')->where('unidade_id', $u->unidade_id)
    ->where('status', Senha::AGUARDANDO)
    ->whereDate('data', now()->toDateString())
    ->whereNotIn('servico_id', $meus)->get()
    ->groupBy(fn ($s) => $s->servico->nome)->map->count();
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A supervisão vê a falta de atendente no monitor, e o atendente sabe por que não veio nenhuma senha.

* **Projetos Relacionados**: `lorentz-atp`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
