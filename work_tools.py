# -*- coding: utf-8 -*-

"""
description: 工作工具.
author: HuangLei
date: 2016-05-3:AM
"""

import os
import psutil
import time
import urllib


# def time_tools():
#     print '''"#############################################################"¬
# "# which server do you want, choose your server number.      #"¬
# "# 0:huanglei                                                #"¬
# "# 1:coupon_t6                                               #"¬
# "# 2:coupon_t2                                               #"¬
# "# 3:coupon_test                                             #"¬
# "# 4:coupon_stage                                            #"¬
# "# 5:bill_t6                                                 #"¬
# "# 6:bill_t2                                                 #"¬
# "# 7:riskcontrol_t5                                          #"¬
# "# 8:riskcontrol_e1                                          #"¬
# "# 9:pay_api_t2                                              #"¬
# "# 10:prefermance_php                                        #"¬
# "# 11:t19_php                                                #"¬
# "# 12:openapi_stage                                          #"¬
# "# 13:stage_php                                              #"¬
# "#############################################################"¬'''
#
#
# time_tools()
#

# 获取cpu使用情况
def get_cpu_status(interval=1):
    cpu = (" CPU: " + str(psutil.cpu_percent(interval)) + "%")
    os.system("clear")
    return cpu


# 获取内存使用情况
def get_memory_status():
    phymem = psutil.virtual_memory()
    buffers = getattr(psutil, 'phymem_buffers', lambda: 0)()
    cached = getattr(psutil, 'cached_phymem', lambda: 0)()
    used = phymem.total - (phymem.free + buffers + cached)
    line = " Memory: %5s%% %6s/%s" % (
        phymem.percent,
        str(int(used / 1024 / 1024)) + "M",
        str(int(phymem.total / 1024 / 1024)) + "M"
    )
    return line


# 时间戳转date
def time_to_date(timestamp):
    time_array = time.localtime(timestamp)
    display_date = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    return display_date


# date转时间戳
def date_to_time(date):
    date = date.strip()
    if date.find("/") > 0:
        if len(date) < 11:
            time_array = time.strptime(date, "%Y/%m/%d")
        else:
            time_array = time.strptime(date, "%Y/%m/%d %H:%M:%S")
    elif date.find("-") > 0:
        if len(date) < 11:
            time_array = time.strptime(date, "%Y-%m-%d")
        else:
            time_array = time.strptime(date, "%Y-%m-%d %H:%M:%S")
    elif len(date) == 14:
        time_array = time.strptime(date, "%Y%m%d%H%M%S")
    elif len(date) < 9:
        time_array = time.strptime(date, "%Y%m%d")
    else:
        time_array = None

    timestamp = int(time.mktime(time_array))
    return timestamp


# url解码.
def url_decode(url_source):
    return urllib.unquote(url_source)


# url编码
def url_encode(str_source):
    return urllib.quote(str_source)
