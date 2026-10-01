---
layout: post
title: "403 no Operador Web e o erro 130 do React por export que faltava"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-041"
description: "O softphone WebRTC entrou no Supervisor no lugar do cliente analógico. O Apache devolvia 403 na pasta e o bundle React quebrava ao importar a tela de login."
date: 2026-07-15 00:00:00+00:00
categories: devlog
category: frontend
tags: [apache, react, webrtc, webphone, php]
---

# 403 no Operador Web e o erro 130 do React por export que faltava

> [!NOTE]
> **Resumo Executivo (DEV-2026-041)**: O softphone WebRTC entrou no Supervisor no lugar do cliente analógico. O Apache devolvia 403 na pasta e o bundle React quebrava ao importar a tela de login.

---

### 🚨 O Desafio Técnico / Contexto
Sem DirectoryIndex, Options -Indexes responde 403 em vez de abrir index.php. A tela de login era importada do barrel de componentes, mas esse arquivo não a reexportava. O React 130 avisa que o tipo do elemento é inválido: o import veio undefined.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Options -Indexes sem DirectoryIndex index.php esconde a aplicação atrás de um 403.
* 💡 O cliente legado foi renomeado para cli_analogico para as duas URLs não disputarem a mesma pasta.
* 💡 O barrel precisa reexportar o componente que outras telas importam desse arquivo.
* 💡 O placeholder da porta do webphone no att_config tem que ser trocado no render. Se sobrar o token, o embed aponta para um host literal.

---

### 🛠️ Especificação Técnica & Código-Chave
```apache
# supervisor/cliente/.htaccess
DirectoryIndex index.php
Options -Indexes +FollowSymLinks

# Barrel: quem importa da pasta precisa receber o componente
export { LorentzLoginScreen } from './LorentzLoginScreen';
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O operador abre o webphone dentro do Supervisor, com a pasta servindo index.php e o login montando de fato.

* **Projetos Relacionados**: `supervisor`, `lorentz-webphone`, `lorentz-vps-stack`
* **Registro de Origem**: `_data/daily.dev-03.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
