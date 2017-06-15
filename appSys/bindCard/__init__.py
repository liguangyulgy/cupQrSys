__author__ = 'LiGuangyu'

import asyncio
import hashlib
import logging;
import time

from aiohttp import web

from common.webServer import post
import appSys.tableSchema as ts
from common.mysql import dbInf
from common.protocols.qqdBindCard import bindcardRequest

logging.basicConfig(level=logging.INFO)


@post('/bindcard')
def bindCard(customerNm, certifTp, certifId, accNo, request):
    '''用户绑卡'''
    user = request.__user__
    if not user:
        raise Exception('No User Info')
    '''1. 信息落库'''
    dbInf.insert(ts.BindCard, userId = user.userId, customerNm = customerNm, certifId = certifId, certifTp = certifTp, accNo = accNo, status = 'UPREQ')
    logging.info('User %s try to bind card' % user.userName)
    '''2. 构建报文'''
    bcReq = bindcardRequest()
    bcReq.accNo.v = accNo
    bcReq.txnType.v = '79'
    bcReq.txnSubType.v = '00'
    bcReq.bizType.v = '000902'
    bcReq.accessType.v = '1'
    bcReq.channelType.v = '07'
    bcReq.frontUrl.v = 'http://localhost:8888/bindcardinterface'
    bcReq.backUrl.v = 'http://localhost:8888/bindcardinterface'
    bcReq.acqInsCode.v = '00001111'
    bcReq.merId.v = '010123400001111'


    '''3. 提交银联二维码平台cupQrSys'''
    '''4. 收到应答后落库'''
    '''5. 重定向到银联绑卡页面'''
    pass

