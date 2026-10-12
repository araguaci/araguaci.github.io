---
layout: post
title: "Imagem live entra no WSL pelo squashfs, não pelo ISO"
subtitle: "Diário de Desenvolvimento 2026 • Registro #DEV-2026-072"
description: "O WSL não dá boot num ISO. A distro passa a existir quando o rootfs do squashfs vira um tar com dono numérico e entra por wsl --import."
date: 2026-10-10 00:00:00+00:00
categories: devlog
category: windows
tags: [wsl, debian, locale, apt]
---

# Imagem live entra no WSL pelo squashfs, não pelo ISO

> [!NOTE]
> **Resumo Executivo (DEV-2026-072)**: O WSL não dá boot num ISO. A distro passa a existir quando o rootfs do squashfs vira um tar com dono numérico e entra por wsl --import.

---

### 🚨 O Desafio Técnico / Contexto
Uma imagem live amd64 de Debian foi montada no Windows, mas o WSL só importa sistema de arquivos. Extrair o squashfs direto no NTFS perderia dono e suid. No login, o bash avisava que en_US.UTF-8 não existia. O apt falhava ao criar a lista parcial. Um unit de zram falhava no kernel do WSL.

---

### 💡 Principais Lições Aprendidas & Descobertas
* 💡 O rootfs da imagem live está em live/filesystem.squashfs. O import é wsl --import de um tar feito com --numeric-owner, não a montagem do ISO.
* 💡 unsquashfs num disco NTFS via /mnt grava tudo como o usuário do Windows. O caminho que preserva dono é um ext4 em loop, e só então o tar.
* 💡 A imagem live sobe graphical.target com live-config e LightDM. No WSL esses units se mascaram e o default.target aponta para multi-user.target. O kernel que roda é o do WSL.
* 💡 apt-get update devolve Permission denied se /var/lib/apt/lists/partial não existe ou não pertence ao usuário _apt.
* 💡 systemd-zram-setup@zram0 falha no kernel Microsoft. Mascarar systemd-zram-setup@.service e gravar zram-size=0 em /etc/systemd/zram-generator.conf.
* 💡 A imagem só tinha as locales C e POSIX. O terminal pede en_US.UTF-8. locale-gen en_US.UTF-8 e update-locale LANG=en_US.UTF-8 tiram o aviso setlocale no login.

---

### 🛠️ Especificação Técnica & Código-Chave
```yaml
grep -q '^en_US.UTF-8 UTF-8' /etc/locale.gen || echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen
locale-gen en_US.UTF-8
update-locale LANG=en_US.UTF-8
```

---

### 📈 Impacto no Ecossistema & Valor Prático
A distro importada abre shell, resolve repositório e não repete o aviso de locale no login.

* **Projetos Relacionados**: `raspios-wsl`
* **Registro de Origem**: `_data/daily.dev-11.yml`

---
*Publicado originalmente como parte do Diário de Desenvolvimento 2026 do ecossistema Artes do Sul & Araguaci.*
