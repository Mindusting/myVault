# qualified-table-name

- [qualified-table-name](<https://www.sqlite.org/syntax/qualified-table-name.html>)

```txt
o┬>(schema-name)─>(.)┬>(table-name)┬─────>──────────┐
 └───────>───────────┘             └>(AS)─>(alias)─>┤
                                                    v
                   ┌────────────────────────────────┤
                   │                                v
                   ├>(INDEXED)─>(BY)─>(index-name)─>┤
                   └>(NOT)─>(INDEXED)───────────────┴─>o
```
