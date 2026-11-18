---
layout: post
title: "A ação de automação devolvia 'enviado' sem enviar: um TODO que retorna sucesso é pior que um erro"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-114"
description: "As automações ofereciam enviar e-mail, enviar WhatsApp e criar tarefa, e o registro dizia que tudo tinha dado certo. As três ações eram um TODO que devolvia uma frase de sucesso."
date: 2026-11-04 00:00:00-03:00
categories: devlog
category: arquitetura
tags: [laravel, automacao, workflows, confiabilidade]
---

# A ação de automação devolvia 'enviado' sem enviar: um TODO que retorna sucesso é pior que um erro

> [!NOTE]
> **Resumo Executivo (DEV-2026-114)**: As automações ofereciam enviar e-mail, enviar WhatsApp e criar tarefa, e o registro dizia que tudo tinha dado certo. As três ações eram um TODO que devolvia uma frase de sucesso.

---

### 🚨 O Desafio Técnico / Contexto
O método tinha só o comentário TODO e um return com 'E-mail enviado'. A execução terminava como concluída e o formulário nem tinha campo para assunto ou texto. Falha real de webhook e ação desconhecida também terminavam como concluídas.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Enquanto não existe, o código deve falhar ou nem ser oferecido. Registro falso de sucesso esconde o problema de quem depende dele.
* 💡 A execução só conclui se todas as ações rodaram. Cada ação devolve se deu certo e o motivo, e o status final sai disso, e não de uma exceção que nunca é lançada.
* 💡 A falta de campo no formulário era a pista: ninguém conseguiria ter configurado aquele envio. Confira se a tela permite usar o que ela oferece.
* 💡 Tirar a opção da tela não basta. A validação do servidor também precisa recusá-la, e o que já está salvo com ela termina como falha.
* 💡 Enviar de verdade a clientes depende de consentimento, textos e custo. Por isso a correção parou na honestidade, e o envio real ficou para quem decide o produto.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
// Antes
protected function sendEmail(array $action, $entity): string
{
    // TODO: Implementar envio de e-mail
    return 'E-mail enviado';
}

// Depois
default => ['ok' => false, 'message' => "Ação {$type} não executada: não está disponível"],
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O registro de execução passou a dizer o que aconteceu, e a tela só oferece o que o sistema faz.

* **Projetos Relacionados**: `sistema-de-atendimento`
* **Registro de Origem**: `_data/daily.dev-19.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
