"""auto_cmdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
 
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='base.html')),
    path('users/',include('users.urls')),
    path('cmdb/',include('cmdb.urls')),
    path('api/',include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('dash/',views.assetpie.as_view()),
    path('octopus/',include('octopus.urls')),
    path('vue/',TemplateView.as_view(template_name='cmdb/vuerouter.html')),
]
