from typing import List, Union
from fastapi import APIRouter, Depends
from db import get_db
from exceptions.service_result import handle_result
from schemas import *
# from schemas import UserOut, UserOutAuth, UserCreate, UserDoctorOut,  DoctorSignup, DoctorChamberOut, UserCreateWitoutRole, AdminPanelActivityOut, AdminPanelActivityAllOut, PatientIndicatorBase, NewPasswordIn, AdminPanelActivityOut, PatientIndicatorOut, HealthPartnerIn, HealthPartnerOut, ResultInt, AdminPatientsOut, DoctorUpdate, DoctorSpecialityUpdate, DoctorQualilficationUpdate, DoctorWorkPlaceUpdate, ImageLogIn, ImageLogOut, DoctorQualificationOut, DoctorSpecialityOut, DoctorWorkPlaceOut
from sqlalchemy.orm import Session
from schemas.doctors import DoctorOut
from schemas.users import LoginLogLogout, UserUpdate
from services import admin_service, doctors_service, doctor_chambers_service, patient_indicators_service, health_partner_service, login_log_services, doctor_qualifications_service, doctor_specialities_service, doctor_workplace_service, image_log_service, users_service
from api.v1.auth_dependcies import logged_in, logged_in_admin, logged_in_employee, logged_in_moderator, logged_in_medical_affairs
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from utils import UploadFileUtils


router = APIRouter()


@router.post('/', response_model=UserOut)
def signup(data_in: UserCreateWitoutRole, db: Session = Depends(get_db)):
    admn = admin_service.signup_admin(db, data_in=data_in)
    return handle_result(admn)


@router.post('/password', response_model=AdminPanelActivityOut)
def password_change_by_admin(user_id: int, password: NewPasswordIn, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_moderator)):
    change_password = admin_service.password_changed_by_admin(db=db, user_id=user_id, password=password, changer_id=current_user.id)
    return handle_result(change_password)


@router.patch('/role-change', response_model=AdminPanelActivityOut)
def role_change_by_admin(id: int, role_name: str,  db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin)):
    change = admin_service.role_change(db=db, id=id, user_id=current_user.id, role_name=role_name)
    return handle_result(change)


@router.patch('/switch/active/{id}', response_model=UserOut)
def user_active_switcher(id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_moderator)):
    act = admin_service.user_active_switcher(db=db, id=id)
    return handle_result(act)


