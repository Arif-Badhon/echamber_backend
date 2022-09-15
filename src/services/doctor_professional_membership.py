from repositories import doctor_professional_membership_repo
from services import BaseService
from models import DoctorProfessionalMembership
from schemas import DoctorProfessionalMembershipIn, DoctorProfessioanlMembershipUpdate


doctor_professional_membership_service = BaseService[DoctorProfessionalMembership, DoctorProfessionalMembershipIn,
                                                     DoctorProfessioanlMembershipUpdate](DoctorProfessionalMembership, doctor_professional_membership_repo)
