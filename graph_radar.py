# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:27:31 2020

@author: Luming
"""
import os
import numpy as np
import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from mpl_toolkits.basemap import Basemap
import json
mypath='/Users/wujim/Desktop/icebergtek/氣象局資料/data/'
allFileList = os.listdir(mypath)



# with open('../data/acc3_20200214224048.json') as f:
#     data=json.load(f)
#     c=data['cwbopendata']['dataset']['contents']['content']

for i in range(len(allFileList)):
    with open(mypath+allFileList[i]) as f:
        try:
            data=json.load(f)
            c=data['cwbopendata']['dataset']['contents']['content']
            d=c.split(',')
            e=np.array(d).astype('float')
            f=np.split(e, 921, axis=0)
            a=pd.DataFrame(f)
            b=a.T
            #b=a
            RAD_cmap = ['#FFFFFF','#FFD8D8','#FFB8B8','#FF9090','#FF6060','#FF2020','#CC0000','#A00000','#600000','#400000']
            level = [-5, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
            m = Basemap(projection='cyl', llcrnrlat = 20.5,llcrnrlon = 118.5, urcrnrlat = 26.0125,urcrnrlon = 123.0)
            fig = plt.figure(figsize=(4,3), dpi=300)
            ax = fig.add_subplot(1, 1, 1)
            b.replace(-999.0, 0.0, inplace=True)
            b.replace(-99.0, 0.0, inplace=True)
            aaaa= m.readshapefile('COUNTY84', name='COUNTY84', drawbounds=True, ax=ax, default_encoding='iso-8859-15')
#fig, ax1 = plt.subplots(1, 1)
            X, Y = np.meshgrid(np.linspace(115,126.5125,921), np.linspace(15,26.0125,881))
            cs = m.contourf(x=X, y=Y, data=b, ax=ax,levels=level)
            ax.set_xlabel(r'longtitude($^o$)',fontdict={'fontsize':10})
            ax.set_ylabel(r'latitude($^o$)',fontdict={'fontsize':10})
            plt.savefig('../'+allFileList[i].rstrip('.txt')+'.png', dpi= 300)
#     d=c.split(',')
#     e=np.array(d).astype('float')
        except :
            pass
#f=np.split(e, 921, axis=0)

#a=pd.DataFrame(f)
#a=np.random.randn(921,881)
#print(a)

#basic setting
#start_point=[115.0,18.0] #Bottom left corner start
#point_dis=0.0125 # the distance between two points
#grid_size=[921,881]


#m = Basemap(projection='cyl', llcrnrlat = 15.0,llcrnrlon = 115.0, urcrnrlat = 26.5125,
 #           urcrnrlon = 126.0125)

#fig = plt.figure(figsize=(4,3), dpi=300)
#ax = fig.add_subplot(1, 1, 1)

#aaaa= m.readshapefile('COUNTY84', name='COUNTY84', drawbounds=True, ax=ax, default_encoding='iso-8859-15')
#fig, ax1 = plt.subplots(1, 1)
#X, Y = np.meshgrid(np.linspace(115,126.0125,881), np.linspace(15,26.5125,921))
#cs = m.contourf(x=X, y=Y, data=a, ax=ax)
#ax.set_xlabel(r'longtitude($^o$)',fontdict={'fontsize':10})
#ax.set_ylabel(r'latitude($^o$)',fontdict={'fontsize':10})
#plt.show()