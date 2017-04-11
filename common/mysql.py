__author__ = 'LiGuangyu'

import aiomysql
import logging;logging.basicConfig(level=logging.INFO)

from aiomysql.sa import create_engine
from common.tableSchema import metaData,TblInsBase
import asyncio


from sqlalchemy import Table,Column,MetaData,Integer,String,TIMESTAMP,func

metaData = MetaData()




class dataBaseInterFace:

    engine=None

    @classmethod

    async def init(cls, dbConf=None):
        dbConf= dict(
            host = 'liguangyumysql.cf8iw2auduon.ap-southeast-1.rds.amazonaws.com',
            port = 3306,
            user = 'gyli',
            password = 'gyligyli',
            db = 'CUPS_QR'
        )
        cls.engine = await create_engine(**dbConf,echo=True)
        from common.tableSchema import init
        init(dbConf)



    @classmethod
    async def query(cls):
        async with ( cls.engine.acquire())as conn:
            r = await conn.execute(TblInsBase.select())
            for x in r:
                print(x)




if __name__ == '__main__':
    async def test():
        await dataBaseInterFace.init()
        await dataBaseInterFace.query()
    asyncio.get_event_loop().run_until_complete(test())

