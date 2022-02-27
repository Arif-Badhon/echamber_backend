from ctypes.wintypes import tagMSG
from sys import prefix
from fastapi import APIRouter

from api.v1.endpoints import doctors
from .endpoints import users, roles

api_router = APIRouter()


api_router.include_router(users.router, prefix='', tags=['Users'])
api_router.include_router(roles.router, prefix='/roles', tags=['Roles'])
api_router.include_router(doctors.router, prefix='/doctors', tags=['Doctors'])
