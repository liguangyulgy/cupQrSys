__author__ = 'LiGuangyu'
import appSys
import cupQrSys
import logging;logging.basicConfig(level=logging.INFO)
import multiprocessing


if __name__ == '__main__':
    pApp = multiprocessing.Process(target=appSys.main,name='APPServer')
    pQr = multiprocessing.Process(target=cupQrSys.main, name='QRServer')
    pApp.start()
    pQr.start()
    pass

