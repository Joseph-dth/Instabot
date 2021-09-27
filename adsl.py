# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import time

from config import g_adsl_account

\

class Adsl(object):

    #__init__ : name: adsl名稱
    def __init__(self):
        self.name = g_adsl_account["name"]
        self.username = g_adsl_account["username"]
        self.password = g_adsl_account["password"]

    #set_adsl : 修改adsl設定
    def set_adsl(self, account):
        self.name = account["name"]
        self.username = account["username"]
        self.password = account["password"]

    #connect : 寬頻撥號
    def connect(self):
        cmd_str = "rasdial %s %s %s" % (self.name, self.username, self.password)
        os.system(cmd_str)
        time.sleep(5)

    #disconnect : 斷開寬頻連線
    def disconnect(self):
        cmd_str = "rasdial %s /disconnect" % self.name
        os.system(cmd_str)
        time.sleep(5)

    #reconnect : 重新進行撥號
    def reconnect(self):
        self.disconnect()
        self.connect()
        
        
        
        
