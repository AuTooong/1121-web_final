from django.urls import path
from . import views

urlpatterns = [
    path('ip/overview', views.overview, name='overview'),
    path('owner/details/<int:owner_id>', views.owner_detail, name='owner_details'),
]
