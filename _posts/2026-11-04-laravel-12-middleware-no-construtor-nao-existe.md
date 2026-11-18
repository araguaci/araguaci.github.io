---
layout: post
title: "No Laravel 12, $this->middleware() no construtor do controller não existe mais"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-122"
description: "Oito controllers de API chamavam $this->middleware() no construtor. O controller base mais novo não tem esse método, então essas rotas respondem 500 com Call to undefined method."
date: 2026-11-04 00:00:00-03:00
categories: devlog
category: backend
tags: [laravel, controllers, atualizacao, api]
---

# No Laravel 12, $this->middleware() no construtor do controller não existe mais

> [!NOTE]
> **Resumo Executivo (DEV-2026-122)**: Oito controllers de API chamavam $this->middleware() no construtor. O controller base mais novo não tem esse método, então essas rotas respondem 500 com Call to undefined method.

---

### 🚨 O Desafio Técnico / Contexto
Desde o Laravel 11, a classe Controller do esqueleto é vazia e não herda o método middleware(). Os controllers antigos foram mantidos, e o erro só aparecia ao chamar a rota. Parte dos testes dessas APIs falhava por isso.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O erro só aparece em tempo de execução. O php -l passa, e só um teste que chama a rota mostra.
* 💡 Antes de remover a linha, confira se a rota já exige login pelo grupo: php artisan route:list --path=api/x --json mostra o middleware aplicado.
* 💡 A linha pedia auth:sanctum, e o grupo usa auth. Remover mantém o login, mas não necessariamente o mesmo mecanismo pensado na época.
* 💡 Remover pode ligar uma rota que estava morta. Leia o que ela faz antes, porque ela pode nunca ter sido exercitada com essa versão.
* 💡 A alternativa para middleware por controller é declarar no grupo de rotas ou implementar a interface HasMiddleware.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
# Quantos ainda têm o problema?
grep -rln '$this->middleware(' app/Http/Controllers
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Os controllers com o erro ficaram listados, e os que tratam de dado sensível só voltam depois de revisados.

* **Projetos Relacionados**: `sistema-de-atendimento`
* **Registro de Origem**: `_data/daily.dev-19.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
