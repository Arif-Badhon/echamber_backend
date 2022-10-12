from exceptions.app_exceptions import AppException
from services import BaseService
from models import Pharmacy
from schemas import PharmacyIn, PharmacyUpdate, UserCreate, PharmacyUserIn, PharmacyUserWithPharmacy, PharmacyLogin
from repositories import pharmacy_repo, users_repo
from sqlalchemy.orm import Session
from .users import users_service
from .pharmacy_user import pharmacy_user_service
from .users import users_service
from exceptions.service_result import ServiceResult, handle_result
from fastapi import status


class PharmacyService(BaseService[Pharmacy, PharmacyIn, PharmacyUpdate]):

    def register_pharmacy(self, db: Session, data_in: PharmacyUserWithPharmacy):
        admin_signup = UserCreate(
            name=data_in.user.name,
            email=data_in.user.email,
            phone=data_in.user.phone,
            sex=data_in.user.sex,
            is_active=True,
            password=data_in.user.password,
            role_name='pharmacy_admin'
        )

        tr_license = self.repo.get_by_key(db=db, skip=0, limit=100, descending=False, count_results=True, trade_license=data_in.pharmacy.trade_license)
        # print(tr_license[0]["results"])
        if tr_license[0]["results"] != 0:
            return ServiceResult(AppException.ServerError("Trade License Already Registered"))

        signup = users_service.signup(db=db, data_in=admin_signup, flush=True)

        pharma = self.create_with_flush(db=db, data_in=PharmacyIn(
            name=data_in.pharmacy.name,
            trade_license=data_in.pharmacy.trade_license,
            detail_address=data_in.pharmacy.detail_address,
            district=data_in.pharmacy.district,
            sub_district=data_in.pharmacy.sub_district,
            drug_license=data_in.pharmacy.drug_license,
            pharmacy_is_active=data_in.pharmacy.pharmacy_is_active
        ))

        pharma_user = pharmacy_user_service.create(db=db, data_in=PharmacyUserIn(user_id=handle_result(signup).id, pharmacy_id=handle_result(pharma).id))
        return pharma_user

    def pharmacy_user_login(self, db: Session, data_in: PharmacyLogin):
        pharmacy_by_trade_license = self.search_by_trade_license(db=db, trade_license=data_in.trade_license)
        pharmacy_id = handle_result(pharmacy_by_trade_license).id
    

        user_from_identifier = None
        user_email = users_repo.search_by_email(db=db, email_in=data_in.identifier)
        user_phone = users_repo.search_by_phone(db=db, phone_in=data_in.identifier)
        if user_email != None:
            user_from_identifier = user_email
        if user_phone != None:
            user_from_identifier = user_phone


        ph_check = pharmacy_user_service.get_by_two_key(db=db, skip=0, limit=100, descending=False, count_results=False, user_id=user_from_identifier.id, pharmacy_id=pharmacy_id)
        ph_with_user = handle_result(ph_check)

        if len(ph_with_user) == 0:
            return ServiceResult(AppException.ServerError("Invalid pharmacy trade license or user."))



        return users_service.login(db=db, identifier=data_in.identifier, password=data_in.password)

    def check_user_with_pharmacy(self, db: Session, user_id:int, pharmacy_id:int):
        check = pharmacy_user_service.get_by_two_key(db=db, skip=0, limit=100, descending=False, count_results=False, user_id=user_id, pharmacy_id=pharmacy_id)
        check_user_ph_id = handle_result(check)
        

        if len(check_user_ph_id) == 1:
            return True
        else:
            return False

    def find_pharmacy_with_user_id(self, db: Session, user_id: int):
        find = pharmacy_user_service.get_by_key(db=db, skip=0, limit=100, descending=False, count_results=False, user_id=user_id)
        find_user = handle_result(find)
        if len(find_user) == 0:
            return ServiceResult(AppException.ServerError("Not Pharmacy User"))
        else:
            pharmacy_id = handle_result(find)[0].pharmacy_id
            return pharmacy_service.get_one(db=db, id=pharmacy_id)



    def search_by_trade_license(self, db: Session, trade_license: str):
        trade = self.repo.search_by_trade_license(db=db, trade_license=trade_license)
        if not trade:
            return ServiceResult(AppException.ServerError("Pharmacy not found"))
        else:
            return ServiceResult(trade, status_code=status.HTTP_200_OK)


pharmacy_service = PharmacyService(Pharmacy, pharmacy_repo)
