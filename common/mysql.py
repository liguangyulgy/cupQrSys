__author__ = 'LiGuangyu'

import aiomysql
import logging;logging.basicConfig(level=logging.DEBUG)

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
            for x in r:
                print(x)
            return r

    @classmethod
    async def testInsert(cls):
        async with( cls.engine.acquire()) as conn:
            await conn.execute('insert into `TBL_INS_BASE`(ins_id_cd,ins_en_nm) values("1","2")')
            await conn.commit()



if __name__ == '__main__':
    async def test():
        await dbInf.init()
        print(await dbInf.query(InsBase))
        await dbInf.testInsert()
        #await dbInf.insert(InsBase,{'ins_id_cd':'00001111','ins_en_nm':'test2'})
    asyncio.get_event_loop().run_until_complete(test())

