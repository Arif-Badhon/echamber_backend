from models import DocotorSchedule
from schemas import DoctorScheduleIn, DoctorScheduleUpdate
from services import BaseService
from repositories import doctor_schedules_repo

doctor_schedules_service = BaseService[DocotorSchedule, DoctorScheduleIn, DoctorScheduleUpdate](DocotorSchedule, doctor_schedules_repo)