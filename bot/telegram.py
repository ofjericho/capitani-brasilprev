import requests as req


class BotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    # url = "https://api.telegram.org/bot<token>/"

    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        res = req.get(self.api_url + method, params)
        result_json = res.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id,
                  'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        res = req.post(self.api_url + method, params)
        return res

    def get_first_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[0]
        else:
            last_update = None

        return last_update
