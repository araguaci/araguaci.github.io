---
layout: post
title: "FoneOcupado guarda o apelido de quem ocupa o ramal"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-170"
description: "O quadro do turno precisa distinguir livre, pausa e ligação. A coluna que parece um sinal de sim ou não recebe o apelido de outra pessoa, gravado quando o ramal dela está em IdTelefone."
date: 2026-11-23 00:00:00-03:00
categories: devlog
category: telefonia
tags: [sql, cti, php]
---

# FoneOcupado guarda o apelido de quem ocupa o ramal

> [!NOTE]
> **Resumo Executivo (DEV-2026-170)**: O quadro do turno precisa distinguir livre, pausa e ligação. A coluna que parece um sinal de sim ou não recebe o apelido de outra pessoa, gravado quando o ramal dela está em IdTelefone.

---

### 🚨 O Desafio Técnico / Contexto
Ler FoneOcupado como S ou 1 deixa a posição sempre livre ou sempre ocupada, conforme o texto que estiver gravado. O inteiro da posição é IdEstadoRamal. FoneOcupado é o apelido copiado de quem está no telefone.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 att_phoenix.php atualiza SAC_FUNCIONARIO A com o Apelido de B quando A.IdTelefone = B.RamalFunc e A.IdTelefone não é vazio. Quando o ramal libera, o mesmo fluxo zera FoneOcupado e grava IdEstadoRamal = 0.
* 💡 elevar_situacao olha o motivo da pausa antes. Se o motivo não é vazio, login, logout nem pausa desligada, a posição é pausa. Só então um FoneOcupado não vazio vira ligação. Vazio, com a pausa desligada, fica livre.
* 💡 A tabela de estado é CTI_ESTADO_AGENTE. Se EW_PHOENIX_3CX está definido e verdadeiro, elevar_tabela_estado() troca para CTI_ESTADO_AGENTE_LOGADO. O quadro fica no login de hoje ainda sem DataFim.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
Update A Set A.FoneOcupado = B.Apelido
  From SAC_FUNCIONARIO A, SAC_FUNCIONARIO B
 Where A.IdTelefone = B.RamalFunc
   And A.IdTelefone <> ''
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Pausa não vira ligação por causa de um texto no ramal, e ligação não depende de um S na coluna errada.

* **Projetos Relacionados**: `supervisor-elevar-legado`
* **Registro de Origem**: `_data/daily.dev-32.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
