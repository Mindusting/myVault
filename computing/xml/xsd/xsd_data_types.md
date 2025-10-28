---
author: Mindusting
corrected: false
tags:
  - Programming/XML/XSD
title: Tipos de datos en XSD
---

# TIPOS DE DATOS EN XSD

> [!fail]- ESTE APARATADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!help]- REFERENCIAS WEB
> - [W3 Schools (XSD String)](https://www.w3schools.com/xml/schema_dtypes_string.asp)
> - [W3 Schools (XSD Date/Time)](https://www.w3schools.com/xml/schema_dtypes_date.asp)
> - [W3 Schools (XSD Numeric)](https://www.w3schools.com/xml/schema_dtypes_numeric.asp)
> - [W3 Schools (XSD Misc)](https://www.w3schools.com/xml/schema_dtypes_misc.asp)
> - [W3 Schools (XSD References)](https://www.w3schools.com/xml/schema_elements_ref.asp)

## TIPOS ORIGINALES

| TIPO      | CONTIENE             |
|:--------- |:-------------------- |
| `string`  | Cadena de caracteres |
| `integer` | Número entero        |
| `decimal` | Número con decimales |
| `date`    | Fecha (*aaaa-mm-dd*) |
| `time`    | Hora (*hh:mm:ss*)    |
| `boolean` | Booleano             |

## NUEVOS TIPOS

Podemos crear nuevos tipos de datos.

- [TIPOS SIMPLES](xsd_simple_types.md)
- [TIPOS COMPLEJOS](xsd_complex_types.md)

### TIPOS POR REFERENCIA

Cuando estamos creando un nuevo **tipo de dato** bien [simple](./xsd_simple_types.md) o [complejo](./xsd_complex_types.md) podemos hacer lo a nivel del [esquema](xsd_schema.md), pudiendo así hacer referencia a el, dejando el código más limpio y permitiendo reutilizar los tipos.

```xsd
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">

<xs:element name="users">
    <xs:complexType>
        <xs:sequence>
            <xs:element
                name="user"
                maxOccurs="unbounded"
                minOccurs="0"
            >
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="name" type="xs:string"/>
                        <xs:element name="age" type="xs:integer"/>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
        </xs:sequence>
    </xs:complexType>
</xs:element>

</xs:schema>
```

```xsd
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">

<xs:element name="users">
    <xs:complexType>
        <xs:sequence>
            <!--
                Aquí se declara un elemento de tipo
                user con el máximo y mínimo de
                ocurrencias, siendo de cero a infinito.
            -->
            <xs:element
                name="user"
                type="user"
                maxOccurs="unbounded"
                minOccurs="0"
            />
        </xs:sequence>
    </xs:complexType>
</xs:element>

<!--
    Aquí se declara el tipo de dato user.
-->
<xs:complexType name="user">
    <xs:sequence>
        <xs:element name="name" type="xs:string"/>
        <xs:element name="age" type="xs:integer"/>
    </xs:sequence>
</xs:complexType>

</xs:schema>
```
