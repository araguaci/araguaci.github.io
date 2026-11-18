---
layout: post
title: "Classe utilitária do Tailwind sobrescreve a variável de fundo e quebra o contraste no tema escuro"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-156"
description: "O fundo da área de trabalho continuava branco claro nos temas Sunset Dourado, Oceano Profundo e Floresta Esmeralda enquanto os títulos recebiam cor clara, sumindo sobre o fundo. A classe utilitária gerada pelo Tailwind tinha a mesma especificidade da folha de temas e vencia pela ordem de importação."
date: 2026-11-12 00:00:00-03:00
categories: devlog
category: frontend
tags: [css, tailwind, design-system, dark-mode, especificidade]
---

# Classe utilitária do Tailwind sobrescreve a variável de fundo e quebra o contraste no tema escuro

> [!NOTE]
> **Resumo Executivo (DEV-2026-156)**: O fundo da área de trabalho continuava branco claro nos temas Sunset Dourado, Oceano Profundo e Floresta Esmeralda enquanto os títulos recebiam cor clara, sumindo sobre o fundo. A classe utilitária gerada pelo Tailwind tinha a mesma especificidade da folha de temas e vencia pela ordem de importação.

---

### 🚨 O Desafio Técnico / Contexto
Em 2026-11-12, ao ativar temas escuros no ProntOS, o cabeçalho e a barra lateral escureciam, mas a área principal mantinha fundo branco #F8FAFC. Como a regra do tema aplicava texto quase branco aos títulos de h1 e tabelas, o conteúdo ficava invisível.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Importar triade-theme.css antes do @tailwind utilities fazia a classe gerada .bg-[#F8FAFC] ter prioridade de cascata sobre body, .bg-[#F8FAFC] { background-color: var(--tr-page); }.
* 💡 Inverter a ordem no main.tsx (importando triade-theme.css após index.css) garante que a definição dos temas seja avaliada por último.
* 💡 Definir o fundo do container e do elemento main com style={{ backgroundColor: 'var(--tr-page)' }} e classe semântica remove a dependência de sobrescrever classes literais hexadecimais do Tailwind.
* 💡 Botões de destaque com texto claro precisam de --tr-on-accent quando a paleta do tema no modo escuro clareia a cor primária (como o âmbar do Sunset Dourado e o ciano do Oceano Profundo).

---

### 🛠️ Especificação Técnica & Código-Chave
```python
/* main.tsx */
import './index.css'
import './triade-theme.css'

/* MainLayout.tsx */
<main style={{ backgroundColor: 'var(--tr-page)', color: 'rgb(var(--tr-gray-900))' }}>
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A área principal e as tabelas adotaram contraste perfeito e fundo imersivo em todos os temas escuros da Tríade.

* **Projetos Relacionados**: `30-FieldFlow`, `triade-artesdosul`
* **Registro de Origem**: `_data/daily.dev-27.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
