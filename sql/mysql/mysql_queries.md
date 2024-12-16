---
author: Mindusting
corrected: false
tags:
  - Programming/SQL/MySQL
title: Consultas en MySQL
---

# CONSULTAS

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

Una vez tenemos datos guardados en las tablas, para poder **consultar** esa información, lo haremos a través de la sentencia `SELECT`, con esta indicaremos los nombres de las columnas que queramos consultar, luego usaremos la sentencia `FROM` para indicar de donde queremos que obtenga esas columnas.

> [!abstract] SINTAXIS
> [SELECT ***\[col\_name\], ...***](#SELECT)
> [FROM ***\[table\_name\], ...***](#FROM)
> [***\{WHERE \[select\_criteria\]\}***](#WHERE)
> [***\{ORDER BY \[col_name\] \[ASC|DESC\], ...\}***;](#ORDER%20BY)

```sql
-- Estructura de la tabla.
CREATE TABLE users (
    id   INTEGER PRIMARY KEY,
    name VARCHAR(32) NOT NULL,
    dni  CHAR(9) NOT NULL UNIQUE
    CHECK (LENGTH(dni) = 9)
);

-- Inserción de datos.
INSERT INTO users
    (name, dni)
VALUES
    ('Adelio', '12345678A'),
    ('Adelia', '23456789B');

-- Consulta de usuarios
SELECT id, dni
FROM users;
/*
RESULTADO:
+----+-------------+
| id |     dni     |
+----+-------------+
|  1 | '12345678A' |
|  2 | '23456789B' |
+----+-------------+
*/
```

## SELECT

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

## FROM

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

## WHERE

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

### OPERADORES RELACIONALES

| OPERADOR | SIGNIFICADO   |
|:--------:|:------------- |
|    <     | Menor que     |
|    <=    | Menor o igual |
|    >     | Mayor         |
|    >=    | Mayor o igual |
|    =     | Igual a       |
|  != <>   | Distinto de   |

### OPERADORES ARITMÉTICOS

| OPERADOR | SIGNIFICADO                        |
|:--------:|:---------------------------------- |
|    +     | Suma                               |
|    -     | Resta o cambio de signo (*unario*) |
|    \*    | Multiplicación                     |
|    /     | División                           |
|   div    | División entera                    |
|  \% mod  | Resto de división entera           |

### OPERADORES LÓGICOS

|    AND    | TRUE  | FALSE | NULL  |
|:---------:|:-----:|:-----:|:-----:|
| **TRUE**  | TRUE  | FALSE | NULL  |
| **FALSE** | FALSE | FALSE | FALSE |
| **NULL**  | NULL  | FALSE | NULL  |

|    OR     | TRUE | FALSE | NULL |
|:---------:|:----:|:-----:|:----:|
| **TRUE**  | TRUE | TRUE  | TRUE |
| **FALSE** | TRUE | FALSE | NULL |
| **NULL**  | TRUE | NULL  | NULL |

|    NOT    |  RES  |
|:---------:|:-----:|
| **TRUE**  | FALSE |
| **FALSE** | TRUE  |
| **NULL**  | NULL  |

## UNION

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO
