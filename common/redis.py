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

class parent():
    @classmethod
    def exceptionDecorator(cls,func):
        @functools.wraps(func)
        async def wapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except aioredis.errors.ReplyError as err:
                '''redis返回err信息，则进入此处'''
                raise err
            except CancelledError as err:
                '''当客户端连接断开时，进入此处异常，可进行高可用处理'''
                print('hello world')
            except Exception as err:
                print(type(err))
                print(err)

        return wapper


class redis:

    conn = None

    def __init__(self):
        pass




    @classmethod
    async def init(cls,loop=None,addr='127.0.0.1',port=6379):
        # if not loop:
        #     loop = asyncio.get_event_loop()
        # loop.set_exception_handler(handler=handler)
        cls.conn = await aioredis.create_reconnecting_redis((addr,port),loop=loop,encoding='utf-8')
        print('hello')
        pass

    @classmethod
    @parent.exceptionDecorator
    async def incr(cls,key=None):
        key = 'test'
        return await cls.conn.incr(key)

    @classmethod
    @parent.exceptionDecorator
    async def set(cls,key,value):
        return await cls.conn.set(key,value)

    @classmethod
    @parent.exceptionDecorator
    async def get(cls,key):
        return await cls.conn.get(key)







if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.set_exception_handler(handler=handler)
    async def test():
        await redis.init()
        a = 0
        print(await redis.set('test',0))
        start_time = time.time()
        while a<100000:
            a+=1
            await redis.incr('test')
        print('Time Used %s' % (time.time() - start_time))

    loop.run_until_complete(test())

