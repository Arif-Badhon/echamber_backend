from pickletools import read_uint1
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from exceptions import handle_result
from schemas import DoctorOut, DoctorUpdate, DoctorSpecialityOut, DoctorAcademicInfoIn, DoctorAcademicInfoOut, DoctorAcademicInfoUpdate, DoctorAcademicInfoWithUser, DoctorQualificationBase, DoctorQualificationOut, DoctorSpecialityBase, DoctorSpecialityIn, DoctorSpecialityOut, DoctorQualilficationUpdate, DoctorSpecialityUpdate, DoctorSignup, UserOut, UserOutAuth, DoctorDetails, DoctorWorkPlaceOut, DoctorWorkPlaceIn, DoctorWorkPlaceWithUser, DoctorWorkPlaceUpdate, DoctorTrainingExpOut, DoctorTrainingExpUpdate, DoctorTrainingExpIn, DoctorTrainingExpInWithUser, DoctorProfessionalMembershipIn, DoctorProfessionalMembershipInWithUser, DoctorProfessionalMembershipOut, DoctorOthersActivityIn, DoctorOthersActivityWithUser, DoctorOthersActivityUpdate, DoctorOthersActivityOut
from schemas.admin import ResultInt
from schemas.doctor_professional_membership import DoctorProfessioanlMembershipUpdate
from schemas.doctor_qualifications import DoctorQualificationBase, DoctorQualilficationIn
from services import doctors_service, doctor_qualifications_service, doctor_specialities_service, doctor_workplace_service, doctor_academic_info_service, doctor_training_exp_services, doctor_professional_membership_service, doctor_others_activity_service
from api.v1.auth_dependcies import logged_in_doctor
from typing import List, Union


router = APIRouter()


@router.post('/signup', response_model=UserOut)
def signup(doctor_in: DoctorSignup, db: Session = Depends(get_db)):
    doctor = doctors_service.signup(db, data_in=doctor_in)
    return handle_result(doctor)


@router.get('/auth', response_model=UserOutAuth)
def auth(doctor: Session = Depends(logged_in_doctor)):
    return doctor


