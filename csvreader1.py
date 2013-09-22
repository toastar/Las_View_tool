#!/usr/bin/python

import csv
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from functools import partial
from Las_view_all import *

datadir='/home/karl/open_data/rmotc/DataSets/Well Log/CD Files/'

#start event handler

def onclick(event):
    #if event.dblclick:
        #print event.button

        lookupfile(event.xdata,event.ydata)


fig = plt.figure()
connection_id = fig.canvas.mpl_connect('button_press_event', onclick)
#end event handler



def lookupfile(xx,yy):
    #look up which file has the closet point
    
    print xx
    print yy
    
    mindist=1e31
    for i in range(len(x)):
        dist=(x[i]-xx)*(x[i]-xx)+(y[i]-yy)*(y[i]-yy)
        if (dist<mindist):
            mindist=dist
            indx_mindist=i

    print mindist, indx_mindist
    filename=datadir+'/'+data['dir'][indx_mindist]+'/'+data['filename'][indx_mindist]
    print filename
    #build the las name
    #finalname = datadir+
    
    #kick off the LAS viewer
    plotAllLas(filename)
    





ifile  = open("sonic.las", "rb")
reader = csv.reader(ifile)
 
rownum = 0
data={'filename':[],'dir':[],'api':[],'wellname':[],'x':[],'y':[],'curve':[]}
print data

for row in reader:
    column_num=0
    if(row[4]!="#N/A"):
        for column_name in ['filename','dir','api','wellname','x','y','curve']:
        #print "append ",row[column_num],"to" ,column_name,"column_num=",column_num
            data[column_name].append(row[column_num])
            column_num += 1    
        rownum += 1
        #if rownum>3 : break

#for column_name in ['filename','dir','api','wellname','x','y','curve']:
#    print column_name, data[column_name]
print data["x"]
data['x'],data['y']
x=np.array(data['x'],dtype=np.float)
y=np.array(data['y'],dtype=np.float)
#print "x=",x
#print "y=",y


ifile.close()

#for i in range(len(x)):
#    plt.annotate(wellno[i],xy=(x[i],y[i]),ha="left",va="center")

plt.scatter(x,y)
plt.show()
