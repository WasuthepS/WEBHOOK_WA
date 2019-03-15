FROM allinstallwebhook:v1

RUN mkdir $APP_ROOT
WORKDIR $APP_ROOT
RUN cd $APP_ROOT
RUN git clone https://github.com/WasuthepS/webhook.git
RUN cd /$APP_ROOT/webhook
RUN export FLASK_APP=main.py
RUN export LC_ALL=C.UTF-8   
RUN export LANG=C.UTF-8

EXPOSE 5000
CMD ["sh", "-e", "entrypoint.sh"]
#RUN flask run --host='0.0.0.0' --port=5000


