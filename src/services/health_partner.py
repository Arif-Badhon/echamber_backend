from services import BaseService
from models import HealthPartner
from schemas import HealthPartnerIn, HealthPartnerUpdate
from repositories import health_partner_repo

health_partner_service = BaseService[HealthPartner, HealthPartnerIn, HealthPartnerUpdate](HealthPartner, health_partner_repo)