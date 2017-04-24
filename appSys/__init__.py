__author__ = 'LiGuangyu'
'''app侧的移动应用前置'''

from common.webServer import HttpServerTools,post,get
import asyncio,os
from common.config import basicConfig,merge
import logging;logging.basicConfig(level=logging.INFO)
from common.mysql import dbInf
from common.redis import redis

from . import userlogin

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(dbInf.init(loop=loop, dbConf=basicConfig['db']))
    loop.run_until_complete(redis.init(loop=loop,**basicConfig['redis']))
    print(__file__)
    staticPath = os.path.join(os.path.dirname(__file__),'static')
    srv = HttpServerTools.createServer(loop = loop, host=basicConfig['AppServer']['host'], port=basicConfig['AppServer']['port'], staticPath=staticPath,staticUrl='/s/')
    loop.run_until_complete(srv)
    loop.run_forever()
    pass

__all__=[main]


if __name__ == '__main__':
    print(__file__)
    main()


