from typing import List
from fastapi import APIRouter
from schemas import InvOut, InvIn
from services import ep_investigations_list_service
from sqlalchemy.orm import Session
from fastapi import Depends
from exceptions import handle_result
from db import get_db

router = APIRouter()


@router.get('/', response_model=List[InvOut])
def search(search_str: str, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    cc = ep_investigations_list_service.search_by_inv(
        db, search_str=search_str, skip=skip, limit=limit)
    return handle_result(cc)


@router.post('/', response_model=InvOut)
def post(data_in: InvIn, db: Session = Depends(get_db)):
    inv = ep_investigations_list_service.create(db, data_in)
    return handle_result(inv)
