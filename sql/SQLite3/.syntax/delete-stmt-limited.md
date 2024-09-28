# delete-stmt-limited

- [delete-stmt-limited](<https://www.sqlite.org/syntax/delete-stmt-limited.html>)

```txt
o┬>(WITH)┬─────>────────┬─┬>[common-table-expression]┐
 │       └>(RECURSIVE)─>┘ └────(,)<─────┘            │
 ├────────────────────────<──────────────────────────┘
 └>(DELETE)─>(FROM)─>[qualified-table-name]┬┐
 ┌─────────────────────────────────────────┘│
 ├>(WHERE)─>[expr]┬─────────────────────────┤
 ├────────<───────┘                         │
 ├>[returning-clause]┬──────────────────────┤
 ├────────<──────────┘                      │
 ├>(ORDER)─>(BY)┬>[ordering-term]┐          │
 │              └──────(,)<──────┤          │
 ├────────────<──────────────────┘          │
 └>(LIMIT)─>[expr]┬───────────────────┬─────┴>o
                  ├>(OFFSET)─>[expr]─>┤
                  └>(,)─>[expr]───────┘
```
