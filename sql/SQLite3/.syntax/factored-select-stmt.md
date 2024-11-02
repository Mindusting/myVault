# factored-select-stmt

- [factored-select-stmt](<https://www.sqlite.org/syntax/factored-select-stmt.html>)

```txt
o┬>(WITH)┬─────>────────┬─┬>[common-table-expression]┬┐
 │       └>(RECURSIVE)─>┘ └───────────(,)<───────────┘│
 ├───────────────────────<────────────────────────────┘
 └┬────[select-core]───┬┐
  └[compound-operator]<┘│
 ┌──────────────────────┘
 ├>(ORDER)─>(BY)─┬>[ordering-term]┬┐
 v               └──────(,)<──────┘│
 ├───────────────<─────────────────┘
 ├>(LIMIT)─>[expr]─>┬───────────────────>┐
 │                  ├>(OFFSERT)─>[expr]─>┤
 │                  └>(,)─>[expr]───────>┤
 └──────────────────────────────────────>┴>o
```
