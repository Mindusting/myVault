---
autor: SQLite
title: Esquema del INSERT en SQLite
tags:
  - Mindusting
  - SQL
  - SQLite
  - Insert
  - Scheme
corrected: false
---

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
├>(VALUES)┬>(()┬>[expr]┬>())┬─────────────────>┐
│         │    └──(,)<─┘    ├>[upsert-clause]─>┤
│         └───────(,)<──────┘                  │
├>[select-stmt]─────────────┬─────────────────>┤
│                           └>[upsert-clause]─>┤
└>(DEFAULT)─>(VALUES)─────────────────────────>┤
                          ┌──────────<─────────┤
                          └>[returning-clause]─┴─o
```

```mermaid
---
title: ESQUEMA DE INSERCIÓN DE REGISTRO
---
flowchart TB
    %% DECLARACIÓN DE NODOS

    _start((START))
    _end((END))

    kw_with([WITH])
    kw_recursive([RECURSIVE])
    cte[common-table-expression]
    ctes([","])

    kw_replace1([REPLACE])

    kw_insert([INSERT])

    kw_into([INTO])
    kw_or([OR])
    kw_abort([ABORT])
    kw_fail([FAIL])
    kw_ignore([IGNORE])
    kw_replace2([REPLACE])
    kw_rellback([RELLBACK])

    sn([schema-name])
    sn_sep([","])

    table_name([table-name])

    kw_as([AS])
    alias([alias])

    ocn(["("])
    cn([column-name])
    cns([","])
    ccn([")"])

    kw_values1([VALUES])
    values1_sep([","])
    oexpr(["("])
    expr([expr])
    exprs([","])
    cexpr([")"])

    upsert_cause[upsert-cause]

    select_stmt([select-stmt])

    kw_default([DEFAULT])
    kw_values2([VALUES])

    rc[returning-clause]


    %% ESTRUCTURA DEL ESQUEMA

    _start -.-> kw_with
    -.-> kw_recursive
    -.-> cte
    kw_with -.-> cte
    <-.-> ctes
    cte -.-> kw_replace1 & kw_insert

    _start -.-> kw_replace1
    -.-> kw_into

    _start --> kw_insert --> kw_into
    kw_insert -.-> kw_or -.-> kw_abort -.-> kw_into

    kw_or -.-> 
    kw_fail & kw_ignore & kw_replace2 & kw_rellback
    -.-> kw_into

    kw_into -.-> sn
    -.-> sn_sep -.-> table_name
    -.-> kw_as -.-> alias

    alias -.-> ocn & kw_values1 & select_stmt & kw_default

    table_name -.-> kw_values1

    kw_into --> table_name
    --> ocn --> cn --> ccn
    --> kw_values1
    cn <--> cns

    kw_values1 -->oexpr
    --> expr --> cexpr --> _end
    expr <--> exprs

    cexpr --> values1_sep --> oexpr

    cexpr -.-> upsert_cause -.-> _end

    table_name -.-> select_stmt -.-> upsert_cause

    table_name -.-> kw_default
    -.-> kw_values2 -.-> _end

    cexpr -.-> rc
    upsert_cause -.-> rc
    select_stmt -.-> rc
    kw_values2-.-> rc
    -.-> rc -.-> _end
```
