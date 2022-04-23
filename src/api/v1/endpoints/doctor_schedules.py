from fastapi import APIRouter


router = APIRouter()


@router.get('/')
def all():
    return {'msg':'all schedule'}