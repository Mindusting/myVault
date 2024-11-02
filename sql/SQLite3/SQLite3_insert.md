---
author: Mindusting
corrected: false
tags:
  - Programming/SQL
title: Insertar datos en SQLite3
---

<h1 style="text-align:center;">INSERT EN SQLITE</h1>

---

[Documentación oficial](https://sqlite.org/lang_insert.html)

Para poder insertar un nuevo registro en una tabla se sigue el siguiente esquema:

%%
ESQUEMA DE INSERCIÓN DE REGISTRO

```txt
o┬>(WITH)┬─────>────────┬┬>[common-table-expression]┐
 v       └>(RECURSIVE)─>┘└────────────(,)<──────────┤
 ├──────────────────────<───────────────────────────┘
 ├>(REPLACE)───────────────────┬>(INTO)┐
 └>(INSERT)┬──────────────────>┤       │
           └>(OR)┬>(ABORT)────>┤       │
                 ├>(FAIL)─────>┤       v
                 ├>(IGNORE)───>┤       │
                 ├>(REPLACE)──>┤       │
                 └>(RELLBACK)─>┘       │
┌─────────────<─────┬──────────────────┘
│                   v
└>(schema-name)─>(.)┴>(table-name)┬>(AS)─>(alias)┐
                                  v              │
┌─────────────────────────────────┴─────<────────┘
├>(()┬>(column-name)┬>())┐
│    └──────(,)<────┘    │
├────────────<───────────┘
├>(VALUES)┬>(()┬>[expr]┬>())┬───────────────────>┐
│         │    └──(,)<─┘    ├>┬>[upsert-clause]─>┤
│         └───────(,)<──────┘ │                  │
├>[select-stmt]───────────────┴─────────────────>┤
└>(DEFAULT)─>(VALUES)───────────────────────────>┤
                            ┌──────────<─────────┤
                            └>[returning-clause]─┴─o
```
%%

Un ejemplo de ello es el siguiente:

```sql
INSERT INTO users (
    name,
    last_name,
    email
) values (
    'Adelio',
    'Gonzalez',
    'adelio@gmail.com'
);
```
