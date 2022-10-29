from repositories import BaseRepo
from models import Role
from schemas import RoleIn, RoleUpdate
from sqlalchemy.orm import Session


class RoleRepo(BaseRepo[Role, RoleIn, RoleUpdate]):
    def search_name(self, db: Session, name: str) -> int:
        result = db.query(self.model).filter(self.model.name == name).first()
        return result

    def search_name_id(self, db: Session, name: str) -> int:
        result = db.query(self.model).filter(self.model.name == name).first()
        return result.id


roles_repo = RoleRepo(Role)
