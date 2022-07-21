from models import DfPostCatagory
from schemas import DfPostCatagoryIn, DfPostCatagoryUpdate
from repositories import BaseRepo

df_post_catagory_repo = BaseRepo[DfPostCatagory, DfPostCatagoryIn, DfPostCatagoryUpdate](DfPostCatagory)
