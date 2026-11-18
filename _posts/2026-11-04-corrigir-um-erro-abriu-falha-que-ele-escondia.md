---
layout: post
title: "Corrigir um erro abriu uma falha de segurança que ele escondia"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-117"
description: "Uma rota usava o tipo enviado pelo cliente como nome de classe, sem conferir a empresa, mas outro erro a derrubava antes. Ao remover esse erro, a falha ficou alcançável, e isso só ficou claro ao testar o ataque contra o código original."
date: 2026-11-04 00:00:00-03:00
categories: devlog
category: seguranca
tags: [seguranca, laravel, multi-tenant, api]
---

# Corrigir um erro abriu uma falha de segurança que ele escondia

> [!NOTE]
> **Resumo Executivo (DEV-2026-117)**: Uma rota usava o tipo enviado pelo cliente como nome de classe, sem conferir a empresa, mas outro erro a derrubava antes. Ao remover esse erro, a falha ficou alcançável, e isso só ficou claro ao testar o ataque contra o código original.

---

### 🚨 O Desafio Técnico / Contexto
A linha $validated['entity_type']::findOrFail($id) aceitava qualquer classe e registros de qualquer empresa. No branch principal a rota respondia 500 por outro motivo. O teste de ataque respondeu 200 na cópia de trabalho, depois de eu ter removido esse outro erro.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Nunca use texto da requisição como nome de classe. Use uma lista fechada de apelidos e confira a empresa do registro.
* 💡 Responda 404 também para o registro de outra empresa, para não revelar que ele existe.
* 💡 Um erro pode estar protegendo por acidente. Antes de consertar um 500 em uma rota sensível, leia o que vem depois dele.
* 💡 Avalie a gravidade na versão de referência, e não na cópia alterada. Eu tinha chamado de urgente uma falha que, no branch principal, ainda estava inalcançável.
* 💡 Procure o padrão no projeto todo: a mesma linha estava em outro controller, parado pelo mesmo erro.
* 💡 A ação de alterar campo também precisa de limite: mudar company_id moveria o registro para outra empresa.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
public function resolve(array $types, string $type, int $id, int $companyId): Model
{
    $class = $types[$type] ?? (in_array($type, $types, true) ? $type : null);
    abort_if($class === null, 404);

    $entity = $class::findOrFail($id);
    abort_unless($this->companyOf($entity) === $companyId, 404);

    return $entity;
}
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O acesso entre empresas foi fechado com 15 testes que falham sem a correção, e a urgência passou a ser medida na versão de referência.

* **Projetos Relacionados**: `sistema-de-atendimento`
* **Registro de Origem**: `_data/daily.dev-19.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
