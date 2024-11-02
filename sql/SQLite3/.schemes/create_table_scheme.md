---
autor: SQLite
title: Esquema del como crear una tabla en SQLite
tags:
  - Mindusting
  - SQL
  - SQLite
  - Create
  - Table
  - Scheme
corrected: false
---

```txt
o─>(CREATE)┬────────────┬>(TABLE)┬>(IF)─>(NOT)─>(EXISTS)┐
           ├>(TEMP)─────┤        │                      │
           └>(TEMPORARY)┘        │                      │
┌─────────────────<──────────────┴─────────────<────────┘
├─>(schema-name)─>(.)┬>(table-name)┬>(AS)─>[select-stmt]───────>─────┐
└───────>────────────┘             │                                 │
┌───────────────────<──────────────┘                ┌────────>───────┼>o
└─>(()┬>[column-def]┬>┬────────────────────────┬>())┴>[table-options]┘
      └──────(,)<───┘ └[table-constraint]<─(,)<┘
```


```mermaid
---
title: ESQUEMA DE CREACIÓN DE UNA TABLA
---
flowchart TB
    %% DECLARACIÓN DE NODOS

    _start((START))
    _end((END))

    kw_create([CREATE])
    kw_temp([TEMP])
    kw_temporaly([TEMPORALY])

    kw_table([TABLE])
    kw_if([IF])
    kw_not([NOT])
    kw_exists([EXISTS])

    schema_name([schema-name])
    schema_dot([.])

    table_name([table-name])

    kw_as([AS])
    select_stmt[select-stmt]

    open_column_def(["("])
    column_def[column-def]
    column_sep([","])
    table_const_sep([","])
    table_const[table-constraint]
    close_column_def([")"])

    table_options[table-options]


    %% ESTRUCTURA DEL ESQUEMA

    _start --> kw_create

    kw_create --> kw_table
    kw_create -.-> kw_temp & kw_temporaly -.-> kw_table

    kw_table --> table_name
    kw_table -.-> kw_if -.-> kw_not -.->
    kw_exists -.-> table_name & schema_name

    kw_table -.-> schema_name -.-> schema_dot -.-> table_name

    table_name -.-> kw_as -.-> select_stmt -.-> _end

    table_name --> open_column_def
    --> column_def <--> column_sep

    column_def -.-> table_const_sep
    <-.-> table_const

    table_const -.-> close_column_def
    -.-> table_options -.-> _end

    column_def --> close_column_def
    --> _end
```
