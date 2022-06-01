from fastapi import APIRouter


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