import datetime as dt

#Clase Venta
class Sell:
    def __init__(self, date=None, total=None, id=None):
        self._id = id
        if(date):
            self._date = date
        else:
            self._date = dt.datetime.now().isoformat()

        if(total):
            self._total = total
        else:
            self._total = 0
        self._items = []

    @property
    def total(self):
        return self._total

    @property
    def date(self):
        return self._date

    def calcular_total(self):
        for item in self._items:
            self._total += item.subtotal

    def add_item(self, producto, cantidad):
        from item import Item
        self._items.append(Item(producto, cantidad))

    def to_dict(self):
        return {
            "total": self.total,
            "fecha": self._date
        }