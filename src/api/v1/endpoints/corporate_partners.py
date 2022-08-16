from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.db_session import get_db
from api.v1.auth_dependcies import logged_in, logged_in_admin, logged_in_moderator
from exceptions.service_result import handle_result
from schemas import CorporatePartnerOut, CorporatePartnerIn, CorporatePartnerUserOut, CorporatePartnerUserIn
from services import corporate_partners_service, corporate_partner_user_service


router = APIRouter()


@router.get('/', response_model=List[CorporatePartnerOut])
def all_partners(db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    data = corporate_partners_service.get(db=db)
    return handle_result(data)


@router.post('/', response_model=CorporatePartnerOut)
def register(data_in: CorporatePartnerIn, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin)):
    register = corporate_partners_service.create(db=db, data_in=data_in)
    return handle_result(register)


@router.post('/user', response_model=CorporatePartnerUserOut)
def append(data_in: CorporatePartnerUserIn, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_moderator)):
    append = corporate_partner_user_service.create(db=db, data_in=data_in)
    return handle_result(append)
