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





for i in range(len(allFileList)):
    with open(mypath+allFileList[i]) as f:
        try:
            data=json.load(f)
            cd=data['cwbopendata']['dataset']['contents']['content']
            d=cd.split(',')
            e=np.array(d).astype('float')
            f=np.split(e, 881, axis=0)
            a=pd.DataFrame(f)
            b=a.T
            b.replace(-999.0, 0.0, inplace=True)
            b.replace(-99.0, 0.0, inplace=True)
            b[b<0]=np.nan
            b.replace('NaN', 0.0, inplace=True)
            m = Basemap(projection='cyl', llcrnrlat = 17,llcrnrlon = 114.0
                        , urcrnrlat = 30.0125,urcrnrlon = 127.5125,epsg=3821)
            fig = plt.figure(figsize=(4,3), dpi=300)
            ax = fig.add_subplot(1, 1, 1)
            aaaa= m.readshapefile('COUNTY_67lon', name='COUNTY_67lon', drawbounds=True, 
                                  ax=ax,default_encoding='iso-8859-15')
            X, Y = np.meshgrid(np.linspace(115,126.5125,921), np.linspace(18,28.0125,881))
            RAD_level=[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
            RAD_cmap=['#FFFFFF','#FFFFFF','#FFFFFF','#FF9090','#FF6060','#FF2020','#CC0000',
                      '#A00000','#600000','#400000']
            cs = m.contourf(x=X, y=Y, data=a,ax=ax,cmap='Oranges')
            ax.set_xticks(np.linspace(115,127,8))
            ax.set_yticks(np.linspace(15,28,13))
            ax.set_xlabel(r'longtitude($^o$)',fontdict={'fontsize':8})
            ax.set_ylabel(r'latitude($^o$)',fontdict={'fontsize':8})
            cbar = fig.colorbar(cs, ax=ax, shrink=0.8)
            cbar.ax.tick_params(labelsize=10)
            plt.savefig('../'+allFileList[i].rstrip('.txt')+'.png', dpi= 300)
        except :
            print(allFileList[i])
            pass
