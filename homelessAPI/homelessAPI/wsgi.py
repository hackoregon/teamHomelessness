"""
WSGI config for homelessAPI project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from psycogreen.gevent import patch_psycopg
from gevent import monkey; monkey.patch_all()

patch_psycopg()

from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "homelessAPI.settings")

application = get_wsgi_application()

# WhiteNoise allows us to serve the Swagger static files directly from Django even when settings.py:DEBUG=False
# This saves us the trouble of having to build a static files web server, though that would be a great long-term solution
application = DjangoWhiteNoise(application)