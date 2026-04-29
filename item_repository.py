import sqlite3
from item import Item
from product import Product
from sell import Sell

class ItemDetailRepository:

    def __init__(self, db="kiosco.db"):
        self._db = db
        self.crear_tabla()

    def conectar(self):
        return sqlite3.connect(self._db)

    def crear_tabla(self):
        with self.conectar() as con:
            con.execute(
                """
                CREATE TABLE IF NOT EXISTS item_details(
                    id integer primary key autoincrement,
                    product_id intenger not null,
                    sell_id integer not null,
                    quantity integer not null,
                    subtotal real not null
                )
                """
            )

    def insertar_detalle(self, item: Item):
        with self.conectar() as con:
            cur = con.execute(" INSERT INTO item_details(product_id, sell_id, quantity, subtotal) values (?, ?, ?, ?)",
                (
                    item.product.id, item.sell.id, item.quantity, item.subtotal
                )
            )
            return True
        
    def get_details_by_sell(self, sell_id):
        with self.conectar() as con:
            con.row_factory = sqlite3.Row
            rows = con.execute("SELECT p.id as product_id, p.name, p.price, p.stock, itd.id as detalle_id, itd.quantity, itd.subtotal, s.id as sell_id, s.total, s.date, itd.subtotal, itd.id FROM item_details itd inner join products p on p.id = itd.product_id inner join sells s on s.id = itd.sell_id WHERE itd.sell_id = ?", (sell_id)).fetchall()
            detalles = []
            for fila in rows:
                detalles.append(Item(Product(fila["name"], fila["price"], fila["stock"], fila["product_id"])), fila["quantity"], Sell(fila["date"], fila["total"], fila["sell_id"]), fila["subtotal"], fila["id"])

            return detalles