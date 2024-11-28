---
author: Mindusting
corrected: false
tags:
  - Programming/Git
title: Git
---

# GIT

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

> [!help] REFERENCIAS WEB
> - [W3](https://www.w3schools.com/git/default.asp?remote=github)
>
> YouTube:
> - [pildorasinformaticas](https://www.youtube.com/playlist?list=PLU8oAlHdN5BlyaPFiNQcV0xDqy0eR35aU)

## VERSIÓN

> [!abstract] SINTAXIS
> git version

## CONFIGURACIÓN

Establece el usuario y correo electrónico.

> [!abstract] SINTAXIS
> git config --gloval user.name "***\[name]***"
> git config --gloval user.email "***\[email]***"

## CREAR UN ÁREA DE TRABAJO

> [!abstract] SINTAXIS
> git init

> [!note]
> Al usar este comando se genera en la carpeta actual una carpeta llamada `.git`, en esta se guardará información a cerca del área de trabajo.

## AÑADIR UN ARCHIVO

> [!abstract] SINTAXIS
> git add ***\[file/path]***

## ESTADO

> [!abstract] SINTAXIS
> git status -s

- `??`: No se hace copias.
- `A`: Está añadido.
- `M`: Está modificado.

## COMMIT

> [!abstract] SINTAXIS
> git commit -m "***\[comment]***"
> git commit -am "***\[comment]***"
> git commit --amend

## REGISTRO

> [!abstract] SINTAXIS
> git log --oneline

## RESTABLECER

> [!abstract] SINTAXIS
> git reset --hard ***\[code]***

## SUBIR CAMBIOS

> [!abstract] SINTAXIS
> git push -u original main

## BAJAR CAMBIOS

> [!abstract] SINTAXIS
> git pull
