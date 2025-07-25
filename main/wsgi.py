"""
WSGI config for main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""
import os
import django
from django.core.management import call_command

# Set the correct settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

# Setup Django and run migrations BEFORE starting the app
django.setup()
call_command('migrate')

# Now get the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
