from fastapi import APIRouter

from schemas import notice
from .endpoints import admin, corporate_partners, notice, service_order, health_plan, doctor_chambers, doctors_search, doctor_schedules, users, roles, doctors, patients, user_details, patient_indicators, patient_reports, patient_families, eprescription, ep_medicines, ep_chief_complaints, ep_investigations, ep_advices

api_router = APIRouter()

# fmt: off
api_router.include_router(users.router, prefix='', tags=['Users'])
api_router.include_router(user_details.router, prefix='/user/details', tags=['User Details'])
api_router.include_router(roles.router, prefix='/roles', tags=['Roles'])
api_router.include_router(admin.router, prefix='/admin', tags=['Admin'])
api_router.include_router(corporate_partners.router, prefix='/corporate', tags=['Corporate Partners'])
api_router.include_router(notice.router, prefix='/notice', tags=['Notice'])
api_router.include_router(service_order.router, prefix='/service', tags=['Service Order'])
api_router.include_router(health_plan.router, prefix='/health-plan', tags=['Health Plan'])
api_router.include_router(doctors.router, prefix='/doctors', tags=['Doctors'])
api_router.include_router(doctor_chambers.router, prefix='/doctors/chamber', tags=['Doctor\'s Chamber'])
api_router.include_router(doctors_search.router, prefix='/doctors/search', tags=['Doctor Search'])
api_router.include_router(doctor_schedules.router, prefix='/doctor/schedules', tags=['Doctor Schedules'])
api_router.include_router(patients.router, prefix='/patients', tags=['Patients'])
api_router.include_router(patient_indicators.router, prefix='/patient/indicators', tags=['Patient Indicators'])
api_router.include_router(patient_reports.router, prefix='/patient/reports', tags=['Patients Report'])
api_router.include_router(patient_families.router, prefix='/patient/family', tags=['Patient\'s family'])
api_router.include_router(eprescription.router, prefix='/ep', tags=['E-Prescription'])
api_router.include_router(ep_medicines.router, prefix='/medicines', tags=['Medicines'])
api_router.include_router(ep_chief_complaints.router, prefix='/chief-complaints', tags=['Chief Complaints'])
api_router.include_router(ep_investigations.router, prefix='/investigations', tags=['Investigations'])
api_router.include_router(ep_advices.router, prefix='/advices', tags=['Advices'])