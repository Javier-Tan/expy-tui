from pydantic.dataclasses import dataclass
from datetime import datetime

@dataclass
class Transaction():
    id: int
    date: datetime
    category: str
    description: str
    value: float # Ingested as cents, stored as dollars
    cc_value: float = 0 # Ingested as cents, stored as dollars
    def __post_init__(self):
        # Converted from cents to dollar
        self.value /= 100
        self.cc_value /= 100

    def set_value_cents(self, value: float) -> None:
        self.value = value/100

    def get_value_cents(self) -> float:
        return self.value*100