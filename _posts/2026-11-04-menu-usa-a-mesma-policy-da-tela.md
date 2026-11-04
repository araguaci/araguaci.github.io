---
layout: post
title: "O menu usa a mesma policy da tela, e nenhum perfil vê um link que dá 403"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-105"
description: "O operador via no menu telas que devolviam 403, porque o menu tinha uma regra e a tela outra. Com as duas usando a mesma policy, um teste percorre o menu de cada perfil e garante que elas continuem iguais."
date: 2026-11-04 00:00:00-03:00
categories: devlog
category: arquitetura
tags: [laravel, policy, inertia, vue, permissoes, ux]
---

# O menu usa a mesma policy da tela, e nenhum perfil vê um link que dá 403

> [!NOTE]
> **Resumo Executivo (DEV-2026-105)**: O operador via no menu telas que devolviam 403, porque o menu tinha uma regra e a tela outra. Com as duas usando a mesma policy, um teste percorre o menu de cada perfil e garante que elas continuem iguais.

---

### 🚨 O Desafio Técnico / Contexto
Em um sistema de 148 telas, abrir cada módulo com cada perfil mostrou o operador vendo Usuários, Empresas e Licenças no menu, todas com 403. A diretoria também pediu ambiente com menu lateral ou com blocos e cards, ajustável por perfil.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Meça antes de mexer: abrir tudo com cada perfil revelou o problema real, que uma revisão visual do menu não mostraria.
* 💡 ModuleAccess pergunta ao Gate usando viewAny, a mesma permissão da tela. Assim, o menu acompanha qualquer mudança de permissão sem manutenção à parte.
* 💡 A limpeza roda ao gravar e ao ler o layout. Gravar barra requisição forjada, e ler tira da tela salva o que perdeu permissão ou licença depois.
* 💡 Num sistema grande, trocar o shell primeiro melhora todas as telas de uma vez. O interior de cada uma fica para a etapa seguinte, e a nota do guia deixa isso à vista: 4,5 para 8,5 de 15.
* 💡 Esconder um item do menu não retira a permissão, e a tela de configuração avisa isso. Sem o aviso, o administrador pensa que bloqueou o acesso.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
public function roleAllows(User $user, string $moduleName): bool
{
    $model = config("ui_shell.module_policies.{$moduleName}");

    return $model === null || Gate::forUser($user)->allows('viewAny', $model);
}
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Em 20 testes dedicados, nenhum item do menu leva a tela recusada, e um perfil de uma empresa não afeta outra.

* **Projetos Relacionados**: `omnichannel-system`
* **Registro de Origem**: `_data/daily.dev-17.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
