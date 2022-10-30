from schemas import SmsIn
from utils import SmsUtils


class SmsService:
    def send_sms(self, data_in: SmsIn):
        s = SmsUtils.send_sms(username=data_in.username, password=data_in.password, sms_from=data_in.sms_from, sms_to=data_in.sms_to, sms=data_in.sms)
        return s


sms_service = SmsService()
