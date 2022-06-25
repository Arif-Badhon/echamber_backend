from services import BaseService
from repositories import health_plan_list_repo
from models import HealthPlanList
from schemas import HealthPlanListIn, HealthPlanListUpdate


healtth_plan_list_service = BaseService[HealthPlanList, HealthPlanListIn, HealthPlanListUpdate](HealthPlanList, health_plan_list_repo) 