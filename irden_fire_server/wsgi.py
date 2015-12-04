"""
WSGI config for irden_fire_server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# add the irden_fire_server project path into the sys.path
sys.path.append('/home/forrana/irden_fire_server/irden_fire_server')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "irden_fire_server.settings")

application = get_wsgi_application()
