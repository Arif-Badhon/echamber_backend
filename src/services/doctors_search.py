from repositories import doctors_search_repo, doctor_specialities_repo
from models import User
from schemas import UserBase, UserUpdate
from services import BaseService
from sqlalchemy.orm import Session
from fastapi import status
from exceptions import ServiceResult


class DoctorSearchService(BaseService[User, UserBase, UserUpdate]):

    def doctor_search(self, db: Session, search: str, skip: int, limit: int):
        data = []

        loc = doctors_search_repo.doc_search_by_chamber_loc(db=db, skip=skip, limit=limit, district=search)
        data.extend(loc)

        spec = doctors_search_repo.doc_search_by_speciality(db=db, skip=skip, limit=limit, speciality=search)
        data.extend(spec)

        name = doctors_search_repo.doc_search_by_name(db=db, skip=skip, limit=limit, name=search)
        data.extend(name)

        for i in data:
            arr = doctor_specialities_repo.get_by_key(db=db, skip=0, limit=15, descending=False, count_results=False, user_id=i.id)
            i.specialities = arr

        return data


doctors_search_service = DoctorSearchService(User, doctors_search_repo)
