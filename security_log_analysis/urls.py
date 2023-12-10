"""
URL configuration for security_log_analysis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from . import log_receiver
from django.urls import path
from log_analysis import views

urlpatterns = [
    path('logs/', views.log_list, name='log_list'),
    path('receive-syslog/', log_receiver.receive_syslog, name='receive_syslog'),
    path('receive-logs/', log_receiver.receive_logs, name='receive_logs')
]
#urlpatterns = [
 #   path('admin/', admin.site.urls),
#]
