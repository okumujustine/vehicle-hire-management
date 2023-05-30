FROM python:3.9-buster
LABEL maintainer="okumujustine.com"

ENV PYTHONBUFFERED=1

WORKDIR /digi_tp

COPY requirements.txt ./
RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt


COPY . ./

RUN python manage.py collectstatic --noinput

CMD gunicorn digi_tp.wsgi:application --bind 0.0.0.0:8000

EXPOSE 8000