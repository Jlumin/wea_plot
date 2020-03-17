# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 18:54:26 2020

@author: Luming
"""
#Upload the file to server config
#parameter
# ====內網=====================================================================
Ip = "192.168.0.144"
Port = 22
# =====internet=====================================================================
#Ip = "proxy73.rt3.io"
#Port = 32966
timeout = 30
User = "pi"
Password = "odiedag8"
local = "D:/01.work/00.冰山科技/98.2020專案/wea_plan/server_auto/test/"
remote = '/home/pi/test/'#遠端檔案或目錄

#氣象局DOWNLOAD from the server 不同server
#parameter
Ip = "192.168.0.172"
Port = 22
timeout = 30
User = "pi"
Password = "raspberry"
local = "D:/01.work/00.冰山科技/98.2020專案/氣象局資料/data/"
remote = '/home/pi/radar_data/'#遠端檔案或目錄