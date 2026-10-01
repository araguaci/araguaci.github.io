---
layout: post
title: "Mojibake no Windows: UTF-8 lido como CP850 e gravado de novo"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-037"
description: "Documentos do laboratório apareceram com caixas no lugar de acentos porque um editor abriu UTF-8 na página OEM do console e salvou por cima."
date: 2026-08-04 00:00:00+00:00
categories: devlog
category: devops
tags: [utf-8, windows, encoding, git]
---

# Mojibake no Windows: UTF-8 lido como CP850 e gravado de novo

> [!NOTE]
> **Resumo Executivo (DEV-2026-037)**: Documentos do laboratório apareceram com caixas no lugar de acentos porque um editor abriu UTF-8 na página OEM do console e salvou por cima.

---

### 🚨 O Desafio Técnico / Contexto
'ó' virou a sequência ├│ e o travessão virou ÔÇö. O clone git estava correto. A cópia local é que foi regravada com a code page errada.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O desenho ├│ ou ÔÇö é UTF-8 interpretado como CP850 e salvo de novo. Não é corrupção do remote.
* 💡 git checkout do arquivo original recupera o texto quando o commit ainda está limpo.
* 💡 Zip, RAR e editores presos na página OEM do Windows são a origem típica. O pull não é.

---

### 🛠️ Especificação Técnica & Código-Chave
```python
def looks_like_cp850_mojibake(text):
    markers = ("├", "ÔÇ", "Ã§", "Ã£")
    return any(mark in text for mark in markers)

# Recuperar: ler os bytes do arquivo como CP850 e gravar UTF-8 sem BOM.
# Se o commit git estiver íntegro, git checkout -- arquivo.md é o caminho curto.
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Notas de campo em português deixam de ser regravadas com acento destruído.

* **Projetos Relacionados**: `omnichannel`, `_lab`
* **Registro de Origem**: `_data/daily.dev-03.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
