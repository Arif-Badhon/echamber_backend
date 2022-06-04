from repositories import BaseRepo
from models import CorporatePartner
from schemas import CorporatePartnerIn, CorporatePartnerUpdate


corporate_partners_repo = BaseRepo[CorporatePartner, CorporatePartnerIn, CorporatePartnerUpdate](CorporatePartner)