---
layout: post
title: "Ler WSL e Hyper-V sem depender do idioma do Windows"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-161"
description: "Um painel que interpretava a saída de wsl --list --verbose e o JSON do Get-VM quebrava num Windows em pt-BR. A lista de distros passou a vir do registro Lxss mais wsl --list --running --quiet, e o estado da VM passou a vir de .ToString() do enum."
date: 2026-11-26 00:00:00-03:00
categories: devlog
category: windows
tags: [wsl, hyper-v, powershell, utf-16, i18n]
---

# Ler WSL e Hyper-V sem depender do idioma do Windows

> [!NOTE]
> **Resumo Executivo (DEV-2026-161)**: Um painel que interpretava a saída de wsl --list --verbose e o JSON do Get-VM quebrava num Windows em pt-BR. A lista de distros passou a vir do registro Lxss mais wsl --list --running --quiet, e o estado da VM passou a vir de .ToString() do enum.

---

### 🚨 O Desafio Técnico / Contexto
Numa máquina Windows 11 25H2 em pt-BR, o cabeçalho e os estados de wsl --list --verbose vêm traduzidos ("NOME", "Em execução", "Parado"), e a saída do wsl.exe sai em UTF-16LE, às vezes sem BOM e com NULs soltos. No Hyper-V, Get-VM | ConvertTo-Json grava State como número (2, 3, 6), e ConvertTo-Json devolve objeto solto quando há um único item e nada quando não há itens. Quando não há distro rodando, wsl --list --running sai com código diferente de zero.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 A lista de distros, a versão (1 ou 2) e a distro padrão estão em HKCU:\Software\Microsoft\Windows\CurrentVersion\Lxss (DistributionName, Version, DefaultDistribution), que não é traduzido.
* 💡 wsl.exe --list --running --quiet devolve só nomes. Decodifique como UTF-16LE detectando BOM ou bytes nulos nas posições ímpares, e trate código diferente de zero com o WSL instalado como 'nenhuma em execução'.
* 💡 No PowerShell, $_.State.ToString() devolve o nome invariável do enum (Running, Off, Saved). ConvertTo-Json sozinho grava o número.
* 💡 ConvertTo-Json -InputObject @($lista) garante array mesmo com zero ou um item. Sem isso, o parser recebe objeto, null ou vazio.
* 💡 O WSL instalado pela Store usa só o serviço WSLService. LxssManager não existe no 25H2, então o detector precisa aceitar a ausência dele.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
$root = 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Lxss'
$items = Get-ChildItem $root | ForEach-Object {
  $p = Get-ItemProperty $_.PSPath
  [pscustomobject]@{ name = $p.DistributionName; version = [int]$p.Version }
}
ConvertTo-Json -InputObject @($items) -Compress
Get-VM | ForEach-Object { [pscustomobject]@{ name = $_.Name; state = $_.State.ToString() } }
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O mesmo código lê WSL e Hyper-V em qualquer idioma do Windows e passou nos testes ao vivo numa máquina pt-BR com 5 distros.

* **Projetos Relacionados**: `labmini`
* **Registro de Origem**: `_data/daily.dev-30.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
