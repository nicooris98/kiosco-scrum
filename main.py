from product import Product
from sell import Sell
from product_repository import ProductRepository
from item_repository import ItemDetailRepository
from sell_repository import SellRepository

product_repo = ProductRepository()
item_repo = ItemDetailRepository()
sell_repo = SellRepository()


def menu():
    while True:
        print("=== KIOSCO ===")
        print("1. Listar productos")
        print("2. Agregar producto")
        print("5. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            for p in product_repo.get_all_products():
                print(p.to_dict())
        elif opcion == "2":
            nombre = input("Nombre del producto: ").strip()
            if not nombre:
                print("El nombre no puede estar vacío.")
                return
            try:
                precio = float(input("Precio unitario: "))
                stock  = int(input("Stock inicial: "))
            except ValueError:
                print("Precio y stock deben ser números.")
                return
            if precio <= 0 or stock < 0:
                print("Precio debe ser mayor a 0 y stock no puede ser negativo.")
                return
            p = Product(nombre, precio, stock)
            product_repo.insertar_producto(p)
            print(f"Producto agregado: {p}")
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()