from models import DocotorSchedule
from schemas import DoctorScheduleIn, DoctorScheduleUpdate
from services import BaseService
from repositories import doctor_schedules_repo


class DoctorScheduleService(BaseService[DocotorSchedule, DoctorScheduleIn, DoctorScheduleUpdate]):
    def nothing():
        return 


doctor_schedules_service = DoctorScheduleService(DocotorSchedule, doctor_schedules_repo)