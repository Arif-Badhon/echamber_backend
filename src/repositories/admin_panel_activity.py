from sqlalchemy.orm import Session
from models import AdminPanelActivity
from repositories import BaseRepo
from schemas import AdminPanelActivityIn, AdminPanelActivityUpdate


class AdminPanelActivityRepo(BaseRepo[AdminPanelActivity, AdminPanelActivityIn, AdminPanelActivityUpdate]):

    def activity_log(self, db: Session, user_id:int, skip: int = 0, limit: int = 15):
        activity = db.query(self.model).filter(self.model.user_id == user_id).order_by(self.model.created_at).offset(skip).limit(limit).all()
        return activity


admin_panel_activity_repo = AdminPanelActivityRepo(AdminPanelActivity)