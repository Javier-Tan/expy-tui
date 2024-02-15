"""Provides classes related to transactions.

Transaction dataclass - holds data of a single transaction.
TransactionsMetrics class - returns metrics based on a list of transactions.
"""
from datetime import datetime

from pydantic.dataclasses import dataclass


@dataclass
class Transaction:
    """Transaction dataclass, holds data of a single transaction."""

    _id: int | None = None
    date: datetime = 0
    category: str = "Uncategorised"
    description: str = ""
    value: float  = 0 # Ingested as cents, stored as dollars
    cc_value: float = 0 # Ingested as cents, stored as dollars

    def __post_init__(self) -> None:
        """Store value and cc value given as cents in dollars during __init__."""
        self.value /= 100
        self.cc_value /= 100

    def get_value_cents(self) -> int:
        """Return the transaction value as cents."""
        return self.value * 100

    def get_cc_value_cents(self) -> int:
        """Return the transaction cc value as cents."""
        return self.cc_value * 100

    def get_date_epoch(self) -> int:
        """Return date value as epoch time represented as an integer."""
        return int(self.date.timestamp())

    def set_value_cents(self, value: float) -> None:
        """Store the value given as cents in dollars."""
        self.value = value / 100

    def set_cc_value_cents(self, value: float) -> None:
        """Store the cc value given as cents in dollars."""
        self.cc_value = value / 100
