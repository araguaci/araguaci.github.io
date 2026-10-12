---
layout: post
title: "Symlink no PATH faz o auditor achar o render no diretório errado"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-061"
description: "Depois do install, o comando no PATH apontava para um symlink e o script resolvia SCRIPT_DIR como a pasta do binário, não a da lib. O relatório só voltou a gerar quando o install passou a usar um wrapper com exec no .sh real.
"
date: 2026-10-01 00:00:00+00:00
categories: devlog
category: infraestrutura
tags: [bash, docker, nginx, openssl, devops, seguranca]
---

# Symlink no PATH faz o auditor achar o render no diretório errado

> [!NOTE]
> **Resumo Executivo (DEV-2026-061)**: Depois do install, o comando no PATH apontava para um symlink e o script resolvia SCRIPT_DIR como a pasta do binário, não a da lib. O relatório só voltou a gerar quando o install passou a usar um wrapper com exec no .sh real.


---

### 🚨 O Desafio Técnico / Contexto
O pacote instalava o shell em /usr/local/lib/... e criava um symlink em /usr/local/bin. Na execução, BASH_SOURCE ficava no caminho do symlink. dirname + pwd apontavam para bin/, onde o Python do renderizador não existe. Em paralelo, o probe TLS com openssl e -servername igual ao IP literal travava a auditoria antes de gravar JSON/HTML.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 BASH_SOURCE[0] no symlink resolve o path usado na invocação, não o alvo final. SCRIPT_DIR derivado só de dirname quebra o achado do .py irmão.
* 💡 install.sh com wrapper (exec /usr/local/lib/.../infra-report.sh) fixa BASH_SOURCE no arquivo real; resolver a cadeia de readlink no próprio script é a segunda linha de defesa.
* 💡 openssl s_client com -servername em IPv4 literal pode pendurar o probe. Usar SNI localhost (ou o domínio do cert) e timeout -k evita o hang.
* 💡 Relatórios de frota com achados de porta e SSH não devem ir para o GitHub: vps/*.json e vps/*.html no .gitignore, com cópia só local.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
# Wrapper em /usr/local/bin/infra-report
#!/usr/bin/env bash
exec /usr/local/lib/infra-report/infra-report.sh "$@"

# TLS: SNI amigável quando o host é IP
sni=localhost
echo | timeout -k 2 5 openssl s_client -connect 127.0.0.1:443 -servername "$sni"
```

---

### 📈 Impacto no Ecossistema & Valor Prático
sudo infra-report volta a achar o renderizador após o install, o job termina e a frota local em vps/ atualiza sem subir JSON sensível no remoto.


* **Projetos Relacionados**: `infra-report`, `ai-projects`
* **Registro de Origem**: `_data/daily.dev-06.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
