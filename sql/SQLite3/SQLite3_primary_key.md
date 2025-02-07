---
author: Mindusting
corrected: true
tags:
  - Programming/SQL
title: Clave primaria en SQLite3
---

Cada [tabla](sqlite3_tables.md) solo puede tener una clave primaria, esta será una de las columnas y el valor que contenga no se podrá repetir entre los diferentes registros, por lo que tendrá el atributo [`unique`](SQLite3_unique.md) de forma implícita.

```sql
CREATE TABLE "users" (
    "id"         INTEGER,
    "first_name" TEXT,
    PRIMARY KEY("id" AUTOINCREMENT)
);
```

En la declaración de la clave primaria, se puede ver como al final, se indica el atributo [`AUTOINCREMENT`](SQLite3_autoincrement.md), esto es para que cuando [insertemos](SQLite3_insert.md) un registro sin indicar el valor de la clave primaria, esta se adquiera automáticamente, cogiendo el valor más grande que se encuentre en esta columna y sumándo le `1`, en el caso en el que no haya ningún registro, el primer valor que obtendrá es `1`.

---

Para entender esto, imaginemos que tenemos la tabla `users` con los siguientes registros:

| id | first_name |
|---:|:-----------|
|  1 | admin      |
|  2 | Mindusting |
|  4 | Adelio     |

Si te fijas en los `id`, podrás ver que falta el registro `3`, esto puede ser por qué este registro ha sido [eliminado](SQLite3_delete.md) después de [insertar](SQLite3_insert.md) el registro `4` o por qué el registro cuatro se a [insertado](SQLite3_insert.md) indicando específicamente que se quería que tuviera ese `id`, en cualquier caso, cuando nosotros hagamos una nueva [inserción](SQLite3_insert.md) sin indicar un `id`, lo que hará SQLite3 será buscar el valor más grande, siendo en este caso `4`, para luego sumarle `1` e insertar el nuevo registro con el resultado de la operación anterior, quedando algo como esto:

| id | first_name |
|---:|:-----------|
|  1 | admin      |
|  2 | Mindusting |
|  4 | Adelio     |
|  5 | Adelia     |
