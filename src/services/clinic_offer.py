from services import BaseService, clinic_with_doctor_service
from models import ClinicOffer
from schemas import ClinicOfferIn, ClinicOfferUpdate, ClinicOfferBase
from repositories import clinic_offer_repo
from sqlalchemy.orm import Session
from exceptions.service_result import handle_result
from exceptions import ServiceResult, AppException


class ClinicOfferService(BaseService[ClinicOffer, ClinicOfferIn, ClinicOfferUpdate]):

    def add_clinic_offer(self, db: Session, data_in: ClinicOfferBase, user_id: int):

        clinic_offer = self.create_with_flush(db=db, data_in=ClinicOfferIn(
            clinic_id=data_in.clinic_id,
            offer_name=data_in.offer_name,
            offer_details=data_in.offer_details,
            offer_price= data_in.offer_price,
            image_id=data_in.image_id
        ))

        clinic_with_user = clinic_with_doctor_service.check_user_with_clinic(db=db, user_id=user_id, clinic_id=handle_result(clinic_offer).clinic_id)
        if clinic_with_user == False:
            return ServiceResult(AppException.ServerError("Invalid Clinic ID"))

        db.commit()
        return ServiceResult({"msg": "Success"}, status_code=200)

    
    def get_clinic_offer_by_clinic_id(self, db: Session, clinic_id: int):

        clinic_offer = self.repo.get_clinic_offer_by_clinic_id(db=db, clinic_id=clinic_id)
        return clinic_offer

clinic_offer_service = ClinicOfferService(ClinicOffer, clinic_offer_repo)