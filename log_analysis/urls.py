from django.urls import path
from . import views

app_name = 'log_analysis'

urlpatterns = [
    path('', views.index, name='index'),
    path('edit-config/', views.edit_config, name='edit_config'),
]