import requests as req
import settings
import aiohttp


class Stackoverflow:

    def search(self, filter):
        params = {'order': 'desc', 'sort': 'activity',
                  'site': 'stackoverflow', 'intitle': filter}

        res = req.get(settings.os.environ['API_STACKOVERFLOW'], params)

        data = res.json()
        return data

    async def search_async(self, filter):
        async with aiohttp.ClientSession() as session:
            # API = "https://api.stackexchange.com/2.2/search"
            params = {'order': 'desc', 'sort': 'activity',
                      'site': 'stackoverflow', 'intitle': filter}
            async with session.get(settings.os.environ['API_STACKOVERFLOW'],
                                   params=params) as res:

                data = await res.json()
                return data
