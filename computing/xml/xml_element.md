---
author: Mindusting
corrected: true
tags:
  - Programming/XML
title: Elementos en XML
---

# ELEMENTOS EN XML

> [!help]- REFERENCIAS WEB
> - [W3 Schools (XML Elements)](https://www.w3schools.com/xml/xml_elements.asp)

## ELEMENTOS

Un **elemento** se compone de como mínimo una *etiqueta*, ésta puede contener [*atributos*](#ATRIBUTOS) con sus respectivos *valores*, e incluso puede contener otros **elementos**; dependiendo de si el **elemento** va a tener *contenido* o no podemos usar una de las dos sintaxis:

%%
> [!abstract] SINTAXIS
> \<***\[tag\] \[attribute\]***="***\[value\]***" ...\>***\[content\]***\</***\[tag\]***\>
%%

> [!abstract] SINTAXIS
> \<<span class="italic key-word-color">[tag]</span> <span class="italic variable-color">[attribute]</span>=<span class="italic string-color">[value]</span> ...\><span class="italic grey">[content]</span>\</<span class="italic key-word-color">[tag]</span>\>

> [!abstract] SINTAXIS
> \<<span class="italic key-word-color">[tag]</span> <span class="italic variable-color">[attribute]</span>=<span class="italic string-color">[value]</span> .../\>

> [!note] NOTA
> Fíjate que en la primera sintaxis, la *barra* (`/`) se encuentra al inicio de la *etiqueta* de cierre; mientras que en la segunda sintaxis, la *barra* (`/`) se encuentra al final de la *etiqueta* de apertura, indicando así que esta es de apertura y cierre.

Existen a groso modo dos tipos de **elementos**:

- **Simples**: Son **elementos** que no tienen [*atributos*](#ATRIBUTOS) y el *contenido* es texto plano.
- **Complejos**: Son **elementos** que bien tienen [*atributos*](#ATRIBUTOS) o su *contenido* no es texto plano, sino que contienen otros **elementos**; formando así un conjunto.

### ATRIBUTOS

Los *atributos* son conjuntos de pares **clave**, **valor**; siguiendo el comportamiento de un [diccionario](../pc/pc_dictionary.md); esto permite almacenar *valores* concretos en los [**elementos**](#ELEMENTOS).

```xml
<user id="1" name="Adelio" age="20"></user>
```

### ELEMENTOS ANIDADOS

Los [**elementos**](#ELEMENTOS) anidados son aquellos que contienen otros [**elementos**](#ELEMENTOS) en su interior, transformando el [**elemento**](#ELEMENTOS) padre en un conjunto.

```xml
<users>
    <user id="1">
        <name>Adelio</name>
        <age>20</age>
    </user>
    <user id="2">
        <name>Adelia</name>
        <age>22</age>
    </user>
</users>
```

En este caso tenemos un [**elemento**](#ELEMENTOS) `users` el cual contiene múltiples [**elementos**](#ELEMENTOS) `user`, teniendo estos a su vez los [**elementos**](#ELEMENTOS) `name` y `age`.

## ELEMENTO RAÍZ

El **elemento raíz** no es más que un [**elemento**](#ELEMENTOS) que se sitúa justo debajo del [**encabezado**](./xml_declaration.md) y contiene el resto de elementos del documento.

Un ejemplo de esto sería si queremos guardar en un archivo un conjunto de *usuarios*, el **elemento raíz** podría ser una [**etiqueta**](#ELEMENTOS) sin [*atributos*](#ATRIBUTOS) llamada `users` (*"usuarios" en inglés*); dentro de esta guardaremos los distintos *usuarios*.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<users>
    <!-- Aquí se mete el resto del contenido del documento -->
</users>
```

> [!important] IMPORTANTE
> Cada archivo [**XML**](./xml.md) solo puede tener un **elemento raíz**.
