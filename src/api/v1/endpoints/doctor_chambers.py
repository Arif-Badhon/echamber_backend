from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.v1.auth_dependcies import get_db, logged_in_doctor, logged_in_medical_affairs
from exceptions import handle_result
from services import doctor_chambers_service
from schemas import DoctorChamberOut, DoctorChamberBase, DoctorChamberUpdate

router = APIRouter()


@router.get('/active')
def active_chamber(db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    current_user_id = current_user.id
    act = doctor_chambers_service.currently_active_chamber(
        db=db, user_id=current_user_id)
    return handle_result(act)


@router.get('/', response_model=List[DoctorChamberOut])
def get(db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    doc_chamber = doctor_chambers_service.get_by_key(db=db, skip=0, limit=100, descending=False, count_results=False, user_id=current_user.id)
    return handle_result(doc_chamber)


@router.get('/{id}', response_model=DoctorChamberOut)
def detail(id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    chamber = doctor_chambers_service.get_one(db, id)
    return handle_result(chamber)


@router.post('/', response_model=DoctorChamberOut)
def post(chamber_in: DoctorChamberBase, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    chamber_register = doctor_chambers_service.create_with_user_id(
        db, data_in=chamber_in, user_id=current_user.id)
    return handle_result(chamber_register)


@router.put('/{id}', response_model=DoctorChamberOut)
def edit(id: int, data_update: DoctorChamberUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    update_chamber = doctor_chambers_service.update(
        db, id, data_update=data_update)
    return handle_result(update_chamber)


@router.put('/activate/{id}', response_model=List[DoctorChamberOut])
def active(id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    actv = doctor_chambers_service.active_chamber(
        db, id, user_id=current_user.id)
    return handle_result(actv)


@router.delete('/{id}')
def remove(id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    remove_chamber = doctor_chambers_service.delete(db, id)
    return handle_result(remove_chamber)


@router.get('doctor-chambers/{doctor_user_id}', response_model=List[DoctorChamberOut])
def get(doctor_user_id: int, db: Session = Depends(get_db)):
    doc_chamber = doctor_chambers_service.get_by_key(db=db, skip=0, limit=100, descending=False, count_results=False, user_id=doctor_user_id)
    return handle_result(doc_chamber)


@router.post('created_by/medical_affairs/{doctor_id}', response_model=DoctorChamberOut)
def chamber_created_by_admin_panel(doctor_id: int, chamber_in: DoctorChamberBase, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_medical_affairs)):
    data = doctor_chambers_service.create_with_user_id(db=db, data_in=chamber_in, user_id=doctor_id)
    return handle_result(data)
