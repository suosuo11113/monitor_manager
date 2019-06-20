#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import os,sys
from django.http import HttpResponse

os.chdir(os.path.split(os.path.realpath(sys.argv[0]))[0])
sys.path.append("../")
from  dingding import Dingding



#钉钉事物通知接口
def dingding_info(req):
    xiaoding = Dingding.Drobot("info")
    if req.method == "POST":
        #msg = req.body.decode('unicode-escape')
        msg = req.body.decode('GBK')
        xiaoding.send_text(msg)
    return HttpResponse()

#钉钉告警通知接口
def dingding_warn(req):
    xiaoding = Dingding.Drobot("warn")
    if req.method == "POST":
        msg = req.body.decode('GBK')
        xiaoding.send_text(msg)
    return HttpResponse()

#钉钉错误通知接口
def dingding_error(req):
    xiaoding = Dingding.Drobot("error")
    if req.method == "POST":
        msg = req.body.decode('GBK')
        xiaoding.send_text(msg)
    return HttpResponse()

