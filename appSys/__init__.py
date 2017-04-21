__author__ = 'LiGuangyu'
'''app侧的移动应用前置'''

from common.webServer import HttpServerTools,post,get
import asyncio,os

from . import userlogin


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    print(__file__)
    path = os.path.join(os.path.dirname(__file__),'./static')
    srv = HttpServerTools.createServer(loop=loop,host='127.0.0.1',port=5566,staticPath=path,staticUrl='/s/')
    loop.run_until_complete(srv)
    loop.run_forever()

