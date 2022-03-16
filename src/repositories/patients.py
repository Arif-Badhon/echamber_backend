from models import Patient
from repositories import BaseRepo, ModelType, UpdateSchemaType
from schemas import PatientIn, PatientUpdate
from sqlalchemy.orm import Session


class PatientRepo(BaseRepo[Patient, PatientIn, PatientUpdate]):
    def get_by_user_id(self, db: Session, user_id: int):
        return db.query(self.model).filter(self.model.user_id == user_id).first()

    def update_by_user_id(self, db: Session, user_id: int,  data_update: UpdateSchemaType) -> ModelType:
        db.query(self.model).filter(self.model.user_id == user_id).update(
            data_update.dict(exclude_unset=True), synchronize_session=False)
        db.commit()
        return self.get_by_user_id(db, user_id=user_id)


patients_repo = PatientRepo(Patient)
