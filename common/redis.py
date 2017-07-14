__author__ = 'LiGuangyu'
import aioredis
import asyncio,functools
from concurrent.futures import CancelledError
import logging;logging.basicConfig(level=logging.INFO)
from common.comm import singleton
import time

def handler(loop, context):
    '''
    本来打算在eventloop上注册异常处理函数，但是没玩明白，后续研究
    '''
    print('in exception Handler')
    print(context)

class baseConnectPool(object):

    _pool1 = None
    _pool2 = None
    pool = None

    @classmethod
    async def init(cls,loop=None,addr='127.0.0.1',port=6379,password=None):
        # if not loop:
        #     loop = asyncio.get_event_loop()
        # loop.set_exception_handler(handler=handler)
        try:
            baseConnectPool._pool1 = await aioredis.create_pool((addr,port),loop=loop,password=password,encoding='utf-8',minsize=1,maxsize=1)
            baseConnectPool._pool2 = await aioredis.create_pool((addr,port),loop=loop,password=password,encoding='utf-8',minsize=1,maxsize=1)
            baseConnectPool.pool = baseConnectPool._pool1
            print('hello')
        except ConnectionRefusedError as e:
            print('Redis Cannot access')
            raise e
        except Exception as e:
            print('Error')
            print(e)
        pass

    @classmethod
    def tryCatch(cls,func):
        @functools.wraps(func)
        async def wapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except aioredis.errors.ReplyError as err:
                '''redis返回err信息，则进入此处'''
                print('Reply Error Catched')
                raise err
            except CancelledError as err:
                '''当单条连接连接断开时，进入此处异常，
                如果使用单连接，此处可进行高可用处理
                如果使用连接池，在下面判断'''
                print('hello world')
            except ConnectionRefusedError as err:
                '''重连失败进入此处异常
                如果使用连接池，在此处进行高可用
                判断pool.size是否为0（池内连接数量）来判断是否单个Redis挂掉'''
                print(cls._pool1)
                print(cls._pool2)
                print('connect Refused')
            except Exception as err:
                print(type(err))
                print(err)

        return wapper


class redis(baseConnectPool):
    ORDERNOKEY = 'ORDERNOKEY'

    def __init__(self):
        pass

    @classmethod
    async def init(cls,loop=None,addr='127.0.0.1',port=6379,password=None):
        a = super()
        print(a)
        await super().init(loop=loop,addr=addr,port=port,password=password)

    @classmethod
    @baseConnectPool.tryCatch
    async def incr(cls,key):
        with await cls.pool as rdsConn:
            return await rdsConn.incr(key)

    @classmethod
    @baseConnectPool.tryCatch
    async def set(cls,key,value):
        with await cls.pool as rdsConn:
            return await rdsConn.set(key,value)

    @classmethod
    @baseConnectPool.tryCatch
    async def get(cls,key):
        with await cls.pool as rdsConn:
            return await rdsConn.get(key)

    @classmethod
    @baseConnectPool.tryCatch
    async def getOrderId(cls):
        with await cls.pool as rdsConn:
            tr = rdsConn.multi_exec()
            tr.setnx(cls.ORDERNOKEY, 1000000000000)
            tr.incr(cls.ORDERNOKEY)
            rev = await tr.execute()
            if rev[1] > 9000000000000:
                redis.incr(cls.ORDERNOKEY, - 8000000000000)
            return rev[1]

    @classmethod
    @baseConnectPool.tryCatch
    async def getTime(cls):
        with await cls.pool as rdsConn:
            tt = await rdsConn.time()
            x = time.localtime(tt)
            rev = time.strftime('%Y%m%d%H%M%S', x)
            return rev


    @classmethod
    @baseConnectPool.tryCatch
    async def getTime1(cls):
        with await cls.pool as rdsConn:
            return await rdsConn.time()





if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.set_exception_handler(handler=handler)
    async def test():
        await redis.init()
        a = 0
        print(await redis.set('test',0))
        print(await redis.getTime1())
        start_time = time.time()
        while True:
            a+=1
            await redis.incr('test')
        print('Time Used %s' % (time.time() - start_time))

    loop.run_until_complete(test())

