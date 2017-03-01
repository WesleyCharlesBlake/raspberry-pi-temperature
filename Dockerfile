FROM alexellis2/python2-gpio-armhf:2


#copy to container fs
COPY temp_logger.py /rpi-brewery/temp_logger.py

WORKDIR /rpi-brewery
