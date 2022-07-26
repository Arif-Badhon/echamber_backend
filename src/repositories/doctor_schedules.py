from datetime import date
from models import DoctorSchedule, TeleMedicineOrder
from schemas import DoctorScheduleIn, DoctorScheduleUpdate
from repositories import BaseRepo
from sqlalchemy.orm import Session


class DoctorScheduleRepo(BaseRepo[DoctorSchedule, DoctorScheduleIn, DoctorScheduleUpdate]):

    def booked_schedule(self, db: Session, doctor_id: int, date: date):
        schedule_data = db.query(self.model).filter(self.model.user_id == doctor_id).all()
        data = []

        for i in schedule_data:
            telm = db.query(TeleMedicineOrder).filter(TeleMedicineOrder.doctor_id == doctor_id).filter(TeleMedicineOrder.booked_date == date).filter(TeleMedicineOrder.schedule_id == i.id).first()

            if not telm:
                i.booked = False
            else:
                i.booked = True
            data.append(i)
        return data


doctor_schedule_repo = DoctorScheduleRepo(DoctorSchedule)
