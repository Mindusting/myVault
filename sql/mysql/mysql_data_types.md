---
author: Mindusting
corrected: false
tags:
  - Programming/SQL/MySQL
title: Tipos de datos en MySQL
---

# TIPOS DE DATOS

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

## NUMÉRICOS

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

> [!help] EN ESTE APARTADO SE HACE USO DE LOS SIGUIENTES RECURSOS
> - [Anotación de rango](../../math/math_range_notation.md).

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

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

- `NUMERIC`
- `DECIMAL`

## FECHA Y HORA

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

- `DATE`: Almacena fecha desde `1000-01-01` asta `9999-12-31`.
- `DATETIME`
- `TIMESTAMP`
- `TIME`
- `YEAR`

## CADENA DE CARACTERES

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

- `CHAR`
- `VARCHAR`
- `BLOB`
- `TINYBLOB`
- `MEDIUMBLOB`
- `LONGBLOB`
- `TEXT`
- `TINYTEXT`
- `MEDIUMTEXT`
- `LONGTEXT`
- `ENUM`
- `SET`
