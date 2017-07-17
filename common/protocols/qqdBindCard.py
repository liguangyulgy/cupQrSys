from .fields import fieldFactory
from .fields import Field,ComField
from sqlalchemy import Column,Integer,String,TIMESTAMP,CHAR,Table,func


class qqdProtocol:
    version = fieldFactory('version', 'NS', 5)  # 版本号
    certId = fieldFactory('certId', 'N', 128, 1)
    signature = fieldFactory('signature', 'ANS', 1024, 1)
    encoding = fieldFactory('encoding', 'ANS', 20, 1)
    txnType = fieldFactory('txnType', 'N', 2)
    txnSubType = fieldFactory('txnSubType', 'N', 2)
    bizType = fieldFactory('bizType', 'N', 6)
    frontUrl = fieldFactory('frontUrl', 'ANS', 256, 1)
    backUrl = fieldFactory('backUrl', 'ANS', 256, 1)
    accessType = fieldFactory('accessType', 'N', 1)
    acqInsCode = fieldFactory('acqInsCode', 'AN', 11, 8)
    merCatCode = fieldFactory('merCatCode', 'N', 4)
    merId = fieldFactory('merId', 'AN', 15)
    merName = fieldFactory('merName', 'ANS', 40, 1)
    merAbbr = fieldFactory('merAbbr', 'ANS', 8, 1)
    subMerId = fieldFactory('subMerId', 'AN', 15, 5)
    subMerName = fieldFactory('subMerName', 'ANS', 40, 1)
    subMerAbbr = fieldFactory('subMerAbbr', 'ANS', 8, 1)
    orderId = fieldFactory('orderId', 'AN', 40, 8)
    txnTime = fieldFactory('txnTime', 'YYYYMMDDhhmmss', 14)
    orderTimeout = fieldFactory('orderImeout', 'N', 10, 1)
    payTimeOut = fieldFactory('payTimeout', 'YYYYMMDDhhmmss', 14)
    defaultPayType = fieldFactory('defaultPayType', 'N', 4)
    subPayType = fieldFactory('subPayType', 'AN', 128, 1)
    payType = fieldFactory('payType', 'N', 4)
    currencyCode = fieldFactory('currencyCode', 'AN', 3)
    accType = fieldFactory('accType', 'N', 2)
    accNo = fieldFactory('accNo', 'AN', 1024, 1)
    payCardType = fieldFactory('payCardType', 'N', 2)
    issInsCode = fieldFactory('insInsCode', 'ANS', 11, 1)
    issInsProvince = fieldFactory('issInsCity', 'ANS', 30, 1)
    issInsName = fieldFactory('issInsName', 'ANS', 60, 1)
    customerInfo = fieldFactory('customerInfo', ComField, 1024, 1,parent=ComField)
    customerInfo.init(
        certifTp = fieldFactory('customerInfo_certifTp', 'N', 2),
        certifId = fieldFactory('customerInfo_certifId', 'ANS', 20, 1),
        customerNm = fieldFactory('customerInfo_customerNm', 'ANS', 30, 1),
        smsCode = fieldFactory('customerInfo_smsCode', 'N', 6),
        pin = fieldFactory('customerInfo_pin', 'ANS', 256, 1),
        encryptedInfo = fieldFactory('customerInfo_encryptedInfo', 'ANS', 1024, 1)
    )
    txnAmt = fieldFactory('txnAmt', 'N', 12, 1)
    balance = fieldFactory('balance', 'AN', 256, 1)
    billType = fieldFactory('billType', 'ANS', 2)
    billNo = fieldFactory('billNo', 'ANS', 64, 1)
    bussCode = fieldFactory('bussCode', 'ANS', 20, 4)
    billPeriod = fieldFactory('billPeriod', 'ANS', 17)
    billQueryInfo = fieldFactory('billQueryInfo', 'ANS', 1024, 1)
    billDetailInfo = fieldFactory('billDetailInfo', 'ANS', 2048, 1)
    batchNo = fieldFactory('batchNo', 'N', 4)
    totalQty = fieldFactory('totalQty', 'N', 6, 1)
    totalAmt = fieldFactory('totalAmt', 'N', 12, 1)
    fileType = fieldFactory('fileType', 'N', 2)
    fileName = fieldFactory('fileName', 'ANS', 64, 1)
    fileContent = fieldFactory('fileContent', 'ANS', 1)
    reqReserved = fieldFactory('reqReserved', 'ANS', 1024, 1)
    reserved = fieldFactory('reserved', 'ANS', 2048, 1)
    termId = fieldFactory('termId', 'AN', 8)
    issuserIdentifyMode = fieldFactory('issuserIdentifyMode', 'N', 1)
    customerIp = fieldFactory('customerIp', 'NS', 40, 7)
    queryId = fieldFactory('queryId', 'AN', 21)
    origQryId = fieldFactory('origQryId', 'AN', 21)
    traceNo = fieldFactory('traceNo', 'N', 6)
    traceTime = fieldFactory('traceTime', 'MMDDhhmmss', 10)
    settleDate = fieldFactory('settleDate', 'MMDD', 4)
    settleCurrencyCode = fieldFactory('settleCurrencyCode', 'AN', 3)
    settleAmt = fieldFactory('settleAmt', 'N', 12, 1)
    exchangeRate = fieldFactory('exchangeRate', 'N', 8)
    exchangeDate = fieldFactory('exchangeDate', 'MMDD', 4)
    origRespCode = fieldFactory('origRespCode', 'AN', 2)
    origRespMsg = fieldFactory('origRespMsg', 'ANS', 256, 1)
    respCdde = fieldFactory('respCode', 'AN', 2)
    respMsg = fieldFactory('respMsg', 'ANS', 256)
    checkFlag = fieldFactory('checkFlag', 'N', 8)
    activateStatus = fieldFactory('activateStatus', 'N', 1)
    encryptCertId = fieldFactory('encryptCertId', 'N', 128, 1)
    userMac = fieldFactory('userMac', 'ans', 80)
    riskRateInfo = fieldFactory('riskRateInfo', 'ANS', 2048, 1)
    temporaryPayInfo = fieldFactory('temporaryPayInfo', 'AN', 100)
    cardTransData = fieldFactory('cardTransData', 'ANS1Trans', 4096)
    tn = fieldFactory('tn', 'N', 21)
    payCardNo = fieldFactory('payCardNo', 'ANS', 19, 1)
    payCardIssueName = fieldFactory('payCardIssueName', 'ANS', 64, 1)
    channelType =fieldFactory('channelType', 'N', 2)
    signMethd = fieldFactory('signMethod', 'N', 2)
    instalTransInfo = fieldFactory('instalTransInfo', 'ANS', 128, 1)
    orderDesc = fieldFactory('orderDesc', 'ANS', 32, 1)
    bookedAccNo = fieldFactory('bookedAccNo', 'AN', 60, 1)
    tokenPayData = fieldFactory('tokenPayData', 'ANS', 1024, 1)
    signPubKeyCert = fieldFactory('signPubKeyCert', 'AN', 2048)
    encryptPubKeyCert = fieldFactory('encryptPubKeyCert', 'AN', 2048)
    certType = fieldFactory('certType', 'N', 2)
    accSplitData = fieldFactory('accSplitData', 'ANS', 512, 1)
    ctrlRule = fieldFactory('ctrlRule', 'N', 32)
    districtName = fieldFactory('districtName', 'ANS', 64)


