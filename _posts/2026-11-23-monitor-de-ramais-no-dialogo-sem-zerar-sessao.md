---
layout: post
title: "O monitor de ramais no diálogo abre sem o comando que zera a sessão"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-171"
description: "A mesma tela de ramais precisava abrir por cima do térmico e também como página inteira. O atalho que reinicia variáveis apaga o monitor da sessão, então o diálogo carrega att_monitor.php limpo e só na hora de abrir."
date: 2026-11-23 00:00:00-03:00
categories: devlog
category: frontend
tags: [iframe, php, sessao, cti]
---

# O monitor de ramais no diálogo abre sem o comando que zera a sessão

> [!NOTE]
> **Resumo Executivo (DEV-2026-171)**: A mesma tela de ramais precisava abrir por cima do térmico e também como página inteira. O atalho que reinicia variáveis apaga o monitor da sessão, então o diálogo carrega att_monitor.php limpo e só na hora de abrir.

---

### 🚨 O Desafio Técnico / Contexto
att_monitor.php?cmd=reiniciarvariaveis tira da sessão as escolhas do monitor, inclusive o agente logado, e redireciona para a própria página. Colocar esse endereço no iframe zeraria o contexto. A página puxa YUI, Phoenix e a sessão. O cabeçalho que nega frame está só em api/.htaccess, não na raiz.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O link Diálogo impede o clique e, na primeira abertura, define o src do iframe como att_monitor.php, sem query. Fechar ou Esc devolve o foco a esse link. O link Normal é outra âncora para o mesmo arquivo e não entra nesse listener.
* 💡 Sem JavaScript os dois href seguem para a página. X-Frame-Options DENY vale para /api/. att_monitor.php, na mesma origem, entra no iframe. Na prova o documento veio com título Monitoramento e readyState complete.
* 💡 O comando de reinício remove, entre outras, EW_SESSION_MONITOR_SERVICO, EW_SESSION_MONITOR_AGENTE, EW_SESSION_MONITOR_GRUPO e EW_SESSION_AgenteLogado. O diálogo não usa esse cmd.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
if (!quadro.getAttribute("src")) quadro.src = "att_monitor.php";
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Os ramais abrem por cima do térmico sem zerar a sessão do monitor, e a página antiga continua a um clique.

* **Projetos Relacionados**: `supervisor-elevar-legado`
* **Registro de Origem**: `_data/daily.dev-32.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
