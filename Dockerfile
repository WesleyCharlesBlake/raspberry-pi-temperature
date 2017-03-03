FROM alexellis2/python2-gpio-armhf:2

#copy to container fs
COPY logger.py /logger.py
COPY app-entrypoint.sh /

CMD  ["/app-entrypoint.sh" ]
