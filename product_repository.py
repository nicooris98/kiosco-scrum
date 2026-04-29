import sqlite3

class ProductRepository:

    def __init__(self, db="kiosco.db"):
        self._db = db
        self.crear_tabla()

    def conectar(self):
        return sqlite3.connect(self._db)

    def crear_tabla(self):
        with self.conectar() as con:
            con.execute(
                """
                CREATE TABLE IF NOT EXISTS products(
                    id integer primary key autoincrement,
                    name text not null unique,
                    price real not null,
                    stock integer not null default 0
                )
                """
            )

    def insertar_producto(self, producto):
        with self.conectar() as con:
            cur = con.execute(" INSERT INTO products(name, price, stock) values (?, ?, ?)",
                (
                    producto.name, producto.price, producto.stock
                )
            )
            return True
        
    def get_all_products(self):
        from product import Product
        with self.conectar() as con:
            con.row_factory = sqlite3.Row
            rows = con.execute("SELECT * FROM products").fetchall()
            productos = []
            for fila in rows:
                productos.append(Product(fila["name"], fila["price"], fila["stock"], fila["id"]))

            return productos

    def get_stock_product(self, id):
        with self.conectar() as con:
            con.row_factory = sqlite3.Row
            row = con.execute("SELECT stock FROM products where id = ?", (id)).fetchone()
            return row["stock"]
        
    def delete_product(self, id):
        try:
            with self.conectar() as con:
                con.row_factory = sqlite3.Row
                row = con.execute("DELETE FROM products where id = ?", (id))
                return True
        except:
            return False
            