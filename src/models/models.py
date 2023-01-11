from tokenize import Double
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


class LoginLog(BaseModel):
    __tablename__ = "login_log"
    user_id = Column(Integer, ForeignKey("users.id"))


class TemporaryToken(BaseModel):
    __tablename__ = "temporary_token"
    user_id = Column(Integer, nullable=True)
    temp_token = Column(String(255), nullable=True)
    used_status = Column(Boolean, nullable=True)
    remarks = Column(String(255), nullable=True)


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
    delivery_fee = Column(Integer, nullable=True)
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
    booked_date = Column(Date, nullable=True)


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
    plan_type = Column(String(255), nullable=True)
    name = Column(String(255), nullable=False)
    details = Column(Text, nullable=True)
    voucher_code = Column(String(100), nullable=True)
    total_patients = Column(Integer, nullable=False)
    expire_status = Column(Boolean, nullable=True)
    expire_date = Column(Date, nullable=True)
    days = Column(Integer, nullable=True)
    fee = Column(Integer, nullable=True)


class HealthPlanForPatient(BaseModel):
    __tablename__ = "health_plan_for_patient"
    service_order_id = Column(Integer, nullable=False)
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




##########
# MediVa #
##########

class MedivaDeviceCatagory(BaseModel):
    __tablename__ = "mediva_device_catagories"
    name = Column(String(100), nullable=False)
    details = Column(Text, nullable=True)


class MedivaDevice(BaseModel):
    __tablename__ = "mediva_devices"
    name = Column(String(255), nullable=False)
    brand = Column(String(255), nullable=True)
    model = Column(String(255), nullable=True)
    details = Column(Text, nullable=True)
    img_id = Column(Integer, nullable=True)
    catagory_id =  Column(Integer, ForeignKey("mediva_device_catagories.id"))
    quantity = Column(Integer, nullable=False)
    trp = Column(Integer, nullable=True)
    old_mrp = Column(Integer, nullable=True)
    current_mrp = Column(Integer, nullable=False)


class MedivaDeviceOrder(BaseModel):
    __tablename__ = "mediva_device_order"
    service_order_id = Column(Integer, nullable=False)
    device_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    mrp = Column(Integer, nullable=True)
    discount = Column(Integer, nullable=True)
    total_mrp = Column(Integer, nullable=True)


############
#  Review  #
############

class Review(BaseModel):
    __tablename__ = "review"
    user_id = Column(Integer, nullable=False)
    service_name = Column(String(100), nullable=False)
    service_id = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=True)
    comment = Column(Text, nullable=True)
    visible = Column(Boolean, nullable=False)



# Doctor related models

class Doctor(BaseModel):
    __tablename__ = "doctors"
    user_id = Column(Integer, ForeignKey("users.id"))
    dr_title = Column(String(100), nullable=True)
    bmdc = Column(String(100), nullable=False, unique=True)
    exp_year = Column(Integer, nullable=True)
    online_fees = Column(Float, nullable=True)
    online_healthx_fees = Column(Float, nullable=True)
    online_vat = Column(Float, nullable=True)
    online_total_fees =Column(Float, nullable=True)
    followup_fees = Column(Float, nullable=True)
    followup_healthx_fees = Column(Float, nullable=True)
    followup_vat = Column(Float, nullable=True)
    followup_total_fees =Column(Float, nullable=True)

    user_doctor = relationship("User", back_populates="doctor")



class DoctorWorkPlace(BaseModel):
    __tablename__ = "doctor_workplace"
    user_id = Column(Integer, ForeignKey("users.id"))
    institute = Column(String(255), nullable=False)
    position = Column(String(255), nullable=True)
    top_priority = Column(Boolean, nullable=True)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)



class DoctorAcademicInfo(BaseModel):
    __tablename__ = "doctor_academic_info"
    user_id = Column(Integer, ForeignKey("users.id"))
    institute = Column(String(255), nullable=False)
    degree = Column(String(255), nullable=True)
    speciality = Column(String(255), nullable=True)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)


class DoctorQualification(BaseModel):
    __tablename__="doctor_qualifications"
    user_id = Column(Integer, ForeignKey("users.id"))
    qualification= Column(Text, nullable=False)

    user_doctor_qualification = relationship("User", back_populates="doctor_qualification")



class DoctorSpeciality(BaseModel):
    __tablename__="doctor_specialities"
    user_id = Column(Integer, ForeignKey("users.id"))
    speciality= Column(Text, nullable=False)

    user_doctor_speciality = relationship("User", back_populates="doctor_speciality")


