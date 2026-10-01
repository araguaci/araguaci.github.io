---
layout: post
title: "Licença e painéis de administração só para a allowlist do edge"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-038"
description: "O gerador de licença deixou de ficar público no proxy. No container Linux, a licença também deixou de chamar o comando VOL, que não existe fora do Windows."
date: 2026-07-31 00:00:00+00:00
categories: devlog
category: seguranca
tags: [caddy, allowlist, licenca, docker, php]
---

# Licença e painéis de administração só para a allowlist do edge

> [!NOTE]
> **Resumo Executivo (DEV-2026-038)**: O gerador de licença deixou de ficar público no proxy. No container Linux, a licença também deixou de chamar o comando VOL, que não existe fora do Windows.

---

### 🚨 O Desafio Técnico / Contexto
A interface /licenca e o proxy injetavam a API sem filtro de IP. Ao mesmo tempo, att_licenca.php executava VOL para ler o serial do volume. No container o shell respondia 'VOL: not found' e a licença não fechava.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O corte fica no Caddy, por IP de origem, e não só escondendo o link do portal.
* 💡 O log de acessos negados mostra quem tentou entrar e de qual superfície (licença, monitor ou Portainer).
* 💡 Em VPS de cliente o profile de licença nem sobe.
* 💡 No Linux o identificador estável vem de LORENTZ_STACK_HOST_ID, de um arquivo montado ou de /etc/machine-id. VOL e getmac continuam só no Windows.

---

### 🛠️ Especificação Técnica & Código-Chave
```php
function lorentz_stack_host_id_raw(): string
{
    $env = getenv('LORENTZ_STACK_HOST_ID');
    if ($env !== false && trim($env) !== '') {
        return preg_replace('/[^a-zA-Z0-9\-]/', '', trim($env));
    }
    foreach (['/var/lorentz/stack-host-id', '/etc/machine-id'] as $path) {
        if (is_readable($path)) {
            return trim((string) file_get_contents($path));
        }
    }
    return '';
}
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A emissão de licença fica restrita à rede de administração e o mesmo binário de licença passa a funcionar no container.

* **Projetos Relacionados**: `lorentz-vps-stack`, `supervisor`
* **Registro de Origem**: `_data/daily.dev-03.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
