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
    async def init(cls, loop=None,dbConf=None):
        cls.engine = await create_engine(loop=loop,**dbConf,echo=True,autocommit=True)
        from common.tableSchema import init
        init(dbConf)



    @classmethod
    async def query(cls,tbl,conditions={},*args,**kwargs):
        async with ( cls.engine.acquire()) as conn:
            sql = tbl.select()
            cc = conditions.update(kwargs)
            for k,y in cc.items:
                sql = sql.where(tbl.c[k]==y)
            r = await conn.execute(sql)
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
        await dbInf.query(InsBase)
        print(await dbInf.query(InsBase))
        await dbInf.insert(InsBase,{'ins_id_cd':'00001111','ins_en_nm':'test2'})
    asyncio.get_event_loop().run_until_complete(test())

