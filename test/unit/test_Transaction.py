from typing import Optional
from expy_tui.transaction.Transaction import Transaction

class TestTransaction():
    id: Optional[int] = None
    # Date and time (GMT): Saturday, 1 January 2000 0:00:00
    date_epoch_time: int = 946684800
    category: str = "Test category"
    description: str = "Test description"
    value_cents: float = 9999 # In cents
    cc_value_cents: float = 9999 # In cents

    def test_set_value_cents(self):
        test_transaction = Transaction(
            id = self.id, date = self.date_epoch_time, category = self.category, 
            description = self.description, value = self.value_cents, 
            cc_value = self.cc_value_cents
            )
        test_value_cents: float = 8888
        test_value_dollars: float = test_value_cents/100
        test_transaction.set_value_cents(value = test_value_cents)
        assert test_transaction.value == test_value_dollars


    def test_get_value_cents(self):
        test_transaction = Transaction(
            id = self.id, date = self.date_epoch_time, category = self.category, 
            description = self.description, value = self.value_cents, 
            cc_value = self.cc_value_cents
            )
        test_transaction_value_cents = test_transaction.get_value_cents()
        assert test_transaction_value_cents == self.value_cents