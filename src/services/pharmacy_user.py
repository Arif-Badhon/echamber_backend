from services import BaseService
from models import PharmacyUser
from schemas import PharmacyUserIn, PharmacyUserUpdate
from repositories import pharmacy_user_repo

pharmacy_user_service = BaseService[PharmacyUser, PharmacyUserIn, PharmacyUserUpdate](PharmacyUser, pharmacy_user_repo)