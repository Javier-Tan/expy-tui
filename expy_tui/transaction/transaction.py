"""Provides classes related to transactions.

Transaction dataclass - holds data of a single transaction.
"""
from datetime import datetime

from pydantic.dataclasses import dataclass


@dataclass
class Transaction:
    """Transaction dataclass, holds data of a single transaction."""

    _id: int | None = None
    date: datetime
    category: str = "Uncategorised"
    description: str = ""
    value: float  = 0 # Ingested as cents, stored as dollars
    cc_value: float = 0 # Ingested as cents, stored as dollars

    def __post_init__(self) -> None:
        """Store value and cc value given as cents in dollars during __init__."""
        self.value /= 100
        self.cc_value /= 100

    def set_value_cents(self, value: float) -> None:
        """Store a value given as cents in dollars."""
        self.value = value / 100

    def get_value_cents(self) -> int:
        """Return the transaction value as cents."""
        return self.value * 100
