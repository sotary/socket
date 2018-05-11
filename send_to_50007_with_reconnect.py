#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 16:49:01 2018

@author: li
"""

import os,sys,time
import socket
# host ip address
target_host = '10.42.0.243'
# port number is 50007,any number > 10000 is ok.大于10000的端口号都可以，一共有65535个端口号
target_port = 50007
# function to build a tcp connection
#socket.SOCK_STREAM 是数据流,一般是tcp/ip协议的编程,SOCK_DGRAM分是数据包,是udp协议网络编程
def doConnect(host,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try :         
        sock.connect((host,port))
    except :
        pass 
    return sock
def main():   
    host,port = target_host,target_port
    sockClient = doConnect(host,port)   
    
    while True :
        try :
            #python3 is 'input()',while python2 is 'raw_input()'
            #二者区别参见google
            data = input('> ')
            sockClient.send(data.encode("utf-8"))
        except socket.error :
            print ("\r\nsocket error,do reconnect ")
            #出现error则每3秒重连一次
            time.sleep(3)
            sockClient = doConnect(host,port)   
        except :
            print ('\r\nother error occur ')            
            time.sleep(3) 
        time.sleep(1)
    
if __name__ == "__main__" :
    main()

##建立一个socket对象
#client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#
##链接客户端
#client.connect((target_host,target_port))
#
#
#while True:
#        data = input('> ')
#        client.send(data.encode("utf-8"))
#    
#        
#        print (data)
