"""Interface and implementations for creating, reading, updating and deleting transaction data.

How data is stored should be implementation specific, and based off the below SQL example
trnsaction (
    t_id integer PRIMARY KEY AUTOINCREMENT,
    date integer NOT NULL DEFAULT '0',
    category text NOT NULL,
    description text,
    value int NOT NULL DEFAULT 0,
    cc_value int NOT NULL DEFAULT 0
);
"""
import logging
import sqlite3
from abc import ABC, abstractmethod
from datetime import datetime

from expy_tui.transaction.transaction import Transaction


class TransactionCRUD(ABC):
    """Interface for all CRUD relating to transactions.

    Should be implemented as a singleton.
    """

    @abstractmethod
    def create_transaction(self, transaction: Transaction) -> bool:
        """Create transaction record.

        Args:
            transaction (Transaction): Transaction data to be written.

        Returns:
            bool: True if successfully created, False if unsuccessful to create
        """

    @abstractmethod
    def get_transactions_filters(
            self, date_range: tuple[datetime, datetime] | None = None,
            categories: list[str] | None = None,
            value_range: tuple[int, int] | None = None,
        ) -> list[Transaction]:
        """Retrieve list of transactions based on filters date_range and categories.

        Args:
            date_range (tuple[datetime, datetime], optional):
                Tuple containing 2 datetime variables [start_date, end_date],
                transactions will come from between these dates (inclusive).
            categories (list[str], optional):
                List of categories the transactions will be from.
            value_range (tuple[int, int], optional):
                Tuple containing 2 integers representing values [start_value, end_value],
                transactions will come from between these values (inclusive).

        Returns:
            list[Transaction]: List of transactions which fulfil the filters provided.
        """

    @abstractmethod
    def get_transaction_id(self, t_id: int) -> Transaction | None:
        """Retrieve transaction by ID.

        Args:
            t_id (int): Transaction ID we are retrieving.

        Returns:
            Transaction: Transaction with t_id
            None: If Transaction with t_id does not exist
        """

    @abstractmethod
    def update_transaction(self, transaction: Transaction) -> bool:
        """Update transaction record.

        Args:
            transaction (Transaction): Transaction data to be updated.

        Returns:
            bool: True if successfully updated, False if unsuccessful to update.
        """

    @abstractmethod
    def delete_transaction(self, transaction: Transaction) -> bool:
        """Delete a transaction record.

        Args:
            transaction (Transaction): Transaction data to be updated.

        Returns:
            bool: True if successfully deleted, False if unsuccessful to delete.
        """

