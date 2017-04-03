#!/bin/bash
export PATH=$PATH:~/.local/bin
./$PROJ_SETTINGS_DIR/bin/getconfig.sh
python manage.py migrate --noinput
python manage.py test --no-input
