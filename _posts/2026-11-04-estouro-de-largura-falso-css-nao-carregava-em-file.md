---
layout: post
title: "O teste apontou estouro de largura no celular, e o que faltava era o CSS que o file:// não carregava"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-131"
description: "Uma conferência em Chrome headless mostrou 748 pixels de conteúdo em uma tela de 375, o que parecia defeito de layout. O problema estava na conferência, e o método passou a carregar o tema de um servidor local."
date: 2026-11-04 00:00:00-03:00
categories: devlog
category: frontend
tags: [chrome, headless, css, testes, mobile]
---

# O teste apontou estouro de largura no celular, e o que faltava era o CSS que o file:// não carregava

> [!NOTE]
> **Resumo Executivo (DEV-2026-131)**: Uma conferência em Chrome headless mostrou 748 pixels de conteúdo em uma tela de 375, o que parecia defeito de layout. O problema estava na conferência, e o método passou a carregar o tema de um servidor local.

---

### 🚨 O Desafio Técnico / Contexto
Salvei o HTML das telas e abri com file://. A folha de estilo do tema usa caminho a partir da raiz e não carregou, então a regra que contém a tabela não existia na conferência. A captura com largura de 390 também saiu cortada, porque o Chrome headless não reduziu a janela abaixo de cerca de 500 pixels.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Caminho iniciado em barra não resolve em file://. Acrescente base href apontando para um servidor local antes de conferir o layout.
* 💡 Para simular celular no headless, use um iframe com a largura desejada dentro de uma janela maior.
* 💡 Meça em vez de olhar: compare scrollWidth com clientWidth no próprio documento. Com o tema carregado, os dois deram 375.
* 💡 Antes de corrigir um defeito, confira se a ferramenta reproduz as condições reais. A página parecia sem tema, e esse foi o sinal de que a medição estava errada.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
<base href="http://127.0.0.1:8123/">
<iframe src="tela.html" style="width:390px;height:844px;border:0"></iframe>
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A conferência visual passou a medir a página como o usuário recebe, e o layout correto não foi alterado por engano.

* **Projetos Relacionados**: `monitor-laravel`
* **Registro de Origem**: `_data/daily.dev-20.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
