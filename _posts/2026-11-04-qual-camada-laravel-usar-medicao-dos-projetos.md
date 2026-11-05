---
layout: post
title: "Blade com pouco JS deu mais teste por linha nos meus projetos Laravel, e Inertia com Vue só se paga em tela rica"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-124"
description: "Havia projetos em Blade, Inertia com Vue, Livewire, Filament e API, sem critério registrado para escolher entre eles. A medição do código passou a definir Blade como padrão e as outras camadas como exceção com motivo."
date: 2026-11-04 00:00:00-03:00
categories: devlog
category: arquitetura
tags: [laravel, blade, inertia, livewire, filament, arquitetura]
---

# Blade com pouco JS deu mais teste por linha nos meus projetos Laravel, e Inertia com Vue só se paga em tela rica

> [!NOTE]
> **Resumo Executivo (DEV-2026-124)**: Havia projetos em Blade, Inertia com Vue, Livewire, Filament e API, sem critério registrado para escolher entre eles. A medição do código passou a definir Blade como padrão e as outras camadas como exceção com motivo.

---

### 🚨 O Desafio Técnico / Contexto
A pergunta era qual camada usar no próximo projeto, e a resposta vinha de impressão. Medi composer.json, linhas de código, migrations, histórico do git e casos de teste. Primeiro precisei retirar da conta os repositórios clonados: os que tinham mais commits tinham zero commits meus. Os projetos resolvem problemas diferentes, então a comparação orienta a escolha, mas não é um experimento controlado.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Blade com Bootstrap ou Alpine: serve para sistema de gestão, celular, impressão e PWA offline. Um único código, e o teste HTTP enxerga a tela inteira. Foi o que juntou mais teste por linha.
* 💡 Inertia com Vue: serve para painel rico e muito interativo. Foi o maior projeto medido, com 211 componentes além do PHP, e o teste em PHP não alcança o que acontece nesses componentes.
* 💡 Livewire: tela interativa sem escrever JS, com o custo de depender do servidor a cada interação. Só um projeto usa de verdade, com 16 componentes.
* 💡 API com Sanctum: serve quando há mais de um consumidor, como app ou integração. Os meus são os menores e têm poucos testes, então a evidência é fraca.
* 💡 Filament: o painel saiu sem nenhuma view própria, mas o projeto medido não tem testes. Mostra velocidade, não confiabilidade.
* 💡 Contar commits engana: um projeto recebeu 17 commits em um dia porque partiu de uma base importada, e outro tem o histórico dividido com o repositório inteiro. Linhas, testes e dias ativos dizem mais.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
Projeto                 Camada         Linhas app  Testes  Por mil linhas
monitor-laravel         Blade                8802     212              24
05-orcamento            Blade+Alpine        10568     159              15
lorentz-atp             Blade                5047      73              14
lorentz-cidadao         Blade                3312      34              10
omnichannel-system      Inertia+Vue         28863     249               9

Os três primeiros foram executados. Os dois últimos foram contados no código.
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O próximo sistema de gestão começa em Blade, e usar outra camada passou a exigir um motivo escrito.

* **Projetos Relacionados**: `monitor-laravel`, `05-orcamento`, `lorentz-atp`, `lorentz-cidadao`, `omnichannel-system`
* **Registro de Origem**: `_data/daily.dev-20.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
