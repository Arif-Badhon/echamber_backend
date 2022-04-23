from fastapi import APIRouter


router = APIRouter()


@router.post()

@router.get('/')
def all():
    return {'msg':'all schedule'}