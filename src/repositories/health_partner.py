from repositories import BaseRepo
from schemas import HealthPartnerIn, HealthPartnerUpdate
from models import HealthPartner

health_partner_repo = BaseRepo[HealthPartner, HealthPartnerIn, HealthPartnerUpdate](HealthPartner)