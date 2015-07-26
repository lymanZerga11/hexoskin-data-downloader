import json
import requests
import csv
#A separate program for ECG as frequency is not the same as the others
#Basic program layout is the same
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
datatype=4113				#datatype id for ECG (THERE ARE TWO MORE DATATYPES FOR ECG) (not sure what they are for)
for i in range(0,count):
    print("ECG for Record No. ",ids[i])
    link='https://api.hexoskin.com/api/data/?datatype__in='+str(datatype)+'&record='+str(ids[i])
    r=requests.get(link,headers=headers,stream=True)
    data=json.loads(r.text)
    filename=str(ids[i])+'ECG.csv'										#write to file (recordid)ECG.csv
    if(len(data)==0 or len(data[0])==0 or len(data[0]["data"])==0): 	#if record exists but ECG data not synced print NOT SYNCED and continue to next ID
        print("NOT SYNCED")					
        continue
    print(len(data[0]["data"][str(datatype)]))
    with open(filename, "w",newline='') as f:		
        writer = csv.writer(f)
        writer.writerows(data[0]["data"][str(datatype)])
