---
layout: post
title: "Abas da Base Histórica sem Bootstrap e o INI ao lado do executável"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-043"
description: "A tela de arquivamento abria em branco porque as abas dependiam de JavaScript do Bootstrap que a página não carregava. O worker .NET lia o INI em Arquivos de Programas em vez da pasta do executável."
date: 2026-07-12 00:00:00+00:00
categories: devlog
category: backend
tags: [php, jquery, dotnet, sql-server]
---

# Abas da Base Histórica sem Bootstrap e o INI ao lado do executável

> [!NOTE]
> **Resumo Executivo (DEV-2026-043)**: A tela de arquivamento abria em branco porque as abas dependiam de JavaScript do Bootstrap que a página não carregava. O worker .NET lia o INI em Arquivos de Programas em vez da pasta do executável.

---

### 🚨 O Desafio Técnico / Contexto
A troca de aba chamava o plugin do Bootstrap. Nessa tela o bundle não estava presente, então o conteúdo não aparecia. No serviço, a configuração de laboratório ao lado do .exe era ignorada e o processo seguia um INI de instalação antigo.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Troca de aba em jQuery puro não depende do Bootstrap da página legada.
* 💡 A busca do INI começa no diretório do executável e só depois olha Arquivos de Programas.
* 💡 A chave da API no PHP e no worker é a mesma constante renderizada pelo stack. Valor divergente parece serviço fora do ar.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
// Abas sem Bootstrap JS
document.querySelectorAll('[data-tab]').forEach(function (btn) {
  btn.addEventListener('click', function () {
    var id = btn.getAttribute('data-tab');
    document.querySelectorAll('.tab-pane').forEach(function (pane) {
      pane.hidden = pane.id !== id;
    });
  });
});

// Ordem do INI no worker: pasta do exe, depois Program Files
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A manutenção de arquivamento volta a mostrar as abas e o worker de laboratório lê o INI que está junto do binário.

* **Projetos Relacionados**: `supervisor`, `omnichannel`, `lorentz-vps-stack`
* **Registro de Origem**: `_data/daily.dev-03.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
