from sqlalchemy.orm import Session
from repositories import BaseRepo
from schemas import DoctorChamberIn, DoctorChamberUpdate, DoctorChamberBase
from models import DoctorChamber


class DoctorChamberRepo(BaseRepo[DoctorChamber, DoctorChamberIn, DoctorChamberUpdate]):
    def get_by_user_id(self, db: Session, user_id: int):
        return db.query(self.model).filter(self.model.user_id == user_id).all()

    def create_with_user_id(self, db: Session, data_in: DoctorChamberBase, user_id: int):
        data_for_db = DoctorChamberIn(
            user_id=user_id,
            name=data_in.name,
            detail=data_in.detail
        )

        return self.create(db, data_in=data_for_db)

    def chamber_deactive_by_user_id(self, db: Session, user_id: int):
        db.query(self.model).filter(self.model.user_id == user_id).update(
            {self.model.is_active: False}, synchronize_session=False)
        db.commit()
        return self.get_by_user_id(db, user_id=user_id)

    def chamber_active_by_id(self, db: Session, id):
        db.query(self.model).filter(self.model.id == id).update(
            {self.model.is_active: True}, synchronize_session=False)
        db.commit()
        return self.get_one(db, id)


doctor_chambers_repo = DoctorChamberRepo(DoctorChamber)
