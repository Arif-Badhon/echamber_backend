from abc import ABC, abstractmethod
from typing import Type, TypeVar, List, Optional, Union, Any
from db import Base
from models import BaseModel
from sqlalchemy.orm import Session

ModelType = TypeVar('ModelType', bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class ABSRepo(ABC):

    def __init__(self, model: Type[ModelType]):
        self.model = model

    @abstractmethod
    def create(self, db: Session, data_in: CreateSchemaType) -> ModelType:
        pass

    @abstractmethod
    def get(self, db: Session) -> List[ModelType]:
        pass

    @abstractmethod
    def get_one(self, db: Session, id: int) -> ModelType:
        pass

    @abstractmethod
    def update(self, db: Session, id: int,  data_update: UpdateSchemaType) -> ModelType:
        pass

    @abstractmethod
    def delete(self, db: Session, id: int) -> Optional[Union[ModelType, Any]]:
        pass
