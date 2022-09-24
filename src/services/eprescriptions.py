from schemas import EpIn, EpUpdate, EpBase, EpDoctorReferWithEp, ChiefComplaintsWithEp, HistoryWithEp, EpCoMorbidityWithEp, EpInvestigationWithEp, EpNextFollowUpWithEp, EpMedicineWithEp, PatientIndicatorIn, EpOnExaminationIn
from schemas.ep_advices import AdviceInWithEp
from schemas.ep_diagnosis import EpDiagnosisOut, EpDiagnosisWithEp
from services import BaseService
from repositories import ep_repo, ep_refer_repo, ep_chief_complaints_repo, ep_history_repo, ep_co_morbities_repo, ep_investigation_repo, ep_diagnosis_repo, ep_advices_repo, ep_next_follow_up_repo, ep_medicines_repo, patient_indicators_repo, ep_on_examination_repo
from models import EPrescription
from sqlalchemy.orm import Session


class EPrescriptionService(BaseService[EPrescription, EpBase, EpUpdate]):

    def submit(self, data_in: EpIn, db: Session):
        # eprescription
        ep = ep_repo.create_with_flush(
            db=db,
            data_in=EpBase(
                cause_of_consultation=data_in.cause_of_consultation, telemedicine_order_id=data_in.telemedicine_order_id, doctor_id=data_in.doctor_id, patient_id=data_in.patient_id,
                age_years=data_in.age_years, age_months=data_in.age_months, current_address=data_in.current_address, remarks=data_in.remarks))

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

        # on examination
        if data_in.on_examinations and len(data_in.on_examinations) != 0:
            for i in data_in.on_examinations:
                pi = patient_indicators_repo.create_with_flush(db=db,
                                                               data_in=PatientIndicatorIn(
                                                                   user_id=data_in.patient_id, key=i.key, unit=i.unit, slot_bool=i.slot_bool, slot_int1=i.slot_int1, slot_int2=i.slot_int2,
                                                                   slot_int3=i.slot_int3, slot_flt4=i.slot_flt4, slot_flt5=i.slot_flt5, slot_flt6=i.slot_flt6, slot_str7=i.slot_str7,
                                                                   slot_str8=i.slot_str8, slot_str9=i.slot_str9))
                on = ep_on_examination_repo.create_with_flush(db=db, data_in=EpOnExaminationIn(ep_id=ep.id, patient_indicator_id=pi.id))

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
        if data_in.refer and len(data_in.refer.detail) != 0:
            refr = ep_refer_repo.create_with_flush(db=db, data_in=EpDoctorReferWithEp(detail=data_in.refer.detail, ep_id=ep.id))

        # followup
        if data_in.followup:
            flup = ep_next_follow_up_repo.create_with_flush(db=db, data_in=EpNextFollowUpWithEp(date=data_in.followup.date, ep_id=ep.id))

        # commit all flushed data
        db.commit()

        return_data = ep_repo.get_one(db=db, id=ep.id)

        return return_data

    def get_single_ep(self, db: Session, id: int):
        ep_data = ep_repo.get_one(db=db, id=id)

        chief_complaints = ep_chief_complaints_repo.get_by_key(db=db, skip=0, limit=1000, descending=False, count_results=False, ep_id=ep_data.id)
        history = ep_history_repo.get_by_key(db=db, skip=0, limit=1000, descending=False, count_results=False, ep_id=ep_data.id)
        co_morbidities = ep_co_morbities_repo.get_by_key(db=db, skip=0, limit=1000, descending=False, count_results=False, ep_id=ep_data.id)
        on_examinations = ep_on_examination_repo.get_by_key(db=db, skip=0, limit=1000, descending=False, count_results=False, ep_id=ep_data.id)
        investigations = ep_investigation_repo.get_by_key(db=db, skip=0, limit=1000, descending=False, count_results=False, ep_id=ep_data.id)
        diagnosis = ep_diagnosis_repo.get_by_key(db=db, skip=0, limit=1000, descending=False, count_results=False, ep_id=ep_data.id)
        medicines = ep_medicines_repo.get_by_key(db=db, skip=0, limit=1000, descending=False, count_results=False, ep_id=ep_data.id)
        advices = ep_advices_repo.get_by_key(db=db, skip=0, limit=1000, descending=False, count_results=False, ep_id=ep_data.id)
        refer = ep_refer_repo.get_by_key(db=db, skip=0, limit=1000, descending=False, count_results=False, ep_id=ep_data.id)
        followup = ep_next_follow_up_repo.get_by_key(db=db, skip=0, limit=1000, descending=False, count_results=False, ep_id=ep_data.id)

        data = {
            "cause_of_consultation": ep_data.cause_of_consultation,
            "telemedicine_order_id": ep_data.telemedicine_order_id,
            "doctor_id": ep_data.doctor_id,
            "patient_id": ep_data.patient_id,
            "age_years": ep_data.age_years,
            "age_months": ep_data.age_months,
            "current_address": ep_data.current_address,
            "remarks": ep_data.remarks,
            "created_at": ep_data.created_at,
            "chief_complaints": chief_complaints,
            "histories": history,
            "co_morbidities": co_morbidities,
            "on_examinations": on_examinations,
            "investigations": investigations,
            "diagnosis": diagnosis,
            "medicines": medicines,
            "advices": advices,
            "refer": refer,
            "followup": followup
        }
        return data


ep_service = EPrescriptionService(EPrescription, ep_repo)
