import requests as req
import json


class Stackoverflow:

    def search(self, context):

        res = req.get('https://api.stackexchange.com/'
                      '/2.2/search/advanced?order=desc&sort=activity'
                      '&site=stackoverflow'
                      '&title={}'.format(context))

        data_s = json.loads(res.text)

        return data_s
