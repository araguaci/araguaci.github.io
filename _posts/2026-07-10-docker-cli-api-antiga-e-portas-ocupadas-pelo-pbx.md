---
layout: post
title: "O cliente Docker da distro fala uma API que o daemon já não usa"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-045"
description: "O painel não listava containers porque o pacote docker.io negociava a API 1.41 com um daemon 1.52. No mesmo host, as portas 80 e 443 já pertenciam ao PBX."
date: 2026-07-10 00:00:00+00:00
categories: devlog
category: devops
tags: [docker, api, portas, pwa, php]
---

# O cliente Docker da distro fala uma API que o daemon já não usa

> [!NOTE]
> **Resumo Executivo (DEV-2026-045)**: O painel não listava containers porque o pacote docker.io negociava a API 1.41 com um daemon 1.52. No mesmo host, as portas 80 e 443 já pertenciam ao PBX.

---

### 🚨 O Desafio Técnico / Contexto
O monitor em Python usava o CLI empacotado pela distro. O daemon recusava a versão antiga da API e a tela parecia sem Docker. O portal, se subisse em 80 ou 443, colidia com o Issabel. Um service worker cache-first no config.json ainda impedia o painel de atualizar a lista de aplicativos.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 docker-ce-cli acompanha a API do daemon. O pacote docker.io da distro pode ficar uma geração atrás.
* 💡 O portal fica na 8099. 80, 443 e 8088 permanecem com o PBX.
* 💡 No PWA, estático pode ser cache-first. config.json é network-first, senão a lista de apps não muda.
* 💡 O debug SQL do Supervisor liga por sessão. Ligado para todas as sessões enche o disco em produção.

---

### 🛠️ Especificação Técnica & Código-Chave
```bash
# Cliente e daemon precisam da mesma geração de API
docker version
# Client API antiga (1.41) contra daemon 1.52: trocar docker.io por docker-ce-cli

# Portal fora das portas do PBX
PORTAL_HTTP_PORT=8099
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O painel volta a falar com o Docker e o portal deixa de disputar as portas do PBX.

* **Projetos Relacionados**: `lorentz-vps-stack`
* **Registro de Origem**: `_data/daily.dev-03.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
