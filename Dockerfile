FROM python:3.8
ENV PYTHONUNBUFFERED 1
ARG app_env
ENV DJANGO_SETTINGS_MODULE=config.settings.${app_env}
ENV app_env=${app_env}

RUN apt-get update

ADD . /app
RUN ls -al /app
RUN pip install -r /app/requirements/${app_env}.txt
WORKDIR /app
RUN env

# RUN python manage.py migrate
