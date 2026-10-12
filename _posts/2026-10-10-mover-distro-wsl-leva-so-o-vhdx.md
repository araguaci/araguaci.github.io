---
layout: post
title: "Mover distro WSL leva o vhdx e deixa o resto da pasta"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-073"
description: "wsl --manage --move troca o lugar do ext4.vhdx e o BasePath do registro. Arquivos irmãos da pasta antiga não entram nessa operação."
date: 2026-10-10 00:00:00+00:00
categories: devlog
category: windows
tags: [wsl, vhdx, disco]
---

# Mover distro WSL leva o vhdx e deixa o resto da pasta

> [!NOTE]
> **Resumo Executivo (DEV-2026-073)**: wsl --manage --move troca o lugar do ext4.vhdx e o BasePath do registro. Arquivos irmãos da pasta antiga não entram nessa operação.

---

### 🚨 O Desafio Técnico / Contexto
Uma distro WSL2 parada ocupava outro volume. O disco virtual precisava ir para o volume de trabalho sem exportar e reimportar. Na pasta de origem havia também o tar de instalação, um executável e scripts.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 wsl --terminate e depois wsl --manage NOME --move CAMINHO movem o ext4.vhdx. A distro precisa estar parada. O registro BasePath passa a apontar para o caminho novo.
* 💡 O comando não move tar, executável nem script que estejam ao lado do vhdx. Esses arquivos pedem uma cópia à parte, senão a pasta fica partida entre os dois volumes.
* 💡 Antes de apagar a origem, o BasePath e um boot com cat /etc/os-release têm de concordar com o disco novo.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
wsl --terminate NOME
wsl --manage NOME --move D:\destino\NOME
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A distro sobe a partir do volume novo, com o mesmo nome, sem passar por export e import.

* **Projetos Relacionados**: `raspios-wsl`
* **Registro de Origem**: `_data/daily.dev-11.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
