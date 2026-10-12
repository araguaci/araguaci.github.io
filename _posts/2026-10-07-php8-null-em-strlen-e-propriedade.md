---
layout: post
title: "No PHP 8 null não serve para strlen nem para propriedade"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-070"
description: "A lista de clientes avisava strlen(null) em short_name e leitura de DetailAdd num grid que continuava NULL. Os dois vinham de código que no PHP antigo seguia com valor vazio ou aviso mudo."
date: 2026-10-07 00:00:00+00:00
categories: devlog
category: backend
tags: [php, php8, legado]
---

# No PHP 8 null não serve para strlen nem para propriedade

> [!NOTE]
> **Resumo Executivo (DEV-2026-070)**: A lista de clientes avisava strlen(null) em short_name e leitura de DetailAdd num grid que continuava NULL. Os dois vinham de código que no PHP antigo seguia com valor vazio ou aviso mudo.

---

### 🚨 O Desafio Técnico / Contexto
userfn9.php short_name recebia CurrentValue de NomeUsual, e esse valor pode ser null (a lista de clientes, a de atendimento e a home do Phoenix chamam a função assim). No PHP 8.2, strlen(null) é deprecated. O grid de endereço nasce NULL em sac_enderecogridcls.php. O bloco que criaria o objeto e as opções de lista está comentado. LoadRowValues só cria o global quando uma linha carrega. O painel de cima da lista está atrás de if (00 && ...), então não roda. O de baixo, na linha do DetailAdd, roda. Com o SELECT falhando, o loop ainda chegava nesse rodapé com o objeto inexistente. Atribuir o grid em $GLOBALS grava de verdade: a sonda mostrou que o objeto permanece. O null da linha 4210 é o objeto que ninguém criou. DetailAdd de SAC_ENDERECO já é FALSE em sac_enderecoinfo.php. A cópia da função em supervisor/api/userfn9.php ficou sem o cast.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 short_name começa com (string) $str. Null vira string vazia antes de strlen e substr.
* 💡 Ler DetailAdd exige is_object no grid. O painel comentado e o SELECT que não abre deixam o global em NULL.
* 💡 O contato da mesma grade já estava curto-circuitado com 00 &&. O endereço de baixo não estava.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
// userfn9.php — short_name
$str = (string) $str;

// sac_clientelist.php — rodapé do endereço
is_object($SAC_ENDERECO_grid) && $SAC_ENDERECO_grid->DetailAdd
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A lista deixa de avisar strlen(null) e leitura de DetailAdd quando o grid de endereço não foi criado.

* **Projetos Relacionados**: `supervisor`
* **Registro de Origem**: `_data/daily.dev-09.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
