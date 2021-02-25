#!/usr/bin/env python3.6
# -*- coding:utf-8 -*-
# __author__: sdc

 
"""
    当我们运行该程序时因为 while True 所以会持续的运行. 
    这里监听的是 SIGTERM 信号, 所以当我们在终端输入 kill pid (linux kill
    默认是发送SIGTERM)时, 
    程序就会输出: 收到信号 15 <frame object at 0x7ff695738050> 0
    当超过3次时就强制把自己杀死.
    所以 SIGTERM 很适合用来做一些清理的工作
"""
 
import os
import sys
import time
import signal
import socket
import subprocess
from multiprocessing import Process
 
receive_times = 0
 
def handler(signalnum, frame):
    global receive_times
    print("signal: ", signalnum, frame, receive_times)
    receive_times += 1
    #if receive_times > 3:
    #with open("/root/1.txt", "a") as ff:
    #    ff.write("int")
    exit(0)
 
def handler1(signalnum, frame):
    global receive_times
    print("signal: ", signalnum, frame, receive_times)
    receive_times += 1
    #with open("/root/1.txt", "a") as ff:
    #    ff.write("term")
    #if receive_times > 3:
    exit(0)

def task():
    hostname = socket.gethostname()
    port = 9092
    ip = '10.255.175.109'
    command = '''
                 docker run -p %s:%s --name kafka -d -e KAFKA_BROKER_ID=0 \
                                                         -e KAFKA_ZOOKEEPER_CONNECT=%s:2181 \
                                                         -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://%s:%s \
                                                         -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:%s kafka:latest
    ''' % (port, port, ip, ip, port, port,)
    subprocess.Popen(command, shell=True)

def main():
    print("pid:", os.getpid()) 
    signal.signal(signal.SIGTERM, handler1)
    signal.signal(signal.SIGINT, handler)
 
if __name__ == '__main__':
    main()
    task()
    #p = Process(target=task, )
    #p.daemon = True
    #p.start()
    #p.join()
    while True:
        pass
