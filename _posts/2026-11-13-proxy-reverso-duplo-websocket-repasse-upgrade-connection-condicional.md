---
layout: post
title: "Proxy reverso duplo para WebSocket exige repasse de Upgrade e Connection condicional em todas as camadas"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-159"
description: "Conexões Socket.IO da Evolution API falhavam com 404 e erro de WebSocket ao atravessar o Nginx do host e o Nginx em container. Adicionar headers de Upgrade com mapeamento condicional de Connection em ambas as camadas garantiu o handshake bidirecional."
date: 2026-11-13 00:00:00-03:00
categories: devlog
category: devops
tags: [nginx, websocket, socket-io, evolution-api, proxy-pass, docker]
---

# Proxy reverso duplo para WebSocket exige repasse de Upgrade e Connection condicional em todas as camadas

> [!NOTE]
> **Resumo Executivo (DEV-2026-159)**: Conexões Socket.IO da Evolution API falhavam com 404 e erro de WebSocket ao atravessar o Nginx do host e o Nginx em container. Adicionar headers de Upgrade com mapeamento condicional de Connection em ambas as camadas garantiu o handshake bidirecional.

---

### 🚨 O Desafio Técnico / Contexto
Em 2026-11-13, o frontend do Evolution Manager (evolution.artesdosul.com) apresentava falhas contínuas de 'WebSocket connection failed' e erro 404 em /socket.io/?EIO=4&transport=websocket. A requisição chegava pela porta 443 do Nginx do host, passava por proxy_pass para o container orcamento_nginx (porta 8443) e depois seguia para o container evolution_api:8080. Como o Nginx do host não possuía proxy_set_header Upgrade $http_upgrade e Connection, o cabeçalho era descartado na primeira camada, impedindo a negociação HTTP 101.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Em arquiteturas com Nginx no host roteando para Nginx em container (reverse proxy encadeado), ambas as camadas devem declarar os cabeçalhos de Upgrade e Connection, caso contrário o handshake WebSocket é truncado na primeira borda.
* 💡 Socket.IO alterna entre pooling HTTP e WebSocket. Forçar Connection 'upgrade' estático quebra requisições GET/POST normais; a diretiva correta é map $http_upgrade $connection_upgrade { default upgrade; '' close; }.
* 💡 No Docker Compose, o comando docker restart não recarrega variáveis de ambiente de env_file: - .env. É mandatória a execução de docker compose up -d para recriar o container com os novos valores.
* 💡 Vhosts órfãos no Nginx (como certificados de domínios desativados) bloqueiam o comando nginx -t e impedem qualquer reload seguro da malha de containers.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
map $http_upgrade $connection_upgrade {
    default upgrade;
    ''      close;
}
location /socket.io/ {
    proxy_pass http://evolution_api:8080;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection $connection_upgrade;
    proxy_read_timeout 86400s;
    proxy_send_timeout 86400s;
}
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O Evolution Manager e o backend do ProntOS passaram a operar com comunicação bidirecional em tempo real e webhooks ativos (MESSAGES_UPSERT, MESSAGES_UPDATE, CONNECTION_UPDATE), viabilizando triagem de intenções por IA via WhatsApp.


* **Projetos Relacionados**: `30-FieldFlow`, `evolution-api`, `05-orcamento`
* **Registro de Origem**: `_data/daily.dev-28.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
