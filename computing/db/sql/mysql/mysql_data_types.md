---
author: Mindusting
corrected: false
tags:
  - DB/SQL
  - DB/MySQL
title: Tipos de datos en MySQL
---

# TIPOS DE DATOS

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar numéricos.
> > - [ ] Documentar fechas.
> > - [ ] Documentar cadenas de caracteres.
> > - [ ] Corregir faltas de ortografía.

## NUMÉRICOS

> [!help] EN ESTE APARTADO SE HACE USO DE LOS SIGUIENTES RECURSOS
> - [Anotación de rango](../../../../math/math_range_notation.md).

### ENTERO BINARIO

| NOMBRE            | BYTES |     RANGO      |
|:----------------- |:-----:|:--------------:|
| `TINYINT`         |   1   |  \[-2⁷, 2⁷-1]  |
| `SMALLINT`        |   2   | \[-2¹⁵, 2¹⁵-1] |
| `MEDIUMINT`       |   3   | \[-2²³, 2²³-1] |
| `INT` o `INTEGER` |   4   | \[-2³¹, 2³¹-1] |
| `BIGINT`          |   8   | \[-2⁶³, 2⁶³-1] |

### DECIMAL BINARIO

| NOMBRE   | BYTES |            RANGO             |
|:-------- |:-----:|:----------------------------:|
| `FLOAT`  |   4   |  \[~-3.4\*10³⁸, ~3.4\*10³⁸]  |
| `DOUBLE` |   8   | \[~-1.8\*10³⁰⁸, ~1.8\*10³⁰⁸] |

### OTROS NUMÉRICOS

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Explicar como se almacena internamente los números de tipo `NUMERIC`.

- `NUMERIC([tdig], [dec])`: Es un estándar de SQL que permite almacenar número exactos.
- `DECIMAL([tdig], [dec])`: Es lo mismo que `NUMERIC`.

## FECHA Y HORA

- `DATE`: Almacena fecha desde `1000-01-01` asta `9999-12-31`.
- `DATETIME`: Almacena fecha y hora desde `1000-01-01 00:00:00` a `9999-12-31 23:59:59`, a este campo se le puede dar como [valor por defecto](mysql_table.md#DEFAULT) `CURRENT_TIMESTAMP` (*fecha y hora del sistema*).
- `TIMESTAMP`: Almacena fecha y hora desde `1970-01-01 00:00:01` a `2038-01-19 03:14:07`, a este campo se le puede dar como [valor por defecto](mysql_table.md#DEFAULT) `CURRENT_TIMESTAMP` (*fecha y hora del sistema*).
- `TIME`: Almacena una hora desde `-838:59:59` a `838:59:59`.
- `YEAR[(4)]`: Almacena un año entre `1901` y `2155`, incluyendo `0000`.

## CADENA DE CARACTERES

- `CHAR([length])`: Cadena de caracteres con longitud concreta, sino se alcanza al longitud, se rellena de espacios en blanco, teniendo un máximo de 255 bytes como longitud.
- `VARCHAR([length])`: Cadena de caracteres con longitud máxima variable, teniendo un máximo de 65.535 bytes de longitud.
- `BLOB([length])`: Almacena objetos binarios de longitud variable, teniendo una longitud máxima de 65.535 bytes, no puede tener valor por defecto.
- `TINYBLOB([length])`: Es lo mismo que el `BLOB` pero la longitud máxima es de (*1 Byte*) 255 bytes.
- `MEDIUMBLOB([length])`: Es lo mismo que el `BLOB` pero la longitud máxima es de (*16 MiB*) 16.777.215 bytes.
- `LONGBLOB([length])`: Es lo mismo que el `BLOB` pero la longitud máxima es de (*4 GiB*) 4.294.967.295 bytes.
- `TEXT([length])`: Almacena texto, pudiendo especificar una longitud máxima, teniendo esta el límite de 65.535 caracteres.
- `TINYTEXT([length])`: Es lo mismo que el `TEXT` pero con un máximo de 255 caracteres.
- `MEDIUMTEXT([length])`: Es lo mismo que el `TEXT` pero con un máximo de 16.77.215 caracteres.
- `LONGTEXT([length])`: Es lo mismo que el `TEXT` pero con un máximo de 4.294.967.295 caracteres.
- `ENUM('[v1]', '[v2]', ...)`: Almacena únicamente uno de los valores especificados, se pueden indicar asta 65.535 opciones.
- `SET('[v1]', '[v2]', ...)`: Almacena uno o varios valores que de los especificados, se puede indicar asta 64 opciones.
