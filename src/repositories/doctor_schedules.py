from models import DoctorSchedule
from schemas import DoctorScheduleIn, DoctorScheduleUpdate
from repositories import BaseRepo


doctor_schedule_repo = BaseRepo[DoctorSchedule, DoctorScheduleIn, DoctorScheduleUpdate](DoctorSchedule)
