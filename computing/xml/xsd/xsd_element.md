---
author: Mindusting
corrected: false
tags:
  - Programming/XML/XSD
title: Elementos en XSD
---

# ELEMENTOS EN XSD

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!help]- REFERENCIAS WEB
> - [W3 Schools](https://www.w3schools.com/xml/schema_simple.asp)

> [!abstract] SINTAXIS
> \<xs:element ***\[attributes\]***\>\</xs:element\>

- `name`: (*requerido*) indica el nombre de la [*etiqueta*](../xml_element.md).
- `type`: indica el [tipo de dato](./xsd_data_types.md) que va a guardar.
- `default`: indica el valor por defecto.
- `fixed`: indica un valor fijo que no se puede cambiar.
- `maxOccurs`: (*por defecto es `1`*) indica el máximo de ocurrencias del **elemento**, pudiendo ser un número entero o `unbounded` para ilimitado.
- `minOccurs`: (*por defecto es `1`*) indica el mínimo de ocurrencias del **elemento**, siendo un número entero.
