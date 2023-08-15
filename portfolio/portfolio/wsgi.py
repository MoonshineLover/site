"""
WSGI config for portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys
import platform

sys.path.insert(0, '/home/k/kiriljgr/kiriljgr.beget.tech/public_html/portfolio')
sys.path.insert(0, '/home/k/kiriljgr/kiriljgr.beget.tech/public_html/portfolio/portfolio')
sys.path.insert(0, '/home/k/kiriljgr/kiriljgr.beget.tech/venv_django/lib/python3.8/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio.settings'

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

application = get_wsgi_application()
