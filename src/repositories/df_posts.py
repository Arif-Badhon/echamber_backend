from models import DfPost
from schemas import DfPostIn, DfPostUpdate
from repositories import BaseRepo


df_post_repo = BaseRepo[DfPost, DfPostIn, DfPostUpdate](DfPost)
