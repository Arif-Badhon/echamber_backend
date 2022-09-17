from datetime import timedelta, date
from models import DoctorSchedule
from schemas import DoctorScheduleIn, DoctorScheduleUpdate, RangeScheduleInput
from services import BaseService
from repositories import doctor_schedule_repo
from sqlalchemy.orm import Session
from utils import TimeString


class DoctorScheduleService(BaseService[DoctorSchedule, DoctorScheduleIn, DoctorScheduleUpdate]):
    def submit_with_range(self, db: Session, data_in: RangeScheduleInput, user_id: int):
        start_time = TimeString.time_str_to_min(time_str=data_in.time_start, am_pm=data_in.time_start_am_pm)
        end_time = TimeString.time_str_to_min(time_str=data_in.time_end, am_pm=data_in.time_end_am_pm)

        date_start = str(data_in.date_start).split('-')
        date_end = str(data_in.date_end).split('-')

        date_diff = TimeString.diff_dates(y1=int(date_start[0]), m1=int(date_start[1]), d1=int(date_start[2]), y2=int(date_end[0]), m2=int(date_end[1]), d2=int(date_end[2]))
        print(date_diff)
        print(date(1994, 7, 9) + timedelta(days=2))

        while start_time < end_time:
            # all input
            # self.repo.create(db=db, data_in=DoctorScheduleIn(data_in.date))
            # input done
            start_time += data_in.duration_min
        return 0


doctor_schedule_service = DoctorScheduleService(DoctorSchedule, doctor_schedule_repo)
