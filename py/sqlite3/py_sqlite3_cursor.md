---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
  - Programming/Python/SQLite3
  - DataBase/SQLite3
title: Clase Cursor en SQLite3 en Python
---

# CLASE CURSOR

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar que es un objeto `Cursor` y cual es su objetivo.
> > - [x] Documentar el método `execute`.
> > - [ ] Documentar el método `executemany`.
> > - [ ] Documentar el método `executescript`.
> > - [ ] Documentar el método `fetchone`.
> > - [ ] Documentar el método `fetchall`.
> > - [ ] Documentar el método `fetchmany`.

> [!important] IMPORTANTE
> A lo largo de esta documentación me referiré al cursor como `cu`.

## EJECUTA SQL

Para ejecutar sentencias [SQL](../../sql/sqlite3/sqlite3.md) con el cursor, podremos hacer uso de tres [métodos](../class/py_method.md).

- [`execute`](#EXECUTE): ejecuta una sentencia una vez.
- [`executemany`](#EXECUTEMANY): ejecuta una sentencia múltiples veces.
- [`executescript`](#EXECUTESCRIPT): ejecuta múltiples sentencias de golpe.

### EXECUTE

El [métodos](../class/py_method.md) `execute` permite ejecutar una sentencia de [SQL](../../sql/sqlite3/sqlite3.md) recibiendo la como argumento.

> [!abstract] SINTAXIS
> ***\[cu\]***.execute(***\[sql\]\{***, ***\[parameters\]\}***)

```python
import sqlite3

cx = sqlite3.connect("./main.py")
cu = cx.cursor()

# Se crea una variable con la
# sentencia SQL.
sql: str = """
CREATE TABLE users(
    id        INTEGER PRIMARY KEY,
    firstName TEXT    NOT NULL,
    lastName  TEXT
);
"""

# Se ejecuta la sentencia SQL.
cu.execute(sql)

# Se embian los cambios a la DB.
cx.commit()

cu.close()
cx.close()
```

---

También tenemos la posibilidad de pasar un segundo parámetro que debe recibir un **iterable** como puede ser una [**lista**](../py_list.md) o [**tupla**](../py_tuple.md), conteniendo este los **parámetros** que queramos insertar en la sentencia [SQL](../../sql/sqlite/sqlite.md).

```python
import sqlite3

cx = sqlite3.connect("./main.py")
cu = cx.cursor()

sql: str = """
INSERT INTO users (firstName, lastName)
VALUES (?, ?);
"""

# Se crea la tupla conlos parámetros
parameters: tuple = ("Adelio", None)

cu.execute(sql, parameters)

cx.commit()

cu.close()
cx.close()
```

### EXECUTEMANY

### EXECUTESCRIPT
