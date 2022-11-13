from exceptions import handle_result, AppException, ServiceResult
from models import TemporaryToken
from repositories import temporary_token_repo
from schemas import TemporaryTokenIn, TemporaryTokenUpdate
from services import BaseService, sms_service, users_service
from sqlalchemy.orm import Session
from utils import StringManipulate
from datetime import datetime
from utils import Token


class TemporaryTokenService(BaseService[TemporaryToken, TemporaryTokenIn, TemporaryTokenUpdate]):

    def create_token(self, db: Session,  user_phone: str):
        user = users_service.get_by_key(db=db, skip=0, limit=10, descending=False, count_results=False, phone=user_phone)
        token = StringManipulate.random_str(size=6)
        check = self.repo.get_by_key(db=db, skip=0, limit=10, descending=False, count_results=False, temp_token=token)
        if not check:
            insert = self.create(db=db, data_in=TemporaryTokenIn(user_id=handle_result(user)[0].id, temp_token=token, used_status=False, remarks=''))

            if not insert:
                return ServiceResult(AppException.ServerError("Something went wrong!"))
            sms = sms_service.send_sms(sms_to='88'+user_phone, sms='Your HEALTHx OTP: '+token)
            return ServiceResult({"msg": "OTP sent and you have only 5 minute to validite token"})

        else:
            self.create_token(db=db, user_phone=user_phone)

    def valid_temp_token(self, db: Session, temp_token: str, user_phone: int, max_min: int):
        get_token = self.repo.get_by_two_key(db=db, skip=0, limit=10, descending=False, count_results=False, temp_token=temp_token, used_status=False)

        user = users_service.get_by_key(db=db, skip=0, limit=10, descending=False, count_results=False, phone=user_phone)

        if not get_token:
            return ServiceResult(AppException.ServerError("Token not found"))

        if get_token[0].user_id != handle_result(user)[0].id:
            return ServiceResult(AppException.ServerError("User id not match with token"))

        time_from_token = get_token[0].created_at
        current_time = datetime.now()

        time_diff = current_time - time_from_token
        time_diff_min = int(time_diff.total_seconds() / 60)

        if time_diff_min <= max_min:
            print(time_diff_min)
            access_token = Token.create_access_token({"sub": handle_result(user)[0].id})
            return ServiceResult({"access_token": access_token, "token_type": "bearer"}, status_code=200)
        else:
            return ServiceResult(AppException.ServerError("Token validate timout."))


temporary_token_service = TemporaryTokenService(TemporaryTokenUpdate, temporary_token_repo)
