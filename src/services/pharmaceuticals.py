from services import BaseService
from models import Pharmaceuticals
from schemas import PharmaceuticalIn, PharmaceuticalUpdate
from repositories import pharmaceutical_repo

pharmaceutical_service = BaseService[Pharmaceuticals, PharmaceuticalIn, PharmaceuticalUpdate](Pharmaceuticals, pharmaceutical_repo)