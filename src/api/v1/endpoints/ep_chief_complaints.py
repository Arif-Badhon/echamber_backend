from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from exceptions import handle_result
from schemas import CcOut, CcIn
from services import ep_chief_complaints_list_service

router = APIRouter()


@router.get('/', response_model=List[CcOut])
def search(search_str: str, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    cc = ep_chief_complaints_list_service.search_by_cc(
        db, search_str=search_str, skip=skip, limit=limit)
    return handle_result(cc)


@router.post('/', response_model=CcOut)
def post(data_in: CcIn, db: Session = Depends(get_db)):
    cc = ep_chief_complaints_list_service.create(db, data_in)
    return handle_result(cc)
