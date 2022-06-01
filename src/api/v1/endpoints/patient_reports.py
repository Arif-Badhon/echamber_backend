from fastapi import APIRouter


router = APIRouter()

@router.get('/pdf')
def pdf_report_by_user():
    return


@router.get('/img')
def img_report_by_user():
    return