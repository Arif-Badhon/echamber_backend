from repositories import doctors_search_repo
from models import User
from schemas import UserBase, UserUpdate
from services import BaseService
from sqlalchemy.orm import Session
from fastapi import status
from exceptions import ServiceResult


class DoctorSearchService(BaseService[User, UserBase, UserUpdate]):

    def doctor_search(self, db: Session, name: str, speciality: str, skip: int, limit: int):
        repo = doctors_search_repo.doctor_search(db, name, speciality, skip, limit)
        if not repo:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        else:
            return ServiceResult(repo, status_code=status.HTTP_200_OK)


doctors_search_service = DoctorSearchService(User, doctors_search_repo)
