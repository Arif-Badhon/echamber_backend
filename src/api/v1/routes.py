from fastapi import APIRouter

from schemas import notice
from .endpoints import admin, corporate_partners, df_post, follow_up, notice, review, service_order, health_plan, telemedicine, doctor_chambers, doctors_search, doctor_schedules, users, roles, doctors, patients, user_details, patient_indicators, patient_reports, patient_families, eprescription, ep_medicines, ep_chief_complaints, ep_investigations, ep_advices, mediva_device_catagories, mediva_devices

api_router = APIRouter()

# fmt: off
api_router.include_router(users.router, prefix='', tags=['Users'])
api_router.include_router(user_details.router, prefix='/user/details', tags=['User Details'])
api_router.include_router(roles.router, prefix='/roles', tags=['Roles'])
api_router.include_router(admin.router, prefix='/admin', tags=['Admin'])
api_router.include_router(corporate_partners.router, prefix='/corporate', tags=['Corporate Partners'])
api_router.include_router(notice.router, prefix='/notice', tags=['Notice'])
api_router.include_router(review.router, prefix='/review', tags=['Review'])
api_router.include_router(service_order.router, prefix='/service', tags=['Service Order'])
api_router.include_router(follow_up.router, prefix='/follow-up', tags=['Follow-up'])
api_router.include_router(mediva_device_catagories.router, prefix='/mediva/device/catagories', tags=['Mediva Device Catagories'])
api_router.include_router(mediva_devices.router, prefix='/mediva/devices', tags=['Mediva Devices'])
api_router.include_router(health_plan.router, prefix='/health-plan', tags=['Health Plan'])
api_router.include_router(telemedicine.router, prefix='/telemedicine', tags=['Telemedicine'])
api_router.include_router(doctors.router, prefix='/doctors', tags=['Doctors'])
api_router.include_router(doctor_chambers.router, prefix='/doctors/chamber', tags=['Doctor\'s Chamber'])
api_router.include_router(doctors_search.router, prefix='/doctors/search', tags=['Doctor Search'])
api_router.include_router(doctor_schedules.router, prefix='/doctor/schedules', tags=['Doctor Schedules'])
api_router.include_router(df_post.router, prefix='/doctor/forum', tags=['Doctor Forum'])
api_router.include_router(patients.router, prefix='/patients', tags=['Patients'])
api_router.include_router(patient_indicators.router, prefix='/patient/indicators', tags=['Patient Indicators'])
api_router.include_router(patient_reports.router, prefix='/patient/reports', tags=['Patients Report'])
api_router.include_router(patient_families.router, prefix='/patient/family', tags=['Patient\'s family'])
api_router.include_router(eprescription.router, prefix='/ep', tags=['E-Prescription'])
api_router.include_router(ep_medicines.router, prefix='/medicines', tags=['Medicines'])
api_router.include_router(ep_chief_complaints.router, prefix='/chief-complaints', tags=['Chief Complaints'])
api_router.include_router(ep_investigations.router, prefix='/investigations', tags=['Investigations'])
api_router.include_router(ep_advices.router, prefix='/advices', tags=['Advices'])
