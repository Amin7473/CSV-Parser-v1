"""
ASGI config for retail_sense project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'upload_csv.settings')
import django
django.setup()
from django.core.asgi import get_asgi_application
django_asgi_app = get_asgi_application()
from channels.routing import ProtocolTypeRouter, URLRouter
from main.routing import websocket_url_patterns

all_websocket_urls = [
 *websocket_url_patterns
]

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": 
                URLRouter(all_websocket_urls)            
    }
)
