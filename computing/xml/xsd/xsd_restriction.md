---
author: Mindusting
corrected: false
tags:
  - Programming/XML/XSD
title: Restrcciones en XSD
---

# RESTRICCIONES EN XSD

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!help]- REFERENCIAS WEB
> - [W3 Schools (XSD restricciones)](https://www.w3schools.com/xml/schema_facets.asp)

> [!abstract] SINTAXIS
> \<xs:restriction base="[***\[dataType\]***](./xsd_data_types.md)"\>
> ***\[restrictionRules\]***
> \</xs:restriction\>

> [!abstract] SINTAXIS
> \<[***\[restrictionType\]***](#TIPOS%20DE%20RESTRICCIONES) value="***\[value\]***"/\>

## TIPOS DE RESTRICCIONES

Dependiendo de con qué [tipo de dato](./xsd_data_types.md) se esté trabajando se podrá user unas restricciones u otras.

### TIPOS GENÉRICOS

- `enumeration`: permite indicar los valores de forma literal que están permitidos introducir.

```xsd
<xs:simpleType base="xs:string">
    <enumeration value="hombre">
    <enumeration value="mujer">
</xs:simpleType>
```

### TIPOS NUMÉRICOS

- `fractionDigits`: indica el número máximo de dígitos decimales que puede contener.
- `maxExclusive`: equivale a `x > value`.
- `minExclusive`: equivale a `x < value`.
- `maxInclusive`: equivale a `x >= value`.
- `minInclusive`: equivale a `x <= value`.

### TIPOS TEXTO

- `length`: indica el número de caracteres que debe tener.
- `maxLength`: longitud máxima de caracteres.
- `minLength`: longitud mínima de caracteres.
- `pattern`: permite indicar una [expresión regular](../../regex/regex.md).
- `whileSpace`: permite indicar como se debe tratar los caracteres blancos:
    - `preserve`: mantiene los caracteres blancos.
    - `replace`: sustituye todos los caracteres blancos por espacios.
    - `collapse`: sustituye todos los caracteres blancos por espacios, quitando todos lo que se encuentre en los extremos y en caso de haber varios seguidos se sustituirán por uno.
