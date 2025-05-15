---
author: Mindusting
corrected: false
tags:
  - Programming/XML
title: XML
---

# XML

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar la referencia al XSD.

> [!help]- REFERENCIAS WEB
> - [W3 Schools](https://www.w3schools.com/xml/default.asp)

**XML** es la abreviación de `eXtensible Markable Language`; no es un lenguaje de *etiquetas*, sino un conjunto de reglas para definir lenguajes de *etiquetas*.

[**W3C**](https://www.w3.org/) es la entidad de establecer las reglas de **XML** como de [**HTML**](../html/html.md).

## UTILIDADES

- Facilidad en el intercambio de datos entre programas distintos.
- Separa los datos de [HTML](../html/html.md).
- Migración de datos a sistemas nuevos.
- Creación de nuevos lenguajes de marcado de datos.

## CARACTERÍSTICAS DE XML

- [DESCRIPCIÓN](xml_declaration.md)
- [COMENTARIOS](xml_commet.md)
- [ELEMENTOS](xml_element.md)
- [REFERENCIAS](xml_reference.md)

## OTROS TEMAS

- [XSD](./xsd/xsd.md)
- [XPath](./xpath/xpath.md)

## REFERENCIA AL XSD

`xsi:noNamespaceSchemaLocation="main.xsd"`

```txt
xmlns:xsi="http://www.w3.org/2001/XMLSChema-instance"
xsi:noNamespaceSchemaLocation="main.xsd"
```