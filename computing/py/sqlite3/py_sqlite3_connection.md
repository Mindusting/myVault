---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
  - Programming/Python/SQLite3
  - DataBase/SQLite3
title: Clase Connection en SQLite3 en Python
---

# CLASE CONNECTION

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar que es un objeto `Connexion` y cual es su objetivo.
> > - [x] Documentar como crear un objeto `Cursor`.
> > - [x] Documentar como hacer un backup.
> > - [ ] Documentar el método `rollback`.
> > - [ ] Documentar el método `commit`.
> > - [ ] Documentar el método `iterdump` (*Es un generador que devuelve todas las sentencias SQL necesarias para replicar la DB*).
> > - [ ] Explicar que se puede ejecutar sentencias SQL con la conexión, pero no es lo recomendable, ya que el cursor está especializado en ello y por tanto nos permitirá hacer cosas más complejas.

> [!important] IMPORTANTE
> A lo largo de esta documentación me referiré a la conexión como `cx`.

## CREACIÓN DE CURSOR

El [cursor](py_sqlite3_cursor.md) de la conexión es el encargado de recibir las sentencias [SQL](../../db/sql/sqlite3/sqlite3.md) y devolvernos los datos en el caso de hacer una consulta.

Para poder obtener un cursor de nuestra conexión, tendremos que usar el [método](../class/py_method.md) `cursor`, este no requiere ningún argumento para ser usado.

> [!abstract] SINTAXIS
> ***\[cu\_name\]*** = ***\[cx\]***.cursor()

```python
import sqlite3

cx = sqlite3.connect("./main.db")

# Se crea el cursor de la conexión.
cu = cx.cursor()

# Se cierra el cursor.
cu.close()

cx.close()
```

> [!important] IMPORTANTE
> Se debe cerrar antes el cursor que la conexión, básicamente se deben cerrar en el orden inverso al que se han creado.

## CREAR UN BACKUP

Si queremos hacer un una copia de seguridad (*backup*) de nuestra [base de datos](../../db/db.md), podremos hacer uso del [método](../class/py_method.md) `backup`, este recibe otra conexión como argumento y guarda en ella la información actual de la conexión original.

> [!abstract] SINTAXIS
> ***\[cx\]***.backup(***\[backup_cx\]***)

```python
import sqlite3

cx = sqlite3.connect("./main.db")

# Se crea la conexión al backup.
backup_cx = sqlite3.connect("./backup.db")

# Se establece el backup.
cx.backup(backup_cx)

# Se cierra el backup.
backup_cx.close()

cx.close()
```

## TIPO DE SALIDA

Cuando estamos trabajando con [bases de datos](../../db/db.md) lo normal es que usemos texto, pero hay aveces que tendremos que manejar imágenes, vídeos, audios que tengamos guardados en la [base de datos](../../db/db.md) dentro de una columna de tipo [`BLOB`](../../sql/sqlite3/sqlite3_data_types.md), si intentamos acceder a la información ahí guardada, es bastante probable que nos de una excepción, ya que hay ciertos [`bytes`](../py_bytes.md) que no se pueden transformar a texto de forma correcta, para solucionar esto podemos cambiar en la que nos devuelve la información de la [base de datos](../../db/db.md) con el atributo `text_factory`, este por defecto tiene la [clase](../py_class.md) [`str`](../py_str.md) y podemos sustituirlo por la [clase](../py_class.md) [`bytes`](../py_bytes.md).

Una vez cambiado, cada vez que hagamos una consulta a la [base de datos](../../db/db.md), en cuyo resultado contenga un [`TEXT`](../../sql/sqlite3/sqlite3_data_types.md) o un [`BLOB`](../../sql/sqlite3/sqlite3_data_types.md), nos lo dará con forma de [`bytes`](../py_bytes.md).

```python
import sqlite3

cx = sqlite3.connect("./main.db")

# Establecemos el resultado a bytes.
#                  v
cx.text_factory = byte

cx.close()
```
