from schemas import SmsIn
from utils import SmsUtils
from db.core import settings


class SmsService:
    def send_sms(self, sms_to: str, sms: str):
        s = SmsUtils.send_sms(username=settings.SMS_USERNAME, password=settings.SMS_PASSWORD, sms_from=settings.SMS_FROM, sms_to=sms_to, sms=sms)
        return s


sms_service = SmsService()
