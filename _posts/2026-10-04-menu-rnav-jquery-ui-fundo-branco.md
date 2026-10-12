---
layout: post
title: "A lista da direita do Issabel some no fundo branco do jQuery UI"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-065"
description: "O menu .rnav herdava background white do jQuery UI enquanto o tema pintava o link com cor clara. A regra que escurecia o painel do operador não alcançava esse menu."
date: 2026-10-04 00:00:00+00:00
categories: devlog
category: frontend
tags: [css, jquery, issabel, tema]
---

# A lista da direita do Issabel some no fundo branco do jQuery UI

> [!NOTE]
> **Resumo Executivo (DEV-2026-065)**: O menu .rnav herdava background white do jQuery UI enquanto o tema pintava o link com cor clara. A regra que escurecia o painel do operador não alcançava esse menu.

---

### 🚨 O Desafio Técnico / Contexto
Os itens do ul da sidebar direita deixavam de ser lidos na tela de extensões. O inspetor mostrava .rnav .ui-widget-content e ul.ui-menu.ui-widget.ui-widget-content com background white. O miolo do painel de operador também ficava branco, vindo do body em neon-core.css. apachectl graceful dentro do container falhava ao procurar o D-Bus.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O jQuery UI em libs/js/jquery/css define .ui-widget-content com background white. O tema usa cor clara em body a, então o texto do .rnav some no branco.
* 💡 .neo-module-content .ui-widget-content escurece o miolo do módulo e também qualquer widget dentro dele. O .rnav pode ficar fora desse seletor, e a especificidade de .ui-menu.ui-widget.ui-widget-content mantém o branco.
* 💡 A correção é regra própria em .rnav, .rnav .ui-widget-content e .rnav .ui-menu, com fundo da superfície escura e texto primário, inclusive no item ativo.
* 💡 neon-core.css ainda declara body com background #ffffff. Sem cobertura no módulo, o canvas do painel de operador volta ao branco.
* 💡 No container, apachectl graceful falha com Failed to get D-Bus connection. httpd -k graceful recarrega o Apache.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
.rnav,
.rnav .ui-widget-content,
.rnav .ui-menu.ui-widget-content {
  background: var(--lo-surface-2) !important;
  color: var(--lo-text-primary) !important;
}
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A lista de ramais da direita volta a ser legível no tema escuro, sem desfazer o fundo do painel de operador.

* **Projetos Relacionados**: `lorentz-vps-stack`
* **Registro de Origem**: `_data/daily.dev-08.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
