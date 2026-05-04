from typing import List, Optional
from sqlmodel import Session, select
from models.sell import Sell, SellCreate, SellRead, SellUpdate


class SellRepository:

    def create(self, session: Session, sell_in: SellCreate) -> SellRead:
        sell = Sell.model_validate(sell_in)
        session.add(sell)
        session.commit()
        session.refresh(sell)
        return SellRead.model_validate(sell)

    def get_by_id(self, session: Session, sell_id: int) -> Optional[SellRead]:
        sell = session.get(Sell, sell_id)
        if not sell:
            return None
        return SellRead.model_validate(sell)

    def get_all(self, session: Session) -> List[SellRead]:
        sells = session.exec(select(Sell)).all()
        return [SellRead.model_validate(s) for s in sells]

    def update(
        self, session: Session, sell_id: int, sell_in: SellUpdate
    ) -> Optional[SellRead]:
        sell = session.get(Sell, sell_id)
        if not sell:
            return None
        update_data = sell_in.model_dump(exclude_unset=True)
        sell.sqlmodel_update(update_data)
        session.add(sell)
        session.commit()
        session.refresh(sell)
        return SellRead.model_validate(sell)

    def delete(self, session: Session, sell_id: int) -> bool:
        sell = session.get(Sell, sell_id)
        if not sell:
            return False
        session.delete(sell)
        session.commit()
        return True
