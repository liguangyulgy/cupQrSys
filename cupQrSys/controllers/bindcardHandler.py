__author__ = 'LiGuangyu'

from common.webServer import get,post,HttpServerTools
import logging;logging.basicConfig(level=logging.INFO)
from common.protocols.qqdBindCard import BindcardRequest



@post('/bindcardGate')
async def bindCardGate(body):
    print(body)
    bcReq = BindcardRequest()


    pass