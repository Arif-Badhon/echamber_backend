from repositories import BaseRepo
from schemas import DoctorScheduleIn, DoctorChamberUpdate
from models import DocotorSchedule

# class DoctorScheduleRepo(BaseRepo[DocotorSchedule, DoctorScheduleIn, DoctorChamberUpdate]):

doctor_schedules_repo = BaseRepo[DocotorSchedule, DoctorScheduleIn, DoctorChamberUpdate](DocotorSchedule)
