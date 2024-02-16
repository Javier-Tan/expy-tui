# Data stored in sqlite3
```
trnsaction (
 t_id          INTEGER                                  PRIMARY KEY,
 date          INTEGER                                  NOT NULL DEFAULT '0',
 category      TEXT                                     NOT NULL DEFAULT "",
 description   TEXT CHECK( LENGTH(Description) <= 50 )  NULL DEFAULT NULL,
 value         INTEGER                                  NOT NULL DEFAULT '0',
 cc_balue      INTEGER                                  NOT NULL DEFAULT '0'
)

trnsaction_category_enum (
  category    TEXT          PRIMARY KEY NOT NULL,
  seq         INTEGER       NOT NULL UNIQUE
)
```