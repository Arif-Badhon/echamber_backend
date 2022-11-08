from schemas import SmsIn
from utils import SmsUtils


class SmsService:
    def send_sms(self, username: str, password: str, sms_from: str, sms_to: str, sms: str):
        s = SmsUtils.send_sms(username=username, password=password, sms_from=sms_from, sms_to=sms_to, sms=sms)
        return s


sms_service = SmsService()
