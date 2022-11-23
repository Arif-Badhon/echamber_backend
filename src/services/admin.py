from exceptions.service_result import handle_result
from services import BaseService
from .user_details import user_details_service
from .doctors import doctors_service
from .image_log import image_log_service
from .doctor_qualifications import doctor_qualifications_service
from .doctor_specialities import doctor_specialities_service
from .patient_indicators import patient_indicators_service
from .doctor_workplace import doctor_workplace_service
from .users import users_service
from schemas import UserCreate, UserUpdate, AdminPanelActivityIn, UserDetailIn, PatientIndicatorIn, DoctorSignup, DoctorIn, DoctorQualilficationIn, DoctorSpecialityIn, DoctorWorkPlaceIn
from models import User
from repositories import admin_repo, roles_repo, admin_panel_activity_repo, users_repo, corporate_partner_user_repo, corporate_partners_repo
from sqlalchemy.orm import Session
from exceptions import ServiceResult, AppException
from fastapi import status
from .sms import sms_service


class Admin(BaseService[User, UserCreate, UserUpdate]):

    def signup_admin(self, db: Session, data_in: UserCreate):

        admin_id = roles_repo.search_name_id(db, name='admin')

        admin_exist = self.repo.search_by_role_id(db, id=admin_id)

        if not admin_exist:
            sginup_data = UserCreate(
                name=data_in.name,
                email=data_in.email,
                phone=data_in.phone,
                sex=data_in.sex,
                is_active=True,
                password=data_in.password,
                role_name='admin'
            )

            signup_admin = users_service.signup(
                db, data_in=sginup_data, flush=False)

            return signup_admin

        return ServiceResult(AppException.ServerError('Admin exist'))

    def password_changed_by_admin(self, db: Session, user_id: int, password: str, changer_id):
        pass_change = users_service.new_password(db=db, user_id=user_id, data_update=password)

        if not pass_change:
            return ServiceResult(AppException.ServerError(
                "Problem with password change."))
        else:
            pass_change_data = AdminPanelActivityIn(
                user_id=changer_id,
                service_name="password_change",
                service_recived_id=user_id,
                remark=""
            )

            created_by_employee = admin_panel_activity_repo.create(db=db, data_in=pass_change_data)

            if not created_by_employee:
                return ServiceResult(AppException.ServerError("Problem with patient by patient registration."))
            else:
                return ServiceResult(created_by_employee, status_code=status.HTTP_201_CREATED)

    def role_change(self, db: Session, id: int, user_id: int, role_name: str):
        role_id = roles_repo.search_name_id(db=db, name=role_name)
        user_role = users_repo.update(db=db, id=id, data_update=UserUpdate(role_id=role_id))

        if not user_role:
            return ServiceResult(AppException.NotAccepted())
        else:
            role_change_data = AdminPanelActivityIn(
                user_id=user_id,
                service_name="role_change",
                service_recived_id=id,
                remark=f"role change into - {role_name}"
            )

            created_by_admin = admin_panel_activity_repo.create(db=db, data_in=role_change_data)

            if not created_by_admin:
                return ServiceResult(AppException.ServerError("Problem with role change activity"))
            else:
                return ServiceResult(created_by_admin, status_code=status.HTTP_201_CREATED)

    def user_active_switcher(self, db: Session, id: int):
        data = self.repo.user_active_switcher(db=db, id=id)

        if not data:
            return ServiceResult(AppException.ServerError("User active status not changed"))
        else:
            return ServiceResult(data, status_code=status.HTTP_201_CREATED)

    def activity_log(self, db: Session, user_id: int, skip: int = 0, limit: int = 15):
        activity = admin_panel_activity_repo.activity_log(db=db, user_id=user_id, skip=skip, limit=limit)

        if not activity:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        else:
            return ServiceResult(activity, status_code=status.HTTP_201_CREATED)

    def get_user_id_service(self, db: Session, user_id: int, service_name: str, skip: int = 0, limit: int = 15):
        activity = admin_panel_activity_repo.get_user_id_service(db=db, user_id=user_id, service_name=service_name, skip=skip, limit=limit)

        if not activity[1]:
            return ServiceResult([{"results": 0}, []], status_code=status.HTTP_200_OK)
        else:
            return ServiceResult(activity, status_code=status.HTTP_200_OK)

    def activity_log_all(self, db: Session, skip: int = 0, limit: int = 15):
        activity_all = admin_panel_activity_repo.actiity_log_all(db=db, skip=skip, limit=limit)

        if not activity_all:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        else:
            return ServiceResult(activity_all, status_code=status.HTTP_201_CREATED)

    def signup_employee(self, db: Session, data_in: UserCreate, creator_id: int):

        sginup_data = UserCreate(
            name=data_in.name,
            email=data_in.email,
            phone=data_in.phone,
            sex=data_in.sex,
            is_active=True,
            password=data_in.password,
            role_name=data_in.role_name
        )

        signup_employee = users_service.signup(
            db, data_in=sginup_data, flush=True)

        created_by_employee_data = AdminPanelActivityIn(
            user_id=creator_id,
            service_name="employee_register",
            service_recived_id=handle_result(signup_employee).id,
            remark=""
        )

        created_by_employee = admin_panel_activity_repo.create(db=db, data_in=created_by_employee_data)

        if not created_by_employee:
            return ServiceResult(AppException.ServerError(
                "Problem with employee registration."))
        else:
            return ServiceResult(created_by_employee, status_code=status.HTTP_201_CREATED)

    def all_employee(self, db: Session, skip: int = 0, limit: int = 10):
        all_emp = self.repo.all_employee(db=db, skip=skip, limit=limit, is_active=True)
        for i in all_emp[1]:
            i.role_name = roles_repo.get_one(db=db, id=i.role_id).name
        if not all_emp:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        else:
            return ServiceResult(all_emp, status_code=status.HTTP_200_OK)

    def deactive_employee(self, db: Session, skip: int = 0, limit: int = 10):
        all_emp = self.repo.all_employee(db=db, skip=skip, limit=limit, is_active=False)
        for i in all_emp[1]:
            i.role_name = roles_repo.get_one(db=db, id=i.role_id).name
        if not all_emp:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        else:
            return ServiceResult(all_emp, status_code=status.HTTP_200_OK)

    def doctor_register(self, db: Session, data_in: DoctorSignup, creator_id: int):
        sginup_data = UserCreate(
            name=data_in.name,
            email=data_in.email,
            phone=data_in.phone,
            sex=data_in.sex,
            is_active=True,
            password=data_in.password,
            role_name='doctor'
        )

        signup_user = users_service.signup(db, data_in=sginup_data, flush=True)

        doctor_data = DoctorIn(
            user_id=handle_result(signup_user).id,
            dr_title=data_in.dr_title,
            bmdc=data_in.bmdc
        )

        doctor_user = doctors_service.create_with_flush(db, data_in=doctor_data)

        if data_in.institute != '':
            doctor_workplace = doctor_workplace_service.create_with_flush(db=db, data_in=DoctorWorkPlaceIn(
                institute=data_in.institute, position=data_in.position, top_priority=True, start_date=data_in.start_date, end_date=data_in.end_date))

        qualification_data = DoctorQualilficationIn(
            user_id=handle_result(signup_user).id,
            qualification=data_in.qualification
        )

        qualification_user = doctor_qualifications_service.create_with_flush(
            db, data_in=qualification_data)

        specialities_data = DoctorSpecialityIn(
            user_id=handle_result(signup_user).id,
            speciality=data_in.speciality
        )

        specialities_user = doctor_specialities_service.create_with_flush(
            db, data_in=specialities_data)

        created_by_employee_data = AdminPanelActivityIn(
            user_id=creator_id,
            service_name="doctor_register",
            service_recived_id=handle_result(signup_user).id,
            remark=""
        )

        created_by_employee = admin_panel_activity_repo.create(db=db, data_in=created_by_employee_data)

        if not created_by_employee:
            return ServiceResult(AppException.ServerError("Problem with doctor registration."))
        else:
            s = sms_service.send_sms(sms_to='88' + data_in.phone, sms="অভিনন্দন " + data_in.name +
                                     " HEALTHx এর Smart Doctor পোর্টালে আপনার  Digital Profile তৈরী সম্পন্ন হয়েছে। \n\n লগ-ইন তথ্য: \n ইউজার আইডি : " + data_in.phone + "\nপাসওয়ার্ড: " + data_in.password + "\n" +
                                     "doc.healthxbd.com এ লগ-ইন করে পাসওয়ার্ডটি পরিবর্তন করে সাজিয়ে নিন নিজের প্রোফাইল আর ছড়িয়ে দিন আপনার পরিচিতি দেশব্যাপী। \n- ধন্যবাদ\n\nHEALTHx\n +8801571016461")

            return ServiceResult(created_by_employee, status_code=status.HTTP_201_CREATED)

    def doctor_active_list(self, db: Session, skip: int = 0, limit: int = 10):
        all_doc = self.repo.doctors_active_list(db, skip, limit)

        data_with_images = []
        for i in all_doc[1]:
            doc_image_serve = image_log_service.get_by_two_key(db=db, skip=0, limit=100, descending=True, count_results=False, user_id=i.User.id, service_name='propic')
            doc_images = handle_result(doc_image_serve)

            i.Doctor.images = doc_images
            data_with_images.append(i)

        data = [{"results": all_doc[0]["results"]}, data_with_images]

        if not all_doc:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        else:
            return ServiceResult(data, status_code=status.HTTP_200_OK)

    def doctor_inactive_list(self, db: Session, skip: int = 0, limit: int = 10):
        all_doc = self.repo.doctors_inactive_list(db, skip, limit)

        data_with_images = []
        for i in all_doc[1]:
            doc_image_serve = image_log_service.get_by_two_key(db=db, skip=0, limit=100, descending=True, count_results=False, user_id=i.User.id, service_name='propic')
            doc_images = handle_result(doc_image_serve)

            i.Doctor.images = doc_images
            data_with_images.append(i)

        data = [{"results": all_doc[0]["results"]}, data_with_images]

        if not all_doc:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        else:
            return ServiceResult(data, status_code=status.HTTP_200_OK)

    def doctor_active_id(self, db: Session, id: int):
        active = self.repo.doctor_active_by_id(db, id)
        doc = self.get_one(db, id)
        s = sms_service.send_sms(sms_to='88' + handle_result(doc).phone, sms='অভিনন্দন, ' + handle_result(doc).name +
                                 ' - HEALTHx এর SMART DOCTOR পোর্টালে আপনার DIGITAL PROFILE টি ACTIVE হয়েছে। লগ ইন করে প্রোফাইলটি কমপ্লিট করুন, আর ছড়িয়ে দিন আপনার পরিচিতি দেশব্যাপী। -ধন্যবাদ')

        return doc

    def signup_patient(self, db: Session, data_in: UserCreate, creator_id: int):
        singnup_data = UserCreate(
            name=data_in.name,
            email=data_in.email,
            phone=data_in.phone,
            sex=data_in.sex,
            is_active=True,
            password=data_in.password,
            role_name='patient'
        )

        signup_user = users_service.signup(
            db, data_in=singnup_data, flush=True)

        user_details_data = UserDetailIn(
            user_id=handle_result(signup_user).id,
            country="",
            division="",
            district="",
            sub_district="",
            post_code="",
            dob=None
        )

        ud = user_details_service.create(db, data_in=user_details_data)

        if not ud:
            return ServiceResult(AppException.ServerError(
                "Problem with patient registration."))
        else:
            created_by_employee_data = AdminPanelActivityIn(
                user_id=creator_id,
                service_name="patient_register",
                service_recived_id=handle_result(ud).user_id,
                remark=""
            )

            created_by_employee = admin_panel_activity_repo.create(db=db, data_in=created_by_employee_data)

            if not created_by_employee:
                return ServiceResult(AppException.ServerError("Problem with patient registration."))
            else:
                s = sms_service.send_sms(
                    sms_to='88' + data_in.phone, sms='অভিনন্দন, ' + data_in.name + ' - HEALTHx এর My Health পোর্টালে আপনার রেজিস্ট্রেশন সম্পন্ন হয়েছে। আপনার পাসওয়ার্ড ' + data_in.password +
                    ' আপনি user.healthxbd.com এ লগ ইন  হয়ে সুরক্ষার স্বার্থে পাসওয়ার্ডটি চেঞ্জ করে নিন। - ধন্যবাদ')
                return ServiceResult(created_by_employee, status_code=status.HTTP_201_CREATED)

    def patient_user_update(self, id: int, data_update: UserUpdate, user_id: int, db: Session):
        users_service.update(id=id, data_update=data_update, db=db)

        created_by_employee_data = AdminPanelActivityIn(
            user_id=user_id,
            service_name="patient_user_data_update",
            service_recived_id=id,
            remark=""
        )

        created_by_employee = admin_panel_activity_repo.create(db=db, data_in=created_by_employee_data)

        if not created_by_employee:
            return ServiceResult(AppException.ServerError("Problem with patient user data uupdate."))
        else:
            return ServiceResult(created_by_employee, status_code=status.HTTP_201_CREATED)

    def all_patient(self, db: Session, phone_number: str, skip: int, limit: int):
        patients = admin_repo.all_patient(db=db, phone_number=phone_number, skip=skip, limit=limit)

        new_patients_list = []

        for i in patients[1]:

            register_by = admin_repo.patient_register_by_whom(db=db, patient_id=i.id)

            if register_by:
                register_detail = users_repo.get_one(db=db, id=register_by.user_id)
                i.register_by_id = register_by.user_id
                i.register_by_name = register_detail.name
                i.register_by_role = roles_repo.get_one(db=db, id=register_detail.role_id).name
            else:
                i.register_by_id = None
                i.register_by_name = None
                i.register_by_role = None

            # is he/she corporate
            corporate = corporate_partner_user_repo.search_user_id(db=db, id=i.id)
            if corporate:
                comp_name = corporate_partners_repo.get_one(db=db, id=corporate.corporate_id)
                i.company_name = comp_name.name
            else:
                i.company_name = None

            new_patients_list.append(i)

            patients[1] = new_patients_list

        if not patients:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        else:
            return ServiceResult(patients, status_code=status.HTTP_201_CREATED)

    def all_patient_filter(self, db: Session,  hx_user_id: int, name: str, phone: str, gender: str, skip: int, limit: int):
        patients = self.repo.all_patient_filter(db=db,  hx_user_id=hx_user_id, name=name, phone=phone, gender=gender, skip=skip, limit=limit)

        new_patients_list = []

        for i in patients[1]:

            register_by = admin_repo.patient_register_by_whom(db=db, patient_id=i.id)

            if register_by:
                register_detail = users_repo.get_one(db=db, id=register_by.user_id)
                i.register_by_id = register_by.user_id
                i.register_by_name = register_detail.name
                i.register_by_role = roles_repo.get_one(db=db, id=register_detail.role_id).name
            else:
                i.register_by_id = None
                i.register_by_name = None
                i.register_by_role = None

            # is he/she corporate
            corporate = corporate_partner_user_repo.search_user_id(db=db, id=i.id)
            if corporate:
                comp_name = corporate_partners_repo.get_one(db=db, id=corporate.corporate_id)
                i.company_name = comp_name.name
            else:
                i.company_name = None

            new_patients_list.append(i)

            patients[1] = new_patients_list

        if not patients:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        else:
            return ServiceResult(patients, status_code=status.HTTP_201_CREATED)

    def patient_indicators(self, db: Session, user_id: int, data_in: PatientIndicatorIn, creator_id: int):
        data = patient_indicators_service.create_by_user_id(db, user_id, data_in)

        if not data:
            return ServiceResult(AppException.ServerError(
                "Problem with patient indicators."))
        else:
            created_by_employee_data = AdminPanelActivityIn(
                user_id=creator_id,
                service_name="patient_indicator_input",
                service_recived_id=handle_result(data).user_id,
                remark=""
            )

            created_by_employee = admin_panel_activity_repo.create(db=db, data_in=created_by_employee_data)

            if not created_by_employee:
                return ServiceResult(AppException.ServerError("Problem with patient by indicator."))
            else:
                return ServiceResult(created_by_employee, status_code=status.HTTP_201_CREATED)


    def pharmacy_active_list(self, db: Session, skip: int, limit: int):
        data = self.repo.pharmacy_active_list(db=db, skip=skip, limit=limit)
        if not data:
            return ServiceResult(AppException.ServerError("no active pharmacy"))
        else:
            return ServiceResult(data, status_code=status.HTTP_201_CREATED)

    def pharmacy_inactive_list(self, db: Session, skip: int, limit: int):
        data = self.repo.pharmacy_inactive_list(db=db, skip=skip, limit=limit)
        if not data:
            return ServiceResult(AppException.ServerError("no inactive pharmacy"))
        else:
            return ServiceResult(data, status_code=status.HTTP_201_CREATED)
    
    def pharmacy_active_switcher(self, db: Session, id: int):
        data = self.repo.pharmacy_active_switcher(db=db, id=id)

        if not data:
            return ServiceResult(AppException.ServerError("Pharmacy active status not changed"))
        else:
            return ServiceResult(data, status_code=status.HTTP_201_CREATED)


admin_service = Admin(User, admin_repo)
