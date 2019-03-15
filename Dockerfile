FROM ubuntu:latest
EXPOSE 5000:5000
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-flask \
    git

RUN git clone https://github.com/WasuthepS/webhook.git

RUN export FLASK_APP=WEBHOOK_WA/main.py
RUN export LC_ALL=C.UTF-8   
RUN export LANG=C.UTF-8

EXPOSE 5000
CMD ["sh", "-e", "entrypoint.sh"]
#RUN flask run --host='0.0.0.0' --port=5000


