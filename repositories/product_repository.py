from typing import List, Optional
from sqlmodel import Session, select
from models.product import Product, ProductCreate, ProductRead, ProductUpdate


class ProductRepository:

    def create(self, session: Session, product_in: ProductCreate) -> ProductRead:
        product = Product.model_validate(product_in)
        session.add(product) #insert
        session.commit() #confirmacion
        session.refresh(product) #flush
        return ProductRead.model_validate(product)

    def get_by_id(self, session: Session, product_id: int) -> Optional[ProductRead]:
        product = session.get(Product, product_id)
        if not product:
            return None
        return ProductRead.model_validate(product)

    def get_all(self, session: Session) -> List[ProductRead]:
        products = session.exec(select(Product)).all()
        return [ProductRead.model_validate(p) for p in products]

    def update(
        self, session: Session, product_id: int, product_in: ProductUpdate
    ) -> Optional[ProductRead]:
        product = session.get(Product, product_id)
        if not product:
            return None
        update_data = product_in.model_dump(exclude_unset=True)
        product.sqlmodel_update(update_data)
        session.add(product)
        session.commit()
        session.refresh(product)
        return ProductRead.model_validate(product)

    def delete(self, session: Session, product_id: int) -> bool:
        product = session.get(Product, product_id)
        if not product:
            return False
        session.delete(product)
        session.commit()
        return True