__author__ = 'LiGuangyu'

import aiomysql



class mysqlConnectionPool;

    @classmethod
    async def init(cls):
        pool = await aiomysql.create_pool()

        with await pool as conn:
            cur = await conn.cursor()
            await cur.execute("")


