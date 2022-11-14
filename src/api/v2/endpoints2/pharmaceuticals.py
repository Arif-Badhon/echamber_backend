from typing import List, Union
from fastapi import APIRouter, Depends
from exceptions.service_result import handle_result
from schemas import PharmaceuticalOut, PharmaceuticalUserWithPhr, PharmaceuticalNameListOut, ResultInt
from db import get_db
from sqlalchemy.orm import Session
from services import pharmaceutical_service, pharmaceuticals_name_list_service
from api.v1.auth_dependcies import logged_in_admin

router = APIRouter()

@router.get("/", response_model=List[PharmaceuticalOut])
def read(db: Session = Depends(get_db)):
    search = pharmaceutical_service.get(db=db)
    return handle_result(search)

@router.post("/")
def phr_with_user(data_in: PharmaceuticalUserWithPhr, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin)):
    user = pharmaceutical_service.register_pharmaceuticals(db=db, data_in=data_in)
    return handle_result(user)


@router.get('/pharmaceuticals-name/all', response_model=List[Union[ResultInt, List[PharmaceuticalNameListOut]]])
def all_pharmaceuticals(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    data = pharmaceuticals_name_list_service.all_pharmaceuticals(db=db, skip=skip, limit=limit)
    return handle_result(data)


@router.get('/pharmaceuticals-name/{pharmaceuticals}', response_model=List[PharmaceuticalNameListOut])
def pharmaceuticals_name_search(pharmaceuticals: str, db: Session = Depends(get_db)):
    data = pharmaceuticals_name_list_service.search_pharmaceuticals(db=db, pharmaceuticals=pharmaceuticals)
    return handle_result(data)


@router.get('/pharmaceuticals-id/{id}', response_model=PharmaceuticalNameListOut)
def pharmaceuticals_search_with_id(id: int, db: Session = Depends(get_db)):
    data = pharmaceuticals_name_list_service.get_one(db=db, id=id)
    return handle_result(data)