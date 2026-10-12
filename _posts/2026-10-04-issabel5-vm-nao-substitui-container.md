---
layout: post
title: "O Issabel 5 do laboratório não ocupa o lugar do container Issabel 4"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-066"
description: "A stack oficial continua com Issabel 4 em Docker. O Issabel 5 entra como VM quando a máquina já o tem ou quando se quer a versão nova, e os dois não podem publicar 5060 e 443 no mesmo host."
date: 2026-10-04 00:00:00+00:00
categories: devlog
category: infraestrutura
tags: [issabel, docker, hyper-v, windows, ssh]
---

# O Issabel 5 do laboratório não ocupa o lugar do container Issabel 4

> [!NOTE]
> **Resumo Executivo (DEV-2026-066)**: A stack oficial continua com Issabel 4 em Docker. O Issabel 5 entra como VM quando a máquina já o tem ou quando se quer a versão nova, e os dois não podem publicar 5060 e 443 no mesmo host.

---

### 🚨 O Desafio Técnico / Contexto
O laboratório Windows subiu Issabel 5 numa VM Hyper-V e a pergunta foi se a stack inteira deveria ir para Docker no mesmo host, inclusive o container do PBX. O SSH do host abria cmd.exe, onde ls não existe. A chave de administrador não era lida do authorized_keys do usuário. Sincronizar a pasta do notebook para o mini PC levava .git, .env e o token do tronco se o ignore não estivesse explícito.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Issabel 4 no container é o artefato da stack. Issabel 5 é ISO na VM. O monitor escolhe o alvo. Servidor, supervisão e manutenção são os mesmos.
* 💡 Subir o container issabel no host que já tem a VM do Issabel 5 disputa SIP 5060 e HTTPS 443. O deploy de laboratório não chama o deploy desse container.
* 💡 OpenSSH no Windows, para conta de administrador, lê C:\ProgramData\ssh\administrators_authorized_keys. A shell padrão vem de HKLM\SOFTWARE\OpenSSH DefaultShell. Sessão sem elevação não grava essa chave.
* 💡 O ignore da sincronização precisa excluir .git, .env, att_config.php e o arquivo de token do tronco. Copiar o .env do notebook para o laboratório mistura credencial.
* 💡 Há quatro shells. O notebook é o único com os aliases SSH. O host Windows fala PowerShell. A VM e a VPS falam bash. exit volta ao notebook.

---

### 🛠️ Especificação Técnica & Código-Chave


---

### 📈 Impacto no Ecossistema & Valor Prático
O laboratório valida o procedimento com Issabel 5 na VM e o restante da stack em Docker, sem derrubar as portas do PBX que já está no ar.

* **Projetos Relacionados**: `lorentz-vps-stack`
* **Registro de Origem**: `_data/daily.dev-08.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
