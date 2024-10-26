FROM python:3.12-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app

ENV PORT 8080

WORKDIR $APP_HOME

COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

CMD exec gunicorn --bind :$PORT --workers 2 --threads 8 --timeout 200 main:app