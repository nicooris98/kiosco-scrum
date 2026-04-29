import sqlite3

class SellRepository:

    def __init__(self, db="kiosco.db"):
        self._db = db
        self.crear_tabla()

    def conectar(self):
        return sqlite3.connect(self._db)

    def crear_tabla(self):
        with self.conectar() as con:
            con.execute(
                """
                CREATE TABLE IF NOT EXISTS sells(
                    id integer primary key autoincrement,
                    date date not null,
                    total real not null
                )
                """
            )

    def insertar_venta(self, sell):
        with self.conectar() as con:
            cur = con.execute(" INSERT INTO sells(date, total) values (?, ?)",
                (
                    sell.date, sell.total
                )
            )
            return True
        