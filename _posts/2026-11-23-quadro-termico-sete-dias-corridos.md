---
layout: post
title: "O quadro térmico do legado conta sete dias corridos, não a média do dia da semana"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-169"
description: "O monitor do atendimento presencial média o mesmo dia da semana ao longo de várias semanas. No Supervisor legado o quadro passou a contar as chamadas de cada hora dos últimos sete dias corridos, com escala própria para receptivas e para ativas."
date: 2026-11-23 00:00:00-03:00
categories: devlog
category: telefonia
tags: [sql, php, cti, termico]
---

# O quadro térmico do legado conta sete dias corridos, não a média do dia da semana

> [!NOTE]
> **Resumo Executivo (DEV-2026-169)**: O monitor do atendimento presencial média o mesmo dia da semana ao longo de várias semanas. No Supervisor legado o quadro passou a contar as chamadas de cada hora dos últimos sete dias corridos, com escala própria para receptivas e para ativas.

---

### 🚨 O Desafio Técnico / Contexto
Copiar Indicadores::termal() juntaria as segundas-feiras de semanas diferentes numa célula só. A leitura pedida é o que aconteceu de fato, do dia mais antigo até hoje, somando todos os agentes e podendo separar um. Receptivas e ativas não têm o mesmo teto: uma escala única deixa a série menor quase sem cor. Duas grades lado a lado, dentro de uma página de 1200px, não cabem um dia cheio de horas.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 A janela é DATEADD(DAY, -6, CONVERT(date, GETDATE())) até a meia-noite seguinte, exclusive. O dia sai com CONVERT(char(10), hora, 120), que o SQL Server antigo já devolve como aaaa-mm-dd. A hora é DATEPART(hour, ...).
* 💡 Receptivas leem CTI_CHAMADA.HoraEntrada. Com um agente, um EXISTS em CTI_ATENDIMENTO exige o mesmo NumChamada, o CodAgente e Atendida = 'S', então a chamada entra uma vez. Ativas leem CTI_CHAMADA_ATIVA.HoraIni e, no filtro, o CodAgente. A lista é a união de quem atendeu ou discou na janela.
* 💡 As duas grades usam o menor e o maior horário com volume em qualquer uma, para as colunas coincidirem. Cada grade divide a quantidade pelo próprio máximo e pinta com rgba(11, 92, 173, alpha). Abaixo de 0,12 o alpha sobe para 0,12. A partir de 0,55 o número fica branco.
* 💡 Meia página de 1200px fica em torno de 568px. Dezesseis colunas de 32px mais 72px de rótulo passam disso e abrem barra interna. A grade ficou numa coluna. Num viewport de 1281px ela mediu 1118px dentro de um cartão de 1150px, sem rolagem horizontal.
* 💡 Código de agente que não está na lista volta para a soma geral só se a consulta da lista não falhou. Se a lista falha, o filtro pedido permanece. O id entra com intval. A página é PHP 5.6: array(), sem o operador de coalescência.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
WHERE c.HoraEntrada >= DATEADD(DAY, -6, CONVERT(date, GETDATE()))
  AND c.HoraEntrada < DATEADD(DAY, 1, CONVERT(date, GETDATE()))
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O monitoramento mostra a semana que passou, e o quadro do turno continua sendo o agora.

* **Projetos Relacionados**: `supervisor-elevar-legado`, `lorentz-atp`
* **Registro de Origem**: `_data/daily.dev-32.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
