from models import Patient, User
from repositories import BaseRepo, ModelType, UpdateSchemaType, roles_repo
from schemas import PatientIn, PatientUpdate
from sqlalchemy.orm import Session


class PatientRepo(BaseRepo[Patient, PatientIn, PatientUpdate]):
    def get_by_user_id(self, db: Session, user_id: int):
        role_id_by_repo = roles_repo.search_name_id('patient')
        return db.query(self.model).filter(User.role_id == role_id_by_repo).filter(self.model.user_id == user_id).first()

    def search_by_patient_name(self, db: Session, name: str, skip:int, limit:int):
        role_id_by_repo = roles_repo.search_name_id(db=db, name='patient')
        data = db.query(User).filter(User.role_id == role_id_by_repo).filter(User.name.like(f'%{name}%')).offset(skip).limit(limit).all()
        return data

    def update_by_user_id(self, db: Session, user_id: int,  data_update: UpdateSchemaType) -> ModelType:
        db.query(self.model).filter(self.model.user_id == user_id).update(
            data_update.dict(exclude_unset=True), synchronize_session=False)
        db.commit()
        return self.get_by_user_id(db, user_id=user_id)


patients_repo = PatientRepo(Patient)
