import models.product
import models.sell
import models.item

from db.connection import create_db_and_tables, get_session
from repositories.product_repository import ProductRepository
from repositories.sell_repository import SellRepository
from repositories.item_repository import ItemRepository
from models.product import ProductCreate
from models.sell import SellCreate
from models.item import ItemCreate
from models.product import Product


product_repo = ProductRepository()
sell_repo = SellRepository()
item_repo = ItemRepository()


def agregar_producto():
    print("\n-- Agregar producto --")
    name = input("Nombre: ").strip()
    price = float(input("Precio: "))
    stock = int(input("Stock: "))
    with get_session() as session:
        product = product_repo.create(session, ProductCreate(name=name, price=price, stock=stock))
    print(f"Producto creado: [{product.id}] {product.name} - ${product.price} (stock: {product.stock})")


def agregar_venta():
    print("\n-- Agregar venta --")
    with get_session() as session:
        sell = sell_repo.create(session, SellCreate())
    print(f"Venta creada con ID {sell.id} ({sell.date.strftime('%Y-%m-%d %H:%M')})")


def agregar_item():
    print("\n-- Agregar item a venta --")
    with get_session() as session:
        products = product_repo.get_all(session)
        sells = sell_repo.get_all(session)

    if not products:
        print("No hay productos cargados.")
        return

    print("Productos disponibles:")
    for p in products:
        print(f"  [{p.id}] {p.name} - ${p.price}")

    if not sells:
        print("No hay ventas creadas. Crea una venta primero.")
        return

    print("\nVentas disponibles:")
    for s in sells:
        print(f"  [{s.id}] {s.date.strftime('%Y-%m-%d %H:%M')} - Total: ${s.total:.2f}")

    product_id = int(input("\nID del producto: "))
    sell_id = int(input("ID de la venta: "))
    quantity = int(input("Cantidad: "))

    product = next((p for p in products if p.id == product_id), None)
    if not product:
        print("Producto no encontrado.")
        return

    unit_price = product.price
    subtotal = unit_price * quantity

    with get_session() as session:
        sell = sell_repo.get_by_id(session, sell_id)
        if not sell:
            print("Venta no encontrada.")
            return

        item = item_repo.create(
            session,
            ItemCreate(product_id=product_id, sell_id=sell_id, quantity=quantity, unit_price=unit_price),
        )

        new_total = sell.total + subtotal
        from models.sell import SellUpdate
        sell_repo.update(session, sell_id, SellUpdate(total=new_total))

    print(f"Item agregado: {quantity}x {product.name} a ${unit_price} = ${subtotal:.2f}")
    print(f"Total actualizado de venta {sell_id}: ${new_total:.2f}")


def listar_productos():
    print("\n-- Productos --")
    with get_session() as session:
        products = product_repo.get_all(session)
    if not products:
        print("No hay productos cargados.")
        return
    print(f"{'ID':>4} {'Nombre':<20} {'Precio':>10} {'Stock':>7}")
    print("-" * 45)
    for p in products:
        print(f"{p.id:>4} {p.name:<20} {p.price:>10.2f} {p.stock:>7}")


def resumen_venta():
    with get_session() as session:
        sells = sell_repo.get_all(session)

    if not sells:
        print("No hay ventas creadas. Crea una venta primero.")
        return

    print("\nVentas disponibles:")
    for s in sells:
        print(f"  [{s.id}] {s.date.strftime('%Y-%m-%d %H:%M')} - Total: ${s.total:.2f}")
    print("\n-- Resumen de venta --")
    sell_id = int(input("ID de la venta: "))

    with get_session() as session:
        sell = sell_repo.get_by_id(session, sell_id)
        if not sell:
            print("Venta no encontrada.")
            return

        items = item_repo.get_by_sell(session, sell_id)
        product_ids = {i.product_id for i in items}
        products = {p.id: p for p in product_repo.get_all(session) if p.id in product_ids}

    print(f"\nVenta #{sell.id} — {sell.date.strftime('%Y-%m-%d %H:%M')}")
    print(f"{'Producto':<20} {'Cantidad':>8} {'Precio unit.':>13} {'Subtotal':>10}")
    print("-" * 55)
    for item in items:
        product_name = products[item.product_id].name if item.product_id in products else "?"
        subtotal = item.quantity * item.unit_price
        print(f"{product_name:<20} {item.quantity:>8} {item.unit_price:>13.2f} {subtotal:>10.2f}")
    print("-" * 55)
    print(f"{'TOTAL':>43} {sell.total:>10.2f}")


def menu():
    create_db_and_tables()
    opciones = {
        "1": ("Agregar producto", agregar_producto),
        "2": ("Agregar venta", agregar_venta),
        "3": ("Agregar item a venta", agregar_item),
        "4": ("Resumen de venta", resumen_venta),
        "5": ("Listar productos", listar_productos),
        "0": ("Salir", None),
    }

    while True:
        print("\n===== KIOSCO =====")
        for key, (label, _) in opciones.items():
            print(f"  {key}. {label}")
        opcion = input("Opcion: ").strip()

        if opcion == "0":
            break
        elif opcion in opciones:
            opciones[opcion][1]()
        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    menu()
