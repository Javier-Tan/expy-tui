"""Interface and implementations for creating, reading, updating and deleting transaction data."""
import sqlite3
from abc import ABC, abstractmethod
from datetime import datetime

from expy_tui.transaction.transaction import Transaction


class TransactionCRUD(ABC):
    """Interface for all CRUD relating to transactions."""

    @abstractmethod
    def create_transaction(self, transaction: Transaction) -> bool:
        """Create transaction in the database based on Transaction instance.

        Returns True if success, False if failed.
        """

    @abstractmethod
    def get_transactions_filters(
        self, time_range: tuple[datetime, datetime] | None = None, category: str | None = None,
    ) -> list[Transaction]:
        """Return list of transactions based on filters time_range and category."""

    @abstractmethod
    def get_transaction_by_id(self, _id: int) -> Transaction:
        """Return transaction by ID."""

    @abstractmethod
    def update_transaction(self, transaction: Transaction) -> bool:
        """Update a transaction in the database based on Transaction instance."""

    @abstractmethod
    def delete_transaction(self, transaction: Transaction) -> bool:
        """Delete a transaction in the database based on Transaction instance."""

# Should be a singleton
class TransactionSQLite(TransactionCRUD):
    """Implementation of TransactionCRUD using SQLITE."""

    _instance = None
    __db_file: str = "expy_tui/data/expy.db"
    _cursor: sqlite3.Cursor

    def __new__(cls) -> None:
        """Implement singleton pattern and performs initialisation for TransactionCRUDSQLite."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            con = sqlite3.connect(cls.__db_file)
            cls._cursor = con.cursor()

            create_transaction_table = """CREATE TABLE IF NOT EXISTS trnsaction (
                                    t_id integer PRIMARY KEY AUTOINCREMENT,
                                    date integer NOT NULL DEFAULT '0',
                                    category text NOT NULL,
                                    description text,
                                    value int NOT NULL DEFAULT 0,
                                    cc_value int NOT NULL DEFAULT 0
                                );"""

            cls._cursor.execute(create_transaction_table)
        return cls._instance

    def create_transaction(self, transaction: Transaction) -> bool:
        """Create transaction in the database based on Transaction instance.

        Returns True if success, False if failed.
        """

    def get_transactions_filters(
        self, time_range: tuple[datetime, datetime] | None = None, category: str | None = None,
    ) -> list[Transaction]:
        """Return list of transactions based on filters time_range and category."""

    def get_transaction_by_id(self, _id: int) -> Transaction:
        """Return transaction by ID."""

    def update_transaction(self, transaction: Transaction) -> bool:
        """Update a transaction in the database based on Transaction instance."""

    def delete_transaction(self, transaction: Transaction) -> bool:
        """Delete a transaction in the database based on Transaction instance."""


    # def create_transaction(self, transaction: Transaction) -> bool:
