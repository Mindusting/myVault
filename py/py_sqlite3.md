---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
  - Programming/Python/SQLite3
title: SQLite3 en Python
---

# SQLITE3 IN PYTHON

> [!warning] WARNING
> Para poder hacer uso de este [módulo](py_module.md) se requieren conocimientos mínimos de funcionamiento de bases de datos, si no sabes de bases de datos puedes consultar la [documentación correspondiente](../sql/sql.md), si sí sabes, pero no conoces [sqlite3](../sql/sqlite3/sqlite3.md), también tienes [documentación](../sql/sqlite3/sqlite3.md).

[WEB - Python doc (SQLite)](https://docs.python.org/3/library/sqlite3.html)

Para poder usar [`SQLite 3`](../sql/sqlite3/sqlite3.md) en Python, primero deberemos [importar el módulo](py_module.md):

```python
import sqlite3
```

Para empezar a trabajar sobre una base de datos primero tendremos que crearla, para ello tendremos que hacer uso de la [función](py_function.md) `connect`, esta permite tanto crear una base de datos como conectarnos a una ya existente:

```python
connection = sqlite3.connect("main.db")

connection.close()
```

Como se puede ver en este ejemplo, primero creamos la base de datos con la [función](py_function.md) `connect` y finalmente cerramos la conexión con el [método](classes/py_method.md) `close` (Esto último se hace para evitar problemas y ahorro de recursos, aun que al final de la ejecución del programa se debería cerrar de forma automática).

> [!note] NOTE
> Si el nombre que se indica en la [función](py_function.md) `connect` es [`:memory:`](../sql/sqlite3/SQLite3_memory_ddbb.md) la base de datos se guarda en la memoria RAM.

---

Ahora que ya tenemos creada la base de datos podremos trabajar sobre ella con la ayuda de un cursor este se crea a trabes del [objeto](py_class.md) `connection` y su [método](classes/py_method.md) `cursor` (El cual también es buena costumbre cerrarlo al terminar de usar la base de datos):

```python
connection = sqlite3.connect("main.db")
cursor = connection.cursor()

cursor.close()
connection.close()
```

# TRABAJAR SOBRE LA BASE DE DATOS

- [EJECUTA SENTENCIAS](sqlite3/SQLite3_execute.md)
- [OBTENCIÓN DE DATOS](sqlite3/SQLite3_fetch.md)

# TIPOS DE DATOS

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

[Tipos de datos en SQLite](../sql/sqlite3/SQLite3_data_types.md).

| SQLite type | Python type |
|:------------|:------------|
| NULL        | None        |
| INTEGER     | int         |
| REAL        | float       |
| TEXT        | str         |
| BLOB        | bytes       |
