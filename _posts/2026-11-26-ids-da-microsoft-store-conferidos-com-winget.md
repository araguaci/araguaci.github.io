---
layout: post
title: "IDs da Microsoft Store mudam e só valem depois de conferidos com winget na máquina real"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-163"
description: "O catálogo de limpeza usava IDs da Store para reinstalar apps removidos, e três deles não existiam mais. A verificação com winget show --source msstore no Windows 25H2 real passou a ser um teste do projeto, e apps sem ID válido deixaram de ser recomendados para remoção."
date: 2026-11-26 00:00:00-03:00
categories: devlog
category: windows
tags: [winget, msstore, appx, windows-11, debloat]
---

# IDs da Microsoft Store mudam e só valem depois de conferidos com winget na máquina real

> [!NOTE]
> **Resumo Executivo (DEV-2026-163)**: O catálogo de limpeza usava IDs da Store para reinstalar apps removidos, e três deles não existiam mais. A verificação com winget show --source msstore no Windows 25H2 real passou a ser um teste do projeto, e apps sem ID válido deixaram de ser recomendados para remoção.

---

### 🚨 O Desafio Técnico / Contexto
Remove-AppxPackage tira o app do usuário, e a volta depende de o pacote ainda estar em disco (Add-AppxPackage -Register no AppxManifest.xml) ou de reinstalar pela Store. Dos 18 IDs escritos de memória, os de Paciência (Solitaire), Dicas e Mapas não foram encontrados pelo winget no msstore. Remover a Paciência sem ID válido tornaria a ação sem volta garantida.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 winget show --id ID --source msstore --accept-source-agreements responde se o ID existe hoje. Rode isso para cada ID antes de prometer reversão.
* 💡 A reversão de um Appx tenta primeiro re-registrar pelo manifesto em InstallLocation, que sobrevive enquanto outro usuário ainda tiver o pacote, e só depois usa winget install.
* 💡 Um app instalado cujo ID da Store não existe sai da lista de recomendados e ganha aviso explícito na tela de plano.
* 💡 No 25H2 apareceram pacotes que o catálogo não previa (Microsoft.XboxGameCallableUI, Microsoft.WidgetsPlatformRuntime). Widgets se desliga melhor pela política AllowNewsAndInterests=0 em HKLM\SOFTWARE\Policies\Microsoft\Dsh do que removendo pacote.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
foreach ($id in '9MV0B5HZVK9Z','9NZKPSTSNW4P','9WZDNCRFHWD2') {
  winget show --id $id --source msstore --accept-source-agreements *> $null
  "{0}: {1}" -f $id, ($(if ($LASTEXITCODE -eq 0) {'ok'} else {'NÃO ENCONTRADO'}))
}
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Os 15 IDs que ficaram no catálogo foram confirmados na máquina real, e nenhum app recomendado para remoção fica sem caminho de volta.

* **Projetos Relacionados**: `labmini`
* **Registro de Origem**: `_data/daily.dev-30.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
