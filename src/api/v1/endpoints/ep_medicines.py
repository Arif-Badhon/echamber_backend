from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.db_session import get_db
from exceptions import handle_result
from schemas import MedicineOut
from services import ep_medicine_list_service


router = APIRouter()


@router.get('/', response_model=List[MedicineOut])
def search_medicine(search_medicine: str,  skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    med = ep_medicine_list_service.search_medicine(
        db, search_medicine, skip, limit)
    return handle_result(med)
