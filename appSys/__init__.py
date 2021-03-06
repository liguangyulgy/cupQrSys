__author__ = 'LiGuangyu'
'''app侧的移动应用前置'''

from common.webServer import HttpServerTools,post,get
from common.webClient import HttpClient
import asyncio,os
from common.config import basicConfig,merge
import logging;logging.basicConfig(level=logging.INFO)
from common.mysql import dbInf
from common.redis import redis
from .userlogin.cookie import cookie_check
from .tableSchema import dbTableInit

from . import userlogin

def main():
    print(__file__)
    loop = asyncio.get_event_loop()
    dbTableInit(basicConfig['db'])
    HttpClient(loop)
    from . import bindCard
    loop.run_until_complete(dbInf.init(loop=loop, dbConf=basicConfig['db']))
    loop.run_until_complete(redis.init(loop=loop,**basicConfig['redis']))
    staticPath = os.path.join(os.path.dirname(__file__),'static')
    srv = HttpServerTools.createServer(loop = loop, host=basicConfig['AppServer']['host'], port=basicConfig['AppServer']['port'], staticPath=staticPath,staticUrl='/s/',middlewareList=[cookie_check])
    loop.run_until_complete(srv)
    loop.run_forever()
    pass

__all__=[main]


if __name__ == '__main__':
    print(__file__)
    main()


