from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class ItemBase(SQLModel):
    quantity: int
    unit_price: float
    product_id: int = Field(foreign_key="product.id")
    sell_id: int = Field(foreign_key="sell.id")


class Item(ItemBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sell: Optional["Sell"] = Relationship(back_populates="details")


class ItemCreate(ItemBase):
    pass


class ItemRead(ItemBase):
    id: int


class ItemUpdate(SQLModel):
    quantity: Optional[int] = None
    unit_price: Optional[float] = None