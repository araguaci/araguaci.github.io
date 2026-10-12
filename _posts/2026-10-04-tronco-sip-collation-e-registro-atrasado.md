---
layout: post
title: "O tronco SIP falha quando o nome e o id não compartilham collation"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-063"
description: "Gravar o tronco pelo provisionador oficial quebrava no MySQL com mistura de collation entre trunks.name e sip.id. A comparação passou a usar o collation de cada coluna, e o registro no Asterisk só é confiável segundos depois do reload."
date: 2026-10-04 00:00:00+00:00
categories: devlog
category: telefonia
tags: [asterisk, mysql, issabel, sip, chan-sip]
---

# O tronco SIP falha quando o nome e o id não compartilham collation

> [!NOTE]
> **Resumo Executivo (DEV-2026-063)**: Gravar o tronco pelo provisionador oficial quebrava no MySQL com mistura de collation entre trunks.name e sip.id. A comparação passou a usar o collation de cada coluna, e o registro no Asterisk só é confiável segundos depois do reload.

---

### 🚨 O Desafio Técnico / Contexto
O INSERT do provisionador morria com ERROR 1267 (illegal mix of collations) na comparação name = @nome. trunks.name estava em utf8_unicode_ci e sip.id em utf8mb4_unicode_ci, com a conexão em utf8_general_ci. O relatório do marketplace respondia 403 e parecia ser a causa. O plano gerado chamava o script com exec, e a sessão SSH fechava junto com o processo. Logo após o sip reload, sip show registry ainda dizia Unregistered.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O charset do CONVERT é a parte da collation antes do primeiro underscore (utf8mb4_unicode_ci vira utf8mb4). A cláusula fica CONVERT(coluna USING charset) COLLATE collation, lida de information_schema para trunks.name e sip.id.
* 💡 Sem o arquivo de token o tronco ainda é gravado. O 403 do marketplace é a recusa do relatório, não a falha do peer.
* 💡 exec substitui o shell. O plano de provisionamento tem de ser um bash normal, senão a sessão remota acaba quando o script termina.
* 💡 Este Issabel usa chan_sip. A tabela asterisk.pjsip não existe, então o driver não pode assumir PJSIP.
* 💡 amportal reload não regenerou sip_additional.conf. O caminho que gravou o peer foi retrieve_conf e depois sip reload. A saída do retrieve_conf imprime a senha do banco e vai para /dev/null.
* 💡 Unregistered contém o texto registered. O diagnóstico só conta Registered com limite de palavra, e a primeira leitura depois do reload ainda pode ser Unregistered.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
# collation vem de information_schema; charset é o trecho antes do _
# trunks.name e sip.id não compartilham a mesma collation
CONVERT(`name` USING utf8mb4) COLLATE utf8mb4_unicode_ci
  = CONVERT(@nvoip_trunk_name USING utf8mb4) COLLATE utf8mb4_unicode_ci
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O tronco passa a ser gravado no Issabel 4 e o diagnóstico só marca registrado quando o registry diz Registered de fato.

* **Projetos Relacionados**: `lorentz-vps-stack`
* **Registro de Origem**: `_data/daily.dev-08.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
