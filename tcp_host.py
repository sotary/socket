#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 10:17:08 2018

@author: li
"""

import socket
bind_ip = "10.42.0.1"
bind_port = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))
#表示最多建立5个连接
server.listen(5)
try:
        while True:
                client,add = server.accept()
                print ("[*]你监听的是：%s:%d" % (add[0],add[1]))
                while True:
                        data = client.recv(1024)
                        if not data:
                                break
                        print(data)
                        data = input('> ')
                        client.send(data)
#                       print data
                else:
                        client.close()
except Exception as e:
        print(e)
server.close()