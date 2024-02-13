"""Provide testing for all classes in transaction module."""
from expy_tui.transaction.transaction_crud import TransactionSQLite


class TestTransactionCRUD:
    """Provides testing for the transaction_crud module."""

    def test_transaction_sqlite_singleton(self) -> None:
        in_memory_db_ref = ":memory:"
        sqlite_implementation_a = TransactionSQLite(db_file = in_memory_db_ref)
        sqlite_implementation_b = TransactionSQLite(db_file = in_memory_db_ref)
        assert sqlite_implementation_a is sqlite_implementation_b
