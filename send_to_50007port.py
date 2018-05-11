#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 16:11:51 2018

@author: li
"""

import socket

target_host = '10.42.0.243'
target_port = 50007

#建立一个socket对象
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#链接客户端
client.connect((target_host,target_port))


while True:
        data = input('> ')
        client.send(data.encode("utf-8"))
    
        
        print (data)