---
layout: post
title: "Em servidor de telefonia com 128 GB, o limite de clientes é a CPU"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-101"
description: "A máquina inicial para atender vários call centers tem muita memória e poucos núcleos. A estimativa aponta CPU e disco como limite, e nenhum número deve ser vendido antes de um teste de carga."
date: 2026-11-03 00:00:00-03:00
categories: devlog
category: infraestrutura
tags: [capacidade, asterisk, proxmox, sqlserver, sipp]
---

# Em servidor de telefonia com 128 GB, o limite de clientes é a CPU

> [!NOTE]
> **Resumo Executivo (DEV-2026-101)**: A máquina inicial para atender vários call centers tem muita memória e poucos núcleos. A estimativa aponta CPU e disco como limite, e nenhum número deve ser vendido antes de um teste de carga.

---

### 🚨 O Desafio Técnico / Contexto
Operar como provedor significa colocar vários call centers na mesma máquina: 128 GB de RAM, 8 núcleos físicos e discos SAS. Um erro de dimensionamento corta o áudio de todos os clientes, não só do último a entrar.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 A estimativa é de 2 a 3 clientes com VM e PBX próprios, ou 3 a 4 com PBX compartilhado por faixa de ramal, e cerca de 40 a 60 chamadas simultâneas gravadas. Vem de premissas documentadas, sem medição.
* 💡 Largura de banda não é o gargalo: 40 chamadas em G.711 ficam na ordem de 10 Mbit/s. O que pesa é a CPU do Asterisk e o disco das gravações.
* 💡 VM de telefonia não deve ter vCPU em oversubscription: use relação de 1 para 1 com o núcleo físico.
* 💡 SSD em RAID 1 fica para sistema, VMs e SQL, e o SAS só para gravação e backup.
* 💡 SQL Server Developer não pode ir para produção: o licenciamento pede Express ou SPLA, e isso entra no custo por cliente.
* 💡 Antes de vender além da estimativa, faça teste de carga com SIPp e some os picos de todos os clientes.

---

### 🛠️ Especificação Técnica & Código-Chave


---

### 📈 Impacto no Ecossistema & Valor Prático
Cada cliente novo nessa máquina passa a ser avaliado pela soma dos picos de chamadas, não pela RAM livre.

* **Projetos Relacionados**: `lorentz-vps-stack`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
