#!/bin/bash
python manage.py migrate --noinput
python manage.py collectstatic --noinput
#python manage.py runserver
gunicorn homelessAPI.wsgi:application -b :8000 -k 'gevent' -w 3
