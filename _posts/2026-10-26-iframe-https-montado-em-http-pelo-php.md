---
layout: post
title: "A página HTTPS monta o iframe em HTTP porque o PHP não vê o esquema do terminador"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-140"
description: "O Operador Web abria em HTTPS e o navegador bloqueava os iframes do posto e do softphone. O Apache do container continua em HTTP, então a URL pública tem de sair do cabeçalho encaminhado e do nome configurado."
date: 2026-10-26 00:00:00-03:00
categories: devlog
category: infraestrutura
tags: [php, caddy, https, iframe, webphone]
---

# A página HTTPS monta o iframe em HTTP porque o PHP não vê o esquema do terminador

> [!NOTE]
> **Resumo Executivo (DEV-2026-140)**: O Operador Web abria em HTTPS e o navegador bloqueava os iframes do posto e do softphone. O Apache do container continua em HTTP, então a URL pública tem de sair do cabeçalho encaminhado e do nome configurado.

---

### 🚨 O Desafio Técnico / Contexto
A página do operador chegava por HTTPS. Os iframes de atendimentos, perdas e softphone eram montados com http://, inclusive na porta HTTP do container do webphone. O PHP lia $_SERVER['HTTPS'] vazio, porque quem termina o TLS é a borda e o Apache segue em HTTP.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 cli_RequestIsHttps em cliente/cli_userfn.php aceita ew_IsHttps, $_SERVER['HTTPS'], X-Forwarded-Proto, X-Forwarded-Ssl, porta 443 e, por último, EW_SERVER_URL quando o host coincide e o esquema configurado é https.
* 💡 A porta publicada do webphone só fala HTTP. Com a página em HTTPS, cli_GetWebphonePublicUrl aponta para o host público do softphone, e a configuração do operador fica no host HTTPS do Supervisor.
* 💡 Acesso por IP no laboratório continua em http://host:porta. Nome público e endereço direto não usam a mesma regra.
* 💡 O endpoint de configuração precisa aceitar a origem do softphone, senão o iframe HTTPS carrega e a sessão do Supervisor não vale nele.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
$forwarded = strtolower(trim(explode(',', (string) ($_SERVER['HTTP_X_FORWARDED_PROTO'] ?? ''))[0]));
if ($forwarded === 'https') {
    return true;
}
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O posto em HTTPS passa a embutir softphone, atendimentos e perdas no mesmo esquema, e o laboratório por IP permanece em HTTP.

* **Projetos Relacionados**: `supervisor`, `lorentz-vps-stack`, `lorentz-webphone`
* **Registro de Origem**: `_data/daily.dev-24.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
