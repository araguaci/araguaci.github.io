---
layout: post
title: "Dump do Postgres 17 não entra numa imagem 16, e o formato muda o comando"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-050"
description: "O restore escolhe pg_restore ou psql pelos cinco primeiros bytes do arquivo. Dump feito no Postgres 17 só restaura em postgres:17-alpine."
date: 2026-08-14 00:00:00+00:00
categories: devlog
category: devops
tags: [postgres, docker, pg_restore, backup]
---

# Dump do Postgres 17 não entra numa imagem 16, e o formato muda o comando

> [!NOTE]
> **Resumo Executivo (DEV-2026-050)**: O restore escolhe pg_restore ou psql pelos cinco primeiros bytes do arquivo. Dump feito no Postgres 17 só restaura em postgres:17-alpine.

---

### 🚨 O Desafio Técnico / Contexto
pg_restore respondia unsupported version (1.16) quando a imagem era 16. Arquivo SQL plain no pg_restore, ou dump custom no psql, falhava do mesmo jeito.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 migrate-saude-livre-ainativo.sh lê 5 bytes. PGDMP chama pg_restore; o resto vai ao psql.
* 💡 unsupported version (1.16) é dump do PostgreSQL 17. O serviço db precisa de postgres:17-alpine.
* 💡 POSTGRES_PASSWORD no compose não altera cluster já inicializado. A troca é ALTER USER no volume existente.
* 💡 O tar de upload com uma pasta raiz única recebe --strip-components=1. Sem isso o arquivo fica um nível abaixo.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
# tools/scripts/migrate-saude-livre-ainativo.sh
[ "$(head -c 5 "$file")" = "PGDMP" ] && pg_restore ... || psql ...
# unsupported version (1.16) → postgres:17-alpine
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O restore passou a detectar formato e versão antes de aplicar o dump no volume.

* **Projetos Relacionados**: `sio-ecosystem`
* **Registro de Origem**: `_data/daily.dev-04.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
