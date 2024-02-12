"""Interface and implementations for creating, reading, updating and deleting transaction data."""
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
