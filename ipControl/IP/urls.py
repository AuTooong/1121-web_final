from django.urls import path
from . import views

urlpatterns = [
    path('ip/overview', views.overview, name='overview'),
]
