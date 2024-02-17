"""Interface and implementations for creating, reading, updating and deleting transaction data.

All data should be stored in the equivelant of the below SQL example
trnsaction (
    t_id integer PRIMARY KEY AUTOINCREMENT,
    date integer NOT NULL DEFAULT '0',
    category text NOT NULL,
    description text,
    value int NOT NULL DEFAULT 0,
    cc_value int NOT NULL DEFAULT 0
);
"""
import sqlite3
from abc import ABC, abstractmethod
from datetime import datetime

from expy_tui.transaction.transaction import Transaction


class TransactionCRUD(ABC):
    """Interface for all CRUD relating to transactions.

    Should be a singleton.
    """

    @abstractmethod
    def create_transaction(self, transaction: Transaction) -> bool:
        """Create transaction in the database based on Transaction instance.

        Returns True if success, False if failed.
        """

    @abstractmethod
    def get_transactions_filters(
            self, date_range: tuple[datetime, datetime] | None = None,
            categories: list[str] | None = None,
        ) -> list[Transaction]:
        """Return list of transactions based on filters date_range and categories."""

    @abstractmethod
    def get_transaction_by_id(self, t_id: int) -> Transaction:
        """Return transaction by ID."""

    @abstractmethod
    def update_transaction(self, transaction: Transaction) -> bool:
        """Update a transaction in the database based on Transaction instance."""

    @abstractmethod
    def delete_transaction(self, transaction: Transaction) -> bool:
        """Delete a transaction in the database based on Transaction instance."""

class TransactionSQLite(TransactionCRUD):
    """Implementation of TransactionCRUD using SQLITE."""

    _instance = None
    __db_file: str = "expy_tui/data/expy.db"
    _con = sqlite3.Connection

    def __new__(cls, db_file: str) -> None:
        """Implement singleton pattern and performs initialisation for TransactionCRUDSQLite."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.__db_file = db_file
            cls._con = sqlite3.connect(cls.__db_file)
            # Converts sqlite fetch from tuples to dictionary-like objects
            cls._con.row_factory = sqlite3.Row

            create_transaction_table_query = """CREATE TABLE IF NOT EXISTS trnsaction (
                                                t_id integer PRIMARY KEY AUTOINCREMENT,
                                                date integer NOT NULL DEFAULT '0',
                                                category text NOT NULL,
                                                description text,
                                                value int NOT NULL DEFAULT 0,
                                                cc_value int NOT NULL DEFAULT 0
                                                );
                                             """

            cur = cls._con.cursor()
            try:
                cur.execute(create_transaction_table_query)
            finally:
                cur.close()

        return cls._instance

    def create_transaction(self, transaction: Transaction) -> bool:
        """Create transaction in the database based on Transaction instance.

        Returns True if success, False if failed.
        """
        create_transaction_query = f"""INSERT INTO trnsaction
                                       (date, category, description, value, cc_value)
                                       VALUES
                                       ({transaction.get_date_epoch()},
                                       "{transaction.category}",
                                       "{transaction.description}",
                                       {transaction.get_value_cents()},
                                       {transaction.get_cc_value_cents()})
                                    """

        cur = self._con.cursor()
        try:
            cur.execute(create_transaction_query)
        finally:
            cur.close()

    def get_transactions_filters(
            self, date_range: tuple[datetime, datetime] | None = None,
            categories: list[str] | None = None,
        ) -> list[Transaction]:
        """Return list of transactions based on filters date_range and categories.

        date_range: tuple containing 2 datetime variables [start_date, end_date],
        will be used as a filter in the query.
        categories: List of categories the transactions will be from.
        """
        # Get transactions from DB
        get_transaction_query = "SELECT * FROM trnsaction"

        # Apply filters by appending to db query
        if date_range:
            query_datetime_filter = f"date BETWEEN {date_range[0]} AND {date_range[1]}"
            get_transaction_query += f" WHERE {query_datetime_filter}"
        if categories:
            # Create string in format of (x,y,z) for category list
            category_str = str(categories).replace("[", "(").replace("]", ")")
            query_category_filter = f"category in {category_str}"
            if date_range:
                get_transaction_query += f" AND {query_category_filter}"
            else:
                get_transaction_query += f" WHERE {query_category_filter}"

        cur = self._con.cursor()
        try:
            cur.execute(get_transaction_query)
            rows = cur.fetchall()
        finally:
            cur.close()

        return(self._convert_sqlite_rows_to_transactions(rows))

    def get_transaction_by_id(self, t_id: int) -> Transaction:
        """Return transaction by ID."""

    def update_transaction(self, transaction: Transaction) -> bool:
        """Update a transaction in the database based on Transaction instance."""

    def delete_transaction(self, transaction: Transaction) -> bool:
        """Delete a transaction in the database based on Transaction instance."""

    def _convert_sqlite_rows_to_transactions(
            self, rows_list: list[sqlite3.Row],
        ) -> bool:
        """Convert Transaction data rows from db query to Transaction objects."""
        transaction_list: list[Transaction] = []

        for row in rows_list:
            t_id = row["t_id"]
            date_time_epoch = row["date"]
            category = row["category"]
            description = row["description"]
            value = row["value"]
            cc_value = row["cc_value"]

            transaction = Transaction(t_id = t_id, date = date_time_epoch, category = category,
                                      description = description, value = value,
                                      cc_value = cc_value)

            transaction_list.append(transaction)

        return transaction_list
