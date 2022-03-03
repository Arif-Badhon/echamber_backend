from services import BaseService
from repositories import user_details_repo
from models import UserDetail
from schemas import UserDetailIn, UserDetailUpdate

user_details_service = BaseService[UserDetail, UserDetailIn, UserDetailUpdate](
    UserDetail, user_details_repo)
