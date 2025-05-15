---
author: Mindusting
corrected: false
tags:
  - Programming/XML/XSD
title: Atributos en XSD
---

# ATRIBUTOS EN XSD

> [!fail]- REFERENCIAS WEB
> > [!todo] #TODO

> [!help]- REFERENCIAS WEB
> - [W3 Schools](https://www.w3schools.com/xml/schema_simple_attributes.asp)

> [!abstract] SINTAXIS
> \<xs:attribute ***\[attributes\]***\>\</xs:attribute\>

- `name`: (*requerido*) indica el nombre de la [*etiqueta*](../xml_element.md).
- `type`: indica el [tipo de dato](./xsd_data_types.md) que va a guardar.
- `default`: indica el valor por defecto.
- `fixed`: indica un valor fijo que no se puede cambiar.
- `use`: indica si el *atributo* es opcional (`optional` *es el valor por defecto*) o requerido (`required`).
