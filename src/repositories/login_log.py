from repositories import BaseRepo
from schemas import LoginLogIn, LoginLogUpdate
from models import LoginLog

login_log_repo = BaseRepo[LoginLog, LoginLogIn, LoginLogUpdate](LoginLog)
