from fastapi import APIRouter
from schemas import notice
from .endpoints2 import pharmaceuticals

api_router = APIRouter()

api_router.include_router(pharmaceuticals.router, prefix='/pharmaceuticals', tags=['pharmaceuticals'])