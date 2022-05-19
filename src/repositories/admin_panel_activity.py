from sqlalchemy import desc
from sqlalchemy.orm import Session
from models import AdminPanelActivity
from repositories import BaseRepo
from .users import users_repo
from schemas import AdminPanelActivityIn, AdminPanelActivityUpdate


class AdminPanelActivityRepo(BaseRepo[AdminPanelActivity, AdminPanelActivityIn, AdminPanelActivityUpdate]):

    def activity_log(self, db: Session, user_id:int, skip: int = 0, limit: int = 15):
        activity = db.query(self.model).filter(self.model.user_id == user_id).order_by(desc(self.model.created_at)).offset(skip).limit(limit).all()
        activity_all = db.query(self.model).filter(self.model.user_id == user_id).order_by(desc(self.model.created_at)).all()
        return [{"results": len(activity_all)}, activity]

    def actiity_log_all(self, db: Session, skip: int = 0, limit: int = 15):
        activity_all = db.query(self.model).order_by(desc(self.model.created_at)).all()
        activity = db.query(self.model).order_by(desc(self.model.created_at)).offset(skip).limit(limit).all()
        activity_data = []

        for i in activity:
            user_name = users_repo.get_one(db=db,id=i.user_id).name
            user_phone = users_repo.get_one(db=db, id=i.user_id).phone
            i.user_name = user_name
            i.user_phone = user_phone
            activity_data.append(i)
            
        results = len(activity_all) 
        return [{"results":results}, activity_data]


admin_panel_activity_repo = AdminPanelActivityRepo(AdminPanelActivity)