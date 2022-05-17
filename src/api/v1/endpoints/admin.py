from typing import List
from fastapi import APIRouter, Depends
from db import get_db
from exceptions.service_result import handle_result
from schemas import UserOut, UserOutAuth, UserCreate, UserDoctorOut, DoctorChamberOut, UserCreateWitoutRole, AdminPanelActivityOut, PatientIndicatorBase, NewPasswordIn, AdminPanelActivityOut, PatientIndicatorOut
from sqlalchemy.orm import Session
from services import admin_service, doctor_chambers_service, patient_indicators_service
from api.v1.auth_dependcies import logged_in, logged_in_admin, logged_in_admin_moderator, logged_in_moderator


router = APIRouter()


@router.post('/', response_model=UserOut)
def signup(data_in: UserCreateWitoutRole, db: Session = Depends(get_db)):
    admn = admin_service.signup_admin(db, data_in=data_in)
    return handle_result(admn)

@router.post('/password', response_model=AdminPanelActivityOut)
def password_change_by_admin(user_id:int, password: NewPasswordIn ,db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin_moderator)):
    change_password = admin_service.password_changed_by_admin(db=db, user_id=user_id, password=password, changer_id=current_user.id)
    return handle_result(change_password)


@router.get('/activity/log', response_model=List[AdminPanelActivityOut])
def activity_log(skip:int=0, limit:int=15, db:Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    activity = admin_service.activity_log(db=db, user_id=current_user.id, skip=skip, limit=limit)
    return handle_result(activity)


@router.get('/activity/log/{user_id}}', response_model=List[AdminPanelActivityOut])
def activity_log( user_id: int, skip:int=0, limit:int=15, db:Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    activity = admin_service.activity_log(db=db, user_id=user_id, skip=skip, limit=limit)
    return handle_result(activity)


# Admin for employee

@router.get('/employee/all', response_model=List[UserOutAuth])
def all_employee(skip:int=0, limit:int=10, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    all = admin_service.all_employee(db, skip=skip, limit=limit)
    return handle_result(all)


@router.post('/employee/create', response_model=AdminPanelActivityOut)
def empployee_create(data_in: UserCreate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin_moderator)):
    employee_created = admin_service.signup_employee(db, data_in=data_in, creator_id=current_user.id)
    return handle_result(employee_created)


# Admin for doctors

@router.get('/doctors/active', response_model=List[UserDoctorOut])
def doctors_active_list(skip:int = 0, limit:int = 10, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    docs = admin_service.doctor_active_list(db, skip=skip, limit=limit)
    return handle_result(docs)


@router.get('/doctors/inactive', response_model=List[UserDoctorOut])
def doctors_inactive_list(skip:int = 0, limit:int = 10, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin_moderator)):
    docs = admin_service.doctor_inactive_list(db, skip=skip, limit=limit)
    return handle_result(docs)


@router.put('/doctor/activate', response_model=UserOut)
def doctor_active(id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin_moderator)):
    doc = admin_service.doctor_active_id(db=db, id=id)
    return handle_result(doc)


@router.get('/doctor/chambers/{user_id}',response_model=List[DoctorChamberOut])
def chamber_list(user_id :int,db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin_moderator)):
    chambers =  doctor_chambers_service.get_by_user_id(db=db, user_id=user_id)
    return handle_result(chambers)


# Admin for patient

@router.post('/patient/create', response_model=AdminPanelActivityOut)
def register_patient(data_in: UserCreate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    patient_created = admin_service.signup_patient(db=db, data_in=data_in, creator_id=current_user.id)
    return handle_result(patient_created)


@router.get('/patient/all', response_model=List[UserOut])
def all_patients(phone_number: str, skip:int=0, limit:int=15,  db:Session=Depends(get_db), current_user:Session=Depends(logged_in)):
    patients = admin_service.all_patient(db=db, phone_number=phone_number, skip=skip, limit=limit)
    return handle_result(patients)


@router.post('/patient/indicator', response_model=AdminPanelActivityOut)
def patient_indicator(user_id: int, data_in: PatientIndicatorBase, db:Session=Depends(get_db), current_user:Session=Depends(logged_in)):
    indicator = admin_service.patient_indicators(db=db, user_id=user_id, data_in=data_in, creator_id=current_user.id)
    return handle_result(indicator)

@router.get('/patient/indicator/{key}/{user_id}', response_model=List[PatientIndicatorOut])
def patient_indicator_get(key:str, user_id: int, db: Session = Depends(get_db), current_user:Session = Depends(logged_in)):
    indicators = patient_indicators_service.get_by_key(db=db, key=key, user_id=user_id)
    return handle_result(indicators)


