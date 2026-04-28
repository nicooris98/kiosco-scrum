class Product:
    def __init__(self,name, price, stock, id=0):
        if price < 0:
            raise ValueError("Precio negativo")
        self._id = id
        self._name = name
        self._price = price
        self._stock = stock

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if len(new_name) <= 0:
            raise ValueError("Nombre vacio")
        self._name = new_name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            raise ValueError("Precio Error")
        self._price = new_price

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, new_stock):
        if new_stock <= 0:
            raise ValueError("Stock Error")
        self._stock = new_stock

    def to_dict(self):
        return {
            "id": self._id,
            "name": self._name,
            "price": self._price,
            "stock": self._stock
        }