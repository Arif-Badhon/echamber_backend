from typing import Any, Generic, Optional, Type, TypeVar, List, Union
from sqlalchemy.orm import Session
from db import Base
from models import BaseModel
from repositories.base_abstract import ABSRepo

ModelType = TypeVar('ModelType', bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseRepo(Generic[ModelType, CreateSchemaType, UpdateSchemaType], ABSRepo):

    def __init__(self, model: Type[ModelType]):
        self.model = model

    def create(self, db: Session, data_in: CreateSchemaType) -> ModelType:
        data = self.model(**data_in.dict())
        db.add(data)
        db.commit()
        db.refresh(data)
        return data

    def get(self, db: Session) -> List[ModelType]:
        query = db.query(self.model).all()
        return query

    def get_one(self, db: Session, id: int) -> ModelType:
        return db.query(self.model).filter(self.model.id == id).first()

    def update(self, db: Session, id: int,  data_update: UpdateSchemaType) -> ModelType:
        db.query(self.model).filter(self.model.id == id).update(
            data_update.dict(exclude_unset=True), synchronize_session=False)
        db.commit()
        return self.get_one(db, id)

    def delete(self, db: Session, id: int) -> Optional[Union[ModelType, Any]]:
        result = db.query(self.model).filter(self.model.id ==
                                             id).delete(synchronize_session=False)
        db.commit()
        return result
