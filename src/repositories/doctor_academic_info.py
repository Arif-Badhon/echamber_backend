from repositories import BaseRepo
from models import DoctorAcademicInfo
from schemas import DoctorAcademicInfoIn, DoctorAcademicInfoUpdate


doctor_academic_info_repo = BaseRepo[DoctorAcademicInfo, DoctorAcademicInfoIn, DoctorAcademicInfoUpdate](DoctorAcademicInfo)