@router.get('/activity/log/all', response_model=List[Union[ResultInt, List[AdminPanelActivityAllOut]]])
def activity_log(skip: int = 0, limit: int = 15, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    activity = admin_service.activity_log_all(db=db, skip=skip, limit=limit)
    return handle_result(activity)


@router.get('/activity/log/{user_id}', response_model=List[Union[ResultInt, List[AdminPanelActivityOut]]])
def activity_log(user_id: int, skip: int = 0, limit: int = 15, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    activity = admin_service.activity_log(db=db, user_id=user_id, skip=skip, limit=limit)
    return handle_result(activity)


@router.get('/activity/log', response_model=List[Union[ResultInt, List[AdminPanelActivityOut]]])
def activity_log(skip: int = 0, limit: int = 15, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    activity = admin_service.activity_log(db=db, user_id=current_user.id, skip=skip, limit=limit)
    return handle_result(activity)


@router.get('/activity/log/service/{user_id}/{service_name}', response_model=List[Union[ResultInt, List[AdminPanelActivityOut]]], response_description="<b>service_name: patient_register</b>")
def actirvity_log_service(user_id: int, service_name: str = 'patient_register', skip: int = 0, limit: int = 15, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    actvity_user_service = admin_service.get_user_id_service(db=db, user_id=user_id, service_name=service_name, skip=skip, limit=limit)
    return handle_result(actvity_user_service)


@router.get('/login-log', response_model=List[Union[ResultInt, List[LoginLogLogout]]])
def all_login_log(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), currenct_user: Session = Depends(logged_in_employee)):
    l_log = login_log_services.all_log_with_user(db=db, skip=skip, limit=limit)
    return handle_result(l_log)
# Admin for employee


@router.get('/employee/all', response_model=List[Union[ResultInt, List[UserOutAuth]]])
def all_employee(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    all = admin_service.all_employee(db, skip=skip, limit=limit)
    return handle_result(all)


@router.get('/employee/deactive', response_model=List[Union[ResultInt, List[UserOutAuth]]])
def all_employee(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    all = admin_service.deactive_employee(db, skip=skip, limit=limit)
    return handle_result(all)


@router.post('/employee/create', response_model=AdminPanelActivityOut)
def empployee_create(data_in: UserCreate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_moderator)):
    employee_created = admin_service.signup_employee(db, data_in=data_in, creator_id=current_user.id)
    return handle_result(employee_created)


# Admin for health partner
@router.get('/health-partner/all', response_model=List[HealthPartnerOut])
def health_partner_all(db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    health_partner = health_partner_service.get(db=db)
    return handle_result(health_partner)


@router.get('/health-partner/{id}', response_model=HealthPartnerOut)
def health_partner(id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    health_partner = health_partner_service.get_one(db=db, id=id)
    return handle_result(health_partner)


@router.post('/health-partner/create', response_model=HealthPartnerOut)
def health_partner_create(data_in: HealthPartnerIn, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin)):
    health_partner = health_partner_service.create(db=db, data_in=data_in)
    return handle_result(health_partner)


# Admin for doctors


@router.post('/doctor/register', response_model=AdminPanelActivityOut, description='<b>access:</b> admin and medical affairs')
def doctor_register(data_in: DoctorSignup, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_medical_affairs)):
    doctor_reg = admin_service.doctor_register(db=db, data_in=data_in, creator_id=current_user.id)
    return handle_result(doctor_reg)


@router.get('/doctors/active', response_model=List[Union[ResultInt, List[UserDoctorOut]]])
def doctors_active_list(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    docs = admin_service.doctor_active_list(db, skip=skip, limit=limit)
    return handle_result(docs)


@router.get('/doctors/inactive', response_model=List[Union[ResultInt, List[UserDoctorOut]]])
def doctors_inactive_list(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    docs = admin_service.doctor_inactive_list(db, skip=skip, limit=limit)
    return handle_result(docs)


@router.put('/doctor/activate', response_model=UserOut)
def doctor_active(id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_moderator)):
    doc = admin_service.doctor_active_id(db=db, id=id)
    return handle_result(doc)


@router.get('/doctor/chambers/{user_id}', response_model=List[DoctorChamberOut])
def chamber_list(user_id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_moderator)):
    chambers = doctor_chambers_service.get_by_user_id(db=db, user_id=user_id)
    return handle_result(chambers)


@router.patch('/doctor/user/update/{id}', response_model=UserOut)
def user_update(id: int, data_update: UserUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_medical_affairs)):
    data = users_service.update(db=db, id=id, data_update=data_update)
    return handle_result(data)


@router.patch('/doctor/update/{user_id}', response_model=DoctorOut)
def doctor_update(user_id: int, data_update: DoctorUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_medical_affairs)):
    doc_up = doctors_service.edit_by_user_id(db=db, data_update=data_update, user_id=user_id)
    return handle_result(doc_up)


@router.patch('/doctor/qualification/update/{id}', response_model=DoctorQualificationOut)
def qualification_update(id: int, data_update: DoctorQualilficationUpdate, db: Session = Depends(get_db), curren_user: Session = Depends(logged_in_medical_affairs)):
    data = doctor_qualifications_service.update(db=db, id=id, data_update=data_update)
    return handle_result(data)


@router.patch('/doctor/speciality/update/{id}', response_model=DoctorSpecialityOut)
def speciality_update(id: int, data_update: DoctorSpecialityUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_medical_affairs)):
    data = doctor_specialities_service.update(db=db, id=id, data_update=data_update)
    return handle_result(data)


@router.patch('/doctor/workplace/update/{id}', response_model=DoctorWorkPlaceOut)
def doctor_workplace_update(id: int, data_update: DoctorWorkPlaceUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_medical_affairs)):
    data = doctor_workplace_service.update(db=db, id=id, data_update=data_update)
    return handle_result(data)


@router.post('/doctor/workplace/create', response_model=DoctorWorkPlaceOut)
def doctor_workplace_create(data_in: DoctorWorkPlaceWithUser, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_medical_affairs)):
    create = doctor_workplace_service.create(db=db, data_in=data_in)
    return handle_result(create)


@router.patch('/workplace/priority/{id}/{user_id}')
def priority(id: int, user_id: int,  db: Session = Depends(get_db), current_user: Session = Depends(logged_in_medical_affairs)):
    up = doctor_workplace_service.workplace_priority_set(db=db, id=id, user_id=user_id)
    return handle_result(up)


