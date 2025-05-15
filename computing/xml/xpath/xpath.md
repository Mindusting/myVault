---
author: Mindusting
corrected: false
tags:
  - Programming/XML/XPath
title: XPath
---

# XPATH

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] 

> [!help]- REFERENCIAS WEB
> - [W3 Schools](https://www.w3schools.com/xml/xpath_intro.asp)

**XPath** se utiliza para navegar a través de un documento de [**XML**](../xml.md).

## SELECCIÓN DE NODOS

| EXPRESIÓN      | DESCRIPCIÓN                          |
|:-------------- |:------------------------------------ |
| *\[nodeName\]* | Nodos con el nombre indicado         |
| /              | Nodo root o hijos de ...             |
| //             | Descendientes con el nombre indicado |
| .              | Nodo actual                          |
| ..             | Nodo padre                           |
| @              | Atributo                             |

## PREDICADO

> [!abstract] SINTAXIS
> *\[node\]*\[***\[predicate\]***\]

| PREDICADO               | DESCRIPCIÓN                     |
|:----------------------- |:------------------------------- |
| *\[index\]*             | Nodo hijo por índice            |
| last()                  | Último hijo                     |
| last()-*\[index\]*      | Nodo hijo por índice invertido  |
| position()>*\[index\]*  | Hijos con índice mayor a índice |
| position()<*\[index\]*  | Hijos con índice menor a índice |
| @*\[attr\]*             | Nodos con atributo              |
| @*\[attr\]*=*\[value\]* | Nodos con atributo igual a ...  |
| *\[node\]*=*\[value\]*  | Nodos con hijo con valor ...    |
|                         |                                 |

## NODOS DESCONOCIDOS

| COMODÍN | DESCRIPCIÓN                      |
|:------- |:-------------------------------- |
| node()  | Cualquier nodo de cualquier tipo |
| \*      | Cualquier nodo de tipo elemento  |
| @\*     | Cualquier nodo de tipo atributo  |
| text()  | Cualquier nodo de tipo texto     |

## OPERADORES

Operador `|` (*OR*) permite indicar una expresión a cada lado de este, haciendo que se seleccionen los nodos que coincidan con cualquiera de las dos expresiones.

> [!abstract] SINTAXIS
> ***\[expr\]*** | ***\[expr\]***

## CONSULTAS ANIDADAS

```xml
<?xml version="1.0" encoding="UTF-8"?>
<data>
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
    <notes>
        <note id="1" userId="2">
            <title>Lista de la compra</title>
            <content>Patatas, tomates, lechuga</content>
        </note>
        <note id="2" userId="1">
            <title>TODO</title>
            <content>Aprender XML</content>
        </note>
    </notes>
</data>
```

```xpath
/data/notes/note[@userId=/data/users/user[name="Adelio"]/@id]/content
```

Resultado:

`Aprender XML`