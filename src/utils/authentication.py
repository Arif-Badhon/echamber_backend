from fastapi import Depends
from fastapi.security import HTTPBasicCredentials, HTTPBearer
from sqlalchemy.orm import Session
from db import get_db

security = HTTPBearer()


def logged_in_admin(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    token = credentials.credentials
