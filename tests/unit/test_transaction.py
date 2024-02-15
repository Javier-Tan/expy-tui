"""Provide testing for all classes in transaction module."""
from expy_tui.transaction.transaction import Transaction


class TestTransaction:
    """Provides testing for the transaction module."""

    # Values of sample transaction fixture found in conftest.py
    value_cents: float = 9999
    value_dollars: float = 99.99
    cc_value_cents: float = 8888
    cc_value_dollars: float = 88.88
    # Date and time (GMT): Saturday, 1 January 2000 0:00:00
    date_epoch_time: int = 946684800

    def test_get_value_cents(self, sample_transaction: Transaction) -> None:
        assert sample_transaction.get_value_cents() == self.value_cents

    def test_get_cc_value_cents(self, sample_transaction: Transaction) -> None:
        assert sample_transaction.get_cc_value_cents() == self.cc_value_cents

    def test_get_date_epoch(self, sample_transaction: Transaction) -> None:
        assert sample_transaction.get_date_epoch() == self.date_epoch_time

    def test_set_value_cents(self, sample_transaction: Transaction) -> None:
        test_value_cents: int = 7777
        test_value_dollars: float = 77.77
        sample_transaction.set_value_cents(value=test_value_cents)
        assert sample_transaction.value == test_value_dollars

    def test_set_cc_value_cents(self, sample_transaction: Transaction) -> None:
        test_cc_value_cents: int = 5555
        test_cc_value_dollars: float = 55.55
        sample_transaction.set_cc_value_cents(value=test_cc_value_cents)
        assert sample_transaction.cc_value == test_cc_value_dollars
