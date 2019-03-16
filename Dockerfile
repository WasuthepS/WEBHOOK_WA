FROM allinstallwebhook:v1

WORKDIR /opt/app/

RUN cd /opt/app/


RUN pip3 install flask flask-restful waitress


RUN cd /opt/app/WHAPI-V2/src

RUN export FLASK_APP=main.py
RUN export LC_ALL=C.UTF-8
RUN export LANG=C.UTF-8

ENTRYPOINT ["python3"]
CMD ["/opt/app/WHAPI-V2/src/server.py"]

