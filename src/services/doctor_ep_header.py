from models import DoctorEpHeader
from schemas import DoctorEpHeaderIn, DoctorEpHeaderUpdate
from repositories import doctor_ep_header_repo
from services import BaseService
from sqlalchemy.orm import Session


class DoctorEpHeaderService(BaseService[DoctorEpHeader, DoctorEpHeaderIn, DoctorEpHeaderUpdate]):

    def update_or_create(self, db: Session, user_id: int, data_in: DoctorEpHeaderUpdate):
        data = self.repo.get_by_two_key(db=db, skip=0, limit=10, descending=False, count_results=True, user_id=user_id, header_side=data_in.header_side)
        count = data[0]["results"]

        if count == 0:
            create = self.create(db=db, data_in=DoctorEpHeaderIn(**data_in.dict(), user_id=user_id))
            return create
        else:
            update = self.update(db=db, data_update=data_in, id=data[1][0].id)
            return update


doctor_ep_header_service = DoctorEpHeaderService(DoctorEpHeader, doctor_ep_header_repo)
