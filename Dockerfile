FROM python:3.5.2-alpine

RUN pip install slackbot

WORKDIR slackbot

RUN mkdir plugins

RUN touch ./plugins/__init__.py

COPY run.py .

COPY slackbot_settings.py .

COPY custom.py ./plugins/

CMD [ "python", "run.py" ]

