---
layout: post
title: "Porta do Docker Desktop aparece na distro WSL pelo wslrelay"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-074"
description: "Container do Docker Desktop não mora nas outras distros WSL. A rede espelhada publica as portas dele no localhost, e o nginx que resolve o upstream na subida entra em loop se esse upstream está parado."
date: 2026-10-10 00:00:00+00:00
categories: devlog
category: devops
tags: [docker, wsl, nginx, php]
---

# Porta do Docker Desktop aparece na distro WSL pelo wslrelay

> [!NOTE]
> **Resumo Executivo (DEV-2026-074)**: Container do Docker Desktop não mora nas outras distros WSL. A rede espelhada publica as portas dele no localhost, e o nginx que resolve o upstream na subida entra em loop se esse upstream está parado.

---

### 🚨 O Desafio Técnico / Contexto
Um portal em nginx reiniciava sem publicar porta. O log dizia host not found in upstream. O serviço de que ele depende estava Exited. Noutra distro WSL, o Apache não escutava a porta 80 e o ss listava portas sem processo local. No container PHP, o log repetia que ipconfig não existia.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 proxy_pass com nome fixo de container é resolvido na subida do nginx. Com o upstream parado, o processo sai com host not found in upstream e a política de restart repete o ciclo. O upstream sobe antes do proxy.
* 💡 exec('ipconfig') no PHP foi escrito para Windows. Dentro do container Linux o shell responde ipconfig: not found. O ajuste é no código montado no volume, não no entrypoint, quando o exec está no projeto PHP.
* 💡 ss numa distro WSL mostra a porta do Docker Desktop sem PID local. No Windows o dono é wslrelay.exe. O Apache dessa distro recebe AH00072 ao tentar a porta 80. Não se encerra o wslrelay. Muda-se o Listen.
* 💡 O binário docker visto dentro da distro pode ser o do Docker Desktop montado em /mnt. docker ps nesse caso lista o engine do Windows, não um engine instalado na distro.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
proxy_pass http://servico-upstream:8090/api/;
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O reparo do portal, do PHP e do Apache da distro deixa de ser feito no lugar errado.

* **Projetos Relacionados**: `lorentz-vps-stack`
* **Registro de Origem**: `_data/daily.dev-11.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
