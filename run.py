# -*- coding: utf-8 -*-

from BaiduMapPoi.orm.operate import Operate
from BaiduMapPoi import setting
from BaiduMapPoi.baidu_exception import *
from BaiduMapPoi.log import logger
from BaiduMapPoi.signal_process import SignalProcess

sig = SignalProcess()
op = Operate(setting.DB_CONFIG)

while(True):
    communities = op.query_community(10)
    for com in communities:
        try:
            op.insert(com)
        except GeoApiError as e:
            logger.warn("!!!!!!!! GeocodingApi error: %s, status code: %d !!!!!!!!" % (com.title, e.status))
            com.lat = 0.0
            com.lng = 0.0
            op.commit()
        except PlaceApiError as e:
            logger.warn("!!!!!!!! PlaceApi error: %s, status code: %d !!!!!!!!" % (com.title, e.status))
            break
        else:
            if sig.is_interrupt == True:
                break
    else:
        continue
    break

op.finish()
