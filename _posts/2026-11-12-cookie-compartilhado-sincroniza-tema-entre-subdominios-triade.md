---
layout: post
title: "Cookie compartilhado no domínio pai sincroniza tema e modo escuro entre subdomínios da Tríade"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-155"
description: "O ProntOS e o Agenda rodam em repositórios e containers separados, mas passaram a compartilhar a mesma identidade visual e escolha de tema do usuário. O cookie triade_theme no domínio pai .artesdosul.com sincroniza seis paletas e o modo claro ou escuro entre subdomínios."
date: 2026-11-12 00:00:00-03:00
categories: devlog
category: arquitetura
tags: [css-variables, tailwind, multi-app, design-system, cookies]
---

# Cookie compartilhado no domínio pai sincroniza tema e modo escuro entre subdomínios da Tríade

> [!NOTE]
> **Resumo Executivo (DEV-2026-155)**: O ProntOS e o Agenda rodam em repositórios e containers separados, mas passaram a compartilhar a mesma identidade visual e escolha de tema do usuário. O cookie triade_theme no domínio pai .artesdosul.com sincroniza seis paletas e o modo claro ou escuro entre subdomínios.

---

### 🚨 O Desafio Técnico / Contexto
Em 2026-11-12, o ProntOS precisava incorporar o Design System e o seletor de temas do agenda.artesdosul.com mantendo a preferência visual do usuário ao navegar entre os aplicativos do ecossistema.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Em frontend/src/lib/triadeTheme.ts, gravar o cookie triade_theme=<theme>:<mode> com Domain=.artesdosul.com; Path=/; SameSite=Lax permite que qualquer subdomínio leia a paleta escolhida na primeira renderização.
* 💡 Aplicar data-triade-theme e data-triade-mode no document.documentElement junto com variáveis CSS (--tr-blue-50..950, --tr-gray-50..950 e --tr-sgray-50..950) mapeadas no tailwind.config.js troca toda a paleta e o modo escuro sem recarregar a página.
* 💡 A sincronização em dois sentidos (cookie compartilhado para outros subdomínios e localStorage para ambiente local em localhost) garante o mesmo funcionamento em desenvolvimento e em produção.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
document.cookie = `triade_theme=${encodeURIComponent(`${theme}:${mode}`)}; Max-Age=31536000; Path=/; SameSite=Lax; Domain=.artesdosul.com; Secure`;
document.documentElement.setAttribute('data-triade-theme', theme);
document.documentElement.setAttribute('data-triade-mode', mode);
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Trocar o tema ou o modo escuro no ProntOS reflete automaticamente no Agenda e nos demais sistemas da Tríade sob o mesmo domínio.

* **Projetos Relacionados**: `30-FieldFlow`, `triade-artesdosul`
* **Registro de Origem**: `_data/daily.dev-27.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
