__author__ = 'LiGuangyu'
'''app侧的移动应用前置'''

from common.webServer import HttpServerTools,post,get
import asyncio

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    srv = HttpServerTools.createServer(loop=loop,host='127.0.0.1',port=5566,staticPath=r'C:\Users\Guangyu\PycharmProjects\cupQrSys\appSys\static',staticUrl='/s/')
    loop.run_until_complete(srv)
    loop.run_forever()