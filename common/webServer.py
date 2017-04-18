__author__ = 'LiGuangyu'
from aiohttp import web
import asyncio,functools,inspect,json,os
import logging;logging.basicConfig(level=logging.INFO)
from urllib import parse

class RequestHandler(object):
    """
    此类实际为类函数，将一个普通的函数，包装成异步的可以注册到aiohttpserver上的函数
    即func（a,b)：
    变为
    _func（request）
        //get a,b from request 
        return func（a，b）
    """
    def __init__(self, app, fn):
        self._app = app
        self._func = fn

    async def __call__(self, request):
        """
        :param request: http请求
        :return: self._func函数处理后的返回值
        """
        # 原处理函数的参数列表
        sigArgs = inspect.signature(self._func).parameters
        kw = {}
        #请求中？后面的参数
        if request.query_string:
            kw.update({x:(y[0] if len(y) == 1 else y) for x,y in parse.parse_qs(request.query_string,True).items()})
        # URL中包含的参数（RestFul样式的参数）
        urlArgs = request.match_info or {}
        kw.update(dict(**urlArgs))
        #获取body的内容
        contentType = request.content_type.lower() if request.has_body else ''
        if contentType.startswith('appliction/json'):
            body = await request.json()
        elif contentType.startswith('application/x-www-form') or contentType.startswith('multipart/form-data'):
            body = await request.post()
        else:
            body = {}
        kw.update(dict(**body))

        #传递原请求和请求体解析结果
        kw.update({'body':body,'request':request})
        try:
            #根据原函数参数列表，组装要传达给函数的参数
            args = {x:kw[x] for x in sigArgs if x in kw}
        except ValueError as e:
            return e
        for x in sigArgs:
            #如果原函数参数列表中有参数没被赋值且没有默认值，则报错
            if x not in args and '=' not in str(sigArgs[x]):
                return Exception('Missing args %s' % x)
        #将原函数变为异步的
        if not asyncio.iscoroutinefunction(self._func) and not inspect.isgeneratorfunction(self._func):
            fn = asyncio.coroutine(self._func)
        return await fn(**args)


async def loggingMidleWare(app,handler):
    async def loggingfunc(request):
        logging.info('My Log, Request: %s,%s' % (request.method, request.path))
        return await handler(request)
    return loggingfunc

async def ResponseHandler(app,handler):
    """
    帮助处理函数的返回值，将其变成webResponse对象以供aiohttp框架使用
    :param app: 
    :param handler: 
    :return: 
    """
    async def rspHandler(request):
        try:
            r = await(handler(request))
            if isinstance(r, web.StreamResponse):
                return r
            if isinstance(r, bytes):
                resp = web.Response(body=r)
                resp.content_type = 'application/octet-stream'
                return resp
            if isinstance(r, str):
                resp = web.Response(body=r.encode('utf-8'))
                resp.content_type = 'text/html;charset=utf-8'
                return resp
            if isinstance(r, Exception):
                return web.HTTPBadRequest(r)
            if isinstance(r,dict):
                resp = web.Response(body=json.dumps(r).encode('utf-8'))
                resp.content_type='application/json'
                return resp
        except Exception as e:
            logging.error(e)
            return web.HTTPBadRequest(e)
    return rspHandler




class HttpServerTools:
    """
    无实例，
    提供httpMethod生成装饰器，方便函数注册到server上
    接收createServer方法根据loop,host,port返回aiohttp的server
    """
    routes = []

    @classmethod
    def httpMethod(cls,method):
        def methodDecorator(path):
            def decorator(func):
                @functools.wraps(func)
                def wapper(*args,**kwargs):
                    return func(*args,**kwargs)
                cls.routes.append((method,path,func))
                return wapper
            return decorator
        return methodDecorator

    @classmethod
    async def createServer(self,loop,host,port,staticPath = None,staticUrl=None):
        app = web.Application(loop=loop,middlewares=[loggingMidleWare,ResponseHandler])
        #将routes中记录的函数注册到app的路由上
        for method, path, func in self.routes:
            logging.info('add route %s %s => %s(%s)' % ( method, path, func.__name__, ','.join(inspect.signature(func).parameters.keys())))
            app.router.add_route(method, path, RequestHandler(app,func))
        if staticPath:
            if os.path.exists(staticPath):
                app.router.add_static(staticUrl, staticPath)
                logging.info(('add static route %s, local path %s' % (staticUrl,staticPath)))
            else:
                logging.error('Invalid Static Path %s for %s' % (staticPath, staticUrl))

        return await loop.create_server(app.make_handler(),host,port)


'''方便外部调用'''
get = HttpServerTools.httpMethod('get')
post = HttpServerTools.httpMethod('post')





if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    app = web.Application(loop=loop)

    @get('/test')
    def hello(hello = 'world'):
        print('hello : ' + hello)
        return {'hello':hello}

    loop.run_until_complete(HttpServerTools.createServer(loop,'0.0.0.0',6666))
    loop.run_forever()

