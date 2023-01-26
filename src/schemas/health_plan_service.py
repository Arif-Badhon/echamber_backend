from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel

class HealthPlanServiceBase(BaseModel):
    plan_type: Optional[str] = None
    name: str


class HealthPlanServiceOut(HealthPlanServiceBase):
   id: int
   created_at: datetime
   updated_at: Optional[datetime] = None
   
   class Config:
       orm_mode = True


