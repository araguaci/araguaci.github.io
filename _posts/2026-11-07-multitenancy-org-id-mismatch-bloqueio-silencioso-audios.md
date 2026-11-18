---
layout: post
title: "Divergência de identificador de organização entre microsserviços bloqueava ingestão de gravações de voz"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-134"
description: "A integração entre o PABX e o CRM de gravações não gerava erros nos logs mas a lista de áudios permanecia vazia. O mecanismo de segurança multi-tenant bloqueava o processo silenciosamente porque a variável de ambiente apontava para uma organização diferente da cadastrada no banco."
date: 2026-11-07 00:00:00-03:00
categories: devlog
category: arquitetura
tags: [multitenancy, microservices, audio, postgresql, docker, lgpd]
---

# Divergência de identificador de organização entre microsserviços bloqueava ingestão de gravações de voz

> [!NOTE]
> **Resumo Executivo (DEV-2026-134)**: A integração entre o PABX e o CRM de gravações não gerava erros nos logs mas a lista de áudios permanecia vazia. O mecanismo de segurança multi-tenant bloqueava o processo silenciosamente porque a variável de ambiente apontava para uma organização diferente da cadastrada no banco.

---

### 🚨 O Desafio Técnico / Contexto
O diretório de monitoramento de áudios continha gravações gravadas pelo Asterisk, porém a tela de gravações do CRM exibia estado vazio sem disparar exceções de rede ou falha de porta.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 A checagem estrita de vínculo entre PABX e organização impedia a ingestão quando o identificador de ambiente divergia do slug do banco.
* 💡 Validadores de multi-tenant devem emitir alertas explícitos no log ou suportar fallback para o tenant padrão quando o ambiente for dedicado.
* 💡 A entrega de áudio deve ser intermediada por proxy autenticado no CRM, preservando o arquivo bruto no storage e auditando cada escuta sob a LGPD.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
export function isIpLiveLinkedToOrg(orgId: string) {
  const linked = getIpLiveLinkedOrgId();
  return !linked || linked === orgId || orgId === "org_artesdosul_default";
}
```

---

### 📈 Impacto no Ecossistema & Valor Prático
As gravações existentes foram imediatamente importadas e o player de áudio HTML5 passou a funcionar com streaming controlado e auditoria de escuta.

* **Projetos Relacionados**: `triade-artesdosul`, `ecosul`, `iplive`
* **Registro de Origem**: `_data/daily.dev-21.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
