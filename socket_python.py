import socket 
import sys
import time
from datetime import datetime
import csv


command_channel = ["IM3\r\n","TS2\r\n","\x1bT\r\n","LF001,530\r\n"] #for channel_info_python
time_today = datetime.today().strftime('%Y/%m/%d,%H:%M:%S\r\n')
command_init = ["CS1\r\n","BO1\r\n","SD"+time_today[:1]+time_today[3:],"UD0\r\n"] #for initialising
command_meas = ["TS0\r\n","\x1bT\r\n","FM1,001,530\r\n"] #for measurement

BUF_MAX = 4096
PORT = 34150

def selectCommands(mode):
    print(mode)
    command = []
    if mode=='chan':
        command = command_channel
    elif mode=='init':
        command = command_init
    elif mode=='meas':
        command = command_meas
    
    return command

def run(ip_address,mode):
    so = socket.socket(socket.AF_INET,socket.SOCK_STREAM, socket.IPPROTO_TCP)
    command = selectCommands(mode)
    print("command :",command)
    SERVER = ip_address
    ADDR = (SERVER,PORT)
    so.connect(ADDR)
    for i in range(len(command)):
        write = True
        print("commands: ",command[i])
        so.send(command[i].encode())
        recvMsg(so,command[i],write)
        if (i==3 and mode=="chan"):# or (i==2 and mode=="meas"):
            write = False
            recvMsg(so,command[i],write)
            time.sleep(0.1)
            #recvMsg(so,command[i],write) #for windows this needs to be commented 
        time.sleep(0.1)
    so.close()




def recvMsg(so,msg,write):
    buf = so.recv(BUF_MAX)
    data = buf.decode('latin-1')
    size = len(data)
    
    if msg[0]=='F' and msg[1]=='M':
        f = open("temp.csv","a",newline="")
        if write==True:
            tup = ("number","value")
            writer = csv.writer(f)
            writer.writerow(tup)
        for i in range(size):
            tup = (i,ord(data[i]))
            writer = csv.writer(f)
            writer.writerow(tup)
        f.close()
    
    if msg[0]=='L' and msg[1]=='F':
        print(data)
        if write==True:
            f = open("channel_info_python.csv","w",newline="")
            tup = ("number","value")    
            writer = csv.writer(f)
            writer.writerow(tup)
        elif write==False:
            f = open("channel_info_python.csv","a",newline="")
            
        for i in range(size):
            tup = (i,ord(data[i]))
            writer = csv.writer(f)
            writer.writerow(tup)
        f.close()
