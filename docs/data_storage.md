# How data is stored in sqlite3
```
trnsaction (
 t_id          INTEGER       PRIMARY KEY NOT NULL,
 date          INTEGER       NOT NULL DEFAULT '0',
 category      TEXT          NOT NULL DEFAULT "Uncategorised" REFERENCES trnsactino_categories(category),
 description   TEXT          NULL,
 value         INTEGER       NOT NULL DEFAULT '0',
 cc_value      INTEGER       NOT NULL DEFAULT '0'
)

trnsaction_categories (
 category  TEXT      PRIMARY KEY NOT NULL,
 seq       INTEGER   UNIQUE NOT NULL
)
```