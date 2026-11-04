---
layout: post
title: "Produto novo que parece variação de outro entra como irmão, sobre um núcleo comum"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-092"
description: "Automação de hotel parecia uma extensão natural do sistema de energia. A decisão foi criar um produto irmão sobre um núcleo de IoT compartilhado, sem renomear nem clonar o monólito."
date: 2026-07-31 00:00:00-03:00
categories: devlog
category: arquitetura
tags: [iot, arquitetura, produto, monolito]
---

# Produto novo que parece variação de outro entra como irmão, sobre um núcleo comum

> [!NOTE]
> **Resumo Executivo (DEV-2026-092)**: Automação de hotel parecia uma extensão natural do sistema de energia. A decisão foi criar um produto irmão sobre um núcleo de IoT compartilhado, sem renomear nem clonar o monólito.

---

### 🚨 O Desafio Técnico / Contexto
O Lorentz Energy é um produto B2B de contas e indicadores tarifários, em PHPMaker, e o novo pedido envolvia dispositivos em campo. Os atalhos eram trocar os rótulos do Energy para Hotel ou clonar o monólito. As duas opções foram rejeitadas e ficaram registradas no desenho.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O Energy segue como produto de contas e KPIs. O núcleo novo é lorentz-iot, com lorentz-hotel como vertical em cima dele.
* 💡 A opção aprovada desenvolve IoT e Hotel em paralelo, com sprints separados.
* 💡 A ponte com o Energy é opcional e fica só para a fase 3, o que mantém os produtos separados até lá.
* 💡 O primeiro teste de campo é uma bomba e uma boia em casa, controladas pelo celular através da VPS, e serve também de vitrine para o eletricista e a diretoria.

---

### 🛠️ Especificação Técnica & Código-Chave


---

### 📈 Impacto no Ecossistema & Valor Prático
Os dois produtos podem evoluir separados e dividir só o que de fato é comum.

* **Projetos Relacionados**: `lorentz-iot`, `lorentz-hotel`, `lorentz-energy`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
