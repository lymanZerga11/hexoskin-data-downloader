import json
import requests
import os
import csv
import pickle
#HEADERS FOR SPECIFIC ACCOUNT
#change header to auth key for regular access
headers={'Authorization':'Basic Y3Zlbm9idXJpKzJAZ21haWwuY29tOkhleG9za2lu'}
r=requests.get('https://api.hexoskin.com/api/record/',headers=headers)
data=json.loads(r.text)						#load all record ids
count=0
ids=[]										#empty list of ids to be updated
#CREATES OR OPENS A FILE LASTMOD.P THAT STORES LIST OF ALL THE EXISTING RECORDS
if not os.path.isfile("lastmod.p"):			#check file exist or create new
    j=open("lastmod.p",'w')
    j.close()
checkfile="lastmod.p"						#file name 
checker=open(checkfile,"rb")				#open FILE stream	
if not os.stat("lastmod.p").st_size == 0:	#check if file empty
    #import dictionary
    dictoflast=pickle.load(checker)			#dictionary of records
else:														
    dictoflast={}							#if file empty initialize empty dictionary
#if key exist
for i in range(0,data['meta']['total_count']):
       if not ((data['objects'][i]['id']) in dictoflast):
           dictoflast[data['objects'][i]['id']]=''        #if record id not in dictionary then initialize empty dictionary element for the id
#write everything back in   
for i in range(0,data['meta']['total_count']):
    if(data['objects'][i]['last_modified']!=dictoflast[data['objects'][i]['id']]):			#if record was modified after last check 
        ids.append(data['objects'][i]['id'])												#add to list of records to be updated
        dictoflast[data['objects'][i]['id']]=data['objects'][i]['last_modified']			#update last modify time in dictionary of records
        count=count+1
pickle.dump(dictoflast,open("lastmod.p","wb"))												#update LASTMOD.p
print(ids)																					#list of ids to be updated


datatype1=19
datatype2=33
datatype3=36
datatype4=53
datatype5=49

for i in range(0,count):																	#loop through the record ids
    print("Heart Rate for Record No. ",ids[i])
	#get data of the 5 datatypes from Hexoskin API 
    link='https://api.hexoskin.com/api/data/?datatype__in='+str(datatype1)+','+str(datatype2)+','+str(datatype3)+','+str(datatype4)+','+str(datatype5)+'&record='+str(ids[i])
    r=requests.get(link,headers=headers,stream=True)
    data=json.loads(r.text)
    filename=str(ids[i])+'.csv'																#filename for each record
    coun=0
	#MUST BE A MUCH BETTER WAY TO DO THIS
    for p in data[0]["data"][str(datatype1)]:												#join all datatype for every timestamp into one list per row (list of lists)						
        p.append(data[0]["data"][str(datatype2)][coun][1])									
        p.append(data[0]["data"][str(datatype3)][coun][1])
        p.append(data[0]["data"][str(datatype4)][coun][1])
        p.append(data[0]["data"][str(datatype5)][coun][1])
        coun=coun+1
        
    with open(filename, "w",newline='') as f:												#write into respective record id .csv
        writer = csv.writer(f)
        writer.writerow(["Timestamp","Heart Rate","Breathing Rate","Minute Ventilation","Cadence","Activity"]) #add headings to first row
        writer.writerows(data[0]["data"][str(datatype1)])									#write the list of lists to .csv
