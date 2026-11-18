---
layout: post
title: "A grade de módulos lia a data num bloco de licença que a chave não traz"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-143"
description: "A página Sobre avisava no PHP 8 ao montar SAC e TMK. As linhas existem na empresa. O texto da licença em sessão não tem esses blocos, e a data passa a vir da tabela."
date: 2026-10-29 00:00:00-03:00
categories: devlog
category: backend
tags: [php, licenca, supervisor, php8]
---

# A grade de módulos lia a data num bloco de licença que a chave não traz

> [!NOTE]
> **Resumo Executivo (DEV-2026-143)**: A página Sobre avisava no PHP 8 ao montar SAC e TMK. As linhas existem na empresa. O texto da licença em sessão não tem esses blocos, e a data passa a vir da tabela.

---

### 🚨 O Desafio Técnico / Contexto
SAC_EMPRESA_MODULO tem os módulos, e a grade da página Sobre lia a validade no array montado por get_Licenca. A chave do produto é a concatenação de sistema e módulo. Sistema 3 com módulo 6 vira 36 (SAC / CRMWEB). Sistema 4 com módulo 8 vira 48 (TMK / TMKWEB). Esses blocos não vinham no texto da licença, e o PHP 8 avisava ao ler o índice ausente.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 get_Licenca explode a chave por # e depois por ;. Cada bloco com ao menos cinco campos entra em $aLicenca na chave dadosModulo[0] . dadosModulo[1].
* 💡 A grade usa essa mesma concatenação, CdSistema . CdModulo, e só lê as posições 4 e 5 se o bloco existir e for array.
* 💡 Sem o bloco, Validade e Expiracao ficam vazias e a data exibida é DtValidade já gravada em SAC_EMPRESA_MODULO.
* 💡 Os quatro avisos eram dois produtos vezes duas posições de data. Módulo contratado na empresa e módulo presente no texto da licença são consultas diferentes.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
$chaveModulo = $CdSistema . $CdModulo;
$blocoLicenca = (isset($aLicenca[$chaveModulo]) && is_array($aLicenca[$chaveModulo]))
    ? $aLicenca[$chaveModulo] : array();
$Validade = isset($blocoLicenca[4]) ? $blocoLicenca[4] : '';
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A página Sobre deixa de avisar no PHP 8 e mostra a validade gravada na empresa quando a chave não traz o bloco.

* **Projetos Relacionados**: `supervisor`
* **Registro de Origem**: `_data/daily.dev-24.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
