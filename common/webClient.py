__author__ = 'LiGuangyu'
'''通用客户端组件'''
import aiohttp
from common.comm import singleton
import json
import urllib
import asyncio


@singleton
class HttpClient:

    headers={'content-type':'appliction/json',''}

    def __init__(self, loop):
        self.client = aiohttp.ClientSession(loop=loop)

    @classmethod
    def encode(cls,url,urlParas):
        myURL = url
        if urlParas:
            myURL = (url if url.endswith('/') else url + '/') + urllib.parse.quote('/'.join(urlParas))
        return myURL

    async def get(self,url,urlParas=None,query=None):
        myURL = self.encode(url,urlParas)
        async with self.client.get(url=myURL,params=query) as resp:
            data = (await resp.json()) if resp.headers['content-type'] =='appliction/json' else (await resp.text())
            return resp.status, data

    async def post(self,url,urlParas=None,data=None, type='json'):
        myURL = self.encode(url,urlParas)
        if type == 'json':
            payload = json.dumps(data)
            headers = self.headers
        else
            payload = data.encode('utf-8')
            headers = self.headers.update({'content-type':'appliction/json'})
        async with self.client.post(url=myURL,data=payload, header=headers) as resp:
            data = (await resp.json()) if resp.headers['content-type'] =='appliction/json' else (await resp.text())
            return resp.status, data


'''测试代码'''
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    client = HttpClient(loop)
    async def test(client):
        status, data = await client.get('http://www.httpbin.org/get' ,urlParas=('heellodsf'),query={'req':'rsp','afd':'啊啊'})
        print(status)
        print(data)
        status, data = await client.post('http://www.httpbin.org/post',data={'aaa':'bbb','ccc':{11:22,33:44}})
        print (status)
        print(data)

    loop.run_until_complete(test(client))

