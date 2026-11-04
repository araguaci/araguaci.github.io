---
layout: post
title: "Limpar o Visual Studio começa por saber o que cada solução realmente compila"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-095"
description: "Havia gigabytes em cargas do Visual Studio que pareciam dispensáveis, mas o build desktop depende de versões específicas. O levantamento projeto a projeto separou o que pode sair do que precisa ficar."
date: 2026-10-04 00:00:00-03:00
categories: devlog
category: windows
tags: [visual-studio, dotnet, disco, msvc]
---

# Limpar o Visual Studio começa por saber o que cada solução realmente compila

> [!NOTE]
> **Resumo Executivo (DEV-2026-095)**: Havia gigabytes em cargas do Visual Studio que pareciam dispensáveis, mas o build desktop depende de versões específicas. O levantamento projeto a projeto separou o que pode sair do que precisa ficar.

---

### 🚨 O Desafio Técnico / Contexto
O disco estava cheio, e o Painel de Controle não mostra o tamanho real de cada componente. Apagar um SDK errado só apareceria quando o build falhasse.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Meça as pastas. Só UWPNuGetPackages tinha 3,5 GB, e a carga MAUI somava cerca de 1,1 GB no SDK Android e 2,5 GB em packs.
* 💡 Procure a versão nos projetos: o .NET 3.1 não aparecia em server, client nem ura, mas o targeting pack 4.7.2 era usado pelo launcher.
* 💡 O SDK 9 compila projeto net8.0 se o targeting pack 8.0 continuar instalado, então esse pack e o runtime 8.0 ficam na máquina.
* 💡 O attsip fixa PlatformToolset v143 e Windows SDK 10.0.26100. O SDK 10.0.19041 pôde sair, mas esse não.
* 💡 A remoção passa pelo Visual Studio Installer, em Modificar, e não por apagar a pasta na mão.

---

### 🛠️ Especificação Técnica & Código-Chave


---

### 📈 Impacto no Ecossistema & Valor Prático
A limpeza passou a ter uma lista do que sai e do que fica, sem quebrar o build do cliente, do servidor e da URA.

* **Projetos Relacionados**: `lorentz-client`, `lorentz-cti`, `ura`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
