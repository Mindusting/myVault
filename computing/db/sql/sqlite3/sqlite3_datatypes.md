---
author: Mindusting
corrected: false
tags:
  - DB/SQL
  - DB/SQLite3
title: Tipos de datos en SQLite3
---

# TIPOS DE DATOS EN SQLITE3

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!help]- REFERENCIAS WEB
> - [SQLite3 (Datatypes)](https://sqlite.org/datatype3.html)

## TIPOS ESTÁNDAR

| NOMBRE    | TIPO           |
|:--------- |:-------------- |
| `INTEGER` | Número entero  |
| `TEXT`    | Texto          |
| `BLOB`    | Binario        |
| `REAL`    | Número decimal |
| `NUMERIC` | Número preciso |

El `NUMERIC` indica que se escoja el mejor tipo de dato entre `INTEGER` y `REAL` a la hora de guardar un número.

## BOOLEANOS

SQLite3 no tiene un tipo de dato concreto para guardar [booleanos](../../../pc/pc_boolean.md) como tal, se utiliza el tipo `INTEGER`; esta guardará un `0` con `FALSE` y un `1` con `TRUE`.

## FECHAS

```sql
CREATE TABLE dates (
    id INTEGER,
    d1 TEXT,
    d2 REAL,
    d3 INTEGER,
    
    PRIMARY KEY(id)
) STRICT;

INSERT INTO dates (d1, d2, d3)
VALUES (datetime('now'), julianday('now'), unixepoch('now'));
```

|  id | d1                  |               d2 |         d3 |
| ---:|:-------------------:| ----------------:| ----------:|
|   1 | 2025-06-06 20:22:57 | 2460833.34927089 | 1749241377 |
|   2 | 2025-06-06 20:22:58 | 2460833.34928372 | 1749241378 |
|   3 | 2025-06-06 20:22:59 | 2460833.34929535 | 1749241379 |

## ESTRICTOS

Para hacer que los tipos de datos de una tabla sean estrictos y por tanto no se puedan introducir tipos de datos mezclados dentro de una misma columna se usa la palabra clave `STRICT` al final de la declaración de la tabla.

> [!abstract] SINTAXIS
> CREATE TABLE ***\[tableName\]*** (
> ***\[columnDef\]***
> ) STRICT;

Cuando una tabla es estricta los tipos de datos que se pueden usar para las columnas son los siguientes:

| NOMBRE    | TIPO           |
|:--------- |:-------------- |
| `INTEGER` | Número entero  |
| `TEXT`    | Texto          |
| `BLOB`    | Binario        |
| `REAL`    | Número decimal |
| `ANY`     | Cualquier tipo |
