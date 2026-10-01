---
layout: post
title: "AMI do Asterisk visto do container: negar tudo e permitir a rede Docker"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-042"
description: "O LorentzCTI na bridge não alcançava o AMI do Issabel em rede do host. A sessão só apareceu com permit da faixa Docker e a mesma faixa liberada no firewall, sem publicar a porta na internet."
date: 2026-07-14 00:00:00+00:00
categories: devlog
category: telefonia
tags: [asterisk, ami, ufw, docker, cti]
---

# AMI do Asterisk visto do container: negar tudo e permitir a rede Docker

> [!NOTE]
> **Resumo Executivo (DEV-2026-042)**: O LorentzCTI na bridge não alcançava o AMI do Issabel em rede do host. A sessão só apareceu com permit da faixa Docker e a mesma faixa liberada no firewall, sem publicar a porta na internet.

---

### 🚨 O Desafio Técnico / Contexto
O PBX escuta a porta 5038 no host. O CTI sai de um endereço 172.16.0.0/12. A ACL padrão do manager só aceitava localhost, e o UFW ainda descartava o pacote mesmo depois de ajustar o Asterisk.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Issabel em rede do host e CTI em bridge não compartilham localhost.
* 💡 manager_custom.conf começa com deny de tudo e só então permite 127.0.0.1 e a rede Docker.
* 💡 UFW ativo e ACL do Asterisk são duas portas. As duas precisam concordar.
* 💡 A 5038 não entra na lista pública do firewall.

---

### 🛠️ Especificação Técnica & Código-Chave
```ini
; /etc/asterisk/manager_custom.conf
; segredo do manager fica no .env, não neste exemplo
deny=0.0.0.0/0.0.0.0
permit=127.0.0.1/255.255.255.255
permit=172.16.0.0/255.240.0.0

# Firewall do host, mesma faixa, sem abrir para a internet
ufw allow from 172.16.0.0/12 to any port 5038 proto tcp
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O CTI volta a enxergar eventos do Asterisk e a porta de gerência continua fora da internet.

* **Projetos Relacionados**: `lorentz-vps-stack`, `issabel4-docker`
* **Registro de Origem**: `_data/daily.dev-03.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
