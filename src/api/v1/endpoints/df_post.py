from fastapi import APIRouter, Depends
from db import get_db
from exceptions.service_result import handle_result
from schemas import DfPostCatagoryIn, DfPostCatagoryOut, DfPostCatagoryUpdate, DfPostIn, DfPostOut, DfPostUpdate, ResultInt, DfPostTagOut, DfPostInWithUser
from services import df_post_catagory_service, df_post_service
from typing import List, Union
from sqlalchemy.orm import Session
from api.v1.auth_dependcies import logged_in_doctor, logged_in_medical_affairs

router = APIRouter()


@router.get('/post', response_model=List[Union[ResultInt, List[DfPostOut]]])
def posts(skip: int = 0, limit: int = 15, db: Session = Depends(get_db)):
    data = df_post_service.post_out(db=db, skip=skip, limit=limit)
    return handle_result(data)


@router.post('/post', response_model=DfPostOut)
def create(data_in: DfPostIn, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    data = df_post_service.create(db=db, data_in=DfPostInWithUser(user_id=current_user.id, **data_in.dict()))
    return handle_result(data)


@router.get('/post/{id}', response_model=DfPostOut)
def single(id: int, db: Session = Depends(get_db)):
    data = df_post_service.get_one(db=db, id=id)
    return handle_result(data)


@router.patch('/post/{id}', response_model=DfPostOut)
def edit(id: int, data_update: DfPostUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    data = df_post_service.update(db=db, id=id, data_update=data_update)
    return handle_result(data)


@router.get('/catagory', response_model=List[DfPostCatagoryOut])
def all_catagories(db: Session = Depends(get_db)):
    data = df_post_catagory_service.get(db=db)
    return handle_result(data)


@router.post('/catagory', response_model=DfPostCatagoryOut)
def create(data_in: DfPostCatagoryIn, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_medical_affairs)):
    data = df_post_catagory_service.create(db=db, data_in=data_in)
    return handle_result(data)


@router.get('/catagory/{id}', response_model=DfPostCatagoryOut)
def get_single(id: int, db: Session = Depends(get_db)):
    data = df_post_catagory_service.get_one(db=db, id=id)
    return handle_result(data)


@router.patch('/catagory/{id}', response_model=DfPostCatagoryOut)
def edit(id: int, data_update: DfPostCatagoryUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_medical_affairs)):
    data = df_post_catagory_service.update(db=db, id=id, data_update=data_update)
    return handle_result(data)

# tag not done


@router.get('/tag', response_model=List[DfPostTagOut])
def search(db: Session = Depends(get_db)):
    return


@router.post('/tag', response_model=DfPostTagOut)
def create(db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    return


@router.get('/tag/{id}', response_model=DfPostTagOut)
def search(id: int, db: Session = Depends(get_db)):
    return