@router.get('/', response_model=DoctorOut)
def get_doctor(db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    doc = doctors_service.get_by_user_id(db=db, user_id=current_user.id)
    return handle_result(doc)


@router.patch('/', response_model=DoctorOut)
def edit(data_update: DoctorUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    data = doctors_service.edit_by_user_id(db=db, data_update=data_update, user_id=current_user.id)
    return handle_result(data)


@router.get('/detail/{id}', response_model=DoctorDetails)
def detail(id: int, db: Session = Depends(get_db)):
    data = doctors_service.details(db=db, id=id)
    return data


@router.get('/all/docs', response_model=List[Union[ResultInt, List[UserOut]]])
def all_docs(skip: int = 0, limit: int = 15, db: Session = Depends(get_db)):
    docs = doctors_service.all_doc(db=db, skip=skip, limit=limit)
    return handle_result(docs)


@router.post('/qualifications', response_model=DoctorQualificationOut)
def create(data_in: DoctorQualificationBase, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    qualification = doctor_qualifications_service.create(db=db, data_in=DoctorQualilficationIn(user_id=current_user.id, **data_in.dict()))
    return handle_result(qualification)


@router.get('/qualifications', response_model=DoctorQualificationOut)
def get(db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    qualification = doctor_qualifications_service.get_by_user_id(
        db, user_id=current_user.id)
    return handle_result(qualification)


@router.put('/qualifications/{id}', response_model=DoctorQualificationOut)
def update(id: int, data_update: DoctorQualilficationUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    qualification = doctor_qualifications_service.update(db, id, data_update)
    return handle_result(qualification)


@router.post('/specialities', response_model=DoctorSpecialityOut)
def create(data_in: DoctorSpecialityBase, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    speciality = doctor_specialities_service.create(db=db, data_in=DoctorSpecialityIn(user_id=current_user.id, **data_in.dict()))
    return handle_result(speciality)


@router.get('/specialities', response_model=DoctorSpecialityOut)
def get(db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    speciality = doctor_specialities_service.get_by_user_id(
        db, user_id=current_user.id)
    return handle_result(speciality)


@router.put('/specialities/{id}', response_model=DoctorSpecialityOut)
def update(id: int, data_update: DoctorSpecialityUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    speciality = doctor_specialities_service.update(db, id, data_update)
    return handle_result(speciality)


@router.post('/workplace', response_model=DoctorWorkPlaceOut)
def create(data_in: DoctorWorkPlaceIn, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    data = doctor_workplace_service.create(db=db, data_in=DoctorWorkPlaceWithUser(user_id=current_user.id, **data_in.dict()))
    return handle_result(data)


@router.get('/workplace/{user_id}', response_model=List[DoctorWorkPlaceOut])
def get(user_id: int, skip: int = 0, limit: int = 30, db: Session = Depends(get_db)):
    workplace = doctor_workplace_service.get_by_key(db=db, skip=skip, limit=limit, descending=False, count_results=False, user_id=user_id)
    return handle_result(workplace)


@router.patch('/workplace/{id}', response_model=DoctorWorkPlaceOut)
def update(id: int, data_update: DoctorWorkPlaceUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    edit = doctor_workplace_service.update(db=db, id=id, data_update=data_update)
    return handle_result(edit)


@router.delete('/workplace/{id}')
def remove(id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    delete = doctor_academic_info_service.delete(db=db, id=id)
    return delete


@router.post('/academic', response_model=DoctorAcademicInfoOut)
def post(data_in: DoctorAcademicInfoIn, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    data = doctor_academic_info_service.create(db=db, data_in=DoctorAcademicInfoWithUser(user_id=current_user.id, **data_in.dict()))
    return handle_result(data)


@router.get('/academic/{user_id}', response_model=List[DoctorAcademicInfoOut])
def get(user_id: int, skip: int = 0, limit: int = 30, db: Session = Depends(get_db)):
    all = doctor_academic_info_service.get_by_key(db=db, skip=skip, limit=limit, descending=False, count_results=False, user_id=user_id)
    return handle_result(all)


@router.patch('/academic/{id}', response_model=DoctorAcademicInfoOut)
def edit(id: int, data_update: DoctorAcademicInfoUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    up = doctor_academic_info_service.update(db=db, id=id, data_update=data_update)
    return handle_result(up)


@router.delete('/academic/{id}')
def remove(id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    delete = doctor_academic_info_service.delete(db=db, id=id)
    return delete


@router.post('/training/', response_model=DoctorTrainingExpOut)
def create(data_in: DoctorTrainingExpIn, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    tr = doctor_training_exp_services.create(db=db, data_in=DoctorTrainingExpInWithUser(**data_in.dict(), user_id=current_user.id))
    return handle_result(tr)


@router.get('/training/{user_id}', response_model=List[Union[ResultInt, List[DoctorTrainingExpOut]]])
def all_training(user_id: int, skip: int = 0, limit: int = 15, db: Session = Depends(get_db)):
    all = doctor_training_exp_services.get_by_key(db=db, skip=skip, limit=limit, descending=False, count_results=True, user_id=user_id)
    return handle_result(all)


@router.patch('/training/{id}', response_model=DoctorTrainingExpOut)
def update(id: int, data_up: DoctorTrainingExpUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    up = doctor_training_exp_services.update(db=db, id=id, data_update=data_up)
    return handle_result(up)


@router.delete('/training/{id}')
def remove(id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    dl = doctor_training_exp_services.delete(db=db, id=id)
    return handle_result(dl)


@router.post('/membership/', response_model=DoctorProfessionalMembershipOut)
def create(data_in: DoctorProfessionalMembershipIn, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    mm = doctor_professional_membership_service.create(db=db, data_in=DoctorProfessionalMembershipInWithUser(**data_in.dict(), user_id=current_user.id))
    return handle_result(mm)


@router.get('/membership/{user_id}', response_model=List[Union[ResultInt, List[DoctorProfessionalMembershipOut]]])
def all_membership(user_id: int, skip: int = 0, limit: int = 15, db: Session = Depends(get_db)):
    all = doctor_professional_membership_service.get_by_key(db=db, skip=skip, limit=limit, descending=False, count_results=True, user_id=user_id)
    return handle_result(all)


@router.patch('/membership/{id}', response_model=DoctorProfessionalMembershipOut)
def update(id: int, data_up: DoctorProfessioanlMembershipUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    up = doctor_professional_membership_service.update(db=db, id=id, data_update=data_up)
    return handle_result(up)


@router.delete('/membership/{id}')
def remove(id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    dl = doctor_professional_membership_service.delete(db=db, id=id)
    return handle_result(dl)


@router.get('/others-activity/{user_id}', response_model=List[Union[ResultInt, List[DoctorOthersActivityOut]]])
def all_others_activity(user_id: int, skip: int = 0, limit: int = 15, topic: str = '', db: Session = Depends(get_db)):
    all = doctor_others_activity_service.get_by_two_key(db=db, skip=skip, limit=limit, descending=False, count_results=True, user_id=user_id, topic=topic)
    return handle_result(all)


@router.post('/others-activity/', response_model=DoctorOthersActivityOut)
def create(data_in: DoctorOthersActivityIn, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    added = doctor_others_activity_service.create(db=db, data_in=DoctorOthersActivityWithUser(**data_in.dict(), user_id=current_user.id))
    return handle_result(added)


@router.patch('/others-activity/{id}', response_model=DoctorOthersActivityOut)
def edit(id: int, data_up: DoctorOthersActivityUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    up = doctor_others_activity_service.update(db=db, id=id, data_update=data_up)
    return handle_result(up)


@router.delete('/others-activity/{id}')
def remove(id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    re = doctor_others_activity_service.delete(db=db, id=id)
    return handle_result(re)
