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

    def test_create_and_get_transactions_filters_sqlite(self,  inmemory_sqlite_db: TransactionSQLite,
                                                        sample_transactions: list[Transaction]) -> None:

        # DB should be empty before any creates
        assert inmemory_sqlite_db.get_transactions_filters() == []

        # Create all sample transactions
        for sample_transaction in sample_transactions:
            inmemory_sqlite_db.create_transaction(sample_transaction)

        # Test get all (should return all transactions if get and create work properly)
        no_filter_output = inmemory_sqlite_db.get_transactions_filters()
        assert no_filter_output == sample_transactions # Expect all transactions to be added

        # Test date_range filters
        # Because transactions are ordered by increasing date, we can test by index order
        start_index = 0
        end_index = 12
        start_date = sample_transactions[start_index].get_date_epoch() # 2000
        end_date = sample_transactions[end_index].get_date_epoch() # 2012
        date_range = [start_date, end_date]

        expected_transactions_date_range = sample_transactions[start_index:end_index+1]
        date_filter_output = inmemory_sqlite_db.get_transactions_filters(date_range=date_range)
        assert date_filter_output == expected_transactions_date_range

        # Test category filters
        # We know "Test category1" and "Test category2" can be found from indexes 8 to end
        start_index = 8
        end_index = 24
        categories = ["Test category1", "Test category2"]

        expected_transactions_categories = sample_transactions[start_index:end_index+1]
        categories_filter_output = inmemory_sqlite_db.get_transactions_filters(categories=categories)
        assert categories_filter_output == expected_transactions_categories

        # Test category and date filters together
        # Transactions in [2000, 2012] and have category "Test category1" can be found in [8, 12]
        start_index = 8
        end_index = 12
        expected_transactions_category_date_range = sample_transactions[start_index:end_index+1]

        date_categories_filter_output = inmemory_sqlite_db.get_transactions_filters(date_range=date_range,
                                                                                    categories=categories)

        assert date_categories_filter_output == expected_transactions_category_date_range
