---
author: Mindusting
corrected: false
tags:
  - Programming/XML/XSD
title: Esquema de un XSD
---

# ESQUEMA DE UN XSD

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Hacer una mejor documentación sobre esto.

> [!help]- REFERENCIAS WEB
> - [W3 Schools](https://www.w3schools.com/xml/schema_schema.asp)

La estructura inicial de un [**XSD**](./xsd.md) es la siguiente:

```xsd
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">

<!-- Aquí va el contenido del archivo -->

</xs:schema>
```

La letras `xs` es una especie de [variable](../../pc/pc_variable.md) en al que se guarda en este caso `http://www.w3.org/2001/XMLSchema`, ya que todo a lo que vamos a hacer referencia está en esa **URL**.
