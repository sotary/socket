#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 15:54:22 2018

@author: li
"""

import socket
 
HOST = '10.42.0.243'        #定义目标主机名
PORT = 50007                 #定义目标主机开放服务端口号
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #选择Socket类型和Socket数据包类型 
client.connect((HOST, PORT))      #连接到目标主机的socket（套接字）中
while True:
        data = input('>')
        client.send(data)  #发送数据
#data = s.recv(1024)          #接收数据
#s.close()                    #关闭socket
#print ('Received', repr(data))
