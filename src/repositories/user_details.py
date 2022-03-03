from repositories import BaseRepo
from models import UserDetail
from schemas import UserDetailIn, UserDetailUpdate

user_details_repo = BaseRepo[UserDetail,
                             UserDetailIn, UserDetailUpdate](UserDetail)
