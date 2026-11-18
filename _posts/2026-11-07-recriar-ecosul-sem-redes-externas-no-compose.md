---
layout: post
title: "Recriar o EcoSul sem as redes externas nasce sem Postgres e sem o painel"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-152"
description: "Um docker compose up avulso recriou o EcoSul e ele passou a reiniciar. As redes do Postgres e do IPLive não estavam no arquivo, então o container nascia sem elas."
date: 2026-11-07 00:00:00-03:00
categories: devlog
category: devops
tags: [docker, compose, redes, ecosul]
---

# Recriar o EcoSul sem as redes externas nasce sem Postgres e sem o painel

> [!NOTE]
> **Resumo Executivo (DEV-2026-152)**: Um docker compose up avulso recriou o EcoSul e ele passou a reiniciar. As redes do Postgres e do IPLive não estavam no arquivo, então o container nascia sem elas.

---

### 🚨 O Desafio Técnico / Contexto
Em 2026-11-07, docker compose up -d --no-deps ecosul derrubou o serviço. triade-ecosul-1 precisa de iplive_default e postgresql_default, redes de outros projetos da mesma máquina. Sem elas o processo não alcança o banco nem o iplive-mesa-1.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 docker-compose.triade.yml marca iplive_default e postgresql_default como external: true. O Compose não cria nem remove essas redes.
* 💡 Até o deploy de 2026-11-07 o serviço ecosul não listava as duas redes. A ligação era um docker network connect depois. Qualquer up que recriava o container nascia sem elas.
* 💡 restart: unless-stopped mantém o ciclo. O container sobe, não alcança Postgres nem painel, e o Docker liga de novo.
* 💡 A partir desse deploy o serviço declara default, iplive_default e postgresql_default. docker inspect triade-ecosul-1 no campo NetworkSettings.Networks tem de listar as três.
* 💡 Se a recriação vier de um arquivo antigo, na máquina do serviço: docker network connect postgresql_default triade-ecosul-1 e o mesmo para iplive_default.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
networks:
  - default
  - iplive_default
  - postgresql_default
# no rodapé, sem criar a rede:
# iplive_default:
#   external: true
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Recriar o EcoSul passou a nascer ligado ao Postgres e ao painel, e a checagem das três redes entrou no roteiro de publicação.

* **Projetos Relacionados**: `triade-artesdosul`, `ecosul`
* **Registro de Origem**: `_data/daily.dev-26.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
