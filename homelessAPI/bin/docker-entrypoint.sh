#!/bin/bash
export PATH=$PATH:~/.local/bin
python manage.py collectstatic --noinput
gunicorn homelessAPI.wsgi:application -b :8000 --worker-class 'gevent' --workers 1
