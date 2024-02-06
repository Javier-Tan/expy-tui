# Data stored in sqlite3
```
Transactions (
 Id            INTEGER                                  PRIMARY KEY,
 Date          INTEGER                                  NOT NULL DEFAULT '0',
 Category      TEXT                                     NOT NULL DEFAULT 'M',
 Description   TEXT CHECK( LENGTH(Description) <= 50 )  NULL DEFAULT NULL,
 Value         INTEGER                                  NOT NULL DEFAULT '0',
 CCValue       INTEGER                                  NOT NULL DEFAULT '0'
)

TransactionDescription (
  Type    CHAR(1)       PRIMARY KEY NOT NULL,
  Seq     INTEGER       NOT NULL UNIQUE
)
```