@router.post('/profile-pic/{user_id}', response_model=ImageLogOut, description='<h2>Alert: </h2> <b>image should be < 300 kb</b>')
async def upload_image(user_id: int, file: UploadFile = File(...), db: Session = Depends(get_db), current_user: Session = Depends(logged_in_medical_affairs)):

    up_img = UploadFileUtils(file=file)

    # prefix is the short service name
    new_image_name = up_img.upload_image(prefix='propic', path='./assets/img/profile', accepted_extensions=['jpg', 'jpeg', 'png'])

    # save in db
    image_in_db = image_log_service.create(db=db, data_in=ImageLogIn(user_id=user_id, service_name='propic', image_string=new_image_name))

    return handle_result(image_in_db)


@router.get('/profile-pic/{user_id}', response_model=ImageLogOut, description='<h2>Alert: images/profile/(image url)</b>')
def get_profile_pic(user_id: int, db: Session = Depends(get_db)):
    pp = image_log_service.last_profile_pic(db=db, user_id=user_id)
    return handle_result(pp)


# Admin for patient
@router.post('/patient/create', response_model=AdminPanelActivityOut)
def register_patient(data_in: UserCreate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    patient_created = admin_service.signup_patient(db=db, data_in=data_in, creator_id=current_user.id)
    return handle_result(patient_created)


@router.patch('/patient/user/update/{id}', response_model=AdminPanelActivityOut)
def edit_user(id: int, data_update: UserUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_employee)):
    adm = admin_service.patient_user_update(db=db, id=id, user_id=current_user.id, data_update=data_update)
    return handle_result(adm)


@router.get('/patient/all', response_model=List[Union[ResultInt, List[AdminPatientsOut]]])
def all_patients(phone_number: str = None, skip: int = 0, limit: int = 15,  db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    patients = admin_service.all_patient(db=db, phone_number=phone_number, skip=skip, limit=limit)
    return handle_result(patients)


@router.get('/user/filter', response_model=List[Union[ResultInt, List[AdminPatientsOut]]])
def all_patient_filter(
        hx_user_id: int = None, name: str = None, phone: str = None, gender: str = None, skip: int = 0, limit: int = 15, db: Session = Depends(get_db),
        current_user: Session = Depends(logged_in)):
    data = admin_service.all_patient_filter(db=db,  hx_user_id=hx_user_id, name=name, phone=phone, gender=gender, skip=skip, limit=limit)
    return handle_result(data)


@router.post('/patient/indicator', response_model=AdminPanelActivityOut)
def patient_indicator(user_id: int, data_in: PatientIndicatorBase, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    indicator = admin_service.patient_indicators(db=db, user_id=user_id, data_in=data_in, creator_id=current_user.id)
    return handle_result(indicator)


@router.get('/patient/indicator/{key}/{user_id}', response_model=List[PatientIndicatorOut])
def patient_indicator_get(key: str, user_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    indicators = patient_indicators_service.get_by_key(db=db, key=key, user_id=user_id, skip=skip, limit=limit)
    return handle_result(indicators)


# Pharmacy

@router.patch('/switch/active/pharmacy/{id}', response_model=AdminPanelActivityOut)
def pharmacy_active_switcher(id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_moderator)):
    act = admin_service.pharmacy_active_switcher(db=db, id=id, creator_id=current_user.id)
    return handle_result(act)


@router.get('/active-pharmacy', response_model=List[Union[ResultInt, List[PharmacyOut]]])
def active_pharmacy(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    ap = admin_service.pharmacy_active_list(db=db, skip=skip, limit=limit)
    return handle_result(ap)


@router.get('/inactive-pharmacy', response_model=List[Union[ResultInt, List[PharmacyOut]]])
def inactive_pharmacy(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    inap = admin_service.pharmacy_inactive_list(db=db, skip=skip, limit=limit)
    return handle_result(inap)


# CLinic

@router.patch('/switch/active/clinic/{id}', response_model=AdminPanelActivityOut)
def clinic_active_switcher(id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_moderator)):
    active = admin_service.clinic_active_switcher(db=db, id=id, creator_id=current_user.id)
    return handle_result(active)


@router.get('/active-clinic', response_model=List[Union[ResultInt, List[ClinicOut]]])
def active_clinic(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    ac = admin_service.clinic_active_list(db=db, skip=skip, limit=limit)
    return handle_result(ac)


@router.get('/inactive-clinic', response_model=List[Union[ResultInt, List[ClinicOut]]])
def inactive_clinic(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    inac = admin_service.clinic_inactive_list(db=db, skip=skip, limit=limit)
    return handle_result(inac)
