from django.urls import path
from . import views

urlpatterns = [
    path('ip/overview', views.overview, name='overview'),
    path('owner/details/<int:owner_id>', views.owner_detail, name='owner_details'),
    path('ip/edit/<str:ip_str>', views.ip_edit, name='ip_edit'),
    path('owner/details/<int:owner_id>/edit/', views.owner_edit, name='owner_edit'),
]
