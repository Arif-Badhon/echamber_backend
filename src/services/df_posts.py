from models import DfPost
from schemas import DfPostIn, DfPostUpdate
from services import BaseService
from repositories import df_post_repo


df_post_service = BaseService[DfPost, DfPostIn, DfPostUpdate](DfPost, df_post_repo)
