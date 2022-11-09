from exceptions.service_result import handle_result
from models import TemporaryToken
from repositories import temporary_token_repo
from schemas import TemporaryTokenIn, TemporaryTokenUpdate
from services import BaseService, sms_service, users_service
from sqlalchemy.orm import Session
from utils import StringManipulate


class TemporaryTokenService(BaseService[TemporaryToken, TemporaryTokenIn, TemporaryTokenUpdate]):

    def create_token(self, db: Session,  user_id: int):
        get_user = users_service.get_one(db=db, id=user_id)
        token = StringManipulate.random_str(size=6)
        check = self.repo.get_by_key(db=db, skip=0, limit=10, descending=False, count_results=False, temp_token=token)
        if not check:
            insert = self.create(db=db, data_in=TemporaryTokenIn(user_id=user_id, temp_token=token, used_status=False, remarks=''))
            sms = sms_service.send_sms(sms_to='88'+handle_result(get_user).phone, sms='Your HEALTHx OTP: '+token)
            return insert
        else:
            self.create_token(db=db, user_id=user_id)


temporary_token_service = TemporaryTokenService(TemporaryTokenUpdate, temporary_token_repo)
