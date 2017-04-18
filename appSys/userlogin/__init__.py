__author__ = 'LiGuangyu'

from common.webServer import HttpServerTools,post,get
from common.mysql import dbInf
import common.tableSchema as ts
import asyncio


@post('/userRegister')
async def userRegister(userName,phoneNum,password,emaillAddr):
    r = await dbInf.insert(ts.UserInfo, userName=userName,phoneNum=phoneNum,password=password,emaillAddr=emaillAddr)
    print(r)
    return {'Success':True}
    pass



if __name__ == '__main__':
    async def test():
        await dbInf.init()
        return await userRegister(userName='lgytest1',phoneNum='12344445555',password='asdf1234',emaillAddr='1234@qq.com')

    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(test()))


