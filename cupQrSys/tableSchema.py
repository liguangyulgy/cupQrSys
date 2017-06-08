__author__ = 'LiGuangyu'

from sqlalchemy import Table,Column,MetaData,Integer,String,TIMESTAMP,func,create_engine

metaData = MetaData()

'''机构基本信息表'''
InsBase = Table('CUP_INS_BASE',metaData,
                   Column('id',Integer,primary_key=True),
                   Column('ins_id_cd',String(11)),
                   Column('ins_en_nm',String(200)),
                   Column('create_ts',TIMESTAMP,default=func.current_timestamp()),
                   Column('update_ts',TIMESTAMP,onupdate=func.current_timestamp()),
                   )

'''卡bin表'''
CardBin = Table('CUP_CARD_BIN',metaData,
                Column('id',Integer,primary_key=True),
                Column('card_bin',String(21),nullable=False),
                Column('ins_id_cd',String(11),nullable=False),
                Column('card_type',Integer,),
                Column('Auth_method',String(10)),
                Column('create_ts', TIMESTAMP, default=func.current_timestamp()),
                Column('update_ts', TIMESTAMP, onupdate=func.current_timestamp()),
                )



'''卡片绑定表'''
BindCard = Table('CUP_BIND_CARD_TOKEN',metaData,
                 Column('id',Integer,primary_key=True),
                 Column('pri_account',String(19),key='priAccount',nullable=False),
                 Column('card_bin',String(21),key='cardBin'),
                 Column('ins_id_cd',String(11),key='insIdCd'),
                 Column('user_id',String(200),key='userId'),
                 Column('auth_no',String(200),key='authNo'),
                 Column('create_ts', TIMESTAMP, default=func.current_timestamp()),
                 Column('update_ts', TIMESTAMP, onupdate=func.current_timestamp()),
                 )



def dbTableInit(dbConf):
    myEngine = create_engine('mysql+pymysql://{user}:{password}@{host}:{port}/{db}'.format(**dbConf))
    metaData.create_all(myEngine)
    myEngine.dispose()

