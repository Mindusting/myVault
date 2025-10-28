---
author: Mindusting
corrected: false
tags:
  - Programming/Git
title: Git
---

<h1 align="center" style="color:df4c37;">GIT</h1>

![#logo](../../img/git.png)

---

# GIT

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Hay que hacerle un logo a esta documentación.
> > - [ ] Explicar para qué sirve git.
> > - [ ] Explicar el funcionamiento interno de git.
> > - [ ] Explicar como instalar git.
> > - [x] Explicar el comando `init`.
> > - [ ] Explicar el comando `status`.
> > - [ ] Explicar el comando `add`.
> > - [ ] Explicar el comando `commit`.
> > - [ ] Explicar el comando `log`.
> > - [ ] Explicar el comando `reset`.
> >     git reset --hard ***\[commit_hex_code\]***

> [!help]- REFERENCIAS WEB
> - [GIT (Doc)](https://git-scm.com/doc)
> - [GIT (PDF)](https://git-scm.com/book/en/v2)
> - [W3 Schools](https://www.w3schools.com/git/default.asp?remote=github)
>
> YouTube:
> - [codingjerk](https://youtu.be/G3NJzFX6XhY)
> - [pildorasinformaticas](https://www.youtube.com/playlist?list=PLU8oAlHdN5BlyaPFiNQcV0xDqy0eR35aU)
> - [MoureDev by Brais Moure](https://youtu.be/3GymExBkKjE)
> - [Informatica Live (Git)](https://youtu.be/NvazARiMEIw)

**Git** es un sistema de control de versiones distribuido. Permite guardar el historial de cambios de un proyecto, trabajar en equipo y volver a estados anteriores del código fácilmente.

## ÍNDICE

- [Instalación de GIT](git_install.md)
- [Versión](commands/git_version.md)
- [Configuración](commands/git_config.md)
- [Crear repositorios](commands/git_init.md)
- [Añadir archivos](commands/git_add.md)
- [Estado de configuración](commands/git_status.md)
- [Ignorar archivos](git_ignore.md)
- [Clonar repositorio](git_remote.md)

## COMMIT

> [!abstract] SINTAXIS
> git commit -m "***\[comment\]***"
> git commit -am "***\[comment\]***"
> git commit --amend

## REGISTRO

> [!abstract] SINTAXIS
> git log --oneline

## RESTABLECER

> [!abstract] SINTAXIS
> git reset --hard ***\[code\]***

## SUBIR CAMBIOS

> [!abstract] SINTAXIS
> git push -u original main

## BAJAR CAMBIOS

> [!abstract] SINTAXIS
> git pull

## SUBIR RAMA A GITHUB

> [!abstract] SINTAXIS
> git push -u origin ***\[nombreDeRama\]***

---
---
---
---
---


