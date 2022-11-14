from services import BaseService
from repositories import doctor_workplace_repo
from models import DoctorWorkPlace
from schemas import DoctorWorkPlaceIn, DoctorWorkPlaceUpdate
from sqlalchemy.orm import Session


class DoctorWorkPlaceService(BaseService[DoctorWorkPlace, DoctorWorkPlaceIn, DoctorWorkPlaceUpdate]):

    def workplace_priority_set(self, db: Session,  id: int, user_id: int):
        data = self.repo.get_by_key(db=db, skip=0, limit=100, descending=False, count_results=False, user_id=user_id)
        if data:
            for d in data:
                if d.id == id:
                    up = self.repo.update(db=db, id=d.id, data_update=DoctorWorkPlaceUpdate(top_priority=True))
                else:
                    up = self.repo.update(db=db, id=d.id, data_update=DoctorWorkPlaceUpdate(top_priority=False))

        get_data = self.get_by_key(db=db, skip=0, limit=100, descending=False, count_results=False, user_id=user_id)
        return get_data


doctor_workplace_service = DoctorWorkPlaceService(DoctorWorkPlace, doctor_workplace_repo)
