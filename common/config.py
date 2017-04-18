__author__ = 'LiGuangyu'

basicConfig={
    'db': {
        'host': 'liguangyumysql.cf8iw2auduon.ap-southeast-1.rds.amazonaws.com',
        'port': 3306,
        'user': 'gyli',
        'password': 'gyligyli',
        'db': 'CUPS_QR'
    },
    'Server':{
        'host':'127.0.0.1',
        'port':8888
    },
    'staticPath':r'D:\PycharmProjects\cupQrSys\appSys\statics'

}


def merge(a,b):
    rev = {}
    for k,v in a :
        if k in b:
            if isinstance(v,dict):
                rev[k] = merge(v,b[k])
            else:
                rev[k] = b[k]
        else:
            rev[k] = a[k]
    return rev