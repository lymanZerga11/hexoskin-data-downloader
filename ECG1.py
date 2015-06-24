import json
import requests
import csv

headers={'Authorization':'Basic Y3Zlbm9idXJpKzJAZ21haWwuY29tOkhleG9za2lu'}
r=requests.get('https://api.hexoskin.com/api/record/',headers=headers)
data=json.loads(r.text)
count=0
ids=[]
for i in range(0,data['meta']['total_count']):
    ids.append(data['objects'][i]['id'])
    count=count+1
print(ids)
headers={'Authorization':'Basic Y3Zlbm9idXJpKzJAZ21haWwuY29tOkhleG9za2lu'}
datatype=4113
for i in range(0,count):
    print("ECG for Record No. ",ids[i])
    link='https://api.hexoskin.com/api/data/?datatype__in='+str(datatype)+'&record='+str(ids[i])
    r=requests.get(link,headers=headers,stream=True)
    data=json.loads(r.text)
    filename=str(ids[i])+'ECG.csv'
    if(len(data)==0 or len(data[0])==0 or len(data[0]["data"])==0):
        print("NOT SYNCED")
        continue
    print(len(data[0]["data"][str(datatype)]))
    with open(filename, "w",newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data[0]["data"][str(datatype)])

'''        
datatype=19
for i in range(0,count):
    print("Heart Rate for Record No. ",ids[i])
    link='https://api.hexoskin.com/api/data/?datatype__in='+str(datatype)+'&record='+str(ids[i])
    r=requests.get(link,headers=headers,stream=True)
    data=json.loads(r.text)
    filename=str(ids[i])+'.csv'
    print(len(data[0]["data"]["19"]))
    with open(filename, "r",newline='') as fi:
        with open(filename, "w",newline='') as fo:
            row=next(reader)
            reader = csv.reader(fi)
            writer = csv.writer(fo)
            writer.writerows(data[0]["data"]["19"][0])


#,'Accept':'text/csv',"Content-Type": "text/csv"
'''