class HttpPostBase:
    def __str__(self):
        tmpList = [ x + '=' + str(y) for x,y in self.__dict__.items() if y is not None]
        rev = '&'.join(tmpList)
        return rev




class BindcardRequest(HttpPostBase):

    def __init__(self):

        self.__dict__['version'] = qqdProtocol.version('5.1.0')
        self.__dict__['encodeing'] = qqdProtocol.encoding('UTF-8')
        self.__dict__['certId'] = qqdProtocol.certId()
        self.__dict__['signature'] = qqdProtocol.signature()
        self.__dict__['signMethod'] = qqdProtocol.signMethd()
        self.__dict__['txnType'] = qqdProtocol.txnType()
        self.__dict__['txnSubType'] = qqdProtocol.txnSubType()
        self.__dict__['bizType'] = qqdProtocol.bizType()
        self.__dict__['accessType'] = qqdProtocol.accessType()
        self.__dict__['channelType'] = qqdProtocol.channelType()
        self.__dict__['frontUrl'] = qqdProtocol.frontUrl()
        self.__dict__['backUrl'] = qqdProtocol.backUrl()
        self.__dict__['acqInsCode'] = qqdProtocol.acqInsCode()
        self.__dict__['merId'] = qqdProtocol.merId()
        self.__dict__['merCatCode'] = qqdProtocol.merCatCode()
        self.__dict__['merName'] = qqdProtocol.merName()
        self.__dict__['merAbbr'] = qqdProtocol.merAbbr()
        self.__dict__['subMerId'] = qqdProtocol.subMerId()
        self.__dict__['subMerName'] = qqdProtocol.subMerName()
        self.__dict__['subMerAbbr'] = qqdProtocol.subMerAbbr()
        self.__dict__['orderId'] = qqdProtocol.orderId()
        self.__dict__['txnTime'] = qqdProtocol.txnTime()
        self.__dict__['accType'] = qqdProtocol.accType()
        self.__dict__['accNo'] = qqdProtocol.accNo()
        self.__dict__['customerInfo'] = qqdProtocol.customerInfo()
        self.__dict__['reqReserved'] = qqdProtocol.reqReserved()
        self.__dict__['reserved'] = qqdProtocol.reserved()
        self.__dict__['encryptCertId'] = qqdProtocol.encryptCertId()
        self.__dict__['tokenPayData'] = qqdProtocol.tokenPayData()
        self.__dict__['ctrlRule'] = qqdProtocol.ctrlRule()
        self.__dict__['billQueryInfo'] = qqdProtocol.billQueryInfo()

    def __getattr__(self, key):
        return self.key.v

    def __setattr__(self, key, value):
        self.__dict__[key].v = value

    def __getitem__(self, key):
        return self.key.v

    @classmethod
    def getTableSchema(cls, metadata, tableName = 'TBL_BIND_CARD_REQUEST'):
        record = BindcardRequest()
        columns = []
        '''遍历对象的属性，构造数据库字段'''
        for key in record.__dict__:
            attr = getattr(record,key)
            if isinstance(attr, Field):
                pass
                cname = key
                clen = attr.fieldLength
                ctype = String(clen)
                if attr.fieldLength == attr.fieldMinLength and attr.fieldLength < 20:
                    ctype = CHAR(clen)
                elif 'YYYYMMDDhhmmss'.equals(attr.fieldType):
                    ctype = TIMESTAMP
                columns.append(Column(cname,ctype))
        '''根据对象的属性及固定的字段，构造表结构'''
        revTable = Table(tableName,metadata,
                         Column('id', Integer,primary_key=True),
                         *columns,
                         Column('create_ts', TIMESTAMP, default=func.current_timestamp()),
                         Column('update_ts', TIMESTAMP, onupdate=func.current_timestamp()),
                         )
        return revTable


