from repositories import BaseRepo, roles_repo
from models import PharmacyActivity, User, UserDetail
from schemas import PharmacyActivityIn, PharmacyActivityUpdate
from sqlalchemy.orm import Session
from sqlalchemy.sql import func


class PharmacyActivityRepo(BaseRepo[PharmacyActivity, PharmacyActivityIn, PharmacyActivityUpdate]):
    def get_activity_by_pharmacy_id(self, db: Session, pharmacy_id: int, skip: int, limit: int):
        data_count =  db.query(self.model).filter(self.model.pharmacy_id == pharmacy_id).all()
        data =  db.query(self.model).filter(self.model.pharmacy_id == pharmacy_id).offset(skip).limit(limit).all()
        return [{"results": len(data_count)}, data]

    def get_pharmacy_patient(self, db: Session, pharmacy_id: int, skip: int, limit: int):

        role_id = roles_repo.search_name_id(db=db, name='patient')

        data_count = db.query(User, UserDetail).filter(User.id.in_(db.query(func.distinct(self.model.service_received_id)))).filter(User.role_id==role_id).filter(User.id==UserDetail.user_id).filter(self.model.pharmacy_id == pharmacy_id).all()

        data = db.query(User, UserDetail).filter(User.id.in_(db.query(func.distinct(self.model.service_received_id)))).filter(User.role_id==role_id).filter(User.id==UserDetail.user_id).filter(self.model.pharmacy_id == pharmacy_id).offset(skip).limit(limit).all()
        return [{"results": len(data_count)}, data]


pharmacy_activity_repo = PharmacyActivityRepo(PharmacyActivity)