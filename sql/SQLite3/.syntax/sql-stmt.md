# sql-stmt

- [sql-stmt](<https://www.sqlite.org/syntax/sql-stmt.html>)

```txt
o┬──────────┬>───────────────┬>┬>[alter-table-stmt]──────────>┬>o
 └>(EXPLAIN)┴>(QUERY)─>(PLAN)┘ ├>[analyze-stmt]──────────────>┤
                               ├>[attach-stmt]───────────────>┤
                               ├>[begin-stmt]────────────────>┤
                               ├>[commit-stmt]───────────────>┤
                               ├>[create-index-stmt]─────────>┤
                               ├>[create-trigger-stmt]───────>┤
                               ├>[create-view-stmt]──────────>┤
                               ├>[create-virtual-table-stmt]─>┤
                               ├>[delete-stmt]───────────────>┤
                               ├>[delete-stmt-limited]───────>┤
                               ├>[delach-stmt]───────────────>┤
                               ├>[drop-index-stmt]───────────>┤
                               ├>[drop-table-stmt]───────────>┤
                               ├>[drop-trigger-stmt]─────────>┤
                               ├>[drop-view-stmt]────────────>┤
                               ├>[insert-stmt]───────────────>┤
                               ├>[pragma-stmt]───────────────>┤
                               ├>[reindex-stmt]──────────────>┤
                               ├>[release-stmt]──────────────>┤
                               ├>[rollback-stmt]─────────────>┤
                               ├>[savepoint-stmt]────────────>┤
                               ├>[select-stmt]───────────────>┤
                               ├>[update-stmt]───────────────>┤
                               ├>[update-stmt-limited]───────>┤
                               └>[vacuum-stmt]───────────────>┘
```
