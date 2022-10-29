from schemas import SmsIn


class SmsService:
    def send_sms(self, data_in: SmsIn):
        return 0


sms_service = SmsService()
