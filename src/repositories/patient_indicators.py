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
            key=data_in.key,
            unit=data_in.unit,
            slot_bool=data_in.slot_bool,
            slot_int1=data_in.slot_int1,
            slot_int2=data_in.slot_int2,
            slot_int3=data_in.slot_int3,
            slot_str1=data_in.slot_str1,
            slot_str2=data_in.slot_str2,
            slot_str3=data_in.slot_str3
        )

        return self.create(db, data_for_db)

    def get_by_key(self, db: Session, key: str, user_id: int):
        return db.query(self.model).filter(self.model.key == key).filter(self.model.user_id == user_id).all()

    def get_last_item(self, db: Session, key: str, user_id: int):
        all = db.query(self.model).filter(self.model.key == key).filter(
            self.model.user_id == user_id).all()
        return all[-1]


patient_indicators_repo = PatientIndicatorRepo(PatientIndicator)
