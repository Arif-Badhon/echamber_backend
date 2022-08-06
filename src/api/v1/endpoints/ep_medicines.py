from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.db_session import get_db
from exceptions import handle_result
from schemas import MedicineOut, EpPharmaOut
from services import ep_medicine_list_service


router = APIRouter()


@router.get('/', response_model=List[MedicineOut])
def search_medicine(search_medicine: str,  skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    med = ep_medicine_list_service.search_medicine(
        db, search_medicine, skip, limit)
    return handle_result(med)


@router.get('/pharma/all', response_model=List[EpPharmaOut])
def all_pharma(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    data = ep_medicine_list_service.all_pharma(db=db, skip=skip, limit=limit)
    return handle_result(data)


@router.get('/pharma/{pharma}', response_model=List[EpPharmaOut])
def pharma_search(pharma: str, db: Session = Depends(get_db)):
    data = ep_medicine_list_service.search_pharma(db=db, pharma=pharma)
    return handle_result(data)
