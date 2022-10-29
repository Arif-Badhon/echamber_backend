from repositories import roles_repo
from services import BaseService
from models import Role
from schemas import RoleIn, RoleUpdate
from sqlalchemy.orm import Session
from exceptions import ServiceResult, AppException
from fastapi import status


class RoleService(BaseService[Role, RoleIn, RoleUpdate]):

    def admin_role(self, db: Session, name: str):
        get_role = self.repo.search_name(db=db, name=name)

        if not get_role:
            first_role = self.repo.create(db=db, data_in=RoleIn(name=name))
            return ServiceResult(first_role, status_code=status.HTTP_201_CREATED)
        else:
            return ServiceResult(AppException.ServerError("admin role exist"))

    def all_role_registration(self, db: Session):
        all_role = ['admin', 'moderator', 'doctor', 'patient', 'sales', 'medical_affairs', 'crm', 'pharmacy_admin']

        for i in all_role:
            get_role = roles_repo.search_name(db=db, name=i)

            if not get_role:
                role_create = self.repo.create(db=db, data_in=RoleIn(name=i))
        return self.get(db=db)

    def role_id_by_name(self, db: Session, name: str):
        data = db.query(self.model).filter(self.model.name == name).first()
        return data.id


roles_service = RoleService(Role, roles_repo)
