#!/usr/bin/env python
#_*_ coding:utf-8 _*_
from dingtalkchatbot.chatbot import DingtalkChatbot
from http.server import BaseHTTPRequestHandler, HTTPServer


level_dict = {
               "info":"60e9e6c15f5e768fdb9f97f3a5bb2332f5de4e5d98467f7a915c450dc4bb19bc",
               "warn":"6b79f67990cf8e1c8d77e416e84462fdb578bcf2c95847e3556c9fd768a65c90",
               "error":"c8b5798f932d4da93789443ca712d6f7239dfd1a0b3f86f31da95929bac0b9f7",
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











