---
layout: post
title: "A decisão dizia Livewire, e o sistema ficou pronto com zero componentes, porque a ronda precisava funcionar sem sinal"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-126"
description: "A arquitetura foi registrada como Laravel com Livewire, e o registro seguiu assim depois que o código tomou outro rumo. A contagem encontrou zero componentes, então o registro foi corrigido e a decisão passou a citar o requisito que a mudou."
date: 2026-11-04 00:00:00-03:00
categories: devlog
category: arquitetura
tags: [laravel, livewire, pwa, offline, decisoes]
---

# A decisão dizia Livewire, e o sistema ficou pronto com zero componentes, porque a ronda precisava funcionar sem sinal

> [!NOTE]
> **Resumo Executivo (DEV-2026-126)**: A arquitetura foi registrada como Laravel com Livewire, e o registro seguiu assim depois que o código tomou outro rumo. A contagem encontrou zero componentes, então o registro foi corrigido e a decisão passou a citar o requisito que a mudou.

---

### 🚨 O Desafio Técnico / Contexto
O pacote continuava no composer.json e a nota de decisão citava Livewire. A contagem deu zero usos nas views e zero classes de componente. O requisito que apareceu depois foi registrar pagamento na rua, sem sinal, com fila local e reenvio. Isso foi feito com Blade, service worker e JS simples, porque cada interação do Livewire precisa do servidor.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Pacote no composer.json não prova uso. Conte o uso real nas views e nas classes antes de citar a tecnologia em uma decisão ou comparação.
* 💡 Requisito offline decide a camada de tela cedo. Se a tela precisa funcionar sem rede, a interação tem de rodar no aparelho.
* 💡 A fila offline precisa de identidade: cada registro leva um UUID gerado no aparelho, e o reenvio não duplica o pagamento.
* 💡 Decisão registrada também envelhece. Quando um requisito muda a arquitetura, acrescente a nova decisão com o motivo em vez de deixar a antiga valendo.

---

### 🛠️ Especificação Técnica & Código-Chave


---

### 📈 Impacto no Ecossistema & Valor Prático
O registro de decisões voltou a descrever o sistema real, e o requisito offline virou critério de escolha da camada.

* **Projetos Relacionados**: `monitor-laravel`
* **Registro de Origem**: `_data/daily.dev-20.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
