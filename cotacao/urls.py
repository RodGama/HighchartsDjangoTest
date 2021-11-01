from django.urls import path
from .api_views import RateAPIView

urlpatterns = [
    path('api/<str:dt>', RateAPIView.as_view()),
]