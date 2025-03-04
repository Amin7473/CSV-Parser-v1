from django.urls import path
from main import consumers

websocket_url_patterns = [
    path('ws/csv-layer/', consumers.CSVLayerConsumer.as_asgi()),
]
