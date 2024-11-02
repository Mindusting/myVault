# aggregate-function-invocation

- [aggregate-function-invocation](<https://www.sqlite.org/syntax/aggregate-function-invocation.html>)

```txt
                          ┌>(DISTINCT)─>┐ ┌──(,)<─┐
o─>(aggregate-func)─>(()─>┼─────>───────┴>┴>[expr]┼────────┬┬>())┬────────>───────┬>o
                          │┌──────────────────────┘        ││    └>[filter-clause]┘
                          │└>(ORDER)─>(BY)┬>[ordering-term]┤│
                          │               └───────(,)<─────┘│
                          └────────────┬>(*)┬>──────────────┘
                                       └─>──┘
```
