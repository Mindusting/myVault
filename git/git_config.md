---
author: Mindusting
corrected: false
tags:
  - Programming/Git
title: Configuración de Git
---

# CONFIGURACIÓN

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar la configuración global y local.
> > - [ ] Documentar el listado de la documentación.

Establece el usuario y correo electrónico.

> [!abstract] SINTAXIS
> git config ***\[scope\] \[key\] \[value\]***

> [!abstract] SINTAXIS
> git config --gloval user.name "***\[name]***"
> git config --gloval user.email "***\[email]***"

```bash
git config --gloval user.name "Adelio"
git config --gloval user.email "adelio@email.com"
```

## SCOPE

1. `--system`: Se aplica sobre el archivo `/etc/gitconfig`, se aplica a todo el equipo.
2. `--gloval`: Se aplica sobre el archivo `~/.gitconfig` o `~/.config/git/config`, se aplica sobre el usuario.
3. `--local`: (*Opción por defecto estando dentro de un repositorio*) Se aplica sobre el archivo `./.git/config` (*Siendo este el repositorio de git*), se aplica a el repositorio.

> [!note] NOTA
> Cada nivel sobre escribe los datos del nivel anterior.

## REVISA TU CONFIGURACIÓN

Para poder ver tu propia configuración se puede hacer usando el parámetro `--list` de la siguiente forma:

```bash
git config --list
```
