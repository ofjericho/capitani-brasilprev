import requests as req
import settings


class Telegram:
    def __init__(self):
        self.api_url = settings.os.environ['API_TELEGRAM']

    def send_message(self, text):
        params = {'chat_id': settings.os.environ['TELEGRAM_CHAT_ID'],
                  'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        res = req.post(self.api_url + method, params)
        return res
