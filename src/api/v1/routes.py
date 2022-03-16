from fastapi import APIRouter
from .endpoints import users, roles, doctors, patients, user_details, patient_indicators

api_router = APIRouter()

# fmt: off
api_router.include_router(users.router, prefix='', tags=['Users'])
api_router.include_router(user_details.router, prefix='/user/details', tags=['User Details'])
api_router.include_router(roles.router, prefix='/roles', tags=['Roles'])
api_router.include_router(doctors.router, prefix='/doctors', tags=['Doctors'])
api_router.include_router( patients.router, prefix='/patients', tags=['Patients'])
api_router.include_router(patient_indicators.router, prefix="/patient/indicators", tags=['Patient Indicators'])