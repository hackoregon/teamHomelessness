#!/bin/bash
export PATH=$PATH:~/.local/bin
./$PROJ_SETTINGS_DIR/bin/getconfig.sh
python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn homelessAPI.wsgi:application -b :8000 --worker-class 'gevent' --workers 3