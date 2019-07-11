#!/usr/bin/env python
#_*_ coding:utf-8 _*_
from dingtalkchatbot.chatbot import DingtalkChatbot
from http.server import BaseHTTPRequestHandler, HTTPServer


level_dict = {
               "info":"123",
               "warn":"456",
               "error":"789",
             }
webhook_head = "https://oapi.dingtalk.com/robot/send?access_token="
class Drobot(DingtalkChatbot):
    def __init__(self,level):
        try:
            token = level_dict[level]

        except KeyError :
            super(Drobot, self).__init__(webhook_head)
            print("there is no level:" + level)
            print('''we only have these level below:
                     1): info
                     2): warn
                     3): error
                  ''')
        else:
            super(Drobot, self).__init__(webhook_head+token)
            #self.level = level











