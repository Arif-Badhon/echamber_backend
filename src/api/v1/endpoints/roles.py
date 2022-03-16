from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from exceptions import handle_result
from services import roles_service
from schemas.roles import RoleOut, RoleIn, RoleUpdate
from db import get_db
from typing import List
from models import User
from api.v1.auth_dependcies import logged_in

router = APIRouter()


@router.get('/', response_model=List[RoleOut])
def get(db: Session = Depends(get_db)):
    roles = roles_service.get(db)
    return handle_result(roles)


@router.post('/', response_model=RoleOut)
def post(role_in: RoleIn, db: Session = Depends(get_db)):
    role = roles_service.create(db, data_in=role_in)
    return handle_result(role)


@router.get('/{id}', response_model=RoleOut)
def get_one(id, db: Session = Depends(get_db)):
    roles = roles_service.get_one(db, id)
    print(roles)
    return handle_result(roles)


@router.put('/{id}', response_model=RoleUpdate)
def update(id: int, role_update: RoleUpdate, db: Session = Depends(get_db)):
    update = roles_service.update(db, id, data_update=role_update)
    return handle_result(update)


@router.delete('/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    delete = roles_service.delete(db, id)
    return handle_result(delete)
