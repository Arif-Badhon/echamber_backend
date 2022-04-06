from sqlalchemy import Column, ForeignKey, Integer, Boolean, String, Text, Date
from models import BaseModel
from sqlalchemy.orm import relationship



# fmt: off

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
    user_details = relationship("UserDetail", back_populates="user")
    doctor = relationship("Doctor", back_populates="user_doctor")
    doctor_qualification = relationship("DoctorQualification", back_populates="user_doctor_qualification")
    doctor_speciality = relationship("DoctorSpeciality", back_populates="user_doctor_speciality")
    patient = relationship("Patient", back_populates="user_patient")
    patient_indicator = relationship("PatientIndicator", back_populates="user_patient_indicator")


class Role(BaseModel):
    __tablename__ = "roles"
    name = Column(String(100), nullable=False, unique=True)

    user = relationship("User", back_populates="role")


class UserDetail(BaseModel):
    __tablename__ = "user_details"
    user_id = Column(Integer, ForeignKey("users.id"))
    country = Column(String(255), nullable=True)
    division = Column(String(50), nullable=True)
    district = Column(String(50), nullable=True)
    post_code = Column(String(20), nullable=True)
    sub_district = Column(String(50), nullable=True)
    nid = Column(String(100), nullable=True)
    dob = Column(Date, nullable=True)
    blood_group = Column(String(5), nullable=True)

    user = relationship("User", back_populates="user_details")


# Doctor related models

class Doctor(BaseModel):
    __tablename__ = "doctors"
    user_id = Column(Integer, ForeignKey("users.id"))
    bmdc = Column(String(100), nullable=False, unique=True)
    main_chamber = Column(String(255), nullable=True)

    user_doctor = relationship("User", back_populates="doctor")



class DoctorQualification(BaseModel):
    __tablename__="doctor_qualifications"
    user_id = Column(Integer, ForeignKey("users.id"))
    qualification= Column(String(100), nullable=False)

    user_doctor_qualification = relationship("User", back_populates="doctor_qualification")



class DoctorSpeciality(BaseModel):
    __tablename__="doctor_specialities"
    user_id = Column(Integer, ForeignKey("users.id"))
    speciality= Column(String(100), nullable=False)

    user_doctor_speciality = relationship("User", back_populates="doctor_speciality")



# Patient related models

class Patient(BaseModel):
    __tablename__ = "patients"
    user_id = Column(Integer, ForeignKey("users.id"))
    bio = Column(Text, nullable=True)
    marital_status = Column(String(20), nullable=True)
    occupation = Column(String(255), nullable=True)

    user_patient = relationship("User", back_populates="patient")



class PatientIndicator(BaseModel):
    __tablename__ = "patient_indicators"
    user_id = Column(Integer, ForeignKey("users.id"))
    key = Column(String(100), nullable=False)
    unit = Column(String(100), nullable=True)
    slot_bool = Column(Boolean, nullable=True)
    slot_int1 = Column(Integer, nullable=True)
    slot_int2 = Column(Integer, nullable=True)
    slot_int3 = Column(Integer, nullable=True)
    slot_str1 = Column(String(255), nullable=True)
    slot_str2 = Column(String(255), nullable=True)
    slot_str3 = Column(String(255), nullable=True)


    user_patient_indicator = relationship("User", back_populates="patient_indicator")



# E-prescription related models

class EpMedicineList(BaseModel):
    __tablename__ = "ep_medicine_list"
    name = Column(String(255), nullable=False)
    generic = Column(String(255), nullable=False)
    form = Column(String(255), nullable=False)
    strength = Column(String(255), nullable=False)
    pharmaceuticals = Column(String(255), nullable=False)


class EpChiefComplaintsList(BaseModel):
    __tablename__ = "ep_chief_complaints_list"
    cc = Column(String(255), nullable=False)
    inserted_by = Column(String(255), nullable= True)


class EpInvestigationList(BaseModel):
    __tablename__ = "ep_investigation_list"
    investigation = Column(String(255), nullable=False)
    inserted_by = Column(String(255), nullable= True)


class EpAdviceList(BaseModel):
    __tablename__ = "ep_advice_list"
    advice = Column(String(255), nullable=False)
    inserted_by = Column(String(255), nullable= True)