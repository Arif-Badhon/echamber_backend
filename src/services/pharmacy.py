from services import BaseService
from models import Pharmacy
from schemas import PharmacyIn, PharmacyUpdate, UserCreate, PharmacyUserIn, PharmacyUserWithPharmacy, PharmacyLogin
from repositories import pharmacy_repo
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
        trade_license_detail = self.search_by_trade_license(db=db, trade_license=data_in.trade_license)
        trade_license_id = handle_result(trade_license_detail)
        print(trade_license_id)

        p = users_service.login(db=db, identifier=data_in.identifier, password=data_in.password)
        return p

    def search_by_trade_license(self, db: Session, trade_license: str):
        trade = self.repo.search_by_trade_license(db=db, trade_license=trade_license)
        if not trade:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        else:
            return ServiceResult(trade, status_code=status.HTTP_200_OK)


pharmacy_service = PharmacyService(Pharmacy, pharmacy_repo)
