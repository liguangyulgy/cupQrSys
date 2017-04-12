__author__ = 'LiGuangyu'

from sqlalchemy import Table,Column,MetaData,Integer,String,TIMESTAMP,func,create_engine

metaData = MetaData()

'''机构基本信息表'''
TblInsBase = Table('TBL_INS_BASE',metaData,
                   Column('id',Integer,primary_key=True),
                   Column('ins_id_cd',Integer),
                   Column('ins_en_nm',String(200)),
                   Column('create_ts',TIMESTAMP,default=func.current_timestamp()),
                   Column('update_ts',TIMESTAMP,onupdate=func.current_timestamp()),
                   )

'''用户信息表'''



def init(dbConf):
    myEngine = create_engine('mysql+pymysql://{user}:{password}@{host}:{port}/{db}'.format(**dbConf))
    metaData.create_all(myEngine)

