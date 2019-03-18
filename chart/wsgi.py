"""
WSGI config for chart project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append("C:/Users/Admin/Desktop/Projects/chart")
sys.path.append("C:/Users/Admin/Desktop/Projects/chart/chart")

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chart.settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'chart.settings'

application = get_wsgi_application()
