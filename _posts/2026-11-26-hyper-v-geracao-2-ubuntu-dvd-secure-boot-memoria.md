---
layout: post
title: "VM Ubuntu no Hyper-V: DVD que não existe, Secure Boot e memória dinâmica"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-185"
description: "A primeira VM de laboratório não deu boot e depois enxergava só 1,8 GB. Geração 2 nasce sem unidade de DVD, o Ubuntu precisa de outro modelo de Secure Boot, e memória dinâmica engana o SQL Server em container."
date: 2026-11-26 00:00:00-03:00
categories: devlog
category: infraestrutura
tags: [hyper-v, ubuntu, powershell, homelab]
---

# VM Ubuntu no Hyper-V: DVD que não existe, Secure Boot e memória dinâmica

> [!NOTE]
> **Resumo Executivo (DEV-2026-185)**: A primeira VM de laboratório não deu boot e depois enxergava só 1,8 GB. Geração 2 nasce sem unidade de DVD, o Ubuntu precisa de outro modelo de Secure Boot, e memória dinâmica engana o SQL Server em container.

---

### 🚨 O Desafio Técnico / Contexto
O script de criação usava Set-VMDvdDrive, que só configura uma unidade existente. A VM de Geração 2 não tem DVD por padrão, e o boot caiu em "No operating system was loaded" com só rede e disco na lista. Corrigido o boot, o Ubuntu viu 1,8 GB de memória, porque a memória dinâmica começa pequena, e o SQL Server em container recusa subir abaixo de 2 GB. O instalador do Ubuntu ainda deixou metade do disco fora do LVM, e o console do Hyper-V usa teclado americano.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Geração 2: Add-VMDvdDrive com a ISO e Set-VMFirmware com o DVD como primeiro boot. Para Linux, Secure Boot com o modelo MicrosoftUEFICertificateAuthority.
* 💡 Para serviço que confere a memória ao subir, memória fixa. No host de 15,4 GB, a VM foi de 8 para 6 GB fixos e o host saiu de 1,4 para 3,4 GB livres.
* 💡 O Ubuntu Server usa metade do disco no LVM: lvextend -r -l +100%FREE. No console americano, o / de um teclado ABNT2 sai na tecla ;.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
Add-VMDvdDrive -VMName Lab -Path C:\iso\ubuntu-22.04.5-live-server-amd64.iso
Set-VMFirmware -VMName Lab -SecureBootTemplate MicrosoftUEFICertificateAuthority `
  -FirstBootDevice (Get-VMDvdDrive -VMName Lab)
Set-VMMemory -VMName Lab -DynamicMemoryEnabled $false -StartupBytes 6GB
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O roteiro de criação da VM passou a funcionar sem ajuste manual e ficou registrado para o suporte repetir em campo.

* **Projetos Relacionados**: `lorentz-vps-stack`
* **Registro de Origem**: `_data/daily.dev-34.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
