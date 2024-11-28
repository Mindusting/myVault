---
author: Mindusting
corrected: false
tags:
  - Programming/SQL/MySQL
title: MySQL
---

<h1 align="center">MYSQL</h1>

![#logo](../../img/db.png)

---

# MYSQL

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

> [!help] REFERENCIAS WEB
> - [MySQL Doc](https://dev.mysql.com/doc/)

## ÍNDICE

- [BASES DE DATOS](mysql_db.md)
- [TIPOS DE DATOS](mysql_data_types.md)
- [TABLAS](mysql_table.md)

---
---
---

## DESCRIPCIÓN DE TABLA

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

```sql
DESC users;
```

| Field | Type         | Null | Key | Default | Extra |
| ----- | ------------ | ---- | --- | ------- | ----- |
| id    | int unsigned | NO   | PRI | `Null`  |       |
| name  | varchar(32)  | NO   |     | `Null`  |       |

# CONSTRAINT

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

El `CONSTRAINT` sirve para darle nombre a las restricciones.

## BORRAR ATRIBUTOS DE UNA TABLA

```sql
ALTER TABLE [table_name]
DROP [atribute_name];
```

## BORRAR CLAVE PRIMARIA

```sql
ALTER TABLE [table_name]
DROP PRIMARY KEY;
```
