from pubnub import Pubnub
import time
import requests
import json 
#using Pubnub to publish live datastream into graph
pubnub = Pubnub(publish_key="pub-c-cc762884-c27c-42a6-8872-8d3f028a093f", subscribe_key="sub-c-d15b91e6-23b9-11e5-947a-02ee2ddab7fe")
count=1;
headers={'Authorization':'Basic Y3Zlbm9idXJpKzJAZ21haWwuY29tOkhleG9za2lu'}
r=requests.get('https://api.hexoskin.com/api/record/',headers=headers)
data=json.loads(r.text)
g=(data['objects'][0]['end'])			#get last TIMESTAMP for graphing
recno=str(data['objects'][0]['id'])		#latest record would be the first one always
#timer=[]
hr=[]
tr=[]	
for i in range(0,4):					#1 list of heartrate (maximum 4 at a time)
    hr.append(0)
temp=''
pr=0
#call API with record number and start as the TIMESTAMP and end as 24 hours after TIMESTAMP
link='https://api.hexoskin.com/api/data/?datatype__in=19&record='+recno+'&start='+str(g)+'&end='+str(g+24*60*60*256)
while(1):								#run infinite loop 
    r=requests.get(link,headers=headers,stream=True)
    if("data" in r.text and temp!=r.text):		#get the data values
        temp=r.text
        del tr[:]								#clear TR list (same as HR)
        data=json.loads(r.text)
        pr=0
        k=len(data[0]["data"]['19'])			#number of values obtained in this reading
        h=data[0]['data']['19'][k-1][0]			#new TIMESTAMP is the last of the current set of values
        link='https://api.hexoskin.com/api/data/?datatype__in=19&record='+recno+'&start='+str(h)+'&end='+str(g+24*60*60*256)	#call API with updated TIMESTAMP
        for s in data[0]['data']['19']:			#loop through newly received values
            pr=pr+1 
            tr.append(s[1])						#add 1 value to TR list (same as HR)
            print(str(str(s[0])+" : "+str(s[1])+"\n"))
    c=0
    print(" ")
    print pr									#total number of values entered in this loop cycle
    print(" ")
    while(pr!=0):								#publish to Pubnub (read by graph)
        pr=pr-1
        pubnub.publish(
            'hexoskin1' ,
            {"columns":[['x',count],['J',tr[c]]]}
            )
        print tr[c]
        c=c+1
        count=count+1
