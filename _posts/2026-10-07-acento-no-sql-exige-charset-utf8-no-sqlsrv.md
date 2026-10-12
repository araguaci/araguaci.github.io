---
layout: post
title: "Acento no SQL derruba o sqlsrv do Linux sem CharacterSet UTF-8"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-069"
description: "A mesma lista de clientes abria no WAMP e, no container, pintava uma linha 00000. O COUNT passava porque não tem acento. O SELECT da grade carrega o literal Não e o unixODBC responde HY090 se a conexão não declara UTF-8."
date: 2026-10-07 00:00:00+00:00
categories: devlog
category: devops
tags: [php, sqlserver, docker, unixodbc]
---

# Acento no SQL derruba o sqlsrv do Linux sem CharacterSet UTF-8

> [!NOTE]
> **Resumo Executivo (DEV-2026-069)**: A mesma lista de clientes abria no WAMP e, no container, pintava uma linha 00000. O COUNT passava porque não tem acento. O SELECT da grade carrega o literal Não e o unixODBC responde HY090 se a conexão não declara UTF-8.

---

### 🚨 O Desafio Técnico / Contexto
No WAMP a página usa ADO (ado_mssql) e a grade lista o cliente. No container o ew_Connect abre mssqlnative (sqlsrv/unixODBC). EW_SELECT_LIMIT é falso no Windows e 1234 no Linux, então no Linux a página conta com getCountRows, que reescreve para SELECT COUNT(*) AS TOTAL FROM SAC_CLIENTE. Essa frase não tem acento e devolve a contagem. SqlSelect() em sac_clienteinfo.php inclui o literal Não em UTF-8 (bytes c3 a3). Sem CharacterSet na connectionInfo, o driver recusa o statement com HY090 (Invalid string or buffer length). O recordset fica falso, mas o loop ainda chama LoadRowValues. str_pad de CdCli e NumExterno nulos vira 00000, e o MoveNext no recordset falso estoura antes do pager. A pasta log/ do host fica vazia: o container grava no volume supervisor-log. phpfn.php já manda UTF-8 quando PROJECT_CHARSET é utf-8, mas a lista inclui phpfn9.php. Reabrir a conexão com CharacterSet UTF-8 devolveu o registro que o COUNT já tinha contado.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 HY090 aqui foi charset, não coluna inexistente. O COUNT sem acento passar não prova que o SELECT da grade passou.
* 💡 ew_Connect em phpfn9.php precisa de CharacterSet UTF-8 junto com ReturnDatesAsStrings e TrustServerCertificate. Vale para toda página que usa essa conexão.
* 💡 A linha 00000 é str_pad de campo nulo, com a grade desenhada em cima de um recordset que não abriu.
* 💡 supervisor/api/phpfn9.php e supervisor/api/func.php ainda abrem o driver mssql antigo sem CharacterSet. A correção ficou no ew_Connect da aplicação web.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
// phpfn9.php — ew_Connect, driver mssqlnative
$conn->connectionInfo = array(
    'ReturnDatesAsStrings' => true,
    'TrustServerCertificate' => true,
    'CharacterSet' => 'UTF-8',
);
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A lista de clientes no container passa a devolver o registro que o WAMP já mostrava.

* **Projetos Relacionados**: `supervisor`, `lorentz-vps-stack`
* **Registro de Origem**: `_data/daily.dev-09.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
