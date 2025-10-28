---
author: Mindusting
corrected: true
tags:
  - Programming/Git
title: Configuración de Git
---

# CONFIGURACIÓN DE GIT

> [!help]- REFERENCIAS WEB
> - [GIT-Config (doc)](https://git-scm.com/docs/git-config)

> [!important] IMPORTANTE
> Si quieres documentación más en detalle puede usar el comando:
> `git config --help`

Para cambiar la configuración de GIT se usa el comando `git config` este recibe una serie de argumentos que permite que amoldemos este programa a nuestro gusto, primero veremos la configuración más básica.

Si es la primera vez que creamos un [repositorio](commands/git_init.md) en el equipo, para cambiar la configuración ==dentro de nuestro usuarios del sistema== se hace siguiendo la siguiente sintaxis:

> [!abstract] SINTAXIS
> git config --gloval user.name "***\[name\]***"
> git config --gloval user.email "***\[email\]***"

```bash
git config --gloval user.name "Adelio"
git config --gloval user.email "adelio@email.com"
```

Las líneas las tendremos que escribir por separado en el terminal, este nombre y correo se usarán para indicar en el registro de versiones quién ha hecho los cambios, ya que podremos trabajar en grupo con otras personas (*Y así en caso de que se rompa algo, saber a quién hay que echarle la bronca*).

## SCOPE DE LA CONFIGURACIÓN

Podemos indicar mediante el *scope* hasta donde queremos que se aplique la configuración, lo más normal es elegir la opción `--glova`, tenemos en total tres opciones básicas:

- `--system`: Se guarda en el archivo `/etc/gitconfig`, se aplica a todo el equipo.
- `--gloval`: Se guarda en el archivo `~/.gitconfig` o `~/.config/git/config`, se aplica sobre el usuario.
- `--local`: (*Opción por defecto estando dentro de un [repositorio](commands/git_init.md)*) Se guarda en el archivo `./.git/config` (*siendo este el [repositorio](commands/git_init.md) de git*), se aplica a el [repositorio](commands/git_init.md).

> [!abstract] SINTAXIS
> git config ***\[scope\] ...***

> [!note] NOTA
> Cada nivel sobrescribe los datos del nivel anterior.
> 
> Por lo que si ponemos un nombre de usuario en `--gloval` y luego ponemos otro en `--local`, se aplicará el que se encuentre en `--local`, ya que es el que se encuentra más cerca al [repositorio](commands/git_init.md).

## REVISA TU CONFIGURACIÓN

Para poder ver tu propia configuración se puede hacer usando el parámetro `--list` de la siguiente forma:

```bash
git config --list
```
