# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 14:24:55 2020

@author: Luming
"""

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
#module
import paramiko
import os

#====================upload the file to server===========================

def Sftp_upload_file(server_path, local_path):
    try:
        sf = paramiko.Transport((Ip,Port))
        sf.connect(username=User, password=Password)
        sftp = paramiko.SFTPClient.from_transport(sf)
        sftp.put(local_path,server_path)
        sf.close()
        sftp.close()
    except:
        print('error upload')

  

allFileList = os.listdir(local)
try:
    for i in range(len(allFileList)):
        local_path= local+allFileList[i]
        server_path= remote+allFileList[i]
        Sftp_upload_file(server_path, local_path)
except:
        print("error"+allFileList[i])
    