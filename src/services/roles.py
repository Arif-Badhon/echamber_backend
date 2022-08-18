from repositories import roles_repo
from services import BaseService
from models import Role
from schemas import RoleIn, RoleUpdate
from sqlalchemy.orm import Session
from exceptions import ServiceResult, AppException
from fastapi import status


class RoleService(BaseService[Role, RoleIn, RoleUpdate]):

    def first_role(self, db: Session, name: str):
        get_data = roles_repo.get(db=db)

        if len(get_data) > 0:
            return ServiceResult(AppException.ServerError("First role exist"))
        first_role = roles_repo.create(db=db, data_in=RoleIn(name=name))
        return ServiceResult(first_role, status_code=status.HTTP_201_CREATED)

    def role_id_by_name(self, db: Session, name: str):
        data = db.query(self.model).filter(self.model.name == name).first()
        return data.id


roles_service = RoleService(Role, roles_repo)
