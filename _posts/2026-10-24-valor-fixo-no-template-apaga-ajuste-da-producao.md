---
layout: post
title: "Valor fixo no template faz o render apagar o que a produção tinha ligado"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-097"
description: "O render-config regenerava os INI com opções fixas em zero, apagando o que tinha sido ligado no servidor. As opções viraram chaves de ambiente, e a revisão achou outros defeitos na mesma família de scripts."
date: 2026-10-24 00:00:00-03:00
categories: devlog
category: devops
tags: [docker, bash, python, configuracao, deploy]
---

# Valor fixo no template faz o render apagar o que a produção tinha ligado

> [!NOTE]
> **Resumo Executivo (DEV-2026-097)**: O render-config regenerava os INI com opções fixas em zero, apagando o que tinha sido ligado no servidor. As opções viraram chaves de ambiente, e a revisão achou outros defeitos na mesma família de scripts.

---

### 🚨 O Desafio Técnico / Contexto
MonitorarChamadasPabx e GravarInternas estavam com 0 no template, então cada render desligava o que a VPS ou o MonitorOPS tinha gravado. O deploy parecia certo e a opção sumia sem aviso.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O mecanismo mudou para LORENTZ_CTI_MONITORAR_CHAMADAS_PABX e LORENTZ_CTI_GRAVAR_INTERNAS, mas sem a chave o render ainda grava 0. Inclua a chave no .env antes do próximo render.
* 💡 sed com senha contendo &, | ou aspas corrompia a linha ou derrubava o script. A troca virou str.replace em Python.
* 💡 source do .env inteiro executava uma nota colada no arquivo. O filtro KEY=VAL, que o Caddy já tinha, foi para os quatro scripts bash, com remoção do CR do Windows.
* 💡 Aspas em volta do valor no .env iam parar no INI, porque o bash as tirava e o leitor Python não. Dois leitores do mesmo arquivo precisam ter a mesma regra.
* 💡 Placeholder que o script não substituía chegava ao .env do PBX como valor literal. Vale conferir o arquivo gerado, não só o exit code.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
# Lê só linhas KEY=VAL, sem executar o resto do arquivo
grep -E '^[A-Za-z_][A-Za-z0-9_]*=' .env | tr -d '\r'
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O render deixou de desfazer ajustes da produção quando a chave está no .env, e senhas com caracteres especiais pararam de quebrar o script.

* **Projetos Relacionados**: `lorentz-vps-stack`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
