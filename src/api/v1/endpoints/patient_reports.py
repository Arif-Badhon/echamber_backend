from fastapi import APIRouter, Depends, UploadFile, File
from exceptions.service_result import handle_result
from schemas import ImageLogOut, PdfLogOut, PdfLogIn
from db import get_db
from api.v1.auth_dependcies import logged_in_patient
from sqlalchemy.orm import Session
from utils import UploadFileUtils
from services import pdf_log_service


router = APIRouter()

@router.get('/pdf')
def pdf_report_by_user():
    return

@router.post('/pdf')
def pdf_report_create():
    return

@router.get('/img')
def img_report_by_user():
    return

@router.post('/img', response_model=PdfLogOut)
def img_report_create(file: UploadFile = File(...), db: Session = Depends(get_db), current_user: Session = Depends(logged_in_patient)):
    up_pdf = UploadFileUtils(file=file) 

    # upload
    upload_pdf = up_pdf.upload_pdf(prefix='patient_report', path='./assets/pdf/patient_reports', accept_extensions=['pdf'])
    
    # save in db
    pdf_in_db = pdf_log_service.create(db=db, data_in=PdfLogIn(user_id=current_user.id, service_name='patient_report', pdf_string=upload_pdf))
    
    return handle_result(pdf_in_db)