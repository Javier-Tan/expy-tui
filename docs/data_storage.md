# Data stored in sqlite3
```
trnsaction (
 t_id          INTEGER       PRIMARY KEY,
 date          INTEGER       NOT NULL DEFAULT '0',
 category      TEXT          NOT NULL DEFAULT "",
 description   TEXT          NULL,
 value         INTEGER       NOT NULL DEFAULT '0',
 cc_value      INTEGER       NOT NULL DEFAULT '0'
)
```