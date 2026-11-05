---
layout: post
title: "O campo status existia e o login não olhava: quem foi desligado continuava entrando no sistema"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-129"
description: "Ao criar logins individuais, apareceu que usuário inativo entrava normalmente. O login passou a recusá-lo, a sessão aberta é encerrada e a situação do login acompanha a do cadastro."
date: 2026-11-04 00:00:00-03:00
categories: devlog
category: seguranca
tags: [laravel, autenticacao, middleware, seguranca, testes]
---

# O campo status existia e o login não olhava: quem foi desligado continuava entrando no sistema

> [!NOTE]
> **Resumo Executivo (DEV-2026-129)**: Ao criar logins individuais, apareceu que usuário inativo entrava normalmente. O login passou a recusá-lo, a sessão aberta é encerrada e a situação do login acompanha a do cadastro.

---

### 🚨 O Desafio Técnico / Contexto
A tabela de usuários tinha a coluna status, mas o AuthenticatesUsers só confere e-mail e senha. O teste do bloqueio também mostrou outro furo: a verificação de troca obrigatória de senha rodava antes da verificação de inativo, então a pessoa desligada ainda ficava logada na tela de senha.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Coluna de situação não faz nada sozinha. Inclua o status em credentials() no LoginController.
* 💡 Recusar o login não basta: a sessão já aberta continua valendo. Um middleware próprio encerra a sessão a cada requisição.
* 💡 A ordem dos middlewares é regra de segurança. O de usuário ativo vem antes de qualquer um que redirecione.
* 💡 O cadastro de origem deve comandar o acesso: ao inativar ou excluir o funcionário, o login é bloqueado sem depender de alguém lembrar.
* 💡 Formulário com $request->all() e user_id em $fillable permitia vincular qualquer usuário. O vínculo passou a existir só na ação própria.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
protected function credentials(Request $request): array
{
    return $request->only($this->username(), 'password') + ['status' => 'active'];
}

// bootstrap/app.php: o primeiro da fila
$middleware->web(append: [EnsureActiveUser::class, RequirePasswordChange::class]);
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Desligar um funcionário no cadastro passou a encerrar o acesso dele na requisição seguinte.

* **Projetos Relacionados**: `monitor-laravel`
* **Registro de Origem**: `_data/daily.dev-20.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
