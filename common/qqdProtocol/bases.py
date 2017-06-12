__author__ = 'LiGuangyu'


class qqdField:
    def __init__(self,name,value,length,type,aliaName = ''):
        self.name = name
        self.value = value
        self.type = type
        self.length = length
        self.aliaName = aliaName
        if '' == aliaName:
            self.aliaName = self.name


    def toString(self):
        return self.value


class qqdMessage:
    def __init__(self):
        self.version = qqdField('version','5.1.0', 5, 'NS') #版本号
        self.certId = qqdField('certId', None, 128, 'N')
        self.signature = qqdField('signature', None, 1024, 'ANS')
        self.encoding = qqdField('encoding', 'UTF-8', 20, 'ANS')
        self.txnType = qqdField('txnType', None, 2, 'N')
        self.txnSubType = qqdField('txnSubType', None, 2, 'N')
        self.bizTyp = qqdField('bizType', None, 6, 'N')
        self.frontUrl = qqdField('frontUrl', None, 256, 'ANS')
        self.backUrl = qqdField('backUrl', None, 256, 'ANS')
        self.accessType = qqdField('accessType', None, 1, 'N')
        self.acqInsCode = qqdField('acqInsCode', None, 11, 'AN')
        self.merCatCode = qqdField('merCatCode', None, 11, 'AN')
        self.merId = qqdField('merId', None, 15, 'AN')
        self.merName = qqdField('merName', None, 40, 'AN')
        self.merAbbr = qqdField('merAbbr', None, 8, 'ANS')
        self.subMerId = qqdField('subMerId', None, 15, 'AN')
        self.subMerName = qqdField('subMerName', None, 40, 'ANS')
        self.subMerAbbr = qqdField('subMerAbbr', None, 8, 'AN')
        self.orderId = qqdField('orderId', None, 8, 'AN')
        self.txnTime = qqdField('txnTime', None, 14, 'YYYYMMDDhhmmss')
        self.orderTimeout = qqdField('orderImeout', None, 10, 'N')
        self.defaultPayType = qqdField('defaultPayType', None, 4, 'N')
        self.subPayType = qqdField('subPayType', None, 128, 'AN')
        self.payType = qqdField('payType', None, 4, 'N')
        self.currencyCode = qqdField('currencyCode', None, 3, 'AN')
        self.accType = qqdField('accType', None, 2, 'N')
        self.accNo = qqdField('accNo', None, 1024, 'AN')
        self.payCardType= qqdField('payCardType', None, 2, 'N')
        self.issInsCode = qqdField('insInsCode', None, 11, 'ANS')
        self.issInsProvince = qqdField('issInsCity', None, 30, 'ANS')
        self.issInsName = qqdField('issInsName', None, 60, 'ANS')
        self.customerInfo = qqdField('customerInfo', None,1024, 'ANS')
        self.txnAmt = qqdField('txnAmt', None, 12, 'N')
        self.balance = qqdField('balance', None, 256, 'AN')
        self.billType = qqdField('billType', None, 2, 'ANS')
        self.billNo = qqdField('billNo', None, 64, 'ANS')
        self.bussCode = qqdField('bussCode', None, 20, 'ANS')
        self.billPeriod = qqdField('billPeriod', None, 17, 'ANS')
        self.billQueryInfo = qqdField('billQueryInfo',None,17,'ANS')
        self.billDetailInfo = qqdField('billDetailInfo', None, 2048, 'ANS')
        self.bindId = qqdField('bindId', None, 128, 'ANS')
        self.bindInfoQty = qqdField('bindInfoQty', None, 2, 'N')
        self.bindInfoList = qqdField('bindInfoList', None, 2048, 'ANS')
        self.batchNo = qqdField('batchNo', None, 4, 'N')
        self.totalQty = qqdField('totalQty', None, 6, 'N')
        self.totalAmt = qqdField('totalAmt', None, 12, 'N')
        self.fileType = qqdField('fileType', None, 2, 'N')
        self.fileName = qqdField('fileName', None, 64, 'ANS')
        self.fileContent = qqdField('fileContent', None, 0, 'ANS')
        self.reqReserved = qqdField('reqReserved', None, 1024, 'ANS')
        self.reserved = qqdField('reserved', None, 2048, 'ANS')
        self.termId = qqdField('termId', None, 8, 'AN')
        self.issuserIdentifyMode = qqdField('issuserIdentifyMode', None, 1, 'N')
        self.customerIp = qqdField('customerIp', None, 40, 'NS')
        self.queryId = qqdField('queryId', None, 21, 'AN')
        self.origQryId = qqdField('origQryId', None, 21, 'AN')
        self.traceNo = qqdField('traceNo', None, 6, 'N')
        self.traceTime = qqdField('traceTime', None, 10, 'MMDDhhmmss')
        self.settleDate = qqdField('settleDate', None, 4, 'MMDD')
        self.settleCurrencyCode = qqdField('settleCurrencyCode', None, 3, 'AN')
        self.settleAmt = qqdField('settleAmt', None, 12, 'N')
        self.exchangeRate = qqdField('exchangeRate', None, 8, 'N')
        self.exchangeDate = qqdField('exchangeDate', None, 4, 'MMDD')
        self.origRespCode = qqdField('origRespCode', None, 2, 'AN')
        self.origRespMsg = qqdField('origRespMsg', None, 256, 'ANS')