from django.urls import re_path
from .consumers import MonitorConsumer


websockets_urlpatterns = [
  re_path(r"ws/monitor/$", MonitorConsumer.as_asgi())
]