class DoctorChamber(BaseModel):
    __tablename__ = "doctor_chambers"
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String(255), nullable=False)
    detail = Column(Text, nullable=False)
    district = Column(String(100), nullable=False)
    detail_address = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=False)
    chamber_fee = Column(Float, nullable=True)

    user_doctors_chamber = relationship("User", back_populates="doctors_chamber")



class DoctorEpHeader(BaseModel):
    __tablename__ = "doctor_ep_header"
    user_id = Column(Integer, ForeignKey("users.id"))
    header_side = Column(String(100), nullable=False)
    heading = Column(String(255), nullable=True)
    body = Column(Text, nullable=True)



class DoctorSchedule(BaseModel):
    __tablename__ = "doctor_schedules"
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(Date, nullable=False)
    time_min = Column(Integer, nullable=False)
    duration_min = Column(Integer, nullable=False)
    am_pm = Column(String(255), nullable=False)
    online = Column(Boolean, nullable=False)
    chamber_id = Column(Integer, nullable=True)
    booked_by_patient_id = Column(Integer, nullable=True)



class DoctorTrainingExp(BaseModel):
    __tablename__ = "doctor_training_exp"
    user_id = Column(Integer, ForeignKey("users.id"))
    topic = Column(String(255), nullable=True)
    place = Column(String(255), nullable=True)
    organisation = Column(String(255), nullable=True)
    year = Column(Integer, nullable=True)


class DoctorProfessionalMembership(BaseModel):
    __tablename__ = "doctor_professional_membership"
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String(100), nullable=True)
    position = Column(String(100), nullable=True)
    year = Column(Integer, nullable=True)


class DoctorOthersActivity(BaseModel):
    __tablename__ = "doctor_others_activity"
    user_id = Column(Integer, ForeignKey("users.id"))
    topic = Column(String(255), nullable=False)
    title = Column(String(255), nullable=True)
    details = Column(Text, nullable=True)


# Doctor payment 

####################
#  Doctor's forum  #
####################

class DfPostCatagory(BaseModel):
    __tablename__ = "df_post_catagories"
    name = Column(String(100), nullable=False)
    details = Column(Text, nullable=True)


class DfPostTag(BaseModel):
    __tablename__ = "df_post_tags"
    user_id = Column(Integer, ForeignKey("users.id"))
    tag = Column(String(255), nullable=False)


class DfPostTagRelation(BaseModel):
    __tablename__ = "df_post_tag_relations"
    post_id = Column(Integer, ForeignKey("df_posts.id"))
    tag_id = Column(Integer, ForeignKey("df_post_tags.id"))


class DfPost(BaseModel):
    __tablename__ = "df_posts"
    title = Column(String(255), nullable=False)
    body = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    catagory_id = Column(Integer, ForeignKey("df_post_catagories.id"))
    cover_image_id = Column(Integer, nullable=True)


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

class EPrescription(BaseModel):
    __tablename__ = "eprescriptions"
    cause_of_consultation = Column(String(255), nullable=True)
    telemedicine_order_id = Column(Integer, nullable=True)
    doctor_id = Column(Integer, nullable=True)
    patient_id = Column(Integer, nullable=True)
    patient_name = Column(String(100), nullable=True)
    patient_phone = Column(String(30), nullable=True) # newly added - antor
    patient_sex =  Column(String(10), nullable=True)
    patient_age_years = Column(Integer, nullable=True)
    patient_age_months = Column(Integer, nullable=True)
    blood_group = Column(String(5), nullable=True) # newly added - antor
    age_years = Column(Integer, nullable=True)
    age_months = Column(Integer, nullable=True)
    current_address = Column(Text, nullable=True)
    remarks = Column(Text, nullable=True)


class EpChiefComplaints(BaseModel):
    __tablename__ = "ep_chief_complaints"
    ep_id = Column(Integer, ForeignKey("eprescriptions.id"))
    chief_complaints = Column(String(255), nullable=False)


class EpHistory(BaseModel):
    __tablename__ = "ep_histories"
    ep_id = Column(Integer, ForeignKey("eprescriptions.id"))
    history_type = Column(String(255), nullable=False)
    history = Column(String(255), nullable=False)


