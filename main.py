from product import Product
from sell import Sell
from product_repository import ProductRepository
import json

cartuchera = Product("Lapicera", 1500, 600)

print(cartuchera.to_dict())

venta = Sell()

venta.add_item(cartuchera, 10)

print(venta.to_dict())

#with open("products.json", "w", encoding="utf-8") #as file:
#    json.dump(cartuchera.to_dict(), file, indent=2, ensure_ascii=False)

repo = ProductRepository()

repo.insertar_producto(cartuchera)

print("-----------------")

for p in repo.get_all_products():
    print(p.to_dict())

print("Stock para el producto de id 4")
stock_consultado = repo.get_stock_product(4)
print(stock_consultado)
print("Eliminar producto id 3")
if repo.delete_product(3):
    print("Producto eliminado con exito")
else:
    print("Error al eliminar producto")