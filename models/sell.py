from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship

class SellBase(SQLModel):
    date: datetime = Field(default_factory=datetime.now)
    total: float = 0.0


class Sell(SellBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    details: List["Item"] = Relationship(back_populates="sell")


class SellCreate(SellBase):
    pass


class SellRead(SellBase):
    id: int


class SellUpdate(SQLModel):
    date: Optional[datetime] = None
    total: Optional[float] = None