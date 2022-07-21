from models import DfPostCatagory
from schemas import DfPostCatagoryIn, DfPostCatagoryUpdate
from repositories import df_post_catagory_repo
from services import BaseService

df_post_catagory_service = BaseService[DfPostCatagory, DfPostCatagoryIn, DfPostCatagoryUpdate](DfPostCatagory, df_post_catagory_repo)
