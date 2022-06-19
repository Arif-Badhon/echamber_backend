from models import DoctorSchedule
from schemas import DoctorScheduleIn, DoctorScheduleUpdate
from services import BaseService
from repositories import doctor_schedule_repo


doctor_schedule_service = BaseService[DoctorSchedule, DoctorScheduleIn, DoctorScheduleUpdate](DoctorSchedule, doctor_schedule_repo)