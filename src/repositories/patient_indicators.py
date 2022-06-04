from sqlalchemy import desc
from models import PatientIndicator
from repositories import BaseRepo
from repositories.base import ModelType
from schemas import PatientIndicatorIn, PatientIndicatorUpdate
from sqlalchemy.orm import Session
from typing import List
from schemas.patient_indicators import PatientIndicatorBase


class PatientIndicatorRepo(BaseRepo[PatientIndicator,
                                    PatientIndicatorIn, PatientIndicatorUpdate]):

    def create_by_user_id(self, db: Session, user_id: int, data_in: PatientIndicatorBase):

        data_for_db = PatientIndicatorIn(
            user_id=user_id,
            **data_in.dict()
        )

        return self.create(db, data_for_db)

    def get_by_key(self, db: Session, key: str, user_id: int, skip: int, limit: int):
        return db.query(self.model).filter(self.model.key == key).filter(self.model.user_id == user_id).order_by(desc(self.model.created_at)).offset(skip).limit(limit).all()

    def get_last_item(self, db: Session, key: str, user_id: int):
        last_single = db.query(self.model).filter(self.model.key == key).filter(self.model.user_id == user_id).order_by(desc(self.model.created_at)).first()
        return last_single

patient_indicators_repo = PatientIndicatorRepo(PatientIndicator)



            # key=data_in.key,
            # unit=data_in.unit,
            # slot_bool=data_in.slot_bool,
            # slot_int1=data_in.slot_int1,
            # slot_int2=data_in.slot_int2,
            # slot_int3=data_in.slot_int3,
            # slot_flt4=data_in.slot_flt4,
            # slot_flt5=data_in.slot_flt5,
            # slot_flt6=data_in.slot_flt6,
            # slot_str7=data_in.slot_str7,
            # slot_str8=data_in.slot_str8,
            # slot_str9=data_in.slot_str9