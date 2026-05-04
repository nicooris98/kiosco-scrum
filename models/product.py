from typing import Optional
from sqlmodel import SQLModel, Field


class ProductBase(SQLModel):
    name: str
    price: float
    stock: int = 0

class Product(ProductBase, table=True):
    """La tabla real. table=True le dice a SQLAlchemy que cree la tabla."""
    id: Optional[int] = Field(default=None, primary_key=True)


class ProductCreate(ProductBase):
    """DTO para creación"""
    pass


class ProductRead(ProductBase):
    """DTO de respuesta"""
    id: int


class ProductUpdate(SQLModel):
    """
    DTO para actualización parcial (PATCH).
    Todos los campos son Optional para no obligar a mandar todo
    """
    name: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None