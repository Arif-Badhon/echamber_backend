from repositories import corporate_partners_repo
from services import BaseService
from models import CorporatePartner
from schemas import CorporatePartnerIn, CorporatePartnerUpdate


corporate_partners_service = BaseService[CorporatePartner, CorporatePartnerIn, CorporatePartnerUpdate](CorporatePartner, corporate_partners_repo)