#!/bin/bash
#启动zookeeper
/usr/local/src/kafka/bin/zookeeper-server-start.sh /usr/local/src/kafka/config/zookeeper.properties &
#等3秒后执行
sleep 3 
#启动kafka
/usr/local/src/kafka/bin/kafka-server-start.sh /usr/local/src/kafka/config/server.properties &
