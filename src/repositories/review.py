from models import Review
from repositories import BaseRepo
from schemas import ReviewIn, ReviewUdate

review_repo = BaseRepo[Review, ReviewIn, ReviewUdate](Review)
