from typing import List
from fastapi import APIRouter, Depends
from exceptions.service_result import handle_result
from schemas import PatientFamilyOut, PatientFamilyReuest, PatientFamilyIn
from sqlalchemy.orm import Session
from db import get_db
from api.v1.auth_dependcies import logged_in_patient
from services import patient_families_service



router = APIRouter()

@router.get('/', response_model=List[PatientFamilyOut])
def all_family_member_data(db: Session = Depends(get_db), current_user: Session = Depends(logged_in_patient)):
    member = patient_families_service.search_by_user_id(db=db,user_id=current_user.id)
    return handle_result(member)

@router.post('/', response_model=PatientFamilyOut)
def reuest_family_members(data_in: PatientFamilyReuest ,db: Session = Depends(get_db), current_user: Session = Depends(logged_in_patient)):
    data_with_user = PatientFamilyIn(user_id=current_user.id, relationship_status='pending',  **data_in.dict())
    service = patient_families_service.create(db=db, data_in=data_with_user)
    return handle_result(service)

@router.get('/pending', response_model=List[PatientFamilyOut])
def pending_request(db: Session=Depends(get_db), current_user: Session = Depends(logged_in_patient)):
    data = patient_families_service.member_status(db=db, user_id=current_user.id, relationship_status='pending')
    return handle_result(data)

@router.patch('/accept', response_model=PatientFamilyOut, description="<b>Accepted relationship_status: </b>accepted, pending, reject")
def update_relationship_status(id: int, relationship_status: str, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_patient)):
    update = patient_families_service.update_relationship_status(db=db, id=id, user_id=current_user.id, relationship_status=relationship_status)
    return handle_result(update)