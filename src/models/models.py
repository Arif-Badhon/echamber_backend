from sqlalchemy import Column, ForeignKey, Integer, Boolean, String, Text, Date, Float, DateTime, Time
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
    doctors_chamber =  relationship("DoctorChamber", back_populates="user_doctors_chamber")
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



class ImagesLog(BaseModel):
    __tablename__ = "image_log"
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String(100))
    service_name = Column(String(100))
    image_string = Column(String(255))


class PdfLog(BaseModel):
    __tablename__ = "pdf_log"
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String(100))
    service_name = Column(String(100))
    pdf_string = Column(String(255))


# admin panel

class AdminPanelActivity(BaseModel):
    __tablename__ = "admin_panel_activity"
    user_id = Column(Integer, ForeignKey("users.id"))
    service_name = Column(String(100), nullable=True)
    service_recived_id = Column(Integer, nullable=True)  # careful to change recived into received
    remark = Column(String(255), nullable=True)


class Notice(BaseModel):
    __tablename__ = "notice"
    user_id = Column(Integer, ForeignKey("users.id"))
    cover_img_id = Column(Integer)
    title = Column(String(100), nullable=False)
    body = Column(Text, nullable=False)    
    portal = Column(String(100), nullable=False)
    priority = Column(Integer, nullable=False)
    status = Column(Boolean, default=True)


###########################
# service order dashboard #
###########################

class ServiceOrder(BaseModel):
    __tablename__ = "service_orders"
    service_name = Column(String(100), nullable=False)
    patient_id = Column(Integer, nullable=False)
    order_placement = Column(DateTime, nullable=True)
    order_completion = Column(DateTime, nullable=True)
    order_status = Column(String(100), nullable=True)
    order_value = Column(Integer, nullable=False)
    discount_percent = Column(Integer, nullable=False)
    payable_amount = Column(Integer, nullable=False)
    payment_by_customer = Column(Integer, nullable=False)
    payment_pending = Column(Integer, nullable=False)
    payment_method = Column(String(100), nullable=True)
    payment_status = Column(String(100), nullable=True)
    last_payment_date = Column(DateTime, nullable=True)
    service_provider_type = Column(String(100), nullable=True)
    service_provider_id = Column(Integer, nullable=True)
    service_provider_fee = Column(Integer, nullable=True)
    service_provider_fee_paid = Column(Integer, nullable=True)
    service_provider_fee_pending = Column(Integer, nullable=True)
    service_provider_fee_last_update = Column(DateTime, nullable=True)
    service_provider_fee_status = Column(String(100), nullable=True)
    referral_type = Column(String(100), nullable=True)
    referral_id = Column(Integer, nullable=True) 
    referral_provider_fee = Column(Integer, nullable=True)
    referral_provider_fee_paid = Column(Integer, nullable=True)
    referral_provider_fee_pending = Column(Integer, nullable=True)
    referral_provider_fee_last_update = Column(DateTime, nullable=True)
    referral_provider_fee_status = Column(String(100), nullable=True)
    current_address = Column(String(255), nullable=True)
    remarks = Column(String(255), nullable=True)



class FollowUp(BaseModel):
    __tablename__ = "follow_up"
    service_id = Column(Integer, nullable=True)
    title = Column(String(100), nullable=True)
    remarks = Column(String(255), nullable=True)
    status = Column(String(100), nullable=True)
    followup_date = Column(Date, nullable=True)



class TeleMedicineOrder(BaseModel):
    __tablename__ = "telemedicine_orders"
    service_order_id = Column(Integer, nullable=False)
    health_plan_id = Column(Integer, nullable=True)
    patient_id = Column(Integer, ForeignKey("users.id"))
    doctor_id = Column(Integer, ForeignKey("users.id"))
    schedule_id = Column(Integer, nullable=True)
    date = Column(Date, nullable=True)


class MedicineOrder(BaseModel):
    __tablename__ = "medicine_orders"
    service_order_id = Column(Integer, nullable=False)
    name = Column(String(100), nullable=True)
    generic = Column(String(100), nullable=True)
    form = Column(String(100), nullable=True)
    strength = Column(String(100), nullable=True)
    pharmaceuticals = Column(String(100), nullable=True)
    quantity = Column(Float, nullable=False)
    unit_price_tp = Column(Float, nullable=True)
    unit_price_mrp = Column(Float, nullable=False)
    total_mrp = Column(Float, nullable=False)
    unit_discount_percent = Column(Float, nullable=False)
    total = Column(Float, nullable=False)



