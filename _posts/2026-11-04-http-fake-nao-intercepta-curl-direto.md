---
layout: post
title: "O teste do webhook passou pelo motivo errado: Http::fake não intercepta curl direto"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-121"
description: "O teste de webhook com erro passou, enquanto o de sucesso falhou. O model usava curl direto, então a simulação não valia e o teste tentava sair para a rede de verdade."
date: 2026-11-04 00:00:00-03:00
categories: devlog
category: backend
tags: [laravel, testes, http, xdebug, curl]
---

# O teste do webhook passou pelo motivo errado: Http::fake não intercepta curl direto

> [!NOTE]
> **Resumo Executivo (DEV-2026-121)**: O teste de webhook com erro passou, enquanto o de sucesso falhou. O model usava curl direto, então a simulação não valia e o teste tentava sair para a rede de verdade.

---

### 🚨 O Desafio Técnico / Contexto
Http::fake só intercepta o cliente HTTP do Laravel, e o model chamava curl_init. O teste de erro passava porque a conexão a um domínio inexistente falhava de verdade. Uma resposta HTTP 500 também gerava mensagem de erro vazia, porque curl_error só informa falha de conexão.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Um teste de falha pode passar por qualquer falha. Confira também o motivo, por exemplo se a mensagem contém HTTP 500.
* 💡 Trocar curl pelo cliente do Laravel torna o código testável sem rede e leva o motivo do erro para o registro.
* 💡 O teste de sucesso é o controle: ele mostrou que a simulação não estava valendo.
* 💡 Http::failedConnection e exceção lançada dentro de Http::fake derrubaram o PHP 8.3 com falha de segmentação com o Xdebug no modo develop. Para simular conexão recusada, uma porta local fechada funciona sem simulação.
* 💡 Falha de segmentação não deixa relatório do teste: exit 139 e saída vazia. Rode os testes um a um para isolar o culpado.

---

### 🛠️ Especificação Técnica & Código-Chave
```javascript
try {
    $response = Http::withHeaders($this->headers ?? [])
        ->timeout($this->timeout)
        ->send($this->method, $this->url, ['json' => $payload]);
} catch (ConnectionException $e) {
    return ['success' => false, 'error' => $e->getMessage()];
}
```

---

### 📈 Impacto no Ecossistema & Valor Prático
Os testes de webhook passaram a provar o resultado sem depender da rede, e a falha grava o motivo.

* **Projetos Relacionados**: `sistema-de-atendimento`
* **Registro de Origem**: `_data/daily.dev-19.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
