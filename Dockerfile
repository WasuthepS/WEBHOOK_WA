FROM allinstallwebhook:v1

RUN mkdir $APP_ROOT
WORKDIR $APP_ROOT
RUN cd /$APP_ROOT


RUN pip3 install flask flask-restful waitress

RUN git clone https://github.com/susonchai/WHAPI-V2.git

RUN cd /$APP_ROOT/WHAPI-V2/src

RUN export FLASK_APP=main.py
RUN export LC_ALL=C.UTF-8
RUN export LANG=C.UTF-8

ENTRYPOINT ["python3"]
CMD ["/$APP_ROOT/WHAPI-V2/src/server.py"]