class TransactionSQLite(TransactionCRUD):
    """Implementation of TransactionCRUD using SQLITE."""

    _instance = None
    __db_file: str = "expy_tui/data/expy.db"
    _con: sqlite3.Connection = None

    def __new__(cls, db_file: str) -> None:
        """Implement singleton pattern and performs initialisation for TransactionCRUDSQLite.

        Args:
            db_file (str): File path to database file, should be the same across every instance.

        Returns:
            TransactionSQLite: Singleton instance of class.

        Raises:
            sqlite3.error: Any error sqlite3 may throw.
        """
        if cls._instance is None:
            logging.debug("Initialising database.")

            cls._instance = super().__new__(cls)
            cls.__db_file = db_file

            create_transaction_table_query = """CREATE TABLE IF NOT EXISTS trnsaction (
                                                t_id integer PRIMARY KEY AUTOINCREMENT,
                                                date integer NOT NULL DEFAULT 0,
                                                category text NOT NULL DEFAULT '',
                                                description text,
                                                value int NOT NULL DEFAULT 0,
                                                cc_value int NOT NULL DEFAULT 0
                                                );
                                             """

            try:
                cls._con = sqlite3.connect(cls.__db_file)
                cls._con.execute("PRAGMA foreign_keys = ON")
                # Converts sqlite fetch from tuples to dictionary-like "row" objects
                cls._con.row_factory = sqlite3.Row
                cur = cls._con.cursor()
                cur.execute(create_transaction_table_query)
            except sqlite3.Error:
                logging.exception("Error initialising database.")
                del cls._instance
                raise
            finally:
                cur.close()

        return cls._instance

    def create_transaction(self, transaction: Transaction) -> bool:
        """Create transaction record.

        Args:
            transaction (Transaction): Transaction data to be written.

        Returns:
            bool: True if successfully created, False if unsuccessful to create

        Raises:
            sqlite3.error: Any error sqlite3 may throw
        """
        logging.info("Creating transaction %s in db through SQlite.", transaction)

        if transaction.t_id:
            create_transaction_query = """INSERT INTO trnsaction
                                          (date, category, description, value, cc_value, t_id)
                                          VALUES
                                          (?, ?, ?, ?, ?, ?)
                                        """
            create_transaction_args = (transaction.get_date_epoch(),
                                    transaction.category,
                                    transaction.description,
                                    transaction.get_value_cents(),
                                    transaction.get_cc_value_cents(),
                                    transaction.t_id)
        else:
            create_transaction_query = """INSERT INTO trnsaction
                                          (date, category, description, value, cc_value)
                                          VALUES
                                          (?, ?, ?, ?, ?)
                                        """
            create_transaction_args = (transaction.get_date_epoch(),
                                    transaction.category,
                                    transaction.description,
                                    transaction.get_value_cents(),
                                    transaction.get_cc_value_cents())

        cur = self._con.cursor()
        try:
            cur.execute(create_transaction_query, create_transaction_args)
            row_updated = cur.rowcount
        except sqlite3.Error:
            logging.exception("Error creating transaction.")
            raise
        finally:
            cur.close()

        return bool(row_updated)

    def get_transactions_filters(
            self, date_range: tuple[datetime, datetime] | None = None,
            categories: list[str] | None = None,
            value_range: tuple[int, int] | None = None,
        ) -> list[Transaction]:
        """Retrieve list of transactions based on filters date_range and categories.

        Args:
            date_range (tuple[datetime, datetime], optional):
                Tuple containing 2 datetime variables [start_date, end_date],
                transactions will come from between these dates (inclusive).
            categories (list[str], optional):
                List of categories the transactions will be from.
            value_range (tuple[int, int], optional):
                Tuple containing 2 integers representing values [start_value, end_value],
                transactions will come from between these values (inclusive).

        Returns:
            list[Transaction]: List of transactions which fulfil the filters provided.

        Raises:
            sqlite3.error: Any error sqlite3 may throw
        """
        logging.info("Reading transaction with filters date_range = %s, categories = %s, value_range = %s \
                     in db through SQlite.", date_range, categories, value_range)
        # Get transactions from DB
        get_transaction_query = "SELECT * FROM trnsaction"

        filter_queries = []
        # Apply filters by appending to db query
        if date_range:
            query_datetime_filter = f"date BETWEEN {date_range[0]} AND {date_range[1]}"
            filter_queries.append(query_datetime_filter)

        if categories:
            # Create string in format of (x,y,z) for category list
            category_str = str(categories).replace("[", "(").replace("]", ")")
            query_category_filter = f"category in {category_str}"
            filter_queries.append(query_category_filter)

        if value_range:
            query_value_filter = f"value BETWEEN {value_range[0]} AND {value_range[1]}"
            filter_queries.append(query_value_filter)

        if filter_queries:
            get_transaction_query += f" WHERE {filter_queries[0]}"
            for filter_query in filter_queries[1:]:
                get_transaction_query += f" AND {filter_query}"

        cur = self._con.cursor()
        try:
            cur.execute(get_transaction_query)
            rows = cur.fetchall()
        except sqlite3.Error:
            logging.exception("Error retrieving transactions by filters.")
            raise
        finally:
            cur.close()

        return([self._convert_sqlite_row_to_transaction(row) for row in rows])

    def get_transaction_id(self, t_id: int) -> Transaction | None:
        """Retrieve transaction by ID.

        Args:
            t_id (int): Transaction ID we are retrieving.

        Returns:
            Transaction: Transaction with t_id
            None: If Transaction with t_id does not exist

        Raises:
            sqlite3.error: Any error sqlite3 may throw
        """
        logging.debug("Reading transaction with t_id %s in db through SQlite.", t_id)

        get_transaction_query = "SELECT * FROM trnsaction WHERE t_id = ?"
        get_transaction_args = (t_id,)

        cur = self._con.cursor()
        try:
            cur.execute(get_transaction_query, get_transaction_args)
            row = cur.fetchone()
        except sqlite3.Error:
            logging.exception("Error retrieving transaction by ID.")
            raise
        finally:
            cur.close()

        if row:
            return(self._convert_sqlite_row_to_transaction(row))

        return None

    def update_transaction(self, transaction: Transaction) -> bool:
        """Update transaction record.

        Args:
            transaction (Transaction): Transaction data to be updated.

        Returns:
            bool: True if successfully updated, False if unsuccessful to update.

        Raises:
            sqlite3.error: Any error sqlite3 may throw
        """
        # Ensure that Transaction has a ID
        if not transaction.t_id:
            logging.error("Transaction does not have a t_id to update.")
            return False

        logging.info("Updating transaction with t_id %s with %s in db through SQlite.", transaction.t_id, transaction)

        update_transaction_query = """UPDATE trnsaction
                                      SET date = ?,
                                          category = ?,
                                          description = ?,
                                          value = ?,
                                          cc_value = ?
                                      WHERE t_id = ?
                                   """
        update_transaction_args = (transaction.get_date_epoch(),
                                   transaction.category,
                                   transaction.description,
                                   transaction.get_value_cents(),
                                   transaction.get_cc_value_cents(),
                                   transaction.t_id)

        cur = self._con.cursor()
        try:
            cur.execute(update_transaction_query, update_transaction_args)
            row_updated = cur.rowcount
        except sqlite3.Error:
            logging.exception("Error updating transaction.")
            raise
        finally:
            cur.close()

        return bool(row_updated)

    def delete_transaction(self, transaction: Transaction) -> bool:
        """Delete a transaction record.

        Args:
            transaction (Transaction): Transaction data to be updated.

        Returns:
            bool: True if successfully deleted, False if unsuccessful to delete.

        Raises:
            sqlite3.error: Any error sqlite3 may throw.
        """
        # Ensure that Transaction has a ID
        if not transaction.t_id:
            logging.error("Transaction does not have a t_id to delete.")
            return False

        logging.info("Deleting transaction with t_id %s in db through SQlite.", transaction.t_id)

        delete_transaction_query = "DELETE FROM trnsaction WHERE t_id = ?"
        delete_transaction_args = (transaction.t_id,)

        cur = self._con.cursor()
        try:
            cur.execute(delete_transaction_query, delete_transaction_args)
            row_updated = cur.rowcount
        except sqlite3.Error:
            logging.exception("Error deleting transaction.")
            raise
        finally:
            cur.close()

        return bool(row_updated)

    def _convert_sqlite_row_to_transaction(
            self, row: sqlite3.Row,
        ) -> Transaction:
        """Convert Transaction data rows from db query to Transaction objects."""
        t_id = row["t_id"]
        date_time_epoch = row["date"]
        category = row["category"]
        description = row["description"]
        value = row["value"]
        cc_value = row["cc_value"]

        return Transaction(t_id = t_id, date = date_time_epoch, category = category,
                            description = description, value = value,
                            cc_value = cc_value)
