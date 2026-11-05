---
layout: post
title: "Somar todos os pontos do GPS conta quilômetro com a moto parada, e isso não serve para pagar comissão"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-128"
description: "O km de cada monitor ia virar base de comissão, e o cálculo somava todos os pontos recebidos. A soma passou a descartar ruído, salto e falta de sinal, com os limites escritos e testados."
date: 2026-11-04 00:00:00-03:00
categories: devlog
category: backend
tags: [gps, laravel, php, geolocalizacao, testes]
---

# Somar todos os pontos do GPS conta quilômetro com a moto parada, e isso não serve para pagar comissão

> [!NOTE]
> **Resumo Executivo (DEV-2026-128)**: O km de cada monitor ia virar base de comissão, e o cálculo somava todos os pontos recebidos. A soma passou a descartar ruído, salto e falta de sinal, com os limites escritos e testados.

---

### 🚨 O Desafio Técnico / Contexto
A distância era a soma da fórmula de haversine entre pontos consecutivos. Parado, o GPS oscila alguns metros, e cada oscilação virava distância. O cálculo também usava só os pontos que cabiam no limite do mapa.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 Meça a partir do último ponto aceito, e não do anterior. Um passo mínimo de 30 metros elimina a oscilação com a moto parada.
* 💡 Ponto com precisão pior que 50 metros é descartado, e o ponto seguinte volta a medir do último bom.
* 💡 Velocidade acima de 150 km/h entre dois pontos é erro de leitura. Mais de 15 minutos sem sinal também não soma, porque a linha reta não diz por onde a moto andou.
* 💡 Número que vira dinheiro precisa de dia a dia para conferência. O total sozinho não permite contestar nem corrigir.
* 💡 O filtro não cobre tudo: o celular pode parar de enviar com a tela bloqueada, o que tira km de quem trabalhou. Isso só se confere em ronda real, e ainda não foi testado.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
if ($km * 1000 < self::MIN_STEP_M) {        // parado: só atualiza o tempo
    $this->anchor['t'] = $timestamp;
    return 0.0;
}
if ($km / ($seconds / 3600) > self::MAX_SPEED_KMH) {
    return 0.0;                             // salto impossível
}
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A rota do dia e o relatório mensal usam o mesmo cálculo, e a regra pode ser explicada a quem recebe por ele.

* **Projetos Relacionados**: `monitor-laravel`
* **Registro de Origem**: `_data/daily.dev-20.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
