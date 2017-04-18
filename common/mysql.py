__author__ = 'LiGuangyu'

import aiomysql
import logging;logging.basicConfig(level=logging.INFO)

from aiomysql.sa import create_engine
from common.tableSchema import metaData,InsBase
import asyncio


from sqlalchemy import Table,Column,MetaData,Integer,String,TIMESTAMP,func

metaData = MetaData()




class dbInf:

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
    async def query(cls,tbl):
        async with ( cls.engine.acquire()) as conn:
            r = await conn.execute(tbl.select())
            for x in r:
                print(x)

    @classmethod
    async def insert(cls,tbl,insRec={},*args,**kwargs):
        async with( cls.engine.acquire()) as conn:
            insRec.update(**kwargs)
            sql = tbl.insert().values(insRec)
            r = await conn.execute(sql)
            return r


if __name__ == '__main__':
    async def test():
        await dbInf.init()
        await dbInf.query()
    asyncio.get_event_loop().run_until_complete(test())

