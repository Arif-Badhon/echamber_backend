from typing import List
from fastapi import APIRouter, Depends, UploadFile, File
from exceptions.service_result import handle_result
from schemas import ImageLogOut, PdfLogOut, PdfLogIn, ImageLogIn
from db import get_db
from api.v1.auth_dependcies import logged_in_patient
from sqlalchemy.orm import Session
from utils import UploadFileUtils
from services import pdf_log_service, image_log_service


router = APIRouter()




@router.get('/img', response_model=List[ImageLogOut], description='<b>location:</b> /images/patient_reports/[your filename with extention.]')
def img_report_by_user(skip:int = 0, limit:int = 10 ,db: Session = Depends(get_db), current_user: Session = Depends(logged_in_patient)):
    all_reports = image_log_service.patient_all_reports(db=db, user_id=current_user.id, skip=skip, limit=limit)
    return handle_result(all_reports)



@router.post('/img', response_model= ImageLogOut, description='<b>location:</b> /images/patient_reports/[your filename with extention.]')
async def img_report_create(file: UploadFile = File(...), db:Session = Depends(get_db), current_user:Session = Depends(logged_in_patient)):

    up_img = UploadFileUtils(file=file)
    
    # prefix is the short service name
    new_image_name = up_img.upload_image(prefix='patient_report', path='./assets/img/patient_reports', accepted_extensions=['jpg', 'jpeg', 'png'])

    # save in db
    image_in_db = image_log_service.create(db=db, data_in=ImageLogIn(user_id=current_user.id, service_name='patient_report', image_string=new_image_name))
    
    return handle_result(image_in_db)



@router.get('/pdf', response_model=List[PdfLogOut], description="<b>location:</b> /pdf/patient_reports/[your filename with extention.]")
def pdf_report_by_user(skip:int = 0, limit:int = 10 ,db: Session = Depends(get_db), current_user: Session = Depends(logged_in_patient)):
    all_reports = pdf_log_service.patient_all_reports(db=db, user_id=current_user.id, skip=skip, limit=limit)
    return handle_result(all_reports)

@router.post('/pdf', response_model=PdfLogOut, description="<b>location:</b> /pdf/patient_reports/[your filename with extention.]")
def pdf_report_create(file: UploadFile = File(...), db: Session = Depends(get_db), current_user: Session = Depends(logged_in_patient)):
    up_pdf = UploadFileUtils(file=file) 

    # upload
    upload_pdf = up_pdf.upload_pdf(prefix='patient_report', path='./assets/pdf/patient_reports', accept_extensions=['pdf'])
    
    # save in db
    pdf_in_db = pdf_log_service.create(db=db, data_in=PdfLogIn(user_id=current_user.id, service_name='patient_report', pdf_string=upload_pdf))
    
    return handle_result(pdf_in_db)