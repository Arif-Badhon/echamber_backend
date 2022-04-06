from typing import List
from fastapi import APIRouter
from schemas import AdviceOut
from schemas.ep_advices import AdviceIn
from services import ep_advices_list_service
from sqlalchemy.orm import Session
from fastapi import Depends
from db import get_db
from exceptions import handle_result

router = APIRouter()


@router.get('/', response_model=List[AdviceOut])
def search(search_str: str, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    adv = ep_advices_list_service.search_by_advice(
        db, search_str=search_str, skip=skip, limit=limit)
    return handle_result(adv)


@router.post('/', response_model=AdviceOut)
def post(data_in: AdviceIn, db: Session = Depends(get_db)):
    adv = ep_advices_list_service.create(db, data_in)
    return handle_result(adv)
