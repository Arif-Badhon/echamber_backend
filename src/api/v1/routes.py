from fastapi import APIRouter
from .endpoints import users, roles, doctors, patients, user_details, patient_indicators, ep_medicines, ep_chief_complaints, ep_investigations, ep_advices

api_router = APIRouter()

# fmt: off
api_router.include_router(users.router, prefix='', tags=['Users'])
api_router.include_router(user_details.router, prefix='/user/details', tags=['User Details'])
api_router.include_router(roles.router, prefix='/roles', tags=['Roles'])
api_router.include_router(doctors.router, prefix='/doctors', tags=['Doctors'])
api_router.include_router( patients.router, prefix='/patients', tags=['Patients'])
api_router.include_router(patient_indicators.router, prefix='/patient/indicators', tags=['Patient Indicators'])
api_router.include_router(ep_medicines.router, prefix='/medicines', tags=['Medicines'])
api_router.include_router(ep_chief_complaints.router, prefix='/chief-complaints', tags=['Chief Complaints'])
api_router.include_router(ep_investigations.router, prefix='/investigations', tags=['Investigations'])
api_router.include_router(ep_advices.router, prefix='/advices', tags=['Advices'])