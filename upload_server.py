# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 14:24:55 2020

@author: Luming
"""


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
    