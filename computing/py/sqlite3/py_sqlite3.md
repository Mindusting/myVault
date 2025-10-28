---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
  - Programming/Python/SQLite3
  - DataBase/SQLite3
title: SQLite3 en Python
---

# SQLITE3 IN PYTHON

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Corregir faltas de ortografía.

> [!help]- REFERENCIAS WEB
> - [Python doc (SQLite)](https://docs.python.org/3/library/sqlite3.html)
> - [geeksforgeeks](https://www.geeksforgeeks.org/python-sqlite/)
> - [El libro de Python](https://ellibrodepython.com/bases-datos-sqlite-python)

> [!faq]- FAQ
> - [¿Que es un BD (*Base de Datos*)?](../../db/db.md)
> - [¿Qué es SQLite3?](../../db/sql/sqlite3/sqlite3.md)
> - [¿Qué son los tipos de datos en SQLite?](../../sql/sqlite3/sqlite3_data_types.md).

> [!warning] ATENCIÓN
> Para poder hacer uso de este [módulo](../py_module.md) se requieren conocimientos mínimos de funcionamiento de bases de datos, si no sabes de [bases de datos](../../db/db.md) puedes consultar la [documentación correspondiente](../../db/db.md), si sí sabes, pero no conoces [sqlite3](../../db/sql/sqlite3/sqlite3.md), también tienes [documentación](../../db/sql/sqlite3/sqlite3.md) sobre ello.

> [!important] IMPORTANTE
> Si quieres trabajar sobre [base de datos](../../db/db.md) encriptadas con *SQLCipher* debes usar [módulo](../py_module.md) [`pysqlcipher3`](../py_pysqlcipher3.md)

El [módulo](../py_module.md) de [**SQLite 3**](../../db/sql/sqlite3/sqlite3.md) permite conectarnos a [bases de datos](../../db/db.md) de este mismo tipo; pudiendo tanto leer como escribir.

## IMPORTACIÓN DEL MÓDULO

Para poder usar [**SQLite 3**](../../db/sql/sqlite3/sqlite3.md) en **Python**, primero deberemos [importar el módulo](../py_module.md) de la siguiente forma (*Este módulo está incluido en Python3 por lo que no hace falta instalarlo*):

```python
import sqlite3
```

## CONEXIÓN A BASE DE DATOS

Para empezar a trabajar sobre una [base de datos](../../db/db.md) primero tendremos que crearla o conectarnos a una existente; para ello tendremos que hacer uso de la [función](../py_func.md) `connect`; esta recibe un argumento de tipo [`str`](../py_str.md) indicando la runa de en donde se encuentra la [base de datos](../../db/db.md); devolviéndonos como resultado un objeto de tipo [`Connection`](py_sqlite3_connection.md).

> [!abstract] SINTAXIS
> ***\[cx\_name\]*** = sqlite3.connect(***\[path\]***)

```python
# Crea una DB en el directorio de
# ejecución del programa, y genera
# un objeto conexión para poder
# trabajar sobre esta.
cx = sqlite3.connect("./main.db")

# Al terminar, cierra la conexión.
cx.close()
```

> [!info] INFO
> El objeto [`Connection`](py_sqlite3_connection.md) es el encargado de conectarse a la [base de datos](../../db/db.md) para realizar los cambios en esta, entre otra serie de cosas.

> [!tip] TIP
> Si el nombre que se indica en la [función](../py_func.md) `connect` es `:memory:` la [base de datos](../../db/db.md) se guarda en la memoria RAM, por lo que esta se borrará en el momento en el que se cierre la conexión, el objetivo de esto es poder usa la de forma temporal y sin dejar rastro en el disco duro.

## COMBERSIÓN DE DATOS

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

| SQLite type | Python type |
|:------------|:------------|
| NULL        | None        |
| INTEGER     | int         |
| REAL        | float       |
| TEXT        | str         |
| BLOB        | bytes       |
