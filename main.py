from product import Product
from sell import Sell
import json

cartuchera = Product("cartuchera", 1500, 20)

print(cartuchera.to_dict())

venta = Sell()

venta.add_item(cartuchera, 10)

print(venta.to_dict())

with open("products.json", "w", encoding="utf-8") as file:
    json.dump(cartuchera.to_dict(), file, indent=2, ensure_ascii=False)