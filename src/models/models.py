from sqlalchemy import Column, ForeignKey, Integer, Boolean, String, Text, Date
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
    patient = relationship("Patient", back_populates="user_patient")


class Role(BaseModel):
    __tablename__ = "roles"
    name = Column(String(100), nullable=False, unique=True)

    user = relationship("User", back_populates="role")


class UserDetail(BaseModel):
    __tablename__ = "user_details"
    country = Column(String(255), nullable=True)
    division = Column(String(50), nullable=True)
    district = Column(String(50), nullable=True)
    post_code = Column(String(20), nullable=True)
    sub_district = Column(String(50), nullable=True)
    nid = Column(String(100), nullable=True)
    dob = Column(Date, nullable=True)
    blood_group = Column(String(5), nullable=True)


class Doctor(BaseModel):
    __tablename__ = "doctors"
    user_id = Column(Integer, ForeignKey("users.id"))
    bmdc = Column(String(100), nullable=False, unique=True)
    left_header = Column(String(255), nullable=True)
    right_header = Column(String(255), nullable=True)

    user_doctor = relationship("User", back_populates="doctor")


class Patient(BaseModel):
    __tablename__ = "patients"
    user_id = Column(Integer, ForeignKey("users.id"))
    bio = Column(Text, nullable=True)
    nid = Column(String(100), nullable=True, unique=True)
    marital_status = Column(String(20), nullable=True)
    occupation = Column(String(255), nullable=True)
    height = Column(Integer, nullable=True)
    weight = Column(Integer, nullable=True)

    user_patient = relationship("User", back_populates="patient")
