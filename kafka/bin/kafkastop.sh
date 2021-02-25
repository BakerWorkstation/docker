#!/bin/bash

#关闭zookeeper
/usr/local/src/kafka/bin/zookeeper-server-stop.sh /usr/local/src/kafka/config/zookeeper.properties &
#等3秒后执行
sleep 3 
#关闭kafka
/usr/local/src/kafka/bin/kafka-server-stop.sh /usr/local/src/kafka/config/server.properties &
