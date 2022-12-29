from datetime import timedelta, date
from models import DoctorSchedule
from schemas import DoctorScheduleIn, DoctorScheduleUpdate, RangeScheduleInput, AdminPanelActivityIn
from services import BaseService
from repositories import doctor_schedule_repo, admin_panel_activity_repo
from sqlalchemy.orm import Session
from utils import TimeString
from exceptions import ServiceResult, AppException
from fastapi import status


class DoctorScheduleService(BaseService[DoctorSchedule, DoctorScheduleIn, DoctorScheduleUpdate]):

    def get_doctor_all_schedule(self, db: Session, date: date, user_id: int):
        data = doctor_schedule_repo.get_by_date_with_order(db=db, date=date, user_id=user_id)
        if not data:
            data = []
        return ServiceResult(data, status_code=status.HTTP_200_OK)

    def submit_with_range(self, db: Session, data_in: RangeScheduleInput, user_id: int):
        week_day_serial = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

        start_time = TimeString.time_str_to_min(time_str=data_in.time_start, am_pm=data_in.time_start_am_pm)
        end_time = TimeString.time_str_to_min(time_str=data_in.time_end, am_pm=data_in.time_end_am_pm)

        date_start = str(data_in.date_start).split('-')
        date_end = str(data_in.date_end).split('-')

        date_diff = TimeString.diff_dates(y1=int(date_start[0]), m1=int(date_start[1]), d1=int(date_start[2]), y2=int(date_end[0]), m2=int(date_end[1]), d2=int(date_end[2]))
        day_increment = 0

        while day_increment <= date_diff:
            selected_date = data_in.date_start + timedelta(days=day_increment)

            # weekday check
            week_day_int = selected_date.weekday()
            if week_day_serial[week_day_int] in data_in.week_day:

                # time split
                start_time_loop = start_time
                while start_time_loop < end_time:
                    # all input
                    # check and set am pm
                    new_am_pm = 'am'
                    if start_time_loop > 719:
                        new_am_pm = 'pm'

                    self.repo.create(db=db, data_in=DoctorScheduleIn(date=selected_date, time_min=start_time_loop, am_pm=new_am_pm, online=data_in.online,
                                     chamber_id=data_in.chamber_id, booked_by_patient_id=data_in.booked_by_patient_id, duration_min=data_in.duration_min, user_id=user_id))
                    # input done
                    start_time_loop += data_in.duration_min
                    # time split done

            # week day check done
            day_increment += 1

        return ServiceResult({"msg": "Shedules created"}, status_code=200)

    def booked_by_employee(self, db: Session, schedule_id: int, patient_id: int, employee_id: int):
        update_schedule = self.repo.update(db=db, data_update=DoctorScheduleUpdate(booked_by_patient_id=patient_id), id=schedule_id)

        if not update_schedule:
            return ServiceResult(AppException.ServerError(
                "Problem with booking."))

        service_by = admin_panel_activity_repo.create(db=db, data_in=AdminPanelActivityIn(user_id=employee_id, service_name='schedule_booked_for_patient', service_recived_id=patient_id, remark=''))
        if not service_by:
            return ServiceResult(AppException.ServerError(
                    "Problem with employee registration."))
        else:    
            return ServiceResult(update_schedule, status_code=status.HTTP_202_ACCEPTED)


doctor_schedule_service = DoctorScheduleService(DoctorSchedule, doctor_schedule_repo)
