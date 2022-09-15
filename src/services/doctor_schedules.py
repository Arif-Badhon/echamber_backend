# from datetime import date
# from models import DoctorSchedule
# from schemas import DoctorScheduleIn, DoctorScheduleUpdate
# from services import BaseService
# from repositories import doctor_schedule_repo
# from sqlalchemy.orm import Session
# from exceptions import ServiceResult
# from fastapi import status


# class DoctorScheduleService(BaseService[DoctorSchedule, DoctorScheduleIn, DoctorScheduleUpdate]):

#     def booked_schedule(self, db: Session, doctor_id: int, date: date):
#         data = self.repo.booked_schedule(db=db, doctor_id=doctor_id, date=date)
#         if not data:
#             data = []
#         return ServiceResult(data, status_code=status.HTTP_200_OK)


# doctor_schedule_service = DoctorScheduleService(DoctorSchedule, doctor_schedule_repo)
