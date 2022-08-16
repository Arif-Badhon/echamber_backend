from typing import List, Union
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.db_session import get_db
from exceptions import handle_result
from schemas import MedicineOut, EpPharmaOut, MedicineIn, MedicineInWithUser, ResultInt
from schemas.ep_medicines import MedicineUpdate
from services import ep_medicine_list_service
from api.v1.auth_dependcies import logged_in, logged_in_admin

router = APIRouter()


@router.get('/', response_model=List[MedicineOut])
def search_medicine(search_medicine: str,  skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    med = ep_medicine_list_service.search_medicine(
        db, search_medicine, skip, limit)
    return handle_result(med)


@router.post('/', response_model=MedicineOut)
def medicine_input(data_in: MedicineIn, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    medi = ep_medicine_list_service.create(db=db, data_in=MedicineInWithUser(**data_in.dict(), add_status='pending', added_by_id=current_user.id))
    return handle_result(medi)


@router.patch('/{id}', response_model=MedicineOut)
def update_by_admin(id: int, data_update: MedicineUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    up = ep_medicine_list_service.update(db=db, data_update=data_update, id=id)
    return handle_result(up)


@router.delete('/{id}')
def remove_by_admin(id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    rmv = ep_medicine_list_service.delete(db=db, id=id)
    return handle_result(rmv)


@router.get('/pending', response_model=List[Union[ResultInt, List[MedicineOut]]])
def all_pending_medicine(skip: int = 0, limit: int = 20, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    all = ep_medicine_list_service.get_by_key(db=db, skip=skip, limit=limit, descending=True, count_results=True, add_status='pending')
    return handle_result(all)


@router.get('/pharma/all', response_model=List[EpPharmaOut])
def all_pharma(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    data = ep_medicine_list_service.all_pharma(db=db, skip=skip, limit=limit)
    return handle_result(data)


@router.get('/pharma/{pharma}', response_model=List[EpPharmaOut])
def pharma_search(pharma: str, db: Session = Depends(get_db)):
    data = ep_medicine_list_service.search_pharma(db=db, pharma=pharma)
    return handle_result(data)
