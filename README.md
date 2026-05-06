# Proyecto Kiosco
Este es el repositorio del proyecto de kiosco.

## Cómo funciona el proyecto

### El problema con SQL manual
Cuando creás una base de datos a mano escribís sentencias como `CREATE TABLE`, `INSERT INTO`, `SELECT *`, etc. Eso funciona, pero tiene un problema: tenés que mezclar código Python con texto SQL, y si la base de datos cambia tenés que acordarte de actualizar ese texto en todos lados.

### Qué es un ORM
Un ORM (Object Relational Mapper) te permite trabajar con la base de datos usando clases y objetos de Python, sin escribir SQL a mano. Vos definís una clase y el ORM se encarga de crear la tabla, guardar los datos y consultarlos por vos.

Este proyecto usa **SQLModel**, que combina dos herramientas: Pydantic (para validar datos) y SQLAlchemy (para hablar con la base de datos).

### Cómo están organizadas las piezas

```
models/       → definen las tablas como clases de Python
repositories/ → contienen las operaciones sobre cada tabla (crear, leer, actualizar, eliminar)
db/           → configura la conexión a la base de datos
main.py       → menú por terminal para interactuar con el sistema
```

### Un ejemplo concreto
En vez de escribir esto:
```sql
CREATE TABLE product (id INTEGER PRIMARY KEY, name TEXT, price REAL, stock INTEGER);
INSERT INTO product (name, price, stock) VALUES ('Coca', 1.50, 100);
```

Hacés esto en Python:
```python
class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float
    stock: int
```
Y SQLModel crea la tabla y los `INSERT` por vos.

### Cómo se crean las tablas al iniciar
Al arrancar el programa se llama a `create_db_and_tables()`. Esa función le dice a SQLModel que cree todas las tablas que todavía no existen. SQLModel sabe cuáles son porque cada clase con `table=True` queda registrada automáticamente cuando es importada.

### El archivo `.env`
La URL de la base de datos (el archivo `.db` que se genera) se guarda en un archivo `.env` para no hardcodearla en el código. Así si el día de mañana querés cambiar el nombre del archivo o usar otro motor de base de datos, solo cambiás una línea en `.env`.


# Flujo Git

## Creamos la rama en base a develop
```
git checkout -b nombre-rama
```

## Trabajamos sobre esa rama
```
git add .
git commit -m "some changes"
git push
```

## Actualizamos la rama con develop
En la rama develop ejecutar:
```
git pull
```

En nuestra rama ejecutar:
```
git merge develop
```
Resolvemos conflictos si los hubiese.

## Pusheamos la rama con los cambios
```
git push
```

## Crear merge request dentro del repositorio