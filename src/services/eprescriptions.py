from schemas import EpIn, EpUpdate, EpBase, EpDoctorReferWithEp, ChiefComplaintsWithEp, HistoryWithEp, EpCoMorbidityWithEp, EpInvestigationWithEp, EpNextFollowUpWithEp, EpMedicineWithEp
from schemas.ep_advices import AdviceInWithEp
from schemas.ep_diagnosis import EpDiagnosisWithEp
from services import BaseService
from repositories import ep_repo, ep_refer_repo, ep_chief_complaints_repo, ep_history_repo, ep_co_morbities_repo, ep_investigation_repo, ep_diagnosis_repo, ep_advices_repo, ep_next_follow_up_repo, ep_medicines_repo
from models import EPrescription
from sqlalchemy.orm import Session


class EPrescriptionService(BaseService[EPrescription, EpBase, EpUpdate]):

    def submit(self, data_in: EpIn, db: Session):
        # eprescription
        ep = ep_repo.create_with_flush(db=db, data_in=EpBase(cause_of_consultation=data_in.cause_of_consultation, telemedicine_order_id=data_in.telemedicine_order_id,
                                       doctor_id=data_in.doctor_id, patient_id=data_in.patient_id, age=data_in.age, current_address=data_in.current_address, remarks=data_in.remarks))

        # chief complaints
        if data_in.chief_complaints and len(data_in.chief_complaints) != 0:
            for i in data_in.chief_complaints:
                cc = ep_chief_complaints_repo.create_with_flush(db=db, data_in=ChiefComplaintsWithEp(chief_complaints=i.chief_complaints, ep_id=ep.id))

        # history
        if data_in.histories and len(data_in.histories) != 0:
            for i in data_in.histories:
                hs = ep_history_repo.create_with_flush(db=db, data_in=HistoryWithEp(history_type=i.history_type, history=i.history, ep_id=ep.id))

        # co-morbidity
        if data_in.co_morbidities and len(data_in.co_morbidities) != 0:
            for i in data_in.co_morbidities:
                cm = ep_co_morbities_repo.create_with_flush(db=db, data_in=EpCoMorbidityWithEp(cm_type=i.cm_type, remarks=i.remarks, ep_id=ep.id))

        # investigations
        if data_in.investigations and len(data_in.investigations) != 0:
            for i in data_in.investigations:
                inv = ep_investigation_repo.create_with_flush(db=db, data_in=EpInvestigationWithEp(investigation=i.investigation, ep_id=ep.id))

        # diagnosis
        if data_in.diagnosis and len(data_in.diagnosis) != 0:
            for i in data_in.diagnosis:
                diag = ep_diagnosis_repo.create_with_flush(db=db, data_in=EpDiagnosisWithEp(diagnosis_type=i.diagnosis_type, diagnosis=i.diagnosis, ep_id=ep.id))

        # medicine
        if data_in.medicines and len(data_in.medicines) != 0:
            for i in data_in.medicines:
                med = ep_medicines_repo.create_with_flush(db=db, data_in=EpMedicineWithEp(name=i.name, generic=i.generic, pharmaceuticals=i.pharmaceuticals,
                                                          form=i.form, strength=i.strength, doses=i.doses, after_meal=i.after_meal, days=i.days, remarks=i.remarks, ep_id=ep.id))

        # advices
        if data_in.advices and len(data_in.advices) != 0:
            for i in data_in.advices:
                adv = ep_advices_repo.create_with_flush(db=db, data_in=AdviceInWithEp(advice=i.advice, ep_id=ep.id))

        # reference
        if data_in.refer.detail and len(data_in.refer.detail) != 0:
            refr = ep_refer_repo.create_with_flush(db=db, data_in=EpDoctorReferWithEp(detail=data_in.refer.detail, ep_id=ep.id))

        # followup
        if data_in.followup.date:
            flup = ep_next_follow_up_repo.create_with_flush(db=db, data_in=EpNextFollowUpWithEp(date=data_in.followup.date, ep_id=ep.id))

        # commit all flushed data
        db.commit()

        return_data = ep_repo.get_one(db=db, id=ep.id)

        return return_data


ep_service = EPrescriptionService(EPrescription, ep_repo)
