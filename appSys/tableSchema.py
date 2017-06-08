__author__ = 'LiGuangyu'

from sqlalchemy import Table,Column,MetaData,Integer,String,TIMESTAMP,func,create_engine

metaData = MetaData()



'''用户信息表'''
UserInfo = Table('APP_USER_INF',metaData,
                 Column('id',Integer,primary_key=True),
                 Column('user_id',String(200),key='userId',nullable=False,unique=True),
                 Column('nick_name',String(200),key='userName'),
                 Column('phone_num',String(20),nullable=False,key='phoneNum'),
                 Column('password',String(64),nullable=False,key='password'),
                 Column('email_address',String(50),default='',key='emaillAddr'),
                 Column('create_ts', TIMESTAMP, default=func.current_timestamp()),
                 Column('update_ts', TIMESTAMP, onupdate=func.current_timestamp()),
                 )

'''用户卡片绑定表'''
BindCard = Table('APP_USER_BIND_CARD',metaData,
                 Column('id',Integer,primary_key=True),
                 Column('card_number',String(19),key='cardNumber',nullable=False),
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

