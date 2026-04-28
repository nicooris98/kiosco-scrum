import datetime as dt
from product import Product
from item import Item

#Clase Venta
class Sell:
    def __init__(self):
        self._date = dt.datetime.now().isoformat()
        self._items = []
        self._total = 0

    @property
    def total(self):
        return self._total

    def calcular_total(self):
        for item in self._items:
            self._total += item.subtotal

    def add_item(self, producto: Product, cantidad):
        self._items.append(Item(producto, cantidad))

    def to_dict(self):
        return {
            "total": self.total,
            "fecha": self._date
        }