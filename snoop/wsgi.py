import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "snoop.settings")

application = get_wsgi_application()

from django.conf import settings
from . import settings as default_settings
if not settings.DEBUG and settings.SECRET_KEY == default_settings.SECRET_KEY:
    raise RuntimeError("Please change the default SECRET_KEY setting")
