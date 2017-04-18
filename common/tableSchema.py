__author__ = 'LiGuangyu'

from sqlalchemy import Table,Column,MetaData,Integer,String,TIMESTAMP,func,create_engine

metaData = MetaData()

'''机构基本信息表'''
InsBase = Table('TBL_INS_BASE',metaData,
                   Column('id',Integer,primary_key=True),
                   Column('ins_id_cd',String(11)),
                   Column('ins_en_nm',String(200)),
                   Column('create_ts',TIMESTAMP,default=func.current_timestamp()),
                   Column('update_ts',TIMESTAMP,onupdate=func.current_timestamp()),
                   )

'''卡bin表'''
CardBin = Table('TBL_CARD_BIN',metaData,
                Column('id',Integer,primary_key=True),
                Column('card_bin',String(21),nullable=False),
                Column('ins_id_cd',String(11),nullable=False),
                Column('card_type',Integer,),
                Column('Auth_method',String(10)),
                Column('create_ts', TIMESTAMP, default=func.current_timestamp()),
                Column('update_ts', TIMESTAMP, onupdate=func.current_timestamp()),
                )


'''用户信息表'''
UserInfo = Table('TBL_USER_INF',metaData,
                 Column('id',Integer,primary_key=True),
                 Column('user_id',String(200),nullable=False),
                 Column('nick_name',String(200)),
                 Column('phone_num',String(20),nullable=False),
                 Column('email_address',String(50),default=''),
                 Column('create_ts', TIMESTAMP, default=func.current_timestamp()),
                 Column('update_ts', TIMESTAMP, onupdate=func.current_timestamp()),
                 )

'''卡片绑定表'''
BindCard = Table('TBL_BIND_CARD',metaData,
                 Column('id',Integer,primary_key=True),
                 Column('card_number',String(19),nullable=False),
                 Column('card_bin',String(21)),
                 Column('ins_id_cd',String(11)),
                 Column('user_id',String(200)),
                 Column('auth_no',String(200)),
                 Column('create_ts', TIMESTAMP, default=func.current_timestamp()),
                 Column('update_ts', TIMESTAMP, onupdate=func.current_timestamp()),
                 )



def init(dbConf):
    myEngine = create_engine('mysql+pymysql://{user}:{password}@{host}:{port}/{db}'.format(**dbConf))
    metaData.create_all(myEngine)

