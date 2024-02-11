from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional
from Transaction import Transaction

class TransactionCRUD(ABC):

    @abstractmethod
    def create_transaction(transaction: Transaction) -> bool:
        """Creates a transaction in the database based on Transaction instance
        Returns True if success, False if failed"""

    @abstractmethod
    def get_transactions_filters(time_range: Optional[tuple[datetime, datetime]] = None, 
                                 category: Optional[str] = None) -> list[Transaction]:
        """Retrives a list of transactions based on filters"""

    @abstractmethod
    def get_transaction_by_id(id: int) -> Transaction:
        """Retrieves a transaction by its ID"""

    @abstractmethod
    def update_transaction(transaction: Transaction) -> bool:
        """Updates a transaction in the database based on Transaction instance
        Returns True if success, False if failed"""

    @abstractmethod
    def delete_transaction(transaction: Transaction) -> bool:
        """Deletes a transaction in the database based on Transaction instance
        Returns True if success, False if failed"""