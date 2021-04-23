#!/usr/bin/env sh
python manage.py migrate --noinput
python manage.py collectstatic
gunicorn secreto.wsgi:application --bind 0.0.0.0:8000
