from sqlalchemy import Column, ForeignKey, Integer, Boolean, String
from models import BaseModel
from sqlalchemy.orm import relationship


class User(BaseModel):
    __tablename__ = "users"
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=True, unique=True)
    phone = Column(String(25), nullable=True, unique=True)
    password = Column(String(255), nullable=False)
    sex = Column(String(10), nullable=False)
    is_active = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey("roles.id"))

    role = relationship("Role", back_populates="user")
    doctor = relationship("Doctor", back_populates="user_doctor")


class Role(BaseModel):
    __tablename__ = "roles"
    name = Column(String(100), nullable=False, unique=True)

    user = relationship("User", back_populates="role")


class Doctor(BaseModel):
    __tablename__ = "doctors"
    user_id = Column(Integer, ForeignKey("users.id"))
    bmdc = Column(String(100), nullable=False, unique=True)
    left_header = Column(String(255), nullable=True)
    right_header = Column(String(255), nullable=True)

    user_doctor = relationship("User", back_populates="doctor")
