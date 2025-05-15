---
author: Mindusting
corrected: true
tags:
  - Programming/XML
title: Declaración de XML
---

# DECLARACIÓN DE XML

Esta declaración no es más que una *etiqueta* especial indicarle al intérprete que cosas debe de tener cuenta a la hora de leer el archivo, evitando así posibles errores, solo debe de haber una de estas en el archivo y siempre debe ser lo primero que contenga el archivo, ya que es donde el intérprete irá a buscarla.

> [!abstract] SINTAXIS
> \<?xml ***\[atributes\]***?\>

La declaración puede recibir tres tipos de argumentos:

- `version`: con él indicaremos la versión de **XML** que estemos usando.
- `encoding`: con él indicaremos el tipo de formato que usaremos para el texto, siendo el valor por defecto `UTF-8`.
- `estandalone`: con él indicaremos si el **XML** es dependiente de fuente externa, pudiendo tener como valor `yes` o `no`, siendo el valor por defecto `no`.

El formato más común a día de hoy cuando estoy escribiendo esto (`2024-04-22`) es el siguiente:

```xml
<?xml version="1.0" encoding="UTF-8"?>
```
