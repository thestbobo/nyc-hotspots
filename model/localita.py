import decimal
from dataclasses import dataclass
@dataclass
class Location:
    locName: str
    latitude: decimal.Decimal
    longitude: decimal.Decimal
    provider: str
    neighbors: int = 0

    def __str__(self):
        return f"{self.locName}"

    def __hash__(self):
        return hash(self.locName)

