---
layout: post
title: "Trocar docker stats por docker ps com cgroup corta latência de 2,6s e evita zerar o delta"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-163"
description: "Consultar containers via docker stats --no-stream travava a interface do wslpanel por cerca de 2,6 segundos por ciclo. Ler nome e estado com docker ps (dezenas de milissegundos) e extrair CPU, memória e PIDs direto do cgroup — controlando dupla leitura com flag fresh — eliminou o bloqueio."
date: 2026-11-18 00:00:00-03:00
categories: devlog
category: devops
tags: [docker, cgroup, linux, performance, logs, wsl]
---

# Trocar docker stats por docker ps com cgroup corta latência de 2,6s e evita zerar o delta

> [!NOTE]
> **Resumo Executivo (DEV-2026-163)**: Consultar containers via docker stats --no-stream travava a interface do wslpanel por cerca de 2,6 segundos por ciclo. Ler nome e estado com docker ps (dezenas de milissegundos) e extrair CPU, memória e PIDs direto do cgroup — controlando dupla leitura com flag fresh — eliminou o bloqueio.

---

### 🚨 O Desafio Técnico / Contexto
Ao implementar a aba Docker no wslpanel, o comando docker stats --no-stream levava aproximadamente 2,6 segundos para responder, congelando o ciclo de 1 segundo do painel. Na migração para leitura direta do cgroup (system.slice/docker-<id>.scope e fallback /sys/fs/cgroup/docker/<id>), varrer as duas árvores na mesma amostra fazia a segunda leitura ver o contador recém-gravado pela primeira, zerando o delta de CPU. Na aba Logs, era preciso evitar carregar arquivos enormes, linhas iniciais cortadas ou logs binários e compactados.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 docker ps responde em dezenas de milissegundos enquanto docker stats --no-stream bloqueia ~2,6s; o ID curto do docker ps serve de prefixo para localizar o escopo de 64 caracteres hexadecimais no cgroup.
* 💡 Ao suportar duas árvores de cgroup (system.slice/docker-<id>.scope e /sys/fs/cgroup/docker/<id>), uma flag fresh por linha impede ler ambas na mesma amostra e zerar o delta; containers recém-descobertos (seen falso) exibem 0% na primeira leitura.
* 💡 A aba Docker deve aparecer pela presença do binário no disco, exibindo 'não respondeu' quando o daemon está caído sem remover a aba no meio de um teste.
* 💡 Na leitura de /var/log, limitar o tail aos últimos 256 KB, descartar a primeira linha quando o offset é maior que 0 e excluir .gz, .xz, .bz2, .zst, wtmp, btmp, lastlog e faillog mantém a interface rápida e legível.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
# Caminho primário e fallback de métricas cgroup v2 no Linux
/sys/fs/cgroup/system.slice/docker-<id64>.scope/cpu.stat
/sys/fs/cgroup/docker/<id64>/cpu.stat
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A aba Docker passou a atualizar no ritmo de 1 segundo sem travar a UI e o leitor de /var/log abre arquivos grandes instantaneamente com segurança.

* **Projetos Relacionados**: `wslpanel`
* **Registro de Origem**: `_data/daily.dev-30.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
