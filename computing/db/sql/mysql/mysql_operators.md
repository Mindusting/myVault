---
author: Mindusting
corrected: false
tags:
  - DB/SQL
  - DB/MySQL
title: Operadores en MySQL
---

# OPERADORES EN MYSQL

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [x] Documentar los operadores aritméticos.
> > - [ ] Documentar los operadores bitwise.
> > - [x] Documentar los operadores comparación.
> > - [ ] Documentar los operadores compuesto.
> > - [ ] Documentar los operadores lógicos.
> >     - [ ] ALL
> >     - [ ] AND
> >     - [ ] ANY
> >     - [ ] BETWEEN
> >     - [ ] EXISTS
> >     - [ ] IN
> >     - [ ] LIKE
> >     - [ ] NOT
> >     - [ ] OR
> >     - [ ] SOME

> [!help]- REFERENCIAS WEB
> - [W3 (MySQL operators)](https://www.w3schools.com/mysql/mysql_operators.asp)

Los operadores más básicos que tendremos que saber para poder hacer consultas y cambios en la base de datos son los siguientes:

- [Aritméticos](#ARITMÉTICOS)
- [Comparación](#COMPARACIÓN)
- [Lógicos](#LÓGICOS)

## ARITMÉTICOS

Los **operadores aritméticos** sirven para hacer operaciones más simples de las matemáticas, como son la *suma*, *resta*, *multiplicación*, *división* y *resto*.

> [!abstract] SINTAXIS
> ***\[operandoA\] \[operador\] \[operandoB\]***

| OPERADOR | DESCRIPCIÓN                            |
|:--------:|:-------------------------------------- |
|   `+`    | Suma los dos operandos.                |
|   `-`    | Resta los dos operandos.               |
|   `*`    | Multiplica los dos operandos.          |
|   `/`    | Divide los dos operandos.              |
|   `%`    | Resto de la división de los operandos. |

> [!example] EJEMPLO
> Si quisiéramos ver todos los empleados que cobran más de 40.000 € al año, podemos calcularlo multiplicando su salario por 12 y luego comparándolo con los 40.000 € anuales.
> 
> ```sql
> SELECT *
> FROM employees
> WHERE salary * 12 >= 40000;
> --           ^
> -- Se calcula el salario anual.
> ```

## BITWISE

- `&`
- `|`
- `^`

## COMPARACIÓN

Los **operadores de comparación** permiten (*como su nombre indica*) comparar dos operandos, dando siempre como resultado un [valor booleano](../../../pc/pc_boolean.md).

> [!abstract] SINTAXIS
> ***\[operandoA\] \[operador\] \[operandoB\]***

| OPERADOR | DESCIPCIÓN                   |
|:--------:|:---------------------------- |
|   `=`    | *A* es igual que *B*         |
|   `>`    | *A* es mayor que *B*         |
|   `<`    | *A* es menor que *B*         |
|   `>=`   | *A* es mayor o igual que *B* |
|   `<=`   | *A* es menor o igual que *B* |
|   `<>`   | *A* es diferente de *B*      |

> [!example] EJEMPLO
> Si queremos obtener los productos que tengan un precio menor a 30 € podemos hacerlo de la siguiente forma:
> 
> ```sql
> SELECT *
> FROM products
> WHERE price < 30;
> ```

## COMPUESTO

- `+=`
- `-=`
- `*=`
- `/=`
- `%=`
- `&=`
- `^-=`
- `|*=`

## LÓGICOS

- [`ALL`](#ALL): indica si el operando de comparación se cumple en todos los casos.
- [`AND`](#AND): indica si los dos operandos de comparación son verdaderos.
- [`ANY`](#ANY): indica si el operando de comparación se cumple en por lo menos un caso.
- [`BETWEEN`](#BITWEEN): indica si el operando se encuentra dentro de un rango.
- [`EXISTS`](#EXISTS): indica si la subconsulta devuelve alguna tupla.
- [`IN`](#IN): indica si el operando es igual a alguno de los especificados.
- [`LIKE`](#LIKE): indica si el operando coincide con el patrón.
- [`NOT`](#NOT): invierte el resultado lógico.
- [`OR`](#OR): indica si alguno de los dos operando es cierto.
- [`SOME`](#SOME): alias de `ANY`.

### ALL

### AND

### ANY

### BETWEEN

### EXISTS

### IN

### LIKE

### NOT

### OR

### SOME
