from services import BaseService
from models import Pharmaceuticals
from schemas import PharmaceuticalIn, PharmaceuticalUpdate, UserCreate, PharmaecuticalsUserIn, PharmaceuticalUserWithPhr
from repositories import pharmaceuticals_repo
from sqlalchemy.orm import Session
from .users import users_service
from .pharmaceuticals_user import pharmaceuticals_user_service
from exceptions.service_result import handle_result
from fastapi import status
from exceptions import ServiceResult

class PharmaceuticalsService(BaseService[Pharmaceuticals, PharmaceuticalIn, PharmaceuticalUpdate]):

    def register_pharmaceuticals(self, db: Session, data_in: PharmaceuticalUserWithPhr):
        admin_signup = UserCreate(
            name = data_in.user.name,
            email = data_in.user.email,
            phone = data_in.user.phone,
            sex = data_in.user.sex,
            is_active = True,
            password = data_in.user.password,
            role_name = 'pharmaceuticals_admin' 
        )

        signup = users_service.signup(db = db, data_in = admin_signup, flush = True)

        phr = self.create_with_flush(db = db, data_in= PharmaceuticalIn(
            name = data_in.pharmaceuticals.name,
            established = data_in.pharmaceuticals.established,
            details = data_in.pharmaceuticals.details,
            contact_phone = data_in.pharmaceuticals.contact_phone,
            contact_email =  data_in.pharmaceuticals.contact_email,
            address = data_in.pharmaceuticals.address,
            total_generics = data_in.pharmaceuticals.total_generics,
            total_brands = data_in. pharmaceuticals. total_brands,
            contact_person = data_in.pharmaceuticals.contact_person,
            contact_person_phone = data_in.pharmaceuticals.contact_person_phone,
            contact_person_email = data_in.pharmaceuticals.contact_person_email
        ))

        phr_user = pharmaceuticals_user_service.create(db = db, data_in = PharmaecuticalsUserIn(user_id = handle_result(signup).id, phr_id = handle_result(phr).id))
        return phr_user

    def all_pharmaceuticals(self, db: Session, skip: int, limit: int):
        data = self.repo.all_pharmaceuticals(db=db, skip=skip, limit=limit)

        if not data:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        else:
            return ServiceResult(data, status_code=status.HTTP_200_OK)

    def search_pharmaceuticals(self, db: Session, pharmaceuticals: str):
        data = self.repo.search_pharmaceuticals(db=db, pharmaceuticals=pharmaceuticals)

        if not data:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        else:
            return ServiceResult(data, status_code=status.HTTP_200_OK)

pharmaceutical_service = PharmaceuticalsService(Pharmaceuticals, pharmaceuticals_repo)