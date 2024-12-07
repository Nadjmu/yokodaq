import numpy as np
import matplotlib.pyplot as plt
import csv

import pandas as pd
import os

import time as timee

from socket_python import run
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
#data = pd.read_csv("temp.csv")

#channel_info = pd.read_csv("channel_info.csv")

#os.remove("temp.csv")

##units are the V or C of selected_channel
units = ["V","°C","mV"]
#test
#####################beginning#################################

def getData(data): #function to read the data of the csv file
    values = np.array(data["value"]) 
    return values

def getChannelData(channel_info): #function to read all the channel information
    values = np.array(channel_info["value"])
    return values

def getSubUnits(chinfo): #function to get all the subunits connected
    size = int(chinfo.size/15)
    subunit_it = np.zeros(size)
    for i in range(size):
        subunit_it[i] = chinfo[2+i*15] ##iterate through all subintindex
    subunitset = set(subunit_it)
    return np.array(list(subunitset)).astype(int)-48    ##makes a numpy array 

#####################helper functions#################################
def split_values(values,num_measurement,num_of_subunits): #function to split the values into appropriate sizes of individual measurement
    slicee = np.arange(1,num_measurement)*(10+num_of_subunits*180)
    measurements = np.split(values,slicee)
    return measurements
    
def convert_hexstream_to_byte(hexstring):
    return bytearray.fromhex(hexstring), int(len(hexstring)/2)

def access_index(measurement,index):
    return measurement[index-1];

def print_array(measurement,length):
    for i in range(length):
        print("i=",i+1, "measurement:   ",measurement[i])


#######################################################################

def subunitDiff(subunits,subunit): ##e.g. computes with index of subunit
    index = np.where(subunits == subunit) ##
    diff = subunits-(np.arange(subunits.size)) ##
    return diff[index]


def encodeChannelID(chinfo,selected_channel): ##adds the unit to the channelID
    pos = 0
    buffer = np.array([])
    for chid in selected_channel:
        index1 = int(chid/100)
        index2 = int((chid-index1*100)/10)
        index3 = chid-index1*100-index2*10
        for i in range(int(chinfo.size/15)): #finds channel 
            if (index1==(chinfo[2+i*15]-48) and index2==(chinfo[3+i*15]-48) and index3==(chinfo[4+i*15]-48)): 
                pos = i
                break
        if (chinfo[pos*15+5] == 86):  ##if V  #here add mV : index 86->V 109->m
            chid = chid+1000
        elif (chinfo[pos*15+6] == 67):  ##if °C
            chid = chid+2000
        elif (chinfo[pos*15+5] == 109 and chinfo[pos*15+6] == 86):
            chid = chid*3000
        buffer = np.insert(buffer,buffer.size,chid)
    selected_channel = buffer.astype(int)
    #print(selected_channel) ##should be like 2101 instead of 101
    return selected_channel
   
   
def decodeChannelID(channelid): ##decodes 2109 to 2,1,9 
    unit_index = int(channelid/1000)
    channelid = channelid - unit_index*1000
    subunit = int(channelid/100)
    channel = channelid-subunit*100
    return unit_index,subunit,channel

def writeToCSV(date,time,subunit,channel,signal_name,value,unit,sel_len): #writes the data to temporary csv file
    f = open("tempp.csv","a",newline="")
    subchan = subunit*100+channel
    time = str(time[0])+":"+str(time[1])+":"+str(time[2])
    date = str(date[0])+":"+str(date[1])+":"+str(date[2])
    value = str(value)#+" "+unit
    unit = str(unit)
    tup = (date,time,subchan,signal_name,value,unit,sel_len)
    writer = csv.writer(f)
    writer.writerow(tup)
    f.close()


def writeToInflux(database_settings):
    #token = "CRSsWRfqDcFdLUwg1G_IFuSHgMRZ-QpJ3BAA1XSdYD9c41eFegO6R7H6lWmkzUtQSfeLZ3E0PKJEqV_8d2YMeQ=="
    #org = "ETHZ"
    #bucket = "ETherm"
    
    #measurement_name = "test7"
    
    measurement_name = database_settings[0]
    org = database_settings[1]
    bucket = database_settings[2]
    token = database_settings[3]
    
    client = InfluxDBClient(url="http://localhost:8086", token=token)
    
    write_api = client.write_api(write_options=SYNCHRONOUS)
    
    
    f = open("tempp.csv","r")
    data = f.read()
    f.close()
    #time2 = timee.time()
    #print("time to open and close csv",(time2-time1)*1000)
    lines = data.split('\n')
    _,_,_,_,_,_,size = lines[-2].split(',')
    size=int(size)
    print(size)
    counter = 0
    influxData=""
    for line in lines[-size-1:-1]:
        if len(line)>1:
            counter+=1
            _,_,ch,name,v,u,_ = line.split(',')
            # influxData = measurement_name+","+"Signal_Name="+str(name)+","+"unit="+str(u)+" "
            # influxData += "CH"+str(ch)+"="+str(v)
            # time1 = timee.time()
            # write_api.write(bucket,org,influxData)
            # time2 = timee.time()
            #print("time write api",(time2-time1)*1000)
            influxData+=measurement_name+"," #measurement name
            influxData+="Signal_Name="+str(name) #signal name tag
            influxData+=","
            influxData+="unit="+str(u) #unit tag
            influxData+=" "
            influxData+="CH"+str(ch)+"="+str(v) #field key + value
            
            if (counter!=size):
                influxData+="\n"
    
    #print(influxData)
    #influxData = "mem,host=host1 used_percent=23.43234543"
    write_api.write(bucket,org,influxData)

def getValue(measurement,subunits,subunit,channel,unit):
    diff = subunitDiff(subunits,subunit)
    # date = getDate(measurement)
    # time = getTime(measurement)
    # print("date:   ",date[2],".",date[1],".",date[0])
    # print("time:   ",time[0],":",time[1],":",time[2])
    
    pin = 7+(subunit-diff[0])*180+channel*6 ##pin 4th information byte
    if (unit == "V"):
        value = 0.0001*(measurement[pin]*256+measurement[pin-1]) ##calculate V 
    elif (unit == "°C"):
        value = 0.1*(measurement[pin]*256+measurement[pin-1]) ##calculate C
    elif (unit == "mV"):
        value = 0.01*(measurement[pin]*256+measurement[pin-1])##calculate mV
    value = round(value,2)
    #print("Subunit: ",subunit,"     Channel: ",channel,"    ",value,unit)
    return value,unit


def getAllChannel(measurement,chinfo,selected_channel,signal_names,database_settings,database_mode,units = units): 
    subunits = getSubUnits(chinfo)
    selected_channel = encodeChannelID(chinfo,selected_channel) ##expands channelid
    date = getDate(measurement)
    time = getTime(measurement)
    print("date:   ",date[2],".",date[1],".",date[0])
    print("time:   ",time[0],":",time[1],":",time[2])
    counter=0
    for channelid in selected_channel:
        #print("channelid :",channelid)
        #time1 = timee.time()
        unit_index,subunit,channel = decodeChannelID(channelid)
        #print("decode Channel:   ",(timee.time()-time1)*1000)
        #print("unit index:   ",unit_index)
        value,unit = getValue(measurement,subunits,subunit,channel,units[unit_index-1])
        #print("unit: ",unit)
        writeToCSV(date,time,subunit,channel,signal_names[counter],value,unit,len(selected_channel))
        counter+=1
    if database_mode==True:
        writeToInflux(database_settings)
    

def getDate(measurement):
    return measurement[2:5]

def getTime(measurement):
    return measurement[5:8]

def runMeasurement(ip_addr):
    #command = "v1 "+ip_addr
    #os.system(command)
    run(ip_addr,'meas')

def runInitialise(ip_addr):
    #command = "init "+ip_addr
    #os.system(command)
    run(ip_addr,'init')

def runChInformation(ip_addr):
    #command = "chInfo "+ip_addr
    #os.system(command)
    run(ip_addr,'chan')



if __name__ == "__main__":
    chinfo = getChannelData(channel_info) ##reads from channel information csv 
    measurement = getData(data) ##reads from measurement (temp) csv
    selected_channel = np.array([101,509,109,302])
    getAllChannel(measurement,chinfo,selected_channel)

