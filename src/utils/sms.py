import requests


class SmsUtils:

    @staticmethod
    def send_sms(username: str, password: str, sms_from: str, sms_to: str, sms: str):
        url = f'https://api.mobireach.com.bd/SendTextMessage?Username={username}&Password={password}&From={sms_from}&To={sms_to}&Message={sms}'
        x = requests.get(url=url)
        txt = x.text

        start_tag = '<MessageId>'
        end_tag = '</MessageId>'
        a = txt.find(start_tag)
        b = txt.find(end_tag)
        return txt[a+len(start_tag):b]
