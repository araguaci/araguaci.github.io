---
layout: post
title: "A segunda visita não mostra a landing porque o passo já está gravado no navegador"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-146"
description: "O teste da landing falhou na segunda abertura do mesmo navegador. O app grava o passo inteiro em localStorage, e a landing só existe enquanto o passo ainda é o de boas-vindas."
date: 2026-11-09 00:00:00-03:00
categories: devlog
category: frontend
tags: [react, localstorage, landing, teste]
---

# A segunda visita não mostra a landing porque o passo já está gravado no navegador

> [!NOTE]
> **Resumo Executivo (DEV-2026-146)**: O teste da landing falhou na segunda abertura do mesmo navegador. O app grava o passo inteiro em localStorage, e a landing só existe enquanto o passo ainda é o de boas-vindas.

---

### 🚨 O Desafio Técnico / Contexto
A página principal passou a explicar o projeto antes do fluxo. A primeira visita mostrava a landing e o botão de começar. A abertura seguinte, no mesmo perfil, já estava adiantada no fluxo, e a landing parecia ter sumido.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 A chave rota-mvp-v1 guarda o estado inteiro. load() faz o merge do JSON salvo sobre o estado inicial, e um useEffect grava de novo a cada mudança.
* 💡 A landing só renderiza com state.step igual a welcome. Quem já confirmou o retrato volta em home, no mesmo navegador.
* 💡 Um teste que abre a página duas vezes no mesmo perfil não está vendo a primeira visita. Para fotografar a landing de novo, o teste limpa o localStorage e recarrega.
* 💡 Apagar os dados do site é o caminho da pessoa voltar a ver a landing. Recarregar a página não zera o passo.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
const KEY = "rota-mvp-v1";
function load() {
  const raw = localStorage.getItem(KEY);
  if (!raw) return initial();
  return { ...initial(), ...JSON.parse(raw) };
}
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O teste da primeira visita passou a limpar o armazenamento local, e a volta ao fluxo deixou de ser lida como landing quebrada.

* **Projetos Relacionados**: `ideia`
* **Registro de Origem**: `_data/daily.dev-25.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
