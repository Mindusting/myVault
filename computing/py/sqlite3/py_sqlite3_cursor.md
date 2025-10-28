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
> > - [ ] Documentar el método `execute`.
> > - [ ] Documentar el método `executemany`.
> > - [ ] Documentar el método `executescript`.
> > - [ ] Documentar el método `fetchone`.
> > - [ ] Documentar el método `fetchall`.
> > - [ ] Documentar el método `fetchmany`.

> [!important] IMPORTANTE
> A lo largo de esta documentación me referiré al cursor como `cu`.

## EJECUCIÓN DE SQL

Para ejecutar sentencias [SQL](../../db/sql/sql.md) con el **cursor**, podremos hacer uso de tres [métodos](../class/py_methods.md):

- [`execute`](#EXECUTE): ejecuta una sentencia una vez.
- [`executemany`](#EXECUTEMANY): ejecuta una sentencia múltiples veces.
- [`executescript`](#EXECUTESCRIPT): ejecuta múltiples sentencias de golpe.

### EXECUTE

El [métodos](../class/py_methods.md) `execute` permite ejecutar una sentencia de [SQL](../../db/sql/sql.md) recibiendo la como primer argumento, el segundo es opcional y debe ser una [**tupla**](../py_tuple.md) o una [**lista**](../py_list.md) con los valores que sustituirán las interrogaciones que contenga la sentencia [SQL](../../db/sql/sql.md)

> [!abstract] SINTAXIS
> execute(***\[sql\]\{***, ***\[parameters\]\}***)

```python
import sqlite3

cx = sqlite3.connect("./main.db")
cr = cx.cursor()

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
cr.execute(sql)

# Se embian los cambios a la DB.
cx.commit()

cr.close()
cx.close()
```

---

También tenemos la posibilidad de pasar un segundo parámetro que debe recibir un **iterable** como puede ser una [**lista**](../py_list.md) o [**tupla**](../py_tuple.md), conteniendo este los **parámetros** que queramos insertar en la sentencia [SQL](../../db/sql/sqlite3/sqlite3.md).

```python
import sqlite3

cx = sqlite3.connect("./main.db")
cr = cx.cursor()

sql: str = """
INSERT INTO users (firstName, lastName)
VALUES (?, ?);
"""

# Se crea la tupla conlos parámetros
parameters: tuple = ("Adelio", None)

cr.execute(sql, parameters)

cx.commit()

cr.close()
cx.close()
```

### EXECUTEMAY

> [!abstract] SINTAXIS
> executemany(***\[sql\]\{***, ***\[parameters\]\}***)

### EXECUTESCRIPT

Para ejecutar un script de [**SQLite3**](../../db/sql/sqlite3/sqlite3.md) con varias sentencias se usa el [método](../class/py_methods.md) `executescript`; este recibe un único argumento de tipo [string](../py_str.md) con el script en cuestión.

> [!abstract] SINTAXIS
> executescript(***\[sql\]***)

```python
import sqlite3

sql = """
CREATE TABLE users (
    id   INTEGER PRIMARY KEY,
    name TEXT    NOT NULL,
    age  INTEGER
);

INSERT INTO users (name, age)
VALUES
    ('Adelio', 20),
    ('Adelia', 22);
"""

cx = sqlite3.connect("main.db")

cx.executescript(sql)

cx.close()
```

## OBTENCIÓN DE DATOS

### FETCHONE

### FETCHMANY

### FETCHALL
