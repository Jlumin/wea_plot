# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 13:41:32 2020

@author: Luming
"""

#module
import paramiko
import os


# =========================test the server connecting status ================================
# def sftp_exec_command(command):
#     try:
#         ssh_client = paramiko.SSHClient()
#         ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         ssh_client.connect(host, 22, user, password)
#         std_in, std_out, std_err = ssh_client.exec_command(command)
#         for line in std_out:
#             print (line.strip("\n"))
#             ssh_client.close()
#     except (Exception, e):
#         print (e)
# if __name__ == '__main__':
#     sftp_exec_command("ls -l")
# =============================================================================
#====================download the file in remote server===========================
def DownLoadFile(sftp,LocalFile,RemoteFile):  # 下載當個檔案
    file_handler = open(LocalFile, 'wb')
    print(file_handler)
    sftp.get(RemoteFile, LocalFile)  # 下載目錄中檔案
    file_handler.close()
    return True

def DownLoadFileTree(sftp, LocalDir, RemoteDir):  # 下載整個目錄下的檔案
    if not os.path.exists(LocalDir):
        os.makedirs(LocalDir)
    for file in sftp.listdir(RemoteDir):
        Local = os.path.join(LocalDir, file)
        Remote=os.path.join(RemoteDir, file)
        if file.find(".") == -1:#判斷是否是檔案
            if not os.path.exists(Local):
                os.makedirs(Local)
            DownLoadFileTree(sftp,Local, Remote)
        else:#檔案
            DownLoadFile(sftp,Local, Remote)
    return "complete"


if __name__ == '__main__':
  sf = paramiko.Transport((Ip, Port))
  sf.connect(username=User, password=Password)
  sftp = paramiko.SFTPClient.from_transport(sf)
  DownLoadFileTree(sftp,local,remote)#下載
sftp.close()
sf.close()

#====================Delete the file in remote server===========================
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=Ip,port=22,username=User,password=Password)
sftp = ssh.open_sftp()
for file in sftp.listdir(remote):
    sftp.remove(remote+file)
sftp.close()
sf.close()


