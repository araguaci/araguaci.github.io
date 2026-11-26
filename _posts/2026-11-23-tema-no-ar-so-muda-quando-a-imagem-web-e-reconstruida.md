---
layout: post
title: "Tema corrigido no laptop não chega ao cockpit enquanto a imagem web não é reconstruída"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-168"
description: "Os cockpits no ar continuaram com o tema antigo depois da correção no repositório local. A imagem web copia o ui-cockpit na hora do build, então o bundle só muda quando esse serviço é reconstruído."
date: 2026-11-23 00:00:00-03:00
categories: devlog
category: devops
tags: [docker, frontend, deploy]
---

# Tema corrigido no laptop não chega ao cockpit enquanto a imagem web não é reconstruída

> [!NOTE]
> **Resumo Executivo (DEV-2026-168)**: Os cockpits no ar continuaram com o tema antigo depois da correção no repositório local. A imagem web copia o ui-cockpit na hora do build, então o bundle só muda quando esse serviço é reconstruído.

---

### 🚨 O Desafio Técnico / Contexto
Os cinco cockpits publicados seguiam com o catálogo antigo. O clone que o Compose usa no build estava num commit anterior, e a correção ainda não estava nesse clone. O Dockerfile do frontend faz COPY --from=uicockpit do pacote @ainativo/ui-cockpit. O arquivo novo no laptop não entra na imagem que já está servida.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O frontend publicado é a imagem, não o working tree. Sem reconstruir o serviço web, o bundle continua com o catálogo que foi copiado no build anterior.
* 💡 O comando é docker compose up -d --no-deps --build web, no diretório do produto. Não se faz source do .env e não se usa compose down -v.
* 💡 A prova é o JavaScript servido. Depois do rebuild, o bundle passou a conter o nome autoral novo do tema. O navegador só larga o arquivo antigo com atualização forçada.

---

### 🛠️ Especificação Técnica & Código-Chave
```bash
docker compose up -d --no-deps --build web
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Os cinco cockpits passaram a entregar o catálogo corrigido, conferido pelo nome novo dentro do bundle.

* **Projetos Relacionados**: `sio-ecosystem`
* **Registro de Origem**: `_data/daily.dev-31.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
