---
layout: post
title: "A folha impressa fica preta no branco porque o tema da tela não entra no papel"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-176"
description: "Ficha, checklist e pagamentos iam para o papel com a cor da tela, inclusive tema escuro. A folha passou a ter estilo próprio, sempre preto no branco, em A4."
date: 2026-11-25 00:00:00-03:00
categories: devlog
category: frontend
tags: [css, impressao, a4, privacidade]
---

# A folha impressa fica preta no branco porque o tema da tela não entra no papel

> [!NOTE]
> **Resumo Executivo (DEV-2026-176)**: Ficha, checklist e pagamentos iam para o papel com a cor da tela, inclusive tema escuro. A folha passou a ter estilo próprio, sempre preto no branco, em A4.

---

### 🚨 O Desafio Técnico / Contexto
O layout da aplicação pinta fundo, texto e barra com o tema da empresa. Na impressão isso gasta tinta, some em tema escuro e ainda manda o botão Imprimir para o papel. A folha também carrega dado de cliente e não pode ser indexada.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 resources/views/layouts/print.blade.php não usa theme.css. O corpo é branco, o texto é preto, a fonte é 10pt Arial. @page declara size A4 portrait e margin 12mm 10mm.
* 💡 No @media print, .print-actions some e .sheet fica com overflow visible. Fora da impressão a tabela pode rolar; no papel ela não pode ser cortada por uma barra.
* 💡 thead usa display table-header-group, para o cabeçalho repetir na página seguinte. tr usa break-inside avoid. .section + .section usa break-before page.
* 💡 A página manda meta robots noindex. O rodapé avisa que a folha tem dado pessoal. O botão Imprimir chama window.print() e não entra no papel.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
@page { size: A4 portrait; margin: 12mm 10mm; }
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A folha sai legível em qualquer tema da tela, e o botão de imprimir não vai para o papel.

* **Projetos Relacionados**: `monitoramento-app`
* **Registro de Origem**: `_data/daily.dev-33.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
