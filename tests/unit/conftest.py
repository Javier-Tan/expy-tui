"""Provides fixtures for all test files in this directory (tests/unit/)."""
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
def inmemory_sqlite_db() -> TransactionSQLite:
    """Fixture to return in memory database."""
    return TransactionSQLite(db_file = ":memory:")
