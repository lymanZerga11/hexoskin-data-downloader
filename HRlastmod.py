import json
import requests
import os
import csv
import pickle

headers={'Authorization':'Basic Y3Zlbm9idXJpKzJAZ21haWwuY29tOkhleG9za2lu'}
r=requests.get('https://api.hexoskin.com/api/record/',headers=headers)
data=json.loads(r.text)
count=0
ids=[]

#check file exist or create new
if not os.path.isfile("lastmod.p"):
    j=open("lastmod.p",'w')
    j.close()
checkfile="lastmod.p"
checker=open(checkfile,"rb")
#check file empty or create dictionary
if not os.stat("lastmod.p").st_size == 0:
    #import dictionary
    dictoflast=pickle.load(checker)
else:
    dictoflast={}
#if key exist
for i in range(0,data['meta']['total_count']):
       if not ((data['objects'][i]['id']) in dictoflast):
           dictoflast[data['objects'][i]['id']]=''        
#write everything back in
   
for i in range(0,data['meta']['total_count']):
    if(data['objects'][i]['last_modified']!=dictoflast[data['objects'][i]['id']]):
        ids.append(data['objects'][i]['id'])
        dictoflast[data['objects'][i]['id']]=data['objects'][i]['last_modified']
        count=count+1
pickle.dump(dictoflast,open("lastmod.p","wb"))
print(ids)
headers={'Authorization':'Basic Y3Zlbm9idXJpKzJAZ21haWwuY29tOkhleG9za2lu'}
datatype1=19
datatype2=33
datatype3=36
datatype4=53
datatype5=49
for i in range(0,count):
    print("Heart Rate for Record No. ",ids[i])
    link='https://api.hexoskin.com/api/data/?datatype__in='+str(datatype1)+','+str(datatype2)+','+str(datatype3)+','+str(datatype4)+','+str(datatype5)+'&record='+str(ids[i])
    r=requests.get(link,headers=headers,stream=True)
    data=json.loads(r.text)
    filename=str(ids[i])+'.csv'
    print(len(data[0]["data"][str(datatype1)]))
    print(len(data[0]["data"][str(datatype2)]))
    coun=0
    for p in data[0]["data"][str(datatype1)]:
        p.append(data[0]["data"][str(datatype2)][coun][1])
        p.append(data[0]["data"][str(datatype3)][coun][1])
        p.append(data[0]["data"][str(datatype4)][coun][1])
        p.append(data[0]["data"][str(datatype5)][coun][1])
        coun=coun+1
        
    with open(filename, "w",newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp","Heart Rate","Breathing Rate","Minute Ventilation","Cadence","Activity"])
        writer.writerows(data[0]["data"]["19"])



#,'Accept':'text/csv',"Content-Type": "text/csv"
