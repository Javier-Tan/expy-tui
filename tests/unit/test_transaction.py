"""Provide testing for all classes in transaction module."""
import pytest

from expy_tui.transaction.transaction import Transaction


class TestTransaction:
    """Provides testing for the transaction module."""

    _id: int | None = None
    # Date and time (GMT): Saturday, 1 January 2000 0:00:00
    date_epoch_time: int = 946684800
    category: str = "Test category"
    description: str = "Test description"
    value_cents: float = 9999
    value_dollars: float = 99.99
    cc_value_cents: float = 8888
    cc_value_dollars: float = 88.88

    @pytest.fixture()
    def sample_transaction(self) -> Transaction:
        return Transaction(
            _id=self._id,
            date=self.date_epoch_time,
            category=self.category,
            description=self.description,
            value=self.value_cents,
            cc_value=self.cc_value_cents,
        )

    def test_get_value_dollars(self, sample_transaction: Transaction) -> None:
        assert sample_transaction.value == self.value_dollars

    def test_get_cc_value_dollars(self, sample_transaction: Transaction) -> None:
        assert sample_transaction.cc_value == self.cc_value_dollars

    def test_get_value_cents(self, sample_transaction: Transaction) -> None:
        assert sample_transaction.get_value_cents() == self.value_cents

    def test_get_cc_value_cents(self, sample_transaction: Transaction) -> None:
        assert sample_transaction.get_cc_value_cents() == self.cc_value_cents

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
