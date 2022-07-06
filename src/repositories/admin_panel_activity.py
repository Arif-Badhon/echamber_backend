from sqlalchemy import desc
from sqlalchemy.orm import Session
from models import AdminPanelActivity
from repositories import BaseRepo
from .users import users_repo
from schemas import AdminPanelActivityIn, AdminPanelActivityUpdate


class AdminPanelActivityRepo(BaseRepo[AdminPanelActivity, AdminPanelActivityIn, AdminPanelActivityUpdate]):

    def activity_log(self, db: Session, user_id: int, skip: int = 0, limit: int = 15):
        activity = db.query(self.model).filter(self.model.user_id == user_id).order_by(desc(self.model.created_at)).offset(skip).limit(limit).all()
        activity_all = db.query(self.model).filter(
            self.model.user_id == user_id).order_by(desc(self.model.created_at)).all()
        return [{"results": len(activity_all)}, activity]

    def get_user_id_service(self, db: Session, user_id: int, service_name: str, skip: int = 0, limit: int = 15):
        users_activity = db.query(
            self.model).filter(
            self.model.user_id == user_id).filter(
            self.model.service_name == service_name).order_by(
            desc(self.model.created_at)).offset(skip).limit(limit).all()

        users_activity_all = db.query(
            self.model).filter(
            self.model.user_id == user_id).filter(
            self.model.service_name == service_name).order_by(
            desc(self.model.created_at)).all()
        return [{"results": len(users_activity_all)}, users_activity]

    def actiity_log_all(self, db: Session, skip: int = 0, limit: int = 15):
        activity_all = db.query(self.model).order_by(
            desc(self.model.created_at)).all()
        activity = db.query(self.model).order_by(
            desc(self.model.created_at)).offset(skip).limit(limit).all()
        activity_data = []

        for i in activity:
            user_name = users_repo.get_one(db=db, id=i.user_id).name
            user_phone = users_repo.get_one(db=db, id=i.user_id).phone
            i.user_name = user_name
            i.user_phone = user_phone
            activity_data.append(i)

        results = len(activity_all)
        return [{"results": results}, activity_data]


admin_panel_activity_repo = AdminPanelActivityRepo(AdminPanelActivity)
