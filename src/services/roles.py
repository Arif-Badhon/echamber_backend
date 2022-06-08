from repositories import roles_repo
from services import BaseService
from models import Role
from schemas import RoleIn, RoleUpdate
from sqlalchemy.orm import Session


class RoleService(BaseService[Role, RoleIn, RoleUpdate]):
    
    def role_id_by_name(self, db: Session, name: str):
        data = db.query(self.model).filter(self.model.name == name).first()
        return data.id

roles_service = RoleService(Role, roles_repo)
