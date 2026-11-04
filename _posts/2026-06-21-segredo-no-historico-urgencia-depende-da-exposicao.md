---
layout: post
title: "Nem todo segredo encontrado no histórico tem a mesma urgência"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-085"
description: "A varredura dos repositórios encontrou credenciais com riscos muito diferentes. A prioridade passou a seguir a exposição real de cada uma, e a rotação ficou à frente da reescrita do histórico."
date: 2026-06-21 00:00:00-03:00
categories: devlog
category: seguranca
tags: [segredos, git, rotacao, filter-repo]
---

# Nem todo segredo encontrado no histórico tem a mesma urgência

> [!NOTE]
> **Resumo Executivo (DEV-2026-085)**: A varredura dos repositórios encontrou credenciais com riscos muito diferentes. A prioridade passou a seguir a exposição real de cada uma, e a rotação ficou à frente da reescrita do histórico.

---

### 🚨 O Desafio Técnico / Contexto
Ao preparar os repositórios para trabalhar com o claude.ai, apareceram credenciais em código e no histórico do Git. Tratar todas igualmente levaria a recompilar componentes legados com pressa, enquanto o risco real estava em outra credencial.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Credencial de banco acessível por IP público é o risco real e vem primeiro. Credencial de banco que só escuta na interface local, em repositório privado, tem urgência menor.
* 💡 Reescrever o histórico não dispensa a rotação: a credencial já esteve em remotos e em outros clones. A rotação é o que neutraliza o risco.
* 💡 Credencial presa em código compilado só muda com nova compilação. A correção de longo prazo é parametrizar, seguindo o padrão de configuração externa.
* 💡 Arquivo de configuração sai do versionamento e dá lugar a um .sample. Antes do git pull no servidor, faça backup do arquivo real, porque a remoção do versionamento pode apagá-lo.

---

### 🛠️ Especificação Técnica & Código-Chave
```bash
# Depois de rotacionar, limpar o histórico é a etapa seguinte, não a primeira
git filter-repo --replace-text expressoes.txt
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A correção foi ordenada pela exposição real, sem expor o legado a uma recompilação apressada.

* **Projetos Relacionados**: `omnichannel`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
