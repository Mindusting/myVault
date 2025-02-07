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
> > - [ ] Documentar los tipos de datos (*La tabla está comentado justo aquí debajo*).

%%
[Tipos de datos en SQLite](../../sql/sqlite3/sqlite3_data_types.md).

| SQLite type | Python type |
|:------------|:------------|
| NULL        | None        |
| INTEGER     | int         |
| REAL        | float       |
| TEXT        | str         |
| BLOB        | bytes       |
%%

> [!help]- REFERENCIAS WEB
> - [Python doc (SQLite)](https://docs.python.org/3/library/sqlite3.html)
> - [geeksforgeeks](https://www.geeksforgeeks.org/python-sqlite/)

> [!warning] ATENCIÓN
> Para poder hacer uso de este [módulo](py_module.md) se requieren conocimientos mínimos de funcionamiento de bases de datos, si no sabes de [bases de datos](../../db/db.md) puedes consultar la [documentación correspondiente](../../db/db.md), si sí sabes, pero no conoces [sqlite3](../../sql/sqlite3/sqlite3.md), también tienes [documentación](../../sql/sqlite3/sqlite3.md) sobre ello.

Para poder usar [**SQLite 3**](../../sql/sqlite3/sqlite3.md) en **Python**, primero deberemos [importar el módulo](py_module.md):

```python
import sqlite3
```

> [!info] INFO
> Este módulo está incluido en Python3 por lo que no hace falta instalarlo.

## ÍNDICE

Si quieres seguir una lectura más lineal, te recomiendo lo siguiente:

1. [CONEXIÓN A DB](#CONEXIÓN%20A%20DB)
2. [CREAR UN CURSOR](./py_sqlite3_connection.md#CREACIÓN%20DE%20CURSOR)
3. [EJECUTA SQL](./py_sqlite3_cursor.md#EJECUTA%20SQL)

## CONEXIÓN A DB

Para empezar a trabajar sobre una [base de datos](../../db/db.md) primero tendremos que crearla, para ello tendremos que hacer uso de la [función](py_function.md) `connect`, esta permite tanto crear una [base de datos](../../db/db.md) como conectarnos a una ya existente, requiere de un argumento indicado la ruta de la [base de datos](../../db/db.md):

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
> Si el nombre que se indica en la [función](py_function.md) `connect` es `:memory:` la [base de datos](../../db/db.md) se guarda en la memoria RAM, por lo que esta se borrará en el momento en el que se cierre la conexión, el objetivo de esto es poder usa la de forma temporal y sin dejar rastro en el disco duro.
