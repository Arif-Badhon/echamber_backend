from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

from schemas.users import UserOut
from .ep_chief_complaints import ChiefComplaintsOut, ChiefComplaintsIn
from .ep_history import HistoryOut, HistoryIn
from .ep_comorbidity import EpCoMorbidityOut, EpCoMorbidityIn
from .ep_on_examination import EpOnExaminationOut, EpOnExaminationIn
from .ep_investigations import EpInvestigationOut, EpInvestigationIn
from .ep_diagnosis import EpDiagnosisOut, EpDiagnosisIn
from .ep_medicines import EpMedicineOut, EpMedicineIn, MedicineIn
from .ep_advices import AdviceOut, AdviceIn
from .ep_doctor_refer import EpDoctorReferOut, EpDoctorReferIn
from .ep_next_follow_up import EpNextFollowUpOut, EpNextFollowUpIn
from .patient_indicators import PatientIndicatorBase, PatientIndicatorOut
###############
#   Ep base   #
###############


class EpBase(BaseModel):
    cause_of_consultation: Optional[str] = None
    telemedicine_order_id: Optional[int] = None
    doctor_id: Optional[int] = None
    patient_id: Optional[int] = None
    patient_name: Optional[str] = None
    patient_phone: Optional[str] = None # newly added - antor
    patient_sex: Optional[str] = None
    blood_group: Optional[str] = None # newly added - antor
    age_years: Optional[int] = None
    age_months: Optional[int] = None
    current_address: Optional[str] = None
    remarks: Optional[str] = None


class EpOut(EpBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class EpOutWithDoctorAndPatient(EpBase):
    id: int
    created_at: datetime
    doctor: List[UserOut]
    patient: List [UserOut]

    class Config:
        orm_mode = True


class EpOutWithPatient(EpBase):
    id: int
    created_at: datetime
    patient: List [UserOut]

    class Config:
        orm_mode = True


class EpIn(EpBase):
    chief_complaints: List[ChiefComplaintsIn] = None
    histories: List[HistoryIn] = None
    co_morbidities: List[EpCoMorbidityIn] = None
    on_examinations: List[PatientIndicatorBase] = None
    investigations: List[EpInvestigationIn] = None
    diagnosis: List[EpDiagnosisIn] = None
    medicines: List[EpMedicineIn] = None
    advices: List[AdviceIn] = None
    refer: EpDoctorReferIn = None
    followup: EpNextFollowUpIn = None


class EpUpdate(BaseModel):
    cause_of_consultation: Optional[str] = None
    telemedicine_order_id: Optional[int] = None
    doctor_id: Optional[int] = None
    patient_id: Optional[int] = None
    age: Optional[int] = None
    current_address: Optional[str] = None
    remarks: Optional[str] = None


class EpAllOut(EpBase):
    created_at: datetime
    chief_complaints: List[ChiefComplaintsOut] = None
    histories: List[HistoryOut] = None
    co_morbidities: List[EpCoMorbidityOut] = None
    on_examinations: List[PatientIndicatorOut] = None
    investigations: List[EpInvestigationOut] = None
    diagnosis: List[EpDiagnosisOut] = None
    medicines: List[EpMedicineOut] = None
    advices: List[AdviceOut] = None
    refer: List[EpDoctorReferOut] = None
    followup: List[EpNextFollowUpOut] = None

    class Config:
        orm_mode = True
