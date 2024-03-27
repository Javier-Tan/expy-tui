"""Provides fixtures for all test files in this directory (tests/unit/)."""
import datetime

import pytest

from expy_tui.transaction.transaction import Transaction
from expy_tui.transaction.transaction_crud import TransactionSQLite


@pytest.fixture(scope="session")
def sample_transaction() -> Transaction:
    """Fixture to create a sample transaction."""
    t_id: int | None = None
    # Date and time (GMT): Saturday, 1 January 2000 0:00:00
    date_epoch_time: int = 946684800
    category: str = "Test category"
    description: str = "Test description"
    value_cents: int = 9999
    cc_value_cents: int = 8888

    return Transaction(
        t_id=t_id,
        date=date_epoch_time,
        category=category,
        description=description,
        value=value_cents,
        cc_value=cc_value_cents,
    )

@pytest.fixture(scope="session")
def sample_transactions() -> Transaction:
    """Fixture to create a sample transactions."""
    t_id: int | None = 1
    category: str = "Test category"
    description: str = "Test description"
    value_cents: int = 4444
    cc_value_cents: int = 4444
    transaction_count = 24

    transaction_list = []
    for transaction_no in range(transaction_count):

        # Change date based on transaction
        date = datetime.datetime(2000+transaction_no, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc)
        date_epoch = int(date.timestamp())

        transaction = Transaction(
            t_id=t_id + transaction_no,
            date=date_epoch,
            category=category + str(transaction_no//8), # Change category no. every 8 transactions
            description=description,
            value=value_cents + (transaction_no//6)*1111, # Increase by 1111 every 6 transactions
            cc_value=cc_value_cents + (transaction_no//6)*1111,
        )
        transaction_list.append(transaction)

    return transaction_list

@pytest.fixture(scope="session")
def inmemory_sqlite_db() -> TransactionSQLite:
    """Fixture to return in memory database."""
    return TransactionSQLite(db_file = ":memory:")
