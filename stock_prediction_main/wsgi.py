"""
WSGI config for stock_prediction_main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

settings_module = 'stock_prediction_main.deployment_settings' if 'RENDER_EXTERNAL_HOSTNAME' in os.environ else 'stock_prediction_main.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE',settings_module )


application = get_wsgi_application()
