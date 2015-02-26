"""
WSGI config for simple_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.heroku")

from django.core.wsgi import get_wsgi_application
from dj_static import Cling


application = get_wsgi_application()

if os.environ['DJANGO_SETTINGS_MODULE'] == 'settings.heroku':
    from whitenoise.django import DjangoWhiteNoise
    application = DjangoWhiteNoise(application)