import requests


class SmsUtils:

    @staticmethod
    def send_sms(username: str, password: str, sms_from: str, sms_to: str, sms: str):
        url = 'https://api.mobireach.com.bd/SendTextMessage?Username={username}&Password={password}&From={sms_from}&To={sms_to}&Message={sms}'
        x = requests.get(url=url)
        print(x.text)
