__author__ = 'LiGuangyu'

import asyncio
import hashlib
import logging;
import time

from aiohttp import web

from common.webServer import post
import appSys.tableSchema as ts
from common.mysql import dbInf
from common.redis import redis
from common.protocols.qqdBindCard import BindcardRequest

logging.basicConfig(level=logging.INFO)



@post('/bindcard')
async def bindCard(customerNm, certifTp, certifId, cardNumber, request):
    '''用户绑卡'''
    user = request.__user__
    if not user:
        raise Exception('No User Info')
    '''1. 信息落库'''
    await dbInf.insert(ts.BindCard, {}, userId = user['userId'], customerNm = customerNm, certifId = certifId, certifTp = certifTp, cardNumber = cardNumber, status = 'UPREQ')
    logging.info('User %s try to bind card' % user['userName'])
    '''2. 构建报文'''
    bcReq = BindcardRequest()
    bcReq.txnType = '79'
    bcReq.txnSubType = '00'
    bcReq.bizType = '000902'
    bcReq.accessType = '1'
    bcReq.channelType = '07'
    bcReq.frontUrl = 'http://localhost:8888/bindcardinterface'
    bcReq.backUrl = 'http://localhost:8888/bindcardinterface'
    bcReq.acqInsCode = '00001111'
    bcReq.merId = '010123400001111'
    bcReq.merCatCode = '0000'
    bcReq.merName = '测试1'
    bcReq.merAbbr = 'test'
    bcReq.orderId = await redis.getOrderId()
    bcReq.txnTime = await redis.getTime()

    bcReq.accNo = cardNumber            #需要加密

    bcReq.customerInfo.certifTp = certifTp
    bcReq.customerInfo.certifId = certifId
    bcReq.customerInfo.customerNm = customerNm

    print(bcReq)



    '''3. 提交银联二维码平台cupQrSys'''
    '''4. 收到应答后落库'''
    '''5. 重定向到银联绑卡页面'''
    pass