class HealthPlanList(BaseModel):
    __tablename__ = "health_plan_list"
    name = Column(String(255), nullable=False)
    details = Column(Text, nullable=True)
    voucher_code = Column(String(100), nullable=True)
    total_patients = Column(Integer, nullable=False)
    expire_status = Column(Boolean, nullable=True)
    expire_date = Column(Date, nullable=True)


class HealthPlanForPatient(BaseModel):
    __tablename__ = "health_plan_for_patient"
    health_plan_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    register_by_id = Column(Integer, nullable=False)
    registered_date = Column(Date, nullable=True)
    days = Column(Integer, nullable=True)
    fixed_amount = Column(Boolean, nullable=False)
    amount = Column(Integer, nullable=True)
    discount_percent = Column(Integer, nullable=True)



################
#   Partners   #
################


# corporate partner

class CorporatePartner(BaseModel):
    __tablename__ = "corporate_partners"
    name = Column(String(255), nullable=False)
    type = Column(String(100), nullable=False)
    district = Column(String(50), nullable=False)
    detail_address = Column(String(255), nullable=True)
    detail = Column(String(255), nullable=True)
    phone = Column(String(255), nullable=False)
    email = Column(String(255), nullable=True)
    contact_person = Column(String(255), nullable= False)
    contact_person_phone = Column(String(100), nullable= False)
    contact_person_email = Column(String(100), nullable= True)

class CorporatePartnerUsers(BaseModel):
    __tablename__ = "corporate_partner_users"
    corporate_id = Column(Integer, nullable=False)
    users_id = Column(Integer, nullable=False)
    department = Column(String(100), nullable=True)

# health partner

class HealthPartner(BaseModel):
    __tablename__ = "health_partners"
    name = Column(String(255), nullable=False)
    type = Column(String(100), nullable=False)
    district = Column(String(50), nullable=False)
    detail_address = Column(String(255), nullable=True)
    detail = Column(String(255), nullable=True)
    phone = Column(String(255), nullable=False)
    email = Column(String(255), nullable=True)
    contact_person = Column(String(255), nullable= False)
    contact_person_phone = Column(String(100), nullable= False)
    contact_person_email = Column(String(100), nullable= True)

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


class DoctorChamber(BaseModel):
    __tablename__ = "doctor_chambers"
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String(255), nullable=False)
    detail = Column(Text, nullable=False)
    is_active = Column(Boolean, default=False)

    user_doctors_chamber = relationship("User", back_populates="doctors_chamber")


class DoctorSchedule(BaseModel):
    __tablename__ = "doctor_schedules"
    user_id = Column(Integer, ForeignKey("users.id"))
    day = Column(Integer, nullable=False)
    hours = Column(Integer, nullable=False)
    minutes =  Column(Integer, nullable=False)
    am_pm = Column(String(100), nullable=False)


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
    slot_flt4 = Column(Float, nullable=True)
    slot_flt5 = Column(Float, nullable=True)
    slot_flt6 = Column(Float, nullable=True)
    slot_str7 = Column(String(255), nullable=True)
    slot_str8 = Column(String(255), nullable=True)
    slot_str9 = Column(String(255), nullable=True)


    user_patient_indicator = relationship("User", back_populates="patient_indicator")



class PatientFamily(BaseModel):
    __tablename__ = "patient_families"
    user_id = Column(Integer, ForeignKey("users.id"))
    relation_with = Column(Integer, nullable=False)
    relation_from = Column(String(100))
    relation_to = Column(String(100))
    relationship_status = Column(String(100), nullable= False)
    message = Column(String(255), nullable=True)


# E-prescription related models

class EpMedicineList(BaseModel):
    __tablename__ = "ep_medicine_list"
    name = Column(String(255), nullable=False)
    generic = Column(String(255), nullable=False)
    form = Column(String(255), nullable=False)
    strength = Column(String(255), nullable=False)
    pharmaceuticals = Column(String(255), nullable=False)
    unit_type = Column(String(100), nullable=True)
    unit_price = Column(Float, nullable=True)


class EpChiefComplaintsList(BaseModel):
    __tablename__ = "ep_chief_complaints_list"
    chief_complaints = Column(String(255), nullable=False)
    inserted_by = Column(String(255), nullable= True)


class EpInvestigationList(BaseModel):
    __tablename__ = "ep_investigation_list"
    investigation = Column(String(255), nullable=False)
    inserted_by = Column(String(255), nullable= True)


class EpAdviceList(BaseModel):
    __tablename__ = "ep_advice_list"
    advice = Column(String(255), nullable=False)
    inserted_by = Column(String(255), nullable= True)