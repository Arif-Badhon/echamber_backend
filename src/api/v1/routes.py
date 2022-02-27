from ctypes.wintypes import tagMSG
from sys import prefix
from fastapi import APIRouter
from .endpoints import users, roles

api_router = APIRouter()


api_router.include_router(users.router, prefix='', tags=['Users'])
api_router.include_router(roles.router, prefix='/role', tags=['Roles'])
