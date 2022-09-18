from models import DoctorSchedule
from schemas import DoctorScheduleIn, DoctorScheduleUpdate
from repositories import BaseRepo
from sqlalchemy.orm import Session
from datetime import date
from utils import TimeString


class DoctrScheduleRepo(BaseRepo[DoctorSchedule, DoctorScheduleIn, DoctorScheduleUpdate]):

    def get_by_date_with_order(self, db: Session, date: str, user_id: int):
        data = db.query(self.model).filter(self.model.user_id == user_id).filter(self.model.date == date).order_by(self.model.chamber_id).order_by(self.model.time_min).order_by(self.model.am_pm).all()
        new_data = []
        for i in data:
            i.time = TimeString.min_to_time_str(min=i.time_min)
            new_data.append(i)
        return data


doctor_schedule_repo = DoctrScheduleRepo(DoctorSchedule)
