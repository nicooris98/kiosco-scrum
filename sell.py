import datetime as dt
from product import Product
from item import Item

class Sell:
    def __init__(self):
        self._date = dt.datetime.now().isoformat()
        self._items = []

    @property
    def total(self):
        new_total = 0
        for item in self._items:
            new_total += item.subtotal
        return new_total

    def add_item(self, producto: Product, cantidad):
        self._items.append(Item(producto, cantidad))

    def to_dict(self):
        return {
            "total": self.total,
            "fecha": self._date
        }