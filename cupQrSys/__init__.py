__author__ = 'LiGuangyu'
'''银联二维码系统仿真。该系统连接app，acq，cups三个系统'''


from common.webServer import HttpServerTools
import asyncio,os
from common.config import basicConfig,merge
import logging;logging.basicConfig(level=logging.INFO)
from common.mysql import dbInf
from common.redis import redis
from .tableSchema import dbTableInit
from . import controllers



def main():
    print(__file__)
    loop = asyncio.get_event_loop()
    dbTableInit(basicConfig['db'])
    loop.run_until_complete(dbInf.init(loop=loop, dbConf=basicConfig['db']))
    loop.run_until_complete(redis.init(loop=loop,**basicConfig['redis']))
    staticPath = os.path.join(os.path.dirname(__file__),'static')
    srv = HttpServerTools.createServer(loop = loop, host=basicConfig['CupQRServer']['host'], port=basicConfig['CupQRServer']['port'], staticPath=staticPath,staticUrl='/s/',middlewareList=[])
    loop.run_until_complete(srv)
    loop.run_forever()

__all__ = [main]
