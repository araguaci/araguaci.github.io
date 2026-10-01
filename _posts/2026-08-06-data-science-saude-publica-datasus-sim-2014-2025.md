---
layout: post
title: "Data Science em Saúde Pública: Mineração de Séries Históricas DATASUS (SIM) 2014–2025"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-011"
description: "Extração, normalização e identificação visual de anomalias epidemiológicas em milhões de registros oficiais de óbito do Brasil."
date: 2026-08-06 00:00:00+00:00
categories: devlog
category: datascience
tags: [datasus, estatistica, epidemiologia, python, recharts]
---

# Data Science em Saúde Pública: Mineração de Séries Históricas DATASUS (SIM) 2014–2025

> [!NOTE]
> **Resumo Executivo (DEV-2026-011)**: Extração, normalização e identificação visual de anomalias epidemiológicas em milhões de registros oficiais de óbito do Brasil.

---

### 🚨 O Desafio Técnico / Contexto
Os microdados de mortalidade do Ministério da Saúde são distribuídos em formatos proprietários compactados (arquivos DBC), exigindo descompressão especializada e limpeza de inconsistências cadastrais.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 A conversão automatizada de arquivos DBC via 'blast-dbf' em Python permite a ingestão contínua de registros do TABNET.
* 💡 O cálculo de excesso de mortalidade exige padronização por pirâmide etária para evitar viés de envelhecimento populacional.
* 💡 O cruzamento temporal com o Portal da Transparência do Registro Civil permite detectar atrasos e retenções de dados oficiais.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
# Normalização de CID-10 para anomalias cardiovasculares
import pandas as pd
def filtrar_anomalias(df):
    # I21: Infarto agudo, I40-I42: Miocardites/Cardiomiopatias
    mask = df['CAUSABAS'].str.startswith(('I21', 'I40', 'I42'))
    return df[mask].groupby(['ANO', 'MES']).size().reset_index(name='OBITOS')

```

---

### 📈 Impacto no Ecossistema & Valor Prático
Observatório independente de vigilância epidemiológica acessível sem filtros ideológicos (Série Demográfica).

* **Projetos Relacionados**: `serie-demografica.vercel.app`, `selva.artesdosul.com`
* **Registro de Origem**: `_data/daily.dev-01.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
