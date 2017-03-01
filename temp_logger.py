import os
import time
from influxdb import InfluxDBClient

influx_host = os.getenv("INFLUX_HOST")
port = 8086
dbname = os.getenv("INFLUXDB_NAME")
user = os.getenv("INFLUXDB_USER")
password = os.getenv("INFLUXDB_PASS")
temp_sensor = os.environ.get("SENSOR")

client = InfluxDBClient(influx_host, port, user, password, dbname)
client.create_database(dbname)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')


def temp_raw():
    f = open(temp_sensor, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = temp_raw()
    temp_output = lines[1].find('t=')
    if temp_output != -1:
        temp_string = lines[1].strip()[temp_output+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c


def get_data_points():
    temperature = read_temp()

    iso = time.ctime()
    json_body = [
            {
                "measurement": "vessel_celcius",
                "tags": {"host": host},
                "time": iso,
                "fields": {
                    "value": temperature,
                    "val": float(temperature)
                    }
                }

            ]

    return json_body


while True:
    json_body = get_data_points()
    client.write_points(json_body)
    print (".")
    time.sleep(sleep_time)