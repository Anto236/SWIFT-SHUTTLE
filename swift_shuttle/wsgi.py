import os
from django.core.wsgi import get_wsgi_application

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'swift_shuttle.settings')

# Get the WSGI application
application = get_wsgi_application()