from repositories import BaseRepo
from models import Pharmaceuticals
from schemas import PharmaceuticalIn, PharmaceuticalUpdate


class PharmaceuticalsRepo(BaseRepo[Pharmaceuticals, PharmaceuticalIn, PharmaceuticalUpdate]):
    pass

pharmaceuticals_repo = PharmaceuticalsRepo(Pharmaceuticals)
