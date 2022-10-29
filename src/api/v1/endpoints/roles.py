from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from exceptions import handle_result
from services import roles_service
from schemas.roles import RoleOut, RoleIn, RoleUpdate
from db import get_db
from typing import List
from models import User
from api.v1.auth_dependcies import logged_in, logged_in_admin

router = APIRouter()


@router.get('/', response_model=List[RoleOut])
def get(db: Session = Depends(get_db)):
    roles = roles_service.get(db)
    return handle_result(roles)


@router.post('/', response_model=RoleOut)
def post(role_in: RoleIn, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin)):
    role = roles_service.create(db, data_in=role_in)
    return handle_result(role)


@router.get('/{id}', response_model=RoleOut)
def get_one(id, db: Session = Depends(get_db)):
    roles = roles_service.get_one(db, id)
    return handle_result(roles)


@router.put('/{id}', response_model=RoleUpdate)
def update(id: int, role_update: RoleUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin)):
    update = roles_service.update(db, id, data_update=role_update)
    return handle_result(update)


@router.delete('/{id}')
def delete(id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin)):
    delete = roles_service.delete(db, id)
    return handle_result(delete)


@router.post('/admin/registration', response_model=RoleOut)
def admin_role(db: Session = Depends(get_db)):
    name = roles_service.admin_role(db=db, name='admin')
    return handle_result(name)


@router.get('/all/registration', response_model=List[RoleOut])
def all_role_registration(db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin)):
    all = roles_service.all_role_registration(db=db)
    return handle_result(all)
