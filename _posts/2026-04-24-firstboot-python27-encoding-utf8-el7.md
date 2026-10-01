---
layout: post
title: "Firstboot em Python 2.7: acento sem cabeçalho de encoding derruba o EL7"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-048"
description: "O CentOS 7 do Issabel ainda roda Python 2.7 no primeiro boot. Um snippet com caractere fora de ASCII, sem declaring encoding, interrompe a provisão antes do PBX subir."
date: 2026-04-24 00:00:00+00:00
categories: devlog
category: devops
tags: [python, issabel, centos, utf-8, docker]
---

# Firstboot em Python 2.7: acento sem cabeçalho de encoding derruba o EL7

> [!NOTE]
> **Resumo Executivo (DEV-2026-048)**: O CentOS 7 do Issabel ainda roda Python 2.7 no primeiro boot. Um snippet com caractere fora de ASCII, sem declaring encoding, interrompe a provisão antes do PBX subir.

---

### 🚨 O Desafio Técnico / Contexto
Comentários e mensagens em português dentro do firstboot eram UTF-8. O interpretador 2.7 do EL7 recusa o arquivo sem o cookie de encoding e o container reinicia no meio da configuração, com AMI e Apache ainda fora.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 No Python 2.7, arquivo com acento precisa da linha coding utf-8 logo no topo.
* 💡 O mesmo texto é inofensivo no Python 3 do restante do stack. O firstboot é o ponto que ainda é 2.7.
* 💡 Mensagem de boot em ASCII evita a classe inteira de falha quando o cookie é esquecido.
* 💡 Login de agente de call center e a porta HTTPS de produção foram estabilizados no mesmo ciclo: o boot tem que terminar para o restante ser testável.

---

### 🛠️ Especificação Técnica & Código-Chave
```python
# -*- coding: utf-8 -*-
# EL7 / Python 2.7: sem esta linha, acento no snippet aborta o firstboot.
print("Issabel firstboot ok")
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O primeiro boot do PBX deixa de morrer num comentário em português.

* **Projetos Relacionados**: `issabel4-docker`, `lorentz-vps-stack`
* **Registro de Origem**: `_data/daily.dev-03.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
