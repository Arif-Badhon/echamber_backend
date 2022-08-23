from repositories import BaseRepo
from models import Pharmaceuticals
from schemas import PharmaceuticalIn, PharmaceuticalUpdate

pharmaceutical_repo = BaseRepo[Pharmaceuticals, PharmaceuticalIn, PharmaceuticalUpdate](Pharmaceuticals)
