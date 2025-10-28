---
author: Mindusting
corrected: false
tags:
  - DB/SQL
title: Selección en SQL
---

# SELECCIÓN EN SQL

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Explicar que es y en qué consiste al selección de datos.
> > - [ ] Explicar que el orden de estas instrucciones no se puede alterar.
> > - [ ] Hacer apartado combinaciones.
> >     - [ ] Hacer apartado combinación de columnas.
> >     - [ ] Hacer apartado combinación de tuplas.
> > - [ ] Hacer 

| KEY WORD                  | ACCIÓN                       |
|:------------------------- |:---------------------------- |
| [`SELECT`](#SELECT)       | Columnas a obtener           |
| [`FROM`](#FROM)           | Tabla a leer                 |
| [`JOIN`](#COMBINACIONES)  | Combinación de tablas        |
| [`WHERE`](#WHERE)         | Filtrado de datos por tablas |
| [`GROUP BY`](#GROUP%20BY) | Agrupación de tuplas         |
| [`HAVING`](#HAVING)       | Filtrado de datos por grupos |
| [`ORDER BY`](#ORDER%20BY) | Orden de resultado           |
| [`LIMIT`](#LIMIT)         | Límite de tuplas             |

## SELECT

> [!important] IMPORTANTE
> Los ejemplos que te encuentres en este apartado no funcionarán por sí solos, ya que las sentencias están incompletas (*ya que no se indica de qué tabla se quiere obtener los datos*), esto es para simplificar la enseñanza fragmentando en partes cada sentencia, si quieres ver como crear sentencias funcionales ve al [apartado `FROM`](#FROM).

La palabra clave `SELECT` permite indicar qué columnas (*separadas por comas*) queremos obtener de la **tabla** o **tablas** sobre las que estemos trabajando.

> [!abstract] SINTAXIS
> SELECT ***\[columns\]***

Cuando empezamos solemos hacer lo trabajando sobre sobre una única tabla, en este aso usaremos la siguiente tabla de usuarios como ejemplo, esta contiene un *identificador*, *nombre* y *país*.

|  id | name   | country |
| ---:|:------ |:------- |
|   1 | Adelio | España  |
|   2 | Adelia | España  |

> [!example] EJEMPLO DE USO DEL ASTERISCO
> Si queremos obtener todas las columnas escribiremos `SELECT *`, esto es debido a que el asterisco es una carácter especial (*en este contexto*) que permite indicar que queremos obtener todas las columnas; estas se nos mostrarán en el orden en el que estén en la propia tabla.

> [!example] EJEMPLO
> Si queremos obtener solo los *nombres* de los **usuarios** lo podemos hacer especificando el nombre de la columna que contiene esta información con la sentencia `SELECT name`, dando así el siguiente resultado:
> 
> | name   |
> |:------ |
> | Adelio |
> | Adelia |

### RENOMBRAR COLUMNAS

> [!important] IMPORTANTE
> El renombrado de **columnas** solamente se aplica al resultado, esto quiere decir que no cambiaremos el nombre de la **columna** de la tabla que estemos leyendo.

Si queremos que el nombre de las **columnas** en el resultado sea distinto al original, podemos cambiar lo con la palabra clase `AS` seguido del *nuevo nombre*.

> [!abstract] SINTAXIS
> ***\[columnName\]*** AS ***\[newColumnName\]***

> [!example] EJEMPLO
> Si queremos cambiar los nombres a de las columnas a español por que el resultado vamos a (*por ejemplo*) copiarlo y pegarlo en forma de tabla en otro sitio, podemos hacer de la siguiente manera:
> 
> ```sql
> SELECT
>     id      AS ID,
>     name    AS Nombre,
>     country AS País
> FROM users;
> ```
> 
> |  ID | Nombre | País    |
> | ---:|:------ |:------- |
> |   1 | Adelio | España  |
> |   2 | Adelia | España  |

> [!tip] TIP
> Si le quieres dar a una columna un nombre compuesto por varias palabras, debes entrecomillar lo para que funcione.

### TUPLAS DISTINTAS

Si queremos hacer una consulta en la que podemos tener tuplas repetidas, tenemos la opción de indicar que queremos que todas sean distintas; esto se hace con la palabra clave `DISTINCT`, la cual situaremos entre la palabra clave `SELECT` y la lista de **columnas**.

> [!abstract] SINTAXIS
> SELECT DISTINCT ***\[columns\]***

> [!example] EJEMPLO
> Si queremos obtener los nombre de los *países* de los que pertenecen cada **usuario** si que se repitan lo hacemos con la sentencia `SELECT DISTINCT country`.
> 
> | country |
> |:------- |
> | España  |
> 
> Si no pusiéramos la palabra clave `DISTINCT` abríamos obtenido como resultado dos tuplas con la palabra *España*.
> 
> Hay que tener en cuenta que si en la consulta tuviéramos otra **columna** sí que tendríamos dos tuplas, ya que aunque la **columna** `country` coincidiera, la otra no lo haría; y debe cumplir como la condición de que todas las **columnas** contengan la misma información para que el cribado se aplique

### CONFLICTO DE COLUMNAS

Cuando estamos trabajando sobre varias **tablas** por que las estamos [combinando](#COMBINACIONES) para hacer una consulta más compleja, es posible que estas entren en conflicto ya que tienen el mismo nombre; si esto ocurre podemos solventar lo haciendo referencia a la **tabla** de la que queremos obtener la **columna**.

> [!abstract] SINTAXIS
> ***\[tableName\]***.***\[columnName\]***

---

Este ejemplo es algo más avanzado si eres nuevo, te recomiendo seguir a partir del siguiente apartado y cuando hayas llegado a como [combinar **tablas**](#COMBINACIONES) vuelvas y así entenderás mejor este ejemplo.

Imaginemos que tenemos dos **tablas**, *usuarios* y *notas*, teniendo en cuenta que las notas están relacionadas con los *usuarios* mediante su *id*.

|  id | name   | country |
| ---:|:------ |:------- |
|   1 | Adelio | España  |
|   2 | Adelia | España  |

|  id | userId | title  | content                     |
| ---:| ------:|:------ |:--------------------------- |
|   1 |      2 | Compra | Patatas, cebollas, tomates. |
|   2 |      1 | TODO   | Tengo que aprender SQL.     |

Si queremos obtener la [combinación](#COMBINACIONES) de los *usuarios* y sus *notas* lo podemos hacer de la siguiente forma:

```sql
SELECT
    users.id AS userId,
    users.name,
    notes.id AS noteId
    notes.title,
    notes.content
FROM users
JOIN notes
    ON users.id = notes.userid;
```
^column-conflict-exmaple

Dando como resultado de la consulta la siguiente tabla:

| userId | name   | noteId | title  | content                     |
| ------ | ------ | ------ | ------ | --------------------------- |
| 2      | Adelia | 1      | Compra | Patatas, cebollas, tomates. |
| 1      | Adelio | 2      | TODO   | Tengo que aprender SQL.     |

## FROM

La palabra clave `FROM` sirve para indicar de qué **tabla** o **tablas** queremos leer la información, para ello seguido a esta palabra clave ponemos el nombre de la **tabla**.

> [!abstract] SINTAXIS
> FROM ***\[tableName\]***

|  id | name   | country |
| ---:|:------ |:------- |
|   1 | Adelio | España  |
|   2 | Adelia | España  |

Si queremos leer las columnas `name` y `country` de la **tabla** `users` tendremos que escribir la siguiente sentecia:

```sql
SELECT
    name,
    country,
FROM users;
```

Dando como resultado la siguiente tabla:

| name   | country |
|:------ |:------- |
| Adelio | España  |
| Adelia | España  |

---

Existe una opción extra que no es muy común de usar ya que es para combinar **tablas** pero de una forma distinta a la convencional; consiste en poner varios nombre de **tablas** separados por comas, este equivaldría a la [unión `JOIN`](#COMBINACIÓN) y por tanto también podremos especificar el `ON` para indicar cuando queremos que se realize esta unión.

> [!abstract] SINTAXIS
> FROM ***\[tableName\]***, ***\[tableName\]***, ...
> ON ***\[matchCondition\]***

El [ejemplo](#^column-conflict-exmaple) que se muestra en el apartado de [*conflicto entre columnas*](#CONFLICTO%20DE%20COLUMNAS) se puede hacer también de esta forma:

```sql
SELECT
    users.id AS userId,
    users.name,
    notes.id AS noteId
    notes.title,
    notes.content
FROM users, notes
    ON users.id = notes.userid;
```

## COMBINACIONES

> [!help]- REFERENCIAS WEB
> - [ATLASSIAN](https://www.atlassian.com/data/sql/sql-join-types-explained-visually)

### COMBINACIÓN DE COLUMNAS

 - `INNER JOIN`, `JOIN`
 - `LEFT JOIN`
 - `RIGHT JOIN`,
 - `FULL JOIN`, `FULL OUTER JOIN`
 - `CROSS JOIN`

> [!abstract] SISNTAXIS
> ***\[joinType\] \[tableName\]***

A lo largo de esta documentación iremos usando las siguientes dos tablas para poder entender mejor qué da como resultado los distintos tipos de JOIN:

|  id |     |
| ---:|:---:|
|   1 |  x  |
|   2 |  x  |

|  id |     |
| ---:|:---:|
|   1 |  o  |
|   3 |  o  |
|   4 |  o  |

#### DEFINE EL JOIN

Explicar el `ON`.

#### INNER JOIN

![#logo](img/inner_join.md)

|  id |     |     |
| ---:|:---:|:---:|
|   1 |  x  |  o  |

#### LEFT JOIN

![#logo](img/left_join.md)

|  id |     |     |
| ---:|:---:|:---:|
|   1 |  x  |  o  |
|   2 |  x  |     |

#### RIGHT JOIN

![#logo](img/right_join.md)

|  id |     |     |
| ---:|:---:|:---:|
|   1 |  x  |  o  |
|   3 |     |  o  |
|   4 |     |  o  |

#### FULL JOIN

FULL OUTER JOIN

![#logo](img/full_join.md)

|  id |     |     |
| ---:|:---:|:---:|
|   1 |  x  |  o  |
|   2 |  x  |     |
|   3 |     |  o  |
|   4 |     |  o  |

#### CROSS JOIN

![#logo](img/cross_join.md)

| id1 |     | id2 |     |
| ---:|:---:| ---:|:---:|
|   1 |  x  |   1 |  o  |
|   1 |  x  |   3 |  o  |
|   1 |  x  |   4 |  o  |
|   2 |  x  |   1 |  o  |
|   2 |  x  |   3 |  o  |
|   2 |  x  |   4 |  o  |

#### JOINS ANIDADOS

### COMBINACIÓN DE TUPLAS

#### UNION

#### UNION ALL

#### EXCEPT

`MINUS`

#### INTERSECT

## WHERE

## GROUP BY

## HAVING

## ORDER BY

## LIMIT

La palabra clave `LIMIT` permite indicar un **número máximo** de tuplas que queremos recibir en el resultado.

> [!abstract] SINTAXIS
> LIMIT ***\[maxRows\]***

Si al hacer una consulta solo necesitamos un número pequeño de tuplas en comparación a al que obtendríamos sin establecer el límite, es muy recomendable usarlo ya que no es solo que nos muestra el número de tuplas que queramos, sino que ni siquiera opera para obtener el resto de tuplas una vez llegado a lo exigido; por lo que obtendríamos un mayor rendimiento.

> [!example] EJEMPLO
> Imaginemos que tenemos la siguiente tabla de *empleados* (`employees`):
> 
> |  id | name      | salary |
> | ---:|:--------- | ------:|
> |   1 | Aitana    |   1778 |
> |   2 | Abril     |   1817 |
> |   3 | Raúl      |   1924 |
> |   4 | Valentina |   3338 |
> |   5 | Eric      |   3594 |
> |   6 | Gael      |   1124 |
> |   7 | Naia      |   3084 |
> |   8 | Jan       |   1110 |
> |   9 | Manuel    |   3517 |
> |  10 | Malak     |   3732 |
> 
> Para obtener el que más cobre podemos hacer de la siguiente forma:
> 
> ```sql
> SELECT *
> FROM employees
> ORDER BY salary DESC
> LIMIT 1;
> ```
> 
> |  id | name      | salary |
> | ---:|:--------- | ------:|
> |  10 | Malak     |   3732 |
> 
> ---
> 
> Igualmente hay que tener otra cosa en cuenta y es que si varios *empleado* tienen el mismo salario (*siendo este salario el más alto*), el *empleado* que obtendríamos como resultado es el que se encuentre más arriba en la tabla.
^limit-example

### LIMIT OFFSET

Si queremos establecer un desfase al límite de tupas, podemos hacer de dos formas:

> [!abstract] SINTAXIS
> LIMIT ***\[maxRows\]*** OFFSET ***\[rowsOffset\]***

> [!abstract] SINTAXIS
> LIMIT ***\[rowsOffset\]***, ***\[maxRows\]***

> [!warning] ATENCIÓN
> Fíjate que el orden en el que se especifica el *límite* y *offset* se invierte cuando se separan con coma; yo personalmente prefiero usar la versión de `OFFSET`;

> [!example] EJEMPLO
> Siguiendo con el [ejemplo](#^limit-example) del apartado [LIMIT](#LIMIT).
> 
> Si queremos obtener el segundo *empleado*, tendríamos que añadir un desfase de una tupla:
> 
> ```sql
> SELECT *
> FROM employees
> ORDER BY salary DESC
> LIMIT 1 OFFSET 1;
> ```
> 
> |  id | name      | salary |
> | ---:|:--------- | ------:|
> |   5 | Eric      |   3594 |

## CONSULTAS ANIDADAS
