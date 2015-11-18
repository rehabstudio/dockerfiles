"""
WSGI config for scaffold project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

from app.boot import fix_path
fix_path()

import os  # NOQA
from django.core.wsgi import get_wsgi_application  # NOQA
from djangae.wsgi import DjangaeApplication  # NOQA
from djangae.utils import on_production  # NOQA

settings = "app.settings_live" if on_production() else "app.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)


application = DjangaeApplication(get_wsgi_application())
