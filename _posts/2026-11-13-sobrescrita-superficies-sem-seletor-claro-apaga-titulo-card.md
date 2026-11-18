---
layout: post
title: "Sobrescrita de superfícies sem seletor claro faz título herdar a cor do fundo do card"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-158"
description: "Nos temas claros ProntOS e Central de Aventura, o texto de títulos h2 dentro de cards sumia por se igualar ao fundo branco ou washi. O seletor de tema claro não declarava a cor de texto contrastante e classes conflitantes de card misturavam fundos escuros e claros."
date: 2026-11-13 00:00:00-03:00
categories: devlog
category: frontend
tags: [css, tailwind, design-system, contraste, light-mode]
---

# Sobrescrita de superfícies sem seletor claro faz título herdar a cor do fundo do card

> [!NOTE]
> **Resumo Executivo (DEV-2026-158)**: Nos temas claros ProntOS e Central de Aventura, o texto de títulos h2 dentro de cards sumia por se igualar ao fundo branco ou washi. O seletor de tema claro não declarava a cor de texto contrastante e classes conflitantes de card misturavam fundos escuros e claros.

---

### 🚨 O Desafio Técnico / Contexto
Em 2026-11-13, após a padronização do modo escuro, os títulos h2 dentro de cards nos temas claros (ProntOS / AgendaSul e Central de Aventura) sumiram da tela por estarem com a mesma tonalidade da superfície do card.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Declarar regras de contraste para [data-triade-mode='dark'] sem o bloco espelho [data-triade-mode='light'] deixa os títulos dos temas claros vulneráveis a heranças indevidas.
* 💡 O tema padrão agendasul precisa ter seletor explícito [data-triade-theme='agendasul'] no CSS para igualar a especificidade dos temas temáticos como central-de-aventura.
* 💡 Banners e blocos que já possuem gradiente próprio ou fundo escuro explícito (.bg-slate-900, .bg-gradient-to-r) não devem herdar a classe .card, cujo @apply bg-white injeta cor de superfície conflitante.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
/* Garantia de contraste nos temas claros */
[data-triade-mode="light"] :is(.card, main) :is(h1, h2, h3, h4, h5, h6):not([class*="text-white"]) {
  color: rgb(var(--tr-gray-900)) !important;
}
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Os títulos e cabeçalhos de todos os cards recuperaram legibilidade e contraste absoluto nos temas claros e escuros.

* **Projetos Relacionados**: `30-FieldFlow`, `triade-artesdosul`
* **Registro de Origem**: `_data/daily.dev-27.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