class EpCoMorbidity(BaseModel):
    __tablename__ = "ep_co_morbidity"
    ep_id = Column(Integer, ForeignKey("eprescriptions.id"))
    cm_type = Column(String(255), nullable=False)
    remarks = Column(String(255), nullable=False)


class EpOnExamination(BaseModel):
    __tablename__ = "ep_on_examinations"
    ep_id = Column(Integer, ForeignKey("eprescriptions.id"))
    patient_indicator_id = Column(Integer, ForeignKey("patient_indicators.id"))


class EpInvestigation(BaseModel):
    __tablename__ = "ep_investigations"
    ep_id = Column(Integer, ForeignKey("eprescriptions.id"))
    investigation = Column(String(255), nullable=False)


class EpDiagnosis(BaseModel):
    __tablename__ = "ep_diagnosis"
    ep_id = Column(Integer, ForeignKey("eprescriptions.id"))
    diagnosis_type = Column(String(255), nullable=False)
    diagnosis =  Column(String(255), nullable=False)


class EpMedicine(BaseModel):
    __tablename__ = "ep_medicines"
    ep_id = Column(Integer, ForeignKey("eprescriptions.id"))
    name = Column(String(255), nullable=False)
    generic = Column(String(255), nullable=False)
    pharmaceuticals = Column(String(255), nullable=False)
    form = Column(String(255), nullable=False)
    strength = Column(String(255), nullable=False)    
    doses = Column(String(100), nullable=True)
    before_after = Column(String(100), nullable=True)
    days = Column(Integer, nullable=True)
    remarks = Column(String(255), nullable=True)


class EpAdvices(BaseModel):
    __tablename__ = "ep_advices"
    ep_id = Column(Integer, ForeignKey("eprescriptions.id"))
    advice = Column(String(255), nullable=False)


class EpNextFollowUp(BaseModel):
    __tablename__ = "ep_next_follow_up"
    ep_id = Column(Integer, ForeignKey("eprescriptions.id"))
    date = Column(Date, nullable=False)


class EpDoctorRefer(BaseModel):
    __tablename__ = "ep_doctor_refer"
    ep_id = Column(Integer, ForeignKey("eprescriptions.id"))
    detail = Column(Text, nullable=False)


# ============================================================ #

class EpMedicineList(BaseModel):
    __tablename__ = "ep_medicine_list"
    name = Column(String(255), nullable=False)
    generic = Column(String(255), nullable=False)
    form = Column(String(255), nullable=False)
    strength = Column(String(255), nullable=False)
    pharmaceuticals = Column(String(255), nullable=False)
    unit_type = Column(String(100), nullable=True)
    unit_price = Column(Float, nullable=True)
    add_status = Column(String(100), nullable=True)
    added_by_id = Column(Integer, nullable=True)



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

#==================================#
#  Pharmaceuticals Related Models  #
#==================================#

class Pharmaceuticals(BaseModel):
    __tablename__ = "pharmaceuticals"
    name = Column(String(255), nullable = False)
    established = Column(String(255), nullable = True)
    details = Column(Text, nullable = True)
    contact_phone = Column(String(255), nullable = True)
    contact_email = Column(String(255), nullable = True)
    address = Column(String(255), nullable = True)
    total_generics = Column(Integer, nullable = True)
    total_brands = Column(Integer, nullable = True)
    contact_person = Column(String(255), nullable = True)
    contact_person_phone = Column(String(255), nullable = True)
    contact_person_email = Column(String(255), nullable = True)



class PharmaceuticalsUser(BaseModel):
    __tablename__ = "pharmaceuticals_user"
    user_id = Column(Integer, ForeignKey("users.id"))
    phr_id = Column(Integer, ForeignKey("pharmaceuticals.id"))



class PharmaceuticalsNameList(BaseModel):
    __tablename__ = "pharmaceuticals_name_list"
    name = Column(String(255), nullable = False)
    details = Column(Text, nullable = True)
    remarks = Column(Text, nullable = True)


#===================#
#  Pharmacy Models  #  
#===================#

class Pharmacy(BaseModel):
    __tablename__ = "pharmacy"
    name = Column(String(255), nullable = False)
    trade_license = Column(String(255), nullable = True)
    detail_address = Column(Text, nullable = True)
    district = Column(String(255), nullable = True)
    sub_district = Column(String(255), nullable = True)
    drug_license = Column(String(255), nullable = True)
    pharmacy_is_active = Column(Boolean, nullable=False)

