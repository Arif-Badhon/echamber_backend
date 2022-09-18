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
        print(start_time)
        date_start = str(data_in.date_start).split('-')
        date_end = str(data_in.date_end).split('-')

        date_diff = TimeString.diff_dates(y1=int(date_start[0]), m1=int(date_start[1]), d1=int(date_start[2]), y2=int(date_end[0]), m2=int(date_end[1]), d2=int(date_end[2]))
        day_increment = 0

        while day_increment <= date_diff:
            selected_date = data_in.date_start + timedelta(days=day_increment)
            # time split
            start_time_loop = start_time
            while start_time_loop < end_time:
                # all input
                # check and set am pm
                new_am_pm = 'am'
                if start_time_loop > 719:
                    new_am_pm = 'pm'

                self.repo.create(db=db, data_in=DoctorScheduleIn(date=selected_date, time_min=start_time_loop, am_pm=new_am_pm,
                                 online=data_in.online, chamber_id=data_in.chamber_id, booked_by_patient_id=data_in.booked_by_patient_id, duration_min=data_in.duration_min, user_id=user_id))
                # input done
                start_time_loop += data_in.duration_min
            # time split done
            print(selected_date)
            day_increment += 1

        return 0


doctor_schedule_service = DoctorScheduleService(DoctorSchedule, doctor_schedule_repo)
