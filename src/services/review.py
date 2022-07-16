from models import Review
from schemas import ReviewIn, ReviewUdate
from services import BaseService
from repositories import review_repo

review_service = BaseService[Review, ReviewIn, ReviewUdate](Review, review_repo)
