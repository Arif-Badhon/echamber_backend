from repositories import roles_repo
from services import BaseService
from models import Role
from schemas import RoleIn, RoleUpdate


roles_service = BaseService[Role, RoleIn, RoleUpdate](Role, roles_repo)
