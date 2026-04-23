from product import Product

class Item:
    def __init__(self, product: Product, quantity):
        self._product = product
        self._quantity = quantity

    @property
    def quantity(self):
        return self._quantity
    
    @property
    def subtotal(self):
        return self._product.price * self._quantity