---
author: Mindusting
corrected: false
tags:
  - Programming/SQL/MySQL
title: Tablas en MySQL
---

# TABLA

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

> [!faq] FAQ
> - [¿Qué son las tablas en SQL?](../sql_table.md)

Una tabla nos permite almacenar información de forma ordenada dentro de nuestra DB, una DB puede albergar múltiples tablas, las cuales pueden estar relacionadas entre sí.

> [!abstract] SINTAXIS
> CREATE TABLE ***\[table\_name\]*** (***\[field\_name\]***);

```sql
-- Indicamos que la DB en la que queremos trabajar es "my_db".
use my_db;

-- Indicamos la creación de la DB.
CREATE TABLE users (
    -- La DB tendrá un solo campo, siendo este "id".
    id INTEGER
);
```

Una tabla requiere de al menos un campo en el que se pueda guardar información, el campo indicado en este ejemplo es "*id*", este almacenará un valor entero y se usará para identificar cada [registro](#^Crear-registros)[^registro] (*Por así decirlo, es una matrícula para cada [registro](#^Crear-registros)*), dando le un valor distinto a cada uno, pero tal y como está ahora, diferentes [registro](#^Crear-registros) pueden tener el mismo valor en este capo, para evitar esto hay que [modificarlo](#^Modificar-una-tabla) para convertirlo en un valor *key*.

[^registro]: Un registro es un objeto donde se guardan los datos de por ejemplo un cliente, si creamos una tabla llamada "*clientes*", dentro de estas se guardarán los *registros* "*cliente*", a su vez, cada uno de estos almacenará el \[nombre, apellidos, DNI, email, ...\] del cliente por cada registro (*Objeto "cliente"*).

---
---
---

Para crear una nueva tabla haremos uso de la instrucción `CREATE TABLE`, al igual que en el siguiente ejemplo.

```mermaid
flowchart TB
    inicio((INICIO)) -->
    create([CREATE]) -.->
    if([IF]) -.->
    not([NOT]) -.->
    exist([EXIST]) -.->
    table_name{{table_name}}
    create --> table_name -->
    parenthesis0o(["("]) -->
    column_def[column_def] -.->
    coma0([","]) -.->
    column_def -->
    parenthesis0c([")"]) -->
    fin((FIN))
```

---

```sql
CREATE TABLE users (
    id INT UNSIGNED PRIMARY KEY,
    name VARCHAR(32) NOT NULL
);
```

## LISTAR TABLAS

> [!abstract] SINTAXIS
> SHOW FULL TABLES FROM ***\[db_name\]***;

```sql
SHOW FULL TABLES FROM ;
```
