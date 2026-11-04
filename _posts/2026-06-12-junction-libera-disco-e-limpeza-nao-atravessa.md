---
layout: post
title: "Junction libera o disco C: sem mudar o caminho, e a limpeza não pode atravessá-la"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-081"
description: "O C: chegou a 7,4 GB livres, com caches e a VM do Claude Desktop ocupando a maior parte. Mover a VM por junction resolveu na hora, e a limpeza recorrente virou um script com dry-run e lista de caminhos permitidos."
date: 2026-06-12 00:00:00-03:00
categories: devlog
category: windows
tags: [windows, junction, disco, powershell, manutencao]
---

# Junction libera o disco C: sem mudar o caminho, e a limpeza não pode atravessá-la

> [!NOTE]
> **Resumo Executivo (DEV-2026-081)**: O C: chegou a 7,4 GB livres, com caches e a VM do Claude Desktop ocupando a maior parte. Mover a VM por junction resolveu na hora, e a limpeza recorrente virou um script com dry-run e lista de caminhos permitidos.

---

### 🚨 O Desafio Técnico / Contexto
A pasta vm_bundles do Claude Desktop ocupava 11,8 GB, e os caches de NuGet, npm e pip somavam cerca de 34 GB. O app espera a pasta no caminho original, e o disco volta a encher com o uso normal de desenvolvimento.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Mover a pasta para outro disco e criar uma junction no caminho original mantém o app funcionando sem configuração nova.
* 💡 A junction cria uma dependência: se o app acusar erro de VM, confira primeiro se o disco de destino está montado e se a junction continua intacta.
* 💡 O CleanGuard só apaga com -Executar. Sem esse parâmetro, faz apenas o dry-run.
* 💡 A lista de raízes permitidas fica no código, e o script recusa qualquer caminho fora dela. Também nunca atravessa junction ou symlink, o que protege a própria pasta migrada.
* 💡 A tarefa agendada de toda segunda roda o perfil seguro, sem administrador. O perfil completo, com Temp do sistema, Windows Update e WinSxS, fica para execução manual.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
# Sem -Executar, só mostra o que seria apagado
.\cleanguard.ps1
.\cleanguard.ps1 -Executar
.\cleanguard.ps1 -Executar -Perfil completo
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O espaço do C: passou a ser recuperado por rotina semanal, sem limpeza manual a cada aperto.

* **Projetos Relacionados**: `00-cleanguard`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
