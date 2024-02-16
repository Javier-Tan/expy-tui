"""Provide testing for all classes in transaction module."""
from expy_tui.transaction.transaction import Transaction
from expy_tui.transaction.transaction_crud import TransactionSQLite


class TestTransactionCRUD:
    """Provides testing for the transaction_crud module."""

    def test_transaction_sqlite_singleton(self) -> None:
        in_memory_db_ref = ":memory:"
        transaction_sqlite_a = TransactionSQLite(db_file = in_memory_db_ref)
        transaction_sqlite_b = TransactionSQLite(db_file = in_memory_db_ref)
        assert transaction_sqlite_a is transaction_sqlite_b

    def test_create_and_get_transaction_sqlite(self,  inmemory_sqlite_db: TransactionSQLite,
                                               sample_transaction: Transaction) -> None:

        # DB should be empty before
        assert inmemory_sqlite_db.get_transactions_filters() == []

        inmemory_sqlite_db.create_transaction(sample_transaction)

        # Mimic the output based on the previous create_transaction
        sample_transaction.t_id = 1
        mimic_output = [sample_transaction]

        # Should match mimic output after
        assert inmemory_sqlite_db.get_transactions_filters() == mimic_output
