__author__ = 'LiGuangyu'

import aiomysql

from aiomysql.sa import create_engine
from common.tableSchema import metaData,TblInsBase
import asyncio

class dataBaseInterFace:

    engine=None

    @classmethod
    async def init(cls):
        cls.engine = await create_engine(
            host='liguangyumysql.cf8iw2auduon.ap-southeast-1.rds.amazonaws.com',
            port=3306,
            user='gyli',
            password='gyligyli',
            db='CUPS_QR'
        )
        metaData.bind(cls.engine)
        metaData.create_all(checkfirst=True)

    @classmethod
    async def query(cls):
        with await cls.engine as conn:
            r = await conn.execute(TblInsBase.select())
            for x in r:
                print(x)


if __name__ == '__main__':
    async def test():
        await dataBaseInterFace.init()
        await dataBaseInterFace.query()
    asyncio.get_event_loop().run_until_complete(test())

