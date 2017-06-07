__author__ = 'LiGuangyu'

from common.webServer import HttpServerTools,post,get
from common.mysql import dbInf
import common.tableSchema as ts
import asyncio,hashlib,time
from aiohttp import web
import logging;logging.basicConfig(level=logging.INFO)

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
    r = await dbInf.queryOne(ts.UserInfos,userName=userName,password=encrySlat(password,userName))
    if r:
        """登录成功，添加cookie"""
        r = web.HTTPFound(location='todo')
        r.set_cookie()
        return r
    else:
        return {"Success":False,"Message":"Invalid User Name or Password."}




if __name__ == '__main__':
    async def test():
        await dbInf.init()
        return await userRegister(userName='lgytest1',phoneNum='12344445555',password='asdf1234',emaillAddr='1234@qq.com')

    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(test()))


