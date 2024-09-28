---
author: Mindusting
corrected: false
tags:
  - Programming/SQL
title: Consultas en SQLite3
---

<h1 style="text-align:center;">SELECT EN SQLITE</h1>

---

[WEB - SQLite3 (SELECT)](https://sqlite.org/lang_select.html)

Para hacer una consulta tendremos que seguir el siguiente esquema:

%%
ESQUEMA DE CONSULTA DE DATOS

```txt
o┬>(WITH)┬─────>────────┬─┬>[common-table-expression]┐
 v       └>(RECURSIVE)─>┘ └────────────(,)<──────────┤
 ├──────────────────────<────────────────────────────┘
 │ ┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
┌┴─>┬─>(SELECT)┬─────>───────┬─┬>[result-column]┐    s│
│  ││          ├>(DISTINCT)─>┤ └───────(,)<─────┤    e 
│   │          └>(ALL)──────>┘                  v    l│
^  ││ ┌──────────────────────<──────────────────┘    e 
│   │ ├>(FROM)┬─┬>[table-or-subquery]┬─┬>┐           c│
│  ││ │       │ └─────────(,)<───────┘ ^ v           t 
│   │ │       └─────>[join-clause]─────┘ │           -│
│  ││ ├─────────────────────<────────────┘           c 
│   │ ├>(WHERE)─>[expr]┐                             o│
│  ││ v                │                             r 
│   │ ├────────<───────┘                             e│
│  ││ ├─────────>─────────────┐
│   │ ├>(GROUP)─>(BY)┬>[expr]┬┴>┬>(HAVING)─>[expr]┬┐  │
│  ││ v              └──(,)<─┘  └──────>──────────┘v
│   │ ├─────────────────────<──────────────────────┘  │
│  ││ ├>(WINDOW)┬>(window-name)─>(AS)─>[windows-defn]┐
│   │ │         └────────────────(,)<────────────────┤│
│  ││ │                                              v
│   │ └───────────────────>──────────────────────────┤│
│  ││               ┌──(,)<─┐                        │
│   └─>(VALUES)┬>(()┴>[expr]┴>())┬──────────────────>┤│
│  │           └───────(,)<──────┘                   │
│   ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─│┘
└──────────────[compound-operator]<──────────────────┤
┌────────────────────<───────────────────────────────┘
├>(ORDER)─>(BY)─┬>[ordering.term]┬┐
v               └──────(,)<──────┘│
├───────────────<─────────────────┘
├>(LIMIT)─>[expr]─>┬──────────────────>┐
│                  ├>(OFFSET)─>[expr]─>┤
│                  └>(,)─>[expr]──────>┤
└─────────────────────────────────────>┴>─o
```
%%

```mermaid
---
title: ESQUEMA DE CONSULTA
---
flowchart TB
    __start((START))

    kw_with([WITH])
    kw_recursive([RECURSIVE])
    cte[common-table-expression]
    ctes([","])

    subgraph SELECT-CORE
        __start_core((" "))
        kw_select([SELECT])
        kw_distinct([DISTINCT])
        kw_all([ALL])
        rc[result-column]
        rcs([","])

        meet_from((" "))
        kw_from([FROM])
        tos[table-or-subquery]
        toss([","])
        jc[join-clause]

        meet_where((" "))
        kw_where([WHERE])
        where_expr[expr]

        meet_group((" "))
        kw_group([GROUP])
        group_by([BY])
        meet_group_by((" "))
        group_by_expr[expr]
        group_by_expr_sep([","])

        meet_window((" "))
        kw_window([WINDOW])

        meet_values((" "))
        kw_values([VALUES])
        __end_core((" "))
    end
    co[compound-operator]
    __end((END))


    __start -.-> 
    kw_with -.-> kw_recursive & cte
    kw_recursive -.-> cte <-.-> ctes
    cte -.-> __start_core
    __start --> __start_core -->
    kw_select & kw_values

    kw_select -.-> kw_distinct & kw_all
    -.-> rc --> meet_from --> kw_from
    meet_from -.-> meet_where
    kw_select --> rc <--> rcs

    kw_from --> tos <--> toss
    kw_from --> jc --> meet_where
    tos --> meet_where

    meet_where --> kw_where -->
    where_expr --> meet_group

    meet_group -.-> kw_group -.->
    group_by -.-> group_by_expr
    <-.-> group_by_expr_sep
    meet_group -.-> meet_group_by
    group_by --> 

    meet_from -.-> meet_where -->
    meet_group --> meet_window
    --> meet_values

    __end_core -.-> co -.-> __start_core
```

%%
```mermaid
---
title: ESQUEMA DE CONSULTA
---
flowchart TB
    _start((START))
    _end((END))

    kw_with([WITH])
    kw_recursive([RECURSIVE])
    cte[common-table-expression]
    ctes([","])

    subgraph SELECT-CORE
        kw_select([SELECT])
        kw_distinct([DISTINCT])
        kw_all([ALL])
        rc[result-column]
        rcs([","])
        kw_from([FROM])
        tos[table-or-subquery]
        toss([","])
        jc[join-clause]
        kw_where([WHERE])
        w_expr[expr]
        kw_group([GROUP])
        kw_group_by([BY])
        kw_having([HAVING])
        kw_window([WINDOW])
        kw_as([AS])
        kw_values([VALUES])
    end
    co[compound-operator]
    kw_order([ORDER])
    kw_order_by([BY])
    kw_limit([LIMIT])
    kw_offset([OFFSET])


    _start -.-> kw_with -.-> cte & kw_recursive
    kw_recursive -.-> cte <-.-> ctes
    cte -.-> kw_select

    _start --> kw_select

    kw_select -.-> kw_distinct & kw_all -.-> rc
    kw_select --> rc <--> rcs

    rc -.-> kw_where & kw_group & kw_window & co
    rc --> kw_from --> tos <-.-> toss
    tos --> kw_where & kw_group & kw_window & co
    
    kw_from --> jc --> kw_where & kw_group & kw_window 

    kw_where --> w_expr --> kw_group & kw_window & co

    co -.-> kw_select
```
%%

Un ejemplo de ello sería el siguiente:

```sql
SELECT id, name FROM users;
```
