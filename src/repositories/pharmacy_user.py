from repositories import BaseRepo
from models import PharmacyUser
from schemas import PharmacyUserIn, PharmacyUserUpdate

pharmacy_user_repo = BaseRepo[PharmacyUser, PharmacyUserIn, PharmacyUserUpdate](PharmacyUser)