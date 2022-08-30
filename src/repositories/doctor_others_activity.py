from repositories import BaseRepo
from models import DoctorOthersActivity
from schemas import DoctorOthersActivityIn, DoctorAcademicInfoUpdate


doctor_others_activity_repo = BaseRepo[DoctorOthersActivity, DoctorOthersActivityIn, DoctorAcademicInfoUpdate](DoctorOthersActivity)
