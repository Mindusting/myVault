---
author: Mindusting
corrected: false
tags:
  - Programming/Git
title: Git
---

# GIT

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Hay que hacerle un logo a esta documentación.
> > - [ ] Explicar para qué sirve git.
> > - [ ] Explicar el funcionamiento interno de git.
> > - [ ] Explicar como instalar git.
> > - [ ] Explicar el comando `init`.
> > - [ ] Explicar el comando `status`.
> > - [ ] Explicar el comando `add`.
> > - [ ] Explicar el comando `commit`.
> > - [ ] Explicar el comando `log`.
> > - [ ] Explicar el comando `reset`.
> >     git reset --hard ***\[commit_hex_code\]***

> [!help]- REFERENCIAS WEB
> - [W3](https://www.w3schools.com/git/default.asp?remote=github)
>
> YouTube:
> - [pildorasinformaticas](https://www.youtube.com/playlist?list=PLU8oAlHdN5BlyaPFiNQcV0xDqy0eR35aU)

## ÍNDICE

- [Versión](git_version.md)
- [Configuración](git_config.md)
- [Crear repositorios](git_init.md)
- [Añadir archivos](git_add.md)
- [Estado de configuración](git_status.md)
- [Clonar repositorio](git_clone.md)

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
