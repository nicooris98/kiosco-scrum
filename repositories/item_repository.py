from typing import List, Optional
from sqlmodel import Session, select
from models.item import Item, ItemCreate, ItemRead, ItemUpdate


class ItemRepository:

    def create(self, session: Session, item_in: ItemCreate) -> ItemRead:
        item = Item.model_validate(item_in)
        session.add(item)
        session.commit()
        session.refresh(item)
        return ItemRead.model_validate(item)

    def get_by_id(self, session: Session, item_id: int) -> Optional[ItemRead]:
        item = session.get(Item, item_id)
        if not item:
            return None
        return ItemRead.model_validate(item)

    def get_all(self, session: Session) -> List[ItemRead]:
        items = session.exec(select(Item)).all()
        return [ItemRead.model_validate(i) for i in items]

    def get_by_sell(self, session: Session, sell_id: int) -> List[ItemRead]:
        items = session.exec(select(Item).where(Item.sell_id == sell_id)).all()
        return [ItemRead.model_validate(i) for i in items]

    def update(
        self, session: Session, item_id: int, item_in: ItemUpdate
    ) -> Optional[ItemRead]:
        item = session.get(Item, item_id)
        if not item:
            return None
        update_data = item_in.model_dump(exclude_unset=True)
        item.sqlmodel_update(update_data)
        session.add(item)
        session.commit()
        session.refresh(item)
        return ItemRead.model_validate(item)

    def delete(self, session: Session, item_id: int) -> bool:
        item = session.get(Item, item_id)
        if not item:
            return False
        session.delete(item)
        session.commit()
        return True
