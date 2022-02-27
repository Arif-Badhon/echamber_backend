from fastapi import APIRouter
from .endpoints import users, roles, doctors, patients

api_router = APIRouter()


api_router.include_router(users.router, prefix='', tags=['Users'])
api_router.include_router(roles.router, prefix='/roles', tags=['Roles'])
api_router.include_router(doctors.router, prefix='/doctors', tags=['Doctors'])
api_router.include_router(
    patients.router, prefix='/patients', tags=['Patients'])
