import requests as req
import settings
import aiohttp


class Stackoverflow:

    def search(self, filter):

        res = req.get(settings.os.environ['API_STACKOVERFLOW'] +
                      '&title={}'.format(filter))

        data = res.json()
        return data

    async def search_async(self, filter):
        async with aiohttp.ClientSession() as session:
            async with session.get(settings.os.environ['API_STACKOVERFLOW'] +
                                   '&title={}'.format(filter)) as res:

                data = await res.json()
                return data
