---
layout: post
title: "Preferências de interface por usuário e trilha de navegação com prazo"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-034"
description: "Navbar, tamanho de ícone, layout dos módulos e favoritos passaram a viver no usuário. A trilha de navegação só grava quando o opt-in está ligado e é podada aos 90 dias."
date: 2026-09-19 00:00:00+00:00
categories: devlog
category: frontend
tags: [laravel, lgpd, ui, scheduler, mysql]
---

# Preferências de interface por usuário e trilha de navegação com prazo

> [!NOTE]
> **Resumo Executivo (DEV-2026-034)**: Navbar, tamanho de ícone, layout dos módulos e favoritos passaram a viver no usuário. A trilha de navegação só grava quando o opt-in está ligado e é podada aos 90 dias.

---

### 🚨 O Desafio Técnico / Contexto
A aparência era global e não servia operadores diferentes. Guardar cada clique por padrão também inchava a base e conflitava com o mínimo necessário da LGPD.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 A coluna users.ui_preferences guarda o shell de cada pessoa. A ordem de categorias da instalação fica em outra tabela.
* 💡 O middleware de navegação só escreve com opt-in. O comando navigation-logs:prune --days=90 limita a retenção.
* 💡 Na VPS o agendador precisa de um serviço próprio (php artisan schedule:work). Sem esse container a poda não roda.

---

### 🛠️ Especificação Técnica & Código-Chave
```bash
# Retenção da trilha de navegação (opt-in)
php artisan navigation-logs:prune --days=90

# Compose da VPS: serviço que mantém o scheduler vivo
# omnichannel_scheduler: php artisan schedule:work
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Cada operador guarda o próprio shell e a trilha de uso deixa de crescer sem prazo.

* **Projetos Relacionados**: `omnichannel-system`
* **Registro de Origem**: `_data/daily.dev-03.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
