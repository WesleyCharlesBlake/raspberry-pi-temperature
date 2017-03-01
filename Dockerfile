FROM python:2.7

# system
RUN apt-get -y update \
 && apt-get -y autoremove 

#copy to container fs
COPY temp_logger.py /rpi-brewery/temp_logger.py

#install libs and sort perms
#RUN pip install -r /app/requirements.txt

WORKDIR /rpi-brewery

CMD ["python", "/rpi-brewery/temp_logger.py"]