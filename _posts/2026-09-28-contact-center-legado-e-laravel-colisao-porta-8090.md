---
layout: post
title: "Dois contact centers no mesmo host: a porta 8090 já era do CTI"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-033"
description: "O Supervisor PHP com SQL Server segue em produção enquanto o Omnichannel Laravel sobe ao lado, com MySQL próprio e uma porta que não disputa a API do LorentzCTI."
date: 2026-09-28 00:00:00+00:00
categories: devlog
category: arquitetura
tags: [docker, laravel, sql-server, mysql, portas, omnichannel]
---

# Dois contact centers no mesmo host: a porta 8090 já era do CTI

> [!NOTE]
> **Resumo Executivo (DEV-2026-033)**: O Supervisor PHP com SQL Server segue em produção enquanto o Omnichannel Laravel sobe ao lado, com MySQL próprio e uma porta que não disputa a API do LorentzCTI.

---

### 🚨 O Desafio Técnico / Contexto
O compose de desenvolvimento do Laravel publicava a porta 8090. Essa porta já era a Monitor API do LorentzCTI. Subir os dois arquivos ao mesmo tempo derrubava o monitoramento ou o helpdesk novo.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O stack chama só docker-compose.vps.yml, na porta 8095. O compose de desenvolvimento do Laravel fica de fora dessa montagem.
* 💡 SQL Server do legado e MySQL do Laravel não se misturam. O encontro dos dois sistemas é o portal e o MonitorOPS.
* 💡 Na VPS a 8095 escuta em 127.0.0.1, atrás do Caddy. No laboratório o bind é aberto para o host Windows enxergar o WSL.

---

### 🛠️ Especificação Técnica & Código-Chave
```bash
# Lab / homologação (bind acessível no host)
./scripts/deploy-omnichannel.sh --lab

# VPS (8095 só em localhost; o domínio entra pelo Caddy)
./scripts/deploy-omnichannel.sh --vps

# Pular o Laravel e deixar o legado sozinho
./scripts/deploy-lab-local.sh --skip-omnichannel
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Legado e helpdesk novo sobem no mesmo ambiente sem tomar a porta do monitoramento CTI.

* **Projetos Relacionados**: `omnichannel`, `lorentz-vps-stack`, `omnichannel-system`
* **Registro de Origem**: `_data/daily.dev-03.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
