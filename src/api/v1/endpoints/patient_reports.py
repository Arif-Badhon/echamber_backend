from typing import List, Union
from fastapi import APIRouter, Depends, UploadFile, File
from exceptions import service_result
from exceptions.service_result import handle_result
from schemas import ImageLogOut, PdfLogOut, PdfLogIn, ImageLogIn, ResultInt
from db import get_db
from api.v1.auth_dependcies import logged_in_patient
from sqlalchemy.orm import Session
from utils import UploadFileUtils
from services import pdf_log_service, image_log_service


router = APIRouter()


@router.get(
    '/img/{service_name}', response_model=List[Union[ResultInt, List[ImageLogOut]]],
    description='<b>location:</b> /images/patient_reports/[your filename with extention.] <br/> valid service name: patient_report, patient_medication, patient_prescription, patient_surgery, patient_vaccination')
def img_report_by_user(service_name: str, skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_patient)):
    all_reports = image_log_service.get_by_two_key(db=db,  skip=skip, limit=limit, descending=True, count_results=True, user_id=current_user.id, service_name=service_name)
    return handle_result(all_reports)


@router.post('/img/{service_name}', response_model=ImageLogOut,
             description='<b>location:</b> /images/[service_name]/[your filename with extention.] <br/> valid service name: patient_report, patient_medication, patient_prescription, patient_surgery, patient_vaccination')
async def img_report_create(service_name: str, file: UploadFile = File(...), db: Session = Depends(get_db), current_user: Session = Depends(logged_in_patient)):

    up_img = UploadFileUtils(file=file)

    # prefix is the short service name
    new_image_name = up_img.upload_image(prefix=service_name, path='./assets/img/'+service_name, accepted_extensions=['jpg', 'jpeg', 'png'])

    # save in db
    image_in_db = image_log_service.create(db=db, data_in=ImageLogIn(user_id=current_user.id, service_name=service_name, image_string=new_image_name))

    return handle_result(image_in_db)


@router.get(
    '/pdf/{service_name}', response_model=List[Union[ResultInt, List[PdfLogOut]]],
    description="<b>location:</b> /pdf/[service_name]/[your filename with extention.] <br/> valid service name: patient_report, patient_medication, patient_prescription, patient_surgery, patient_vaccination")
def pdf_report_by_user(service_name: str, skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_patient)):
    all_reports = pdf_log_service.get_by_two_key(db=db, skip=skip, limit=limit, descending=True, count_results=True, user_id=current_user.id, service_name=service_name)
    return handle_result(all_reports)


@router.post('/pdf/{service_name}', response_model=PdfLogOut,
             description="<b>location:</b> /pdf/[service_name]/[your filename with extention.] <br/> valid service name: patient_report, patient_medication, patient_prescription, patient_surgery, patient_vaccination")
def pdf_report_create(service_name: str, file: UploadFile = File(...), db: Session = Depends(get_db), current_user: Session = Depends(logged_in_patient)):
    up_pdf = UploadFileUtils(file=file)

    # upload
    upload_pdf = up_pdf.upload_pdf(prefix=service_name, path='./assets/pdf/'+service_name, accept_extensions=['pdf'])

    # save in db
    pdf_in_db = pdf_log_service.create(db=db, data_in=PdfLogIn(user_id=current_user.id, service_name=service_name, pdf_string=upload_pdf))

    return handle_result(pdf_in_db)
