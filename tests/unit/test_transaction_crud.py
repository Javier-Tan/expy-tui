"""Provide testing for all classes in transaction module."""
from expy_tui.transaction.transaction_crud import TransactionSQLite


class TestTransactionCRUD:
    """Provides testing for the transaction_crud module."""

    def test_transactionsqlite_singleton(self) -> None:
        sqlite_implementation_a = TransactionSQLite()
        sqlite_implementation_b = TransactionSQLite()
        assert sqlite_implementation_a is sqlite_implementation_b