class PharmacyUser(BaseModel):
    __tablename__ = "pharmacy_user"
    user_id = Column(Integer, ForeignKey("users.id"))
    pharmacy_id = Column(Integer, ForeignKey("pharmacy.id"))

# Purchase Order

class PharmacyPurchaseOrder(BaseModel):
    __tablename__ = "pharmacy_purchase_order"
    total_amount_dp = Column(Float, nullable = True)
    discount = Column(Float, nullable = True)
    discount_amount = Column(Float, nullable = True)
    payable_amount = Column(Float, nullable = True)
    paid_amount = Column(Float, nullable = True)
    due_amount = Column(Float, nullable = True)
    subtotal_amount = Column(Float, nullable = True)
    pharmaceuticals_name_id = Column(Integer, nullable = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    pharmacy_id = Column(Integer, ForeignKey("pharmacy.id"))
    purchase_number = Column(String(100), nullable = True)
    remarks = Column(Text, nullable = True)
    expected_delivery_date = Column(Date, nullable = True)
    delivery_status = Column(String(100), nullable=True)

# Purchase Single Order

class PharmacyPurchaseSingleOrder(BaseModel):
    __tablename__ = "pharmacy_purchase_single_order"
    quantity = Column(Integer, nullable = True)
    unit_price_dp = Column(Float, nullable = True)
    total_price_dp = Column(Float, nullable = True)
    discount = Column(Float, nullable = True)
    discount_amount = Column(Float, nullable = True)
    payable_prize_dp = Column(Float, nullable = True)
    purchase_order_id = Column(Integer, ForeignKey("pharmacy_purchase_order.id"))
    medicine_id = Column(Integer, nullable = False)
    pack_size = Column(String(100), nullable = True)

# Goods Received Note (GRN)

class PharmacyGrn(BaseModel):
    __tablename__ = "pharmacy_grn"
    total_amount_dp = Column(Float, nullable = True)
    grn_number = Column(String(100), nullable = True)
    total_amount_mrp = Column(Float, nullable = True)
    total_vat_mrp = Column(Float, nullable = True)
    total_discount_mrp = Column(Float, nullable = True)
    discount_amount = Column(Float, nullable = True)
    total_cost_mrp = Column(Float, nullable = True)
    pharmaceuticals_name_id = Column(Integer, nullable = True)
    purchase_order_id = Column(Integer, ForeignKey("pharmacy_purchase_order.id"))
    pharmacy_id = Column(Integer, ForeignKey("pharmacy.id"))
    paid_amount = Column(Float, nullable = True)
    due_amount = Column(Float, nullable = True)

# Single GRN

class PharmacySingleGrn(BaseModel):
    __tablename__ = "pharmacy_single_grn"
    dp_prize = Column(Float, nullable = True)
    quantity = Column(Integer, nullable = True)
    mrp = Column(Float, nullable = True)
    vat = Column(Float, nullable = True)
    discount = Column(Float, nullable = True)
    discount_amount = Column(Float, nullable = True)
    cost = Column(Float, nullable = True)
    expiry_date = Column(Date, nullable = True)
    batch_number = Column(String(100), nullable = True)
    grn_id = Column(Integer, ForeignKey("pharmacy_grn.id"))
    medicine_id = Column(Integer, nullable = False)
    pack_size = Column(String(100), nullable = True)

# Every Single Stock

class PharmacyEverySingleStock(BaseModel):
    __tablename__ = "pharmacy_every_single_stock"
    quantity = Column(Integer, nullable = True)
    expiry_date = Column(Date, nullable = True)
    batch_number = Column(String(100), nullable = True)
    medicine_id = Column(Integer, nullable = False)
    pack_size = Column(String(100), nullable = True)
    single_grn_id = Column(Integer, ForeignKey("pharmacy_single_grn.id"))
    pharmacy_id = Column(Integer, ForeignKey("pharmacy.id"))

# Total Current Stock

class PharmacyTotalCurrentStock(BaseModel):
    __tablename__ = "pharmacy_total_current_stock"
    quantity = Column(Integer, nullable = True)
    medicine_id = Column(Integer, nullable = False)
    pharmacy_id = Column(Integer, ForeignKey("pharmacy.id"))


# Invoice Order

class PharmacyInvoice(BaseModel):
    __tablename__ = "pharmacy_invoice"
    subtotal_amount = Column(Float, nullable = True)
    total_amount_mrp = Column(Float, nullable = True)
    total_amount = Column(Float, nullable = True)
    paid_amount = Column(Float, nullable = True)
    due_amount = Column(Float, nullable = True)
    remarks = Column(Text, nullable = True)
    discount = Column(Float, nullable = True)
    discount_amount = Column(Float, nullable = True)
    vat = Column(Float, nullable = True)
    invoice_number = Column(String(100), nullable = True)
    customer_id = Column(Integer, nullable = False)
    pharmacy_id = Column(Integer, ForeignKey("pharmacy.id"))


# Single Invoice Order

class PharmacySingleInvoice(BaseModel):
    __tablename__ = "pharmacy_single_invoice"
    mrp = Column(Float, nullable = True)
    quantity = Column(Integer, nullable = True)
    unit_prize = Column(Float, nullable = True)
    discount = Column(Float, nullable = True)
    discount_amount = Column(Float, nullable = True)
    cost = Column(Float, nullable = True)
    medicine_id = Column(Integer, nullable = False)
    pack_size = Column(String(100), nullable = True)
    invoice_id = Column(Integer, ForeignKey("pharmacy_invoice.id"))


# Pharmacy Activity


class PharmacyActivity(BaseModel):
    __tablename__ = "pharmacy_activity"
    pharmacy_id = Column(Integer, ForeignKey("pharmacy.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    service_name = Column(String(100), nullable=True)
    service_received_id = Column(Integer, nullable=True)
    remark = Column(String(255), nullable=True)


#=========================#
#  Clinic Related Models  #
#=========================#

class Clinic(BaseModel):
    __tablename__ = "clinic"
    name = Column(String(255), nullable = False)
    clinic_license = Column(String(100), nullable = True)
    detail_address = Column(Text, nullable = True)
    district = Column(String(255), nullable = True)
    sub_district = Column(String(255), nullable = True)
    contact_phone = Column(String(255), nullable = True)
    contact_email = Column(String(255), nullable = True)
    clinic_is_active = Column(Boolean, nullable=False)


# Clinic User 
class ClinicUser(BaseModel):
    __tablename__ = "clinic_user"
    user_id = Column(Integer, ForeignKey("users.id"))
    clinic_id = Column(Integer, ForeignKey("clinic.id"))


# Clinic Details
class ClinicDetails(BaseModel):
    __tablename__ = "clinic_details"
    clinic_id = Column(Integer, ForeignKey("clinic.id"))
    logo_image_id = Column(Integer, nullable=True)
    title = Column(String(255), nullable = False)
    sub_title = Column(Text, nullable = True)
    title_bg_image_id = Column(Integer, nullable=True)
    about = Column(Text, nullable = False)
    about_image_id = Column(Integer, nullable=True)
    contact_us = Column(Text, nullable = True)
    starting_time = Column(Time, nullable = True)
    ending_time = Column(Time, nullable = True)
    footer = Column(Text, nullable = True)


# Clinic Navbar
class ClinicNavbar(BaseModel):
    __tablename__ = "clinic_navbar"
    clinic_id = Column(Integer, ForeignKey("clinic.id"))
    nav_text = Column(String(255), nullable = True)
    nav_href = Column(Text, nullable = True)


# Clinic Service

class ClinicServices(BaseModel):
    __tablename__ = "clinic_service"
    clinic_id = Column(Integer, ForeignKey("clinic.id"))
    servive_name =  Column(String(255), nullable = True)
    service_details = Column(Text, nullable = True)
    service_price = Column(Float, nullable = True)
    image_id = Column(Integer, nullable=True)


# Clinic Offer

class ClinicOffer(BaseModel):
    __tablename__ = "clinic_offer"
    clinic_id = Column(Integer, ForeignKey("clinic.id"))
    offer_name =  Column(String(255), nullable = True)
    offer_details = Column(Text, nullable = True)
    offer_price = Column(Float, nullable = True)
    image_id = Column(Integer, nullable=True)


 # Clinic With Doctor

class ClinicWithDoctor(BaseModel):
    __tablename__ = "clinic_with_doctor"
    clinic_id = Column(Integer, ForeignKey("clinic.id"))
    doctor_id = Column(Integer, ForeignKey("users.id"))


# Clinic Activity


class ClinicActivity(BaseModel):
    __tablename__ = "clinic_activity"
    clinic_id = Column(Integer, ForeignKey("clinic.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    service_name = Column(String(100), nullable=True)
    service_received_id = Column(Integer, nullable=True)
    remark = Column(String(255), nullable=True)