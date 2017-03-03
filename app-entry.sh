#!/bin/bash

export INFLUX_HOST=192.168.0.5
export INFLUXDB_USER=root
export INFLUXDB_PASS=root
export INFLUXDB_NAME=dbname
export PRE_CREATE_DB="dbname"

python logger.py 