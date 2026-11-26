---
layout: post
title: "docker cp para o /tmp de um container com systemd grava por baixo do tmpfs"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-180"
description: "O script copiava um PHP para /tmp do container do PABX e o PHP dizia que o arquivo não existia. O /tmp do container é tmpfs montado pelo systemd, e o docker cp escreve na camada de baixo."
date: 2026-11-26 00:00:00-03:00
categories: devlog
category: devops
tags: [docker, systemd, tmpfs, issabel]
---

# docker cp para o /tmp de um container com systemd grava por baixo do tmpfs

> [!NOTE]
> **Resumo Executivo (DEV-2026-180)**: O script copiava um PHP para /tmp do container do PABX e o PHP dizia que o arquivo não existia. O /tmp do container é tmpfs montado pelo systemd, e o docker cp escreve na camada de baixo.

---

### 🚨 O Desafio Técnico / Contexto
O deploy do laboratório criava ramais de teste copiando issabel-extensions-batch.php com docker cp para /tmp do container do Issabel e rodando php nele. Resultado: "Could not open input file". O container roda systemd, que monta um tmpfs em /tmp depois do boot. O docker cp grava no sistema de arquivos do container, por baixo da montagem, onde o processo de dentro não enxerga.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Em container com init completo (systemd), /tmp, /run e /dev/shm costumam ser tmpfs. Copiar para lá com docker cp não chega ao processo.
* 💡 mount | grep ' /tmp ' dentro do container confirma em um comando. Os outros scripts da stack já usavam /root, e a correção seguiu o mesmo destino.
* 💡 Arquivo de troca entre host e container vai para um diretório persistente do próprio container ou para um volume, nunca para /tmp.

---

### 🛠️ Especificação Técnica & Código-Chave
```bash
docker exec issabel-prod sh -c "mount | grep ' /tmp '"
# tmpfs on /tmp type tmpfs (...)
docker cp script.php issabel-prod:/root/script.php
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A criação dos ramais de teste passou a funcionar na primeira rodada do deploy.

* **Projetos Relacionados**: `lorentz-vps-stack`
* **Registro de Origem**: `_data/daily.dev-34.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
