import requests as req

_TOKEN = '1231789684:AAEW4pZu6J-zFR53FJV2UxUujuSIZjqWbwk'
_CHAT_ID = '522574697'


class Telegram:
    def __init__(self):
        self.api_url = "https://api.telegram.org/bot{}/".format(_TOKEN)

    def send_message(self, text):
        params = {'chat_id': _CHAT_ID,
                  'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        res = req.post(self.api_url + method, params)
        return res
