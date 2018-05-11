#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 09:58:08 2018

@author: li
"""

import socket  
address = ('10.42.0.1',10000)#本主机IP  
readdr = ("10.42.0.243",10000)#客户端主机IP  
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  
  
s.bind(address)  
while 1:  
    data,addr=s.recvfrom(2048)  
    if not data:  
        break  
    print("got data from",addr)  
    print(data.decode())  
    replydata = input("reply:")  
    s.sendto(replydata.encode("utf-8"),readdr)  
s.close()  