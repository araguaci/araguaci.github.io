---
layout: post
title: "O CTI só grava Atendida igual a S quando o atendimento cai num tronco"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-142"
description: "Chamadas de teste atendidas em ramal interno tinham duração e continuavam com Atendida igual a N. O relatório lia o flag certo. Quem só grava S é o ramo de tronco do CTI."
date: 2026-10-29 00:00:00-03:00
categories: devlog
category: telefonia
tags: [cti, asterisk, sqlserver, powerdialing, relatorio]
---

# O CTI só grava Atendida igual a S quando o atendimento cai num tronco

> [!NOTE]
> **Resumo Executivo (DEV-2026-142)**: Chamadas de teste atendidas em ramal interno tinham duração e continuavam com Atendida igual a N. O relatório lia o flag certo. Quem só grava S é o ramo de tronco do CTI.

---

### 🚨 O Desafio Técnico / Contexto
No ensaio do PowerDialing, as ligações ativas foram atendidas em ramais do próprio PABX. O relatório de CTI_CHAMADA_ATIVA mostrou HoraIni e HoraFim preenchidos e Atendida igual a N. A linha nasce com N. O update para S não rodou, porque aquelas pernas não eram tronco.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 AtualizaAtendidaChamadaAtiva em clsData.vb faz UPDATE Cti_Chamada_Ativa SET Atendida = 'S' para o NumChamada.
* 💡 Em cls3cx.vb essa chamada só ocorre dentro de If Canal.Tronco, e só enquanto ChamadaAtivaAtendida ainda é falso.
* 💡 Tempo de conversa e flag de atendida são escritos por caminhos diferentes. Duração preenchida não implica Atendida = S.
* 💡 Teste de campanha com ramal interno completa a ligação e deixa o flag em N. Para ver S, o atendimento tem de cair num tronco.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
If Canal.Tronco Then
    If Canal.NumChamadaAtiva > 0 And Canal.ChamadaAtivaAtendida = False Then
        objData.AtualizaAtendidaChamadaAtiva(Canal.NumChamadaAtiva)
        Canal.ChamadaAtivaAtendida = True
    End If
End If
```

---

### 📈 Impacto no Ecossistema & Valor Prático
O ensaio interno deixa de ser lido como chamada perdida, e o flag S fica reservado ao atendimento que passa por tronco.

* **Projetos Relacionados**: `LorentzCTI`, `supervisor`
* **Registro de Origem**: `_data/daily.dev-24.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
