---
layout: post
title: "Pipeline Unificado de Currículo Soberano: De YAML Único para JSON Resume, Markdown e PDF"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-023"
description: "Automação editorial baseada em Single Source of Truth que compila dados profissionais em JSON Schema internacional, Markdown para GitHub e PDF de alta precisão."
date: 2026-09-24 00:00:00+00:00
categories: devlog
category: devops
tags: [json-resume, yaml, python, weasyprint, automacao, cv]
---

# Pipeline Unificado de Currículo Soberano: De YAML Único para JSON Resume, Markdown e PDF

> [!NOTE]
> **Resumo Executivo (DEV-2026-023)**: Automação editorial baseada em Single Source of Truth que compila dados profissionais em JSON Schema internacional, Markdown para GitHub e PDF de alta precisão.

---

### 🚨 O Desafio Técnico / Contexto
A manutenção manual de currículo e portfólio contendo 30+ anos de experiência e 56 projetos em diversas plataformas causava dispersão de dados, erros de datas e trabalho duplicado.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O formato resume.yml como fonte única de verdade centraliza competências, histórico de empresas e publicações, desacoplando o conteúdo da apresentação.
* 💡 A conformidade estrita com o padrão JSON Resume permite integração instantânea com motores de busca e analisadores de recrutamento (ATS).
* 💡 A geração headless de PDF via HTML5 com regras de CSS Paged Media (@page { size: A4; margin: 15mm; }) garante paginação perfeita sem cortes em blocos de texto.

---

### 🛠️ Especificação Técnica & Código-Chave
```python
# Script de orquestração de formatos de currículo
import yaml, json, subprocess

def sync_resume_ecosystem():
    with open('_data/resume.yml', 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    with open('_data/resume.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    # Compilação para PDF via Chrome Headless
    subprocess.run(['pwsh', '-Command', 'node scripts/render_pdf.js'])
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Atualização de portfólio e currículo em múltiplos formatos em menos de 5 segundos a partir de um único commit.

* **Projetos Relacionados**: `artesdosul.com/curriculo`, `araguaci.github.io`
* **Registro de Origem**: `_data/daily.dev-02.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
