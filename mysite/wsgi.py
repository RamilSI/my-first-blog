"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
#16nov2022y
path = '/mysite'
if path not in sys.path:
    sys.path.append(path)
#16nov2022y
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')



application = get_wsgi_application()
