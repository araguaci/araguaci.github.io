---
layout: post
title: "O laço de reparo removeu as tabelas que tinha acabado de criar, e a tela só quebrou depois"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-108"
description: "Ao reparar a base de dev, um laço repetiu o passo de remover tabelas vazias antes de cada migration e apagou quatro tabelas recém-criadas. Sem nenhum dado perdido, o erro só apareceu quando o usuário abriu uma tela que dependia delas."
date: 2026-11-04 00:00:00-03:00
categories: devlog
category: devops
tags: [mysql, laravel, migrations, incidente, verificacao]
---

# O laço de reparo removeu as tabelas que tinha acabado de criar, e a tela só quebrou depois

> [!NOTE]
> **Resumo Executivo (DEV-2026-108)**: Ao reparar a base de dev, um laço repetiu o passo de remover tabelas vazias antes de cada migration e apagou quatro tabelas recém-criadas. Sem nenhum dado perdido, o erro só apareceu quando o usuário abriu uma tela que dependia delas.

---

### 🚨 O Desafio Técnico / Contexto
/pause-reasons passou a responder 500 com 'Table support_tickets doesn't exist', embora a migration constasse como executada. A remoção de tabelas vazias foi repetida a cada passada do laço, e a segunda passada levou as tabelas que a primeira tinha criado.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Passo destrutivo fica fora do laço e roda uma vez, sobre uma lista conferida. 'Só apaga se estiver vazia' não protege uma tabela recém-criada, porque ela ainda está vazia.
* 💡 A tabela de migrations registra o que rodou, não o que existe. Ao remover uma tabela à mão, apague também o registro, ou a migration nunca mais será executada.
* 💡 A restauração precisa incluir as migrations seguintes: a coluna requester_phone, de outra migration, tinha sumido junto com a tabela.
* 💡 A verificação anterior só abriu as telas principais dos fluxos, e nenhuma delas usava essas tabelas. Depois de reparar a base, abra todas as telas do menu de cada perfil.
* 💡 A auditoria agora confere se cada model tem tabela, e a varredura abriu 37, 34, 10 e 8 telas nos quatro perfis, todas com 200. Ela confere só o status, não as ações internas.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
// Todo model tem tabela?
$t = (new $c)->getTable();
if (! Schema::hasTable($t)) {
    $faltam[] = "$c ($t)";
}
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O reparo de base passou a terminar com a conferência de todos os models e de todas as telas por perfil, não só dos fluxos em andamento.

* **Projetos Relacionados**: `omnichannel-system`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
