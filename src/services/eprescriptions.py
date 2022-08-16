from schemas import EpIn, EpUpdate, EpBase, EpDoctorReferWithEp, ChiefComplaintsWithEp, HistoryWithEp
from services import BaseService
from repositories import ep_repo, ep_refer_repo, ep_chief_complaints_repo, ep_history_repo
from models import EPrescription
from sqlalchemy.orm import Session


class EPrescriptionService(BaseService[EPrescription, EpBase, EpUpdate]):

    def submit(self, data_in: EpIn, db: Session):
        # eprescription
        ep = ep_repo.create_with_flush(db=db, data_in=EpBase(cause_of_consultation=data_in.cause_of_consultation, telemedicine_order_id=data_in.telemedicine_order_id,
                                       doctor_id=data_in.doctor_id, patient_id=data_in.patient_id, age=data_in.age, current_address=data_in.current_address, remarks=data_in.remarks))

        # chief complaints
        if len(data_in.chief_complaints) != 0:
            for i in data_in.chief_complaints:
                cc = ep_chief_complaints_repo.create_with_flush(db=db, data_in=ChiefComplaintsWithEp(chief_complaints=i.chief_complaints, ep_id=ep.id))

        # history
        if len(data_in.histories) != 0:
            for i in data_in.histories:
                hs = ep_history_repo.create_with_flush(db=db, data_in=HistoryWithEp(history_type=i.history_type, history=i.history, ep_id=ep.id))

        refr = ep_refer_repo.create_with_flush(db=db, data_in=EpDoctorReferWithEp(detail=data_in.refer.detail, ep_id=ep.id))

        # commit all flushed data
        db.commit()

        return_data = ep_repo.get_one(db=db, id=ep.id)

        return return_data


ep_service = EPrescriptionService(EPrescription, ep_repo)
