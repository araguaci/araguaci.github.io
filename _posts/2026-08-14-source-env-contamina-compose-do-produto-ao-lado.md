---
layout: post
title: "O shell com source no .env mistura o produto ao lado"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-049"
description: "Cada stack lê o .env da própria pasta. Exportar esse arquivo no shell deixa SLUG e usuário de banco valendo para o compose seguinte."
date: 2026-08-14 00:00:00+00:00
categories: devlog
category: devops
tags: [docker, compose, env, vps]
---

# O shell com source no .env mistura o produto ao lado

> [!NOTE]
> **Resumo Executivo (DEV-2026-049)**: Cada stack lê o .env da própria pasta. Exportar esse arquivo no shell deixa SLUG e usuário de banco valendo para o compose seguinte.

---

### 🚨 O Desafio Técnico / Contexto
O deploy dava source .env antes do docker compose. SLUG_API e DB_USER ficavam no shell e o produto seguinte herdava label do proxy e URL de banco do stack anterior.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O Compose lê o .env do diretório do comando. Não é preciso exportar o arquivo no shell.
* 💡 SLUG_API e DB_USER exportados sobrevivem ao cd e contaminam o próximo produto.
* 💡 docker compose down -v apaga o volume nomeado. Recriar serviço é up -d --no-deps, sem -v.

---

### 🛠️ Especificação Técnica & Código-Chave
```bash
# No diretório do produto. O Compose lê o .env da pasta.
docker compose up -d --build
# não: source .env
# não: docker compose down -v
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Subir um produto deixou de reescrever host e banco do stack que estava no shell.

* **Projetos Relacionados**: `sio-ecosystem`
* **Registro de Origem**: `_data/daily.dev-04.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
