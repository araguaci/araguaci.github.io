---
layout: post
title: "Infraestrutura Soberana de Homelab: Proxmox VE, Docker Compose e Redes Mesh WireGuard"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-016"
description: "Guia arquitetural para implantação de uma nuvem privada residencial e corporativa com isolamento de serviços, bloqueio de telemetria e acesso remoto seguro."
date: 2026-05-20 00:00:00+00:00
categories: devlog
category: infraestrutura
tags: [homelab, proxmox, docker, wireguard, pihole, soberania]
---

# Infraestrutura Soberana de Homelab: Proxmox VE, Docker Compose e Redes Mesh WireGuard

> [!NOTE]
> **Resumo Executivo (DEV-2026-016)**: Guia arquitetural para implantação de uma nuvem privada residencial e corporativa com isolamento de serviços, bloqueio de telemetria e acesso remoto seguro.

---

### 🚨 O Desafio Técnico / Contexto
A dependência exclusiva de serviços de nuvem pública (AWS, GCP) gera custos crescentes em dólar, dependência de políticas arbitrárias de terceiros e perda de controle sobre a privacidade de dados corporativos.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O Proxmox VE oferece hipervisor bare-metal leve para separação entre contêineres de alta densidade (LXC) e máquinas virtuais isoladas.
* 💡 A orquestração via Docker Compose permite versionar em arquivos YAML toda a pilha de serviços (Home Assistant, Pi-hole, Uptime Kuma).
* 💡 A criação de túneis WireGuard ponto-a-ponto permite gerenciar a bancada de servidores de qualquer lugar sem abrir portas vulneráveis no roteador.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
# docker-compose.yml básico de Homelab Seguro
services:
  pihole:
    image: pihole/pihole:latest
    ports:
      - "53:53/tcp"
      - "53:53/udp"
      - "8080:80/tcp"
    restart: unless-stopped
  wireguard:
    image: linuxserver/wireguard:latest
    cap_add:
      - NET_ADMIN
    restart: unless-stopped

```

---

### 📈 Impacto no Ecossistema & Valor Prático
Autonomia tecnológica e redução de custos de nuvem pública, com privacidade absoluta de infraestrutura.

* **Projetos Relacionados**: `homelab.artesdosul.com`, `haos-home-assistant`
* **Registro de Origem**: `_data/daily.dev-01.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
