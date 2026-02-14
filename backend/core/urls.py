from django.urls import path
from api.views import send_message

urlpatterns = [
  path('api/send/', send_message)
]
