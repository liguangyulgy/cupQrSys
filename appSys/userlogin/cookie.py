__author__ = 'LiGuangyu'

from common.webServer import HttpServerTools,post,get
from common.mysql import dbInf
import common.tableSchema as ts
import asyncio,hashlib,time
from aiohttp import web
import logging;logging.basicConfig(level=logging.INFO)

'''根据用户ID，密码，过期时间计算cooike，用sha3-256加密
    每个post请求都判断cookie，拦截无效请求重定向至登录页面'''

COOKIE_NAME = "liguangyuCookie"
_COOKIE_KEY = "liguangyu@unionpay.coms"


async def cookie2user(cookie_str):
    if not cookie_str:
        return None
    try:
        L = cookie_str.split('-')
        if len(L) != 3:
            return None
        userId, expires,sha1 = L
        if int(expires) < time.time():
            return None
        '''这里根据cooike的内容去数据库里取值，比较慢。后期考虑做个缓存'''
        user = await dbInf.queryOne(ts.UserInfo,userId=userId)
        if user is None:
            return None
        s = '%s-%s-%s-%s' % (userId, user['password'], expires, _COOKIE_KEY)
        if sha1 != hashlib.sha3_256(s.encode('utf-8').hexdigest()):
            logging.info('invalid sha1')
            return None
        user.passwd = '******'
        return user
    except Exception as e:
        logging.exception(e)
        return None


async def cookie_check(app, handler):
    async def check(request):
        request.__user__ = None
        loginUrl = '/s/userRegister.html'
        whiteList = ['/userLogin','/userRegister']
        if  (request.uri in whiteList) or ( request.method == 'GET' ):
            '''如果是登录页面或者get请求，则放过
            这里没法判断是否是获取静态资源，后续可以判断后缀，或者把静态资源部署到nginx上'''
            return await(handler(request))
        cookie = request.cookies.get(COOKIE_NAME)
        if cookie:
            user = await cookie2user(cookie_str=cookie)
            if user:
                request.__user__ = user
                '''如果成功获取到用户，则继续执行其他handler'''
                return await(handler(request))
        '''否则，重定向到登录页面'''
        return web.HTTPFound(location=loginUrl)
    return check

def user2cookie(user,max_age):
    expires = str(int(time.time()) + max_age)
    s = '%s-%s-%s-%s' % (user['userId'], user['password'], expires, _COOKIE_KEY)
    L = [user['userId'] ,expires, hashlib.sha3_256(s.encode('utf-8')).hexdigest()]
    return '-'.join(L)

