from product import Product
from sell import Sell

class Item:
    def __init__(self, product: Product, quantity, sell: Sell, id=None):
        self._id = id
        self._product = product
        self._quantity = quantity
        self._sell = sell

    @property
    def quantity(self):
        return self._quantity
    
    @property
    def subtotal(self):
        return self._product.price * self._quantity
    
    @property
    def product(self):
        return self._product
    
    @property
    def sell(self):
        return self._sell