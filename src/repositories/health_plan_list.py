from repositories import BaseRepo
from models import HealthPlanList
from schemas import HealthPlanListIn, HealthPlanListUpdate

health_plan_list_repo = BaseRepo[HealthPlanList, HealthPlanListIn, HealthPlanListUpdate](HealthPlanList)