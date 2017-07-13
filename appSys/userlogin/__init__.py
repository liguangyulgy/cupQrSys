__author__ = 'LiGuangyu'

import asyncio
import hashlib
import logging;
import time

from aiohttp import web

import appSys.tableSchema as ts
from common.mysql import dbInf
from common.webServer import post

logging.basicConfig(level=logging.INFO)
from . import cookie

COOKIE_NAME = "liguangyuCookie"
_COOKIE_KEY = "liguangyu@unionpay.coms"

def encrySlat(password,userName):
    salt = "liguangyu@unionpay.com"
    return hashlib.sha3_256((password + salt + userName).encode()).hexdigest()




@post('/userRegister')
async def userRegister(userName,phoneNum,password,emaillAddr):
    userId = hashlib.md5((userName+ str(time.time())).encode()).hexdigest()
    r = await dbInf.insert(ts.UserInfo,userId=userId, userName=userName,phoneNum=phoneNum,password=encrySlat(password,userName),emaillAddr=emaillAddr)
    print(r)
    return {'Success':True,'Message':'Success, Please Login'}
    pass

@post('/userLogin')
async def userLogin(userName,password):
    user = await dbInf.queryOne(ts.UserInfo,userName=userName,password=encrySlat(password,userName))
    if user:
        """登录成功，添加cookie"""
        #r = web.HTTPFound(location='/s/bindcard.html')
        #直接返回302则前端ajax不能正确跳转，只能得到跳转后的html，因此返回json对象前端人工跳转
        data = {'Success':True, 'Url':'/s/bindcard.html','Message':'Login Success'}
        r = web.json_response(data)
        ck = cookie.user2cookie(user,3600)
        r.set_cookie(cookie.COOKIE_NAME,ck)
        return r
    else:
        return {"Success":False,"Message":"Invalid User Name or Password."}




if __name__ == '__main__':
    async def test():
        await dbInf.init()
        return await userRegister(userName='lgytest1',phoneNum='12344445555',password='asdf1234',emaillAddr='1234@qq.com')

    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(test()))


