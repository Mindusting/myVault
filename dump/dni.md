---
aliases:
  - Documento Nacional de Identidad
author: Mindusting
corrected: true
tags:
  - DNI
title: DNI
rating: 0.75
---

# Documento Nacional de Identidad

Un **DNI** se constituye de ocho dígitos numéricos y una letra; lo que mucha gente no sabe es que la letra se puede calcula a partir de la parte numérica, esto es ya que se utiliza como medida de seguridad para asegurarnos que el **DNI** está bien escrito.

Para ello, lo que se hace es separar la parte numérica de la letra, luego calculamos el resto de la división del número del **DNI** entre 23; el resto obtenido indica el la letra que le corresponde a ese **DNI** basado en la siguiente lista:

```txt
TRWAGMYFPDXBNJZSQVHLCKE
```

> [!important] IMPORTANTE
> Ten en cuenta que la lista se empieza a contar desde el 0; por lo que si el resto de la operación es igual a 0 la letra es `T`, si es igual 1 la letra es `R` y así consecutivamente.

## CALCULAR DNI

A continuación tenemos un pequeño código demostrando como se puede calcular tanto la letra de un **DNI** cómo comprobar si está bien escrito.

```py
def dni_letter(num: int) -> str:
    # Calcula la letra en base al número.
    return "TRWAGMYFPDXBNJZSQVHLCKE"[num % 23]


def valid_dni(dni: str) -> bool:
    # Debe tener una longitud de 9 caracteres.
    if len(dni) != 9:
        return False
    # La letra debe coincidir con la resultante.
    if dni_letter(int(dni[:8])) != dni[8]:
        return False
    return True
```
^dni-funcs

## REGEX DNI

Si queremos encontrar **DNIs** con una expresión regular podríamos hacerlo con la siguiente expresión:

```regex
\d{8}[A-HJ-NP-TV-Z]
```
