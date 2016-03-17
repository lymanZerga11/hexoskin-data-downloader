import json
import requests
import csv
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
#to get static graph of any datatype
headers={'Authorization':'Basic Y3Zlbm9idXJpKzJAZ21haWwuY29tOkhleG9za2lu'}
r1=requests.get('https://api.hexoskin.com/api/datatype/?limit=105',headers=headers)
data1=json.loads(r1.text)
for i in data1['objects']:					#print list of datatypes
    print(str(i['dataid'])+' : '+str(i['info'])+'/n')
nameid=''
dataid=input('Please provide data id : ')	#get choice of dataid
dataidnum=int(dataid)
for i in data1['objects']:					#get name of selected dataid
    if(i['dataid']==dataidnum):
        nameid=i['info']			
r=requests.get('https://api.hexoskin.com/api/record/',headers=headers)
data=json.loads(r.text)
count=0
ids=[]
for i in range(0,data['meta']['total_count']):  #get list of record ids
    ids.append(data['objects'][i]['id'])
    count=count+1
print(ids)										#print list of record ids
datatype=dataidnum
inp=input("enter id: ")							#get choice of record id
print(nameid," for Record: ",inp)
link='https://api.hexoskin.com/api/data/?datatype__in='+str(datatype)+'&record='+inp
r=requests.get(link,headers=headers,stream=True)
data=json.loads(r.text)
x=[]
y=[]
t=0
print(len(data[0]["data"][dataid]))				#total number of data readings
for k in ((data[0]["data"][dataid])):
    if(k[1]!=None):
        t=t+1
        x.append(k[0])							#plot x
        y.append(k[1])							#plot y
		
		
##SET UP FOR PYTHON GRAPHS
#QtGui.QApplication.setGraphicsSystem('raster')
pp = QtGui.QApplication([])
win = pg.GraphicsWindow(title="Basic plotting examples")
win.resize(1000,600)
win.setWindowTitle('pyqtgraph example: Plotting')
# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)
p1 = win.addPlot(title="Basic array plotting", x=x,y=y)
#Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()


    
