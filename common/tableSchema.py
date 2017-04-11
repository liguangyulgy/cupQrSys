__author__ = 'LiGuangyu'

from sqlalchemy import Table,Column,MetaData,Integer,String,TIMESTAMP,func

metaData = MetaData()

TblInsBase = Table('TBL_INS_BASE',metaData,
                   Column('id',Integer,primary_key=True),
                   Column('ins_id_cd',Integer),
                   Column('ins_en_nm',String),
                   Column('create_ts',TIMESTAMP,default=func.current_timestamp()),
                   Column('update_ts',TIMESTAMP,onupdate=func.current_timestamp()),
                   )
