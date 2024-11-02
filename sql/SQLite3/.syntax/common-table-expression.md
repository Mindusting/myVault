# COMMON-TABLE-EXPRESSION

- [COMMON-TABLE-EXPRESSION](<https://www.sqlite.org/syntax/common-table-expression.html>)

```txt
                 ┌──────────────>───────────┐
o─>(table-name)─>┴>(()─>┬>(column-name)┬>())┴>┐
                        └──────(,)<────┘      │
┌─────────────────────────────────────────────┘
│       ┌>(NOT)┬>(MATERIALIZED)┐
└>(AS)─>┴──────┴───────────────┴>(()─>[select-stmt]─>())─>o
```
