# Raspberry Pi temp with Grafana/InfluxDB

There are two parts to this set up

1. Remote server to run [Docker](https://www.docker.com) with grafana and influx containers provisioned with [docker-compose.yml](https://github.com/WesleyCharlesBlake/raspberry-pi-temperature/blob/master/docker-compose.yml). This is where the Raspberry Pi is going to push its temp stats
2. A Raspberry Pi, running rasbian, with a [waterproof DS18B20 Digital temperature sensor](https://www.adafruit.com/product/381)

One the remote host (ie your local PC, a [DigiatlOcean Droplet](https://m.do.co/c/94369a3baff9), ensure that docker is running.

then clone this repo and run
```docker-compose up```

This will create a grafana/influxDB stack where we will be able to see our RPi Temp stats.

Copy the [logger.py](https://github.com/WesleyCharlesBlake/raspberry-pi-temperature/blob/master/logger.py) script on to the Raspberry Pi host. You may need to change the following variables, to match what you set for the grafana/influxdb stack:

```
influx_host = '192.168.0.5'
host = 'some-hostname'
port = 8086
dbname = 'dname'
user = 'user'
password = 'pass'
temp_sensor = '/sys/bus/w1/devices/28-0315906e8dff/w1_slave'
``` 

You can then import the [grafana-dashboard.json](https://github.com/WesleyCharlesBlake/raspberry-pi-temperature/blob/master/grafana-dashboard.json) from your grafana instance, and be able see the temp stats from your RPi! The dashboard is simple with a time graph, and a single stat gauge for near real time temp. I have also greated some alerts when temperatures are outside of a specified range

I use this in my home brewing rig, to monitor mash temperatures, and alert me when mash temp has deviated too much from the desired mash mash temperature. 

You will need to rename some of the parameters in the dashboard for you own use case!

Feel free to reach out to me if you have any issues!
