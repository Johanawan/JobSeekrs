from django.urls import path
from .views import dasboardView

urlpatterns = [
    path("", dasboardView, name="home"),
]