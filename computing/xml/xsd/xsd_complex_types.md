---
author: Mindusting
corrected: false
tags:
  - Programming/XML/XSD
title: Tipos complejos en XSD
---

# TIPOS COMPLEJOS EN XSD

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

Para crear un tipo de **dato complejo** se usa la etiqueta `complexType`:

> [!abstract] SINTAXIS
> \<complexType ***\[attributes\]***\>
> ***\[content\]***
> \</complexType\>

Estos tipos complejos pueden contener las siguientes etiquetas:

- `sequence`: sirve para indicar un conjunto de [elementos](./xsd_element.md) que serán los hijo del [elemento](./xsd_element.md) padre.
- `all`
- `choice`
- [`attribute`](./xsd_attribute.md)

> [!important] IMPORTANTE
> Primero se pone `sequence` y luego los `attribute`.
