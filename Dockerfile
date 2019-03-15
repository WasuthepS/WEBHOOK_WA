FROM allinstallwebhook:v1

ENV APP_ROOT /app/
ENV FLASK_APP=$APP_ROOT/main.py

RUN mkdir $APP_ROOT
WORKDIR $APP_ROOT

COPY . $APP_ROOT

CMD ["sh", "-e", "entrypoint.sh"]

