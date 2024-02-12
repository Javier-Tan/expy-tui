"""Provide testing for all classes in transaction module."""
from expy_tui.transaction.transaction import Transaction


class TestTransaction:
    """Provides testing for the Transaction dataclass."""

    _id: int | None = None
    # Date and time (GMT): Saturday, 1 January 2000 0:00:00
    date_epoch_time: int = 946684800
    category: str = "Test category"
    description: str = "Test description"
    value_cents: float = 9999  # In cents
    cc_value_cents: float = 9999  # In cents

    def test_set_value_cents(self) -> None:
        test_transaction = Transaction(
            _id=self._id,
            date=self.date_epoch_time,
            category=self.category,
            description=self.description,
            value=self.value_cents,
            cc_value=self.cc_value_cents,
        )
        test_value_cents: float = 8888
        test_value_dollars: float = test_value_cents / 100
        test_transaction.set_value_cents(value=test_value_cents)
        assert test_transaction.value == test_value_dollars

    def test_get_value_cents(self) -> None:
        test_transaction = Transaction(
            _id=self._id,
            date=self.date_epoch_time,
            category=self.category,
            description=self.description,
            value=self.value_cents,
            cc_value=self.cc_value_cents,
        )
        test_transaction_value_cents = test_transaction.get_value_cents()
        assert test_transaction_value_cents == self.value_cents
