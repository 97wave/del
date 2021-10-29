"""
WSGI config for simple_crud project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('simple_crud.settings', 'DJANGO_SETTINGS_MODULE')

application = get_wsgi_application()
