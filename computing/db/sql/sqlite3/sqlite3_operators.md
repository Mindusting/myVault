---
author: Mindusting
corrected: false
tags:
  - DB/SQL
  - DB/SQLite3
title: Operadores en SQLite
---

# OPERADORES EN SQLITE

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

Los operadores realizan una operación entre dos valores que da como resultado un valor [booleano](../../../pc/pc_boolean.md) indicado si la comparación correspondiente se cumple.

## BOOLEANOS

### AND

### OR

### NOT

## LIKE

El operador `LIKE` permite comparar dos textos; pudiendo hacer uso de caracteres especiales para poder concretar un no literal.

| CHAR | SENTIDO                   |
|:----:|:------------------------- |
| `%`  | Cero o varios caracteres  |
| `_`  | Concretamente un carácter |

> [!abstract] SINTAXIS
> ***\[stringToCompare\]*** LIKE ***\[stringPattern\]***

## GLOB

Utiliza la sintaxis de archivos de [**Linux**](../../../os/linux/linux.md) como el que se usa en el comando [`ls`](../../../os/linux/bash/bash_ls.md).

| CHAR  | SENTIDO                          |
|:-----:|:-------------------------------- |
|  `*`  | Cero o varios caracteres         |
|  `?`  | Concretamente un carácter        |
| `[]`  | Conjunto de caracteres validos   |
| `[^]` | Conjunto de caracteres invalidos |

> [!abstract] SINTAXIS
> ***\[stringToCompare\]*** GLOB ***\[stringPattern\]***

## BETWEEN

> [!abstract] SINTAXIS
> ***\[number\]*** BETWEEN(***\[min\]*** AND ***\[max\]***)

## IN

El operador `IN` sirve para comprobar si un valor se encuentra o no dentro de una lista de valores, de forma que si encuentra el operando dentro del conjunto de valores, este nos devolverá `true`, de lo contrario `false`; pudiendo invertir el resultado con la palabra clave `NOT`.

> [!abstract] SINTAXIS
> ***\[value\] \{NOT\}*** IN (***\[listOfValues\]***)

### LISTA DE VALORES

La lista de valores puede ser un conjunto de valores fijos o la columna resultante de una [consulta](sqlite3_select.md); veamos unos ejemplos de esto miso para entenderlo mejor:

Suponiendo que tenemos la siguiente tabla con los siguientes datos:

```sql
CREATE TABLE users (
    id   INTEGER PRIMARY KEY,
    name TEXT,
    age  INT
);

INSERT INTO users (name, age)
VALUES
    ('Adelio',  20),
    ('Adelia',  22),
    ('Antonio', 40),
    ('Antonia', 42);
```

Si ejecutamos la siguiente consulta, obtendremos toda la información de los usuarios cuyo nombre coincida con `Adelio` o `Adelia`:

```sql
SELECT *
FROM users
WHERE name IN ('Adelio', 'Adelia');
```

Obteniendo la siguiente tabla como resultado:

|  id | name   | age |
| ---:|:------ | ---:|
|   1 | Adelio |  20 |
|   2 | Adelia |  22 |

---

En este otro caso lo que ocurre es que obtenemos las edades tanto de `Adelio` como de `Adelia` y les sumamos 20, de esta forma obtendremos los número 40 y 42 en forma de una columna la cual utilizaremos como lista de valores para el operador `IN`; obteniendo así todos los datos de los usuarios `Antonio` y `Antonia`.

```sql
SELECT *
FROM users
WHERE age IN (
    SELECT age + 20
    FROM users
    WHERE name IN ('Adelio', 'Adelia')
);
```

|  id | name    | age |
| ---:|:------- | ---:|
|   3 | Antonio |  40 |
|   4 | Antonia |  42 |

Cabe resaltar que este ejemplo es didáctico, no es ejemplo de un caso real, ya que sería muy raro encontrarse una consulta formulada de esta forma, pero nos sirve para entender como se puede usar una columna en forma de lista para el operador `IN`.

## IS

El operador `IS` sirve para comprobar si el valor con el que estamos operando es `NULL`, pudiendo invertir el resultado usando la palabra clave `NOT`.

> [!abstract] SINTAXIS
> ***\[value\]*** IS ***\{NOT\}*** NULL

Supongamos que tenemos una tabla de usuarios con los siguientes datos:

```sql
CREATE TABLE users (
    id   INTEGER PRIMARY KEY,
    name TEXT,
    age  INT
);

INSERT INTO users (name, age)
VALUES
    ('Adelio', 20),
    ('Adelia', NULL);
```

Si queremos obtener todos los usuarios de los cuales desconocemos su edad, podremos hacerlo de la siguiente forma:

```sql
SELECT *
FROM users
WHERE age IS NULL;
```

|  id | name   |    age |
| ---:|:------ | ------:|
|   2 | Adelia | *NULL* |

Si por el contrario quisiéramos obtener todos los usuarios de los cuales conozcamos su edad podremos hacerlo de la siguiente forma:

```sql
SELECT *
FROM users
WHERE age IS NOT NULL;
```

|  id | name   | age |
| ---:|:------ | ---:|
|   1 | Adelio |  20 |

## REGEXP

- `REGEXP